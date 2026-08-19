---
title: 使用 OpenData 构建 macOS 本地设备面板
id: macos-local-device-panel
description: 使用 Python、Flet 和 OpenData HTTP 构建 macOS 本地设备面板的完整教程
sidebar_label: macOS 本地设备面板
slug: /developer/guides/macos-local-app
---

# 使用 OpenData 构建 macOS 本地设备面板

通过阅读本文档并按照其中的步骤完成示例项目，你可以得到一个可在 macOS 上运行的 INDEVOLT OpenData 桌面 App。这个 App 可以显示设备序列号、电池 SOC、充放电状态、电池直流功率和前面板灯带状态，并支持自动刷新、手动刷新以及开启或关闭前面板灯带。

## 运行条件

|项目|配置|
| ----------| ----------------------------------------------------------|
|设备|SolidFlex 2000 或 PowerFlex 2000，已启用 OpenData HTTP|
|网络|Mac 与设备位于同一可信局域网，已获得设备 IPv4 地址|
|开发环境|macOS 12+、Python 3.13、uv|
|项目依赖|Flet 0.86.5、Requests 2.34.2|
|构建环境|Xcode 15+、CocoaPods 1.16+；Apple Silicon 需要 Rosetta 2|

OpenData HTTP 服务使用设备的 `8080` 端口。请求格式、错误码和数据点定义以 [OpenData HTTP 说明](../http/overview.md) 与 [HTTP API Reference](../http/api-reference.md) 为准。

## 项目结构

|文件或目录|唯一职责|
| ------------| ----------------------------------------------------------|
|`.python-version`|指定项目使用 Python 3.13，由 `uv init` 生成|
|`README.md`|记录项目说明，由 `uv init` 生成|
|`pyproject.toml`|保存项目元数据和依赖，由 uv 管理|
|`uv.lock`|锁定完整依赖版本，由 `uv add` 生成|
|`.venv/`|保存项目虚拟环境，由 `uv add` 创建|
|`main.py`|启动 Flet App|
|`indevolt_panel/config.py`|保存端口、超时、请求间隔和点位常量|
|`indevolt_panel/client.py`|封装 OpenData HTTP 读取与写入|
|`indevolt_panel/queue.py`|串行执行 OpenData 读写、控制请求间隔并把同步调用放入线程|
|`indevolt_panel/models.py`|校验响应值并生成面板数据模型|
|`indevolt_panel/service.py`|组织面板读取、灯带写入和状态读回|
|`indevolt_panel/ui.py`|创建 Flet 控件并处理界面事件|
|`indevolt_panel/__init__.py`|标记 Python 包，保持为空|

## 创建全部目录和文件

下面的命令可以整块复制到 macOS 终端。`uv init` 会创建项目目录、Python 版本文件、项目配置、说明文件和启动文件；后续命令一次创建 7 个业务模块。依赖环境和锁文件会在添加依赖时自动生成。

```bash
uv init --no-package --python 3.13 --vcs none indevolt-opendata-panel
cd indevolt-opendata-panel

mkdir -p indevolt_panel
touch indevolt_panel/{__init__,config,client,queue,models,service,ui}.py

find . -maxdepth 2 -type f | sort
```

`find` 应列出以下文件：

```text
./.python-version
./README.md
./indevolt_panel/__init__.py
./indevolt_panel/client.py
./indevolt_panel/config.py
./indevolt_panel/models.py
./indevolt_panel/queue.py
./indevolt_panel/service.py
./indevolt_panel/ui.py
./main.py
./pyproject.toml
```

## 添加项目依赖

下面的命令会把依赖写入 `pyproject.toml`，同时创建 `.venv`、安装依赖并生成 `uv.lock`：

```bash
uv add "flet==0.86.5" "requests==2.34.2"
```

## 定义 OpenData 常量

### 文件：`indevolt_panel/config.py`

```python
PORT = 8080
TIMEOUT_SECONDS = 10.0
MIN_REQUEST_INTERVAL = 5.0

SERIAL_NUMBER = "0"
BATTERY_POWER = "6000"
BATTERY_STATE = "6001"
BATTERY_SOC = "6002"
LIGHT_STATE = "7171"
LIGHT_WRITE = "7265"

READ_POINTS = (
    SERIAL_NUMBER,
    BATTERY_POWER,
    BATTERY_STATE,
    BATTERY_SOC,
    LIGHT_STATE,
)

STATE_NAMES = {
    1000: "待机",
    1001: "充电",
    1002: "放电",
}
```

## 实现 OpenData HTTP 通信

`Indevolt.GetData` 的 `config` 参数为 `{"t":[点位]}`，响应直接返回点位和值；`Indevolt.SetData` 的参数为 `{"f":16,"t":点位,"v":[值]}`，成功响应包含 `{"result":true}`。

### 文件：`indevolt_panel/client.py`

```python
import json
from collections.abc import Sequence
from typing import Any

import requests

from .config import PORT, TIMEOUT_SECONDS


class OpenDataError(RuntimeError):
    pass


class OpenDataClient:
    def __init__(self, host: str) -> None:
        self._base_url = f"http://{host}:{PORT}/rpc"
        self._session = requests.Session()
        self._session.trust_env = False
        self._session.headers.update({
            "Content-Type": "application/json",
            "Connection": "close",
        })

    def _post(self, method: str, config: dict[str, Any]) -> dict[str, Any]:
        try:
            with self._session.post(
                f"{self._base_url}/{method}",
                params={"config": json.dumps(config, separators=(",", ":"))},
                timeout=TIMEOUT_SECONDS,
                allow_redirects=False,
            ) as response:
                if response.status_code != 200:
                    raise OpenDataError(f"设备返回 HTTP {response.status_code}")
                payload = response.json()
        except requests.RequestException as error:
            raise OpenDataError(f"OpenData 请求失败：{error}") from error

        if not isinstance(payload, dict):
            raise OpenDataError("设备返回的 JSON 不是对象")
        return payload

    def get_data(self, points: Sequence[str]) -> dict[str, Any]:
        return self._post("Indevolt.GetData", {"t": [int(p) for p in points]})

    def set_data(self, point: str, value: int) -> bool:
        payload = self._post(
            "Indevolt.SetData",
            {"f": 16, "t": int(point), "v": [int(value)]},
        )
        return payload.get("result") is True

    def close(self) -> None:
        self._session.close()
```

`trust_env = False` 让局域网设备请求不读取系统代理环境变量。每次请求都有 10 秒超时，并拒绝把请求重定向到其他地址。

## 控制 OpenData 请求顺序

设备 HTTP 请求在后台线程中执行。Flet 事件处理器通过 `asyncio.to_thread()` 等待结果，窗口不会在设备响应期间冻结。

### 文件：`indevolt_panel/queue.py`

```python
import asyncio
from collections.abc import Callable
from typing import TypeVar

from .config import MIN_REQUEST_INTERVAL

T = TypeVar("T")


class RequestQueue:
    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._last_started = 0.0

    async def run(self, request: Callable[[], T]) -> T:
        async with self._lock:
            loop = asyncio.get_running_loop()
            delay = MIN_REQUEST_INTERVAL - (loop.time() - self._last_started)
            if delay > 0:
                await asyncio.sleep(delay)
            self._last_started = loop.time()
            return await asyncio.to_thread(request)
```

自动刷新、手动刷新、灯带写入和灯带读回都只能调用这个 `run()` 方法。

## 解析面板数据

|界面字段|读取点位|有效值|
| --------------| ---------: | -----------------------------|
|设备序列号|`0`|非空字符串|
|电池直流功率|`6000`|整数，单位 `W`|
|充放电状态|`6001`|`1000` 待机、`1001` 充电、`1002` 放电|
|电池 SOC|`6002`|0–100，单位 `%`|
|灯带状态|`7171`|`0` 关闭、`1` 开启|

### 文件：`indevolt_panel/models.py`

```python
from dataclasses import dataclass
from typing import Any

from .config import (
    BATTERY_POWER,
    BATTERY_SOC,
    BATTERY_STATE,
    LIGHT_STATE,
    SERIAL_NUMBER,
    STATE_NAMES,
)


@dataclass(frozen=True, slots=True)
class PanelData:
    serial: str | None
    soc: int | None
    state: str
    battery_power: int | None
    front_light: bool | None


def integer_value(data: dict[str, Any], key: str, low=None, high=None):
    try:
        value = int(data[key])
    except (KeyError, TypeError, ValueError):
        return None
    if low is not None and value < low:
        return None
    if high is not None and value > high:
        return None
    return value


def parse_panel(data: dict[str, Any]) -> PanelData:
    state = integer_value(data, BATTERY_STATE)
    light = integer_value(data, LIGHT_STATE, 0, 1)
    serial = str(data.get(SERIAL_NUMBER, "")).strip() or None
    return PanelData(
        serial=serial,
        soc=integer_value(data, BATTERY_SOC, 0, 100),
        state=STATE_NAMES.get(
            state,
            "—" if state is None else f"未知（{state}）",
        ),
        battery_power=integer_value(data, BATTERY_POWER),
        front_light=None if light is None else bool(light),
    )
```

## 组织读取和灯带控制

灯带写入使用点位 `7265`。界面只在随后读回的 `7171` 与目标值一致时显示成功。

### 文件：`indevolt_panel/service.py`

```python
from .client import OpenDataClient, OpenDataError
from .config import LIGHT_STATE, LIGHT_WRITE, READ_POINTS
from .models import PanelData, integer_value, parse_panel
from .queue import RequestQueue


class PanelService:
    def __init__(self, host: str) -> None:
        self._client = OpenDataClient(host)
        self._queue = RequestQueue()

    async def read(self) -> PanelData:
        data = await self._queue.run(lambda: self._client.get_data(READ_POINTS))
        panel = parse_panel(data)
        if panel.serial is None:
            raise OpenDataError("响应缺少设备序列号")
        return panel

    async def set_front_light(self, enabled: bool) -> bool:
        accepted = await self._queue.run(
            lambda: self._client.set_data(LIGHT_WRITE, int(enabled))
        )
        if not accepted:
            return False
        data = await self._queue.run(
            lambda: self._client.get_data((LIGHT_STATE,))
        )
        return integer_value(data, LIGHT_STATE, 0, 1) == int(enabled)

    def close(self) -> None:
        self._client.close()
```

## 创建 Flet 窗口

界面文件只处理控件和事件。所有设备读写都交给 `PanelService`。

### 文件：`indevolt_panel/ui.py`

```python
import asyncio
from datetime import datetime
from ipaddress import AddressValueError, IPv4Address

import flet as ft

from .client import OpenDataError
from .models import PanelData
from .service import PanelService


async def main(page: ft.Page) -> None:
    page.title = "INDEVOLT OpenData Panel"
    service: PanelService | None = None
    stop = asyncio.Event()
    confirmed_light: bool | None = None

    host_input = ft.TextField(label="设备 IPv4", width=220)
    connect_button = ft.Button("连接")
    refresh_button = ft.Button("刷新", disabled=True)
    serial_text = ft.Text("序列号：—")
    soc_text = ft.Text("SOC：—")
    state_text = ft.Text("状态：—")
    power_text = ft.Text("电池功率：—")
    updated_text = ft.Text("更新时间：—")
    light_switch = ft.Switch(label="前面板灯带", disabled=True)
    status_text = ft.Text("未连接")

    def show(data: PanelData) -> None:
        nonlocal confirmed_light
        serial_text.value = f"序列号：{data.serial or '—'}"
        soc_text.value = f"SOC：{'—' if data.soc is None else f'{data.soc}%'}"
        state_text.value = f"状态：{data.state}"
        power = "—" if data.battery_power is None else f"{data.battery_power} W"
        power_text.value = f"电池功率：{power}"
        updated_text.value = datetime.now().astimezone().strftime(
            "更新时间：%H:%M:%S"
        )
        confirmed_light = data.front_light if data.serial else None
        light_switch.value = confirmed_light or False
        light_switch.disabled = confirmed_light is None

    async def refresh(_=None) -> bool:
        if service is None:
            return False
        refresh_button.disabled = True
        light_switch.disabled = True
        page.update()
        try:
            show(await service.read())
        except OpenDataError as error:
            status_text.value = f"连接失败：{error}"
            ok = False
        else:
            status_text.value = "已连接"
            ok = True
        refresh_button.disabled = False
        light_switch.disabled = confirmed_light is None
        page.update()
        return ok

    async def auto_refresh() -> None:
        while not stop.is_set():
            try:
                await asyncio.wait_for(stop.wait(), timeout=5.0)
            except TimeoutError:
                await refresh()

    async def connect(_=None) -> None:
        nonlocal service
        try:
            host = str(IPv4Address(host_input.value.strip()))
        except AddressValueError:
            status_text.value = "请输入有效的设备 IPv4"
            page.update()
            return

        candidate = PanelService(host)
        service = candidate
        connect_button.disabled = True
        if await refresh():
            host_input.disabled = True
            page.run_task(auto_refresh)
        else:
            candidate.close()
            service = None
            connect_button.disabled = False
        page.update()

    async def change_light(event) -> None:
        nonlocal confirmed_light
        if service is None:
            return
        desired = bool(event.control.value)
        light_switch.disabled = True
        status_text.value = "正在设置灯带"
        page.update()
        try:
            ok = await service.set_front_light(desired)
        except OpenDataError:
            ok = False
        if ok:
            confirmed_light = desired
            status_text.value = "灯带已开启" if desired else "灯带已关闭"
        else:
            light_switch.value = confirmed_light or False
            status_text.value = "灯带结果未确认"
        light_switch.disabled = confirmed_light is None
        page.update()

    async def window_event(event: ft.WindowEvent) -> None:
        if event.type == ft.WindowEventType.CLOSE:
            stop.set()
            if service is not None:
                service.close()
            await page.window.destroy()

    connect_button.on_click = connect
    refresh_button.on_click = refresh
    light_switch.on_change = change_light
    page.window.prevent_close = True
    page.window.on_event = window_event

    page.add(ft.Column([
        ft.Row([host_input, connect_button, refresh_button]),
        serial_text,
        ft.Row([soc_text, state_text, power_text]),
        light_switch,
        updated_text,
        status_text,
    ]))
```

## 添加启动入口

### 文件：`main.py`

```python
import flet as ft

from indevolt_panel.ui import main


if __name__ == "__main__":
    ft.run(main)
```

### 文件：`indevolt_panel/__init__.py`

保持为空。

## 运行与构建

开发运行：

```bash
uv run flet run main.py
```

窗口出现后输入设备 IPv4。首次读取成功时应显示设备序列号和面板数据，灯带开关随后可用。

macOS 构建：

```bash
uv run flet build macos . --python-version 3.13
```

## 验收

|场景|通过条件|
| ------------| ------------------------------------------------------------------|
|项目初始化|`uv init` 生成 4 个项目文件，7 个业务模块全部存在；`uv add` 后生成 `.venv` 和 `uv.lock`|
|模块边界|HTTP、请求队列、面板数据、界面和入口分别位于对应文件|
|首次连接|序列号、SOC、状态、直流功率和灯带状态同时更新|
|请求频率|自动刷新、手动刷新和灯带操作的相邻请求开始时间至少相隔 5 秒|
|界面响应|设备请求期间窗口仍可移动，控件不会冻结|
|异常响应|状态区显示错误，已成功显示的数据不被清空|
|打开灯带|写入 `7265=1`，随后读取 `7171=1`，界面显示“灯带已开启”|
|关闭灯带|写入 `7265=0`，随后读取 `7171=0`，界面显示“灯带已关闭”|
|写入未确认|写入失败或读回不一致时恢复最后一次确认值|
|退出|关闭窗口后停止自动刷新并释放设备连接资源|
|macOS App|构建产物可以启动并完成一次读取和一次灯带开关操作|

## 故障检查

|现象|检查项|
| ------------------------| ---------------------------------------------------------------------------------------|
|无法连接|设备与 Mac 是否在同一局域网；OpenData HTTP 是否启用；IPv4 是否变化；`8080` 端口是否被隔离|
|请求超时|设备是否可达；防火墙是否拦截；窗口是否正在等待前一个请求完成|
|字段显示 `—`|响应是否包含对应点位；值是否为可转换的整数；SOC 和灯带值是否在允许范围内|
|刷新没有立即执行|是否正在等待满足 5 秒请求间隔|
|灯带结果未确认|`7265` 写入结果与下一次 `7171` 读回是否一致|
|依赖添加失败|`uv --version` 是否可用；网络是否可以访问依赖源；Python 3.13 是否成功安装|
|开发运行正常但构建失败|Xcode、CocoaPods、Rosetta 2 和 Flet 版本是否符合运行条件|

## 安全与数据处理

- 只在可信局域网中访问设备的 OpenData HTTP 服务，不把 `8080` 端口暴露到公网。
- OpenData HTTP 调用设置有限超时、禁用环境代理并拒绝 HTTP 重定向。
- 灯带写入只允许 `0` 和 `1`，并且只能由当前窗口中的用户操作触发。
- 首次读取设备序列号并显示在窗口后，才启用写入控件。
- 设备 IP、序列号和响应正文进入日志、截图或问题报告前先脱敏。

## 相关资料

- [INDEVOLT OpenData 介绍](../overview/introduction.md)
- [INDEVOLT OpenData HTTP 说明](../http/overview.md)
- [INDEVOLT OpenData HTTP API Reference](../http/api-reference.md)
- [uv 项目文档](https://docs.astral.sh/uv/guides/projects/)
- [Requests 文档](https://requests.readthedocs.io/)
- [Flet 异步应用](https://flet.dev/docs/cookbook/async-apps/)
- [Flet macOS 构建](https://flet.dev/docs/publish/macos/)
