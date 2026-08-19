---
title: 使用 OpenData HTTP API 构建设备面板
id: opendata-local-device-panel
description: 通过读取设备数据和控制前面板灯带，说明 OpenData HTTP API 的请求格式、点位与调用规则
sidebar_label: OpenData HTTP API 实战
slug: /developer/guides/opendata-local-device-panel
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# 使用 OpenData HTTP API 构建设备面板

本文以读取设备状态和控制前面板灯带为例，展示 INDEVOLT OpenData HTTP API 的完整调用流程。

## 完整示例

示例可以直接在线查看，也可以下载 Python 文件在本地运行。

### 在线示例

<iframe
  src="https://studio.flet.dev/apps/6puPy0aXh5"
  title="INDEVOLT OpenData HTTP API 在线示例"
  loading="lazy"
  allow="local-network-access; local-network; loopback-network"
  style={{
    width: '100%',
    height: '760px',
    border: '1px solid var(--ifm-color-emphasis-300)',
    borderRadius: '8px',
  }}
/>

:::note 浏览器运行限制

在线示例在浏览器内运行，无需本地安装。连接局域网设备时，浏览器可能要求授予局域网访问权限，设备也需要允许浏览器请求。

[打开在线示例](https://studio.flet.dev/apps/6puPy0aXh5) · <a href="/downloads/indevolt-opendata-panel.py" download="main.py">下载 Python 示例</a>

:::

## 开始前准备

|项目|要求|
| --- | --- |
|设备|所有 SolidFlex 和 PowerFlex 系列产品；已[开启 OpenData HTTP](../http/overview.md#enable-api)|
|网络|操作终端与设备位于同一可信局域网|
|设备信息|已经获得设备 IPv4 地址，例如 `192.168.1.75`|
|调试工具|Bash/Zsh 中的 cURL，或 Windows PowerShell|

## 理解 OpenData HTTP 请求

OpenData HTTP API 的基础地址是：

```text
http://{设备 IP}:8080/rpc/{API 名称}
```

本教程使用两个 API：

|API|用途|
| --- | --- |
|`Indevolt.GetData`|读取一个或多个 cJSON 点位的当前值|
|`Indevolt.SetData`|向一个可写 cJSON 点位写入值|

两个 API 都使用 `POST`。具体操作放在 URL 的 `config` 查询参数中：

```text
POST http://{设备 IP}:8080/rpc/{API 名称}?config={JSON 配置}
```

## 第一步：读取一个点位

先读取电池 SOC 点位 `6002`，确认设备地址、网络和 OpenData HTTP 服务均可用。

把示例中的 `192.168.1.75` 替换为你的设备 IP，然后选择对应终端执行：

<Tabs groupId="terminal">
  <TabItem value="bash-zsh" label="Bash / Zsh" default>

```bash
DEVICE_IP="192.168.1.75"

curl --noproxy "${DEVICE_IP}" -g -X POST \
  -H "Content-Type: application/json" \
  "http://${DEVICE_IP}:8080/rpc/Indevolt.GetData?config={\"t\":[6002]}"
```

  </TabItem>
  <TabItem value="powershell" label="PowerShell">

```powershell
$DeviceIp = "192.168.1.75"
$Config = [uri]::EscapeDataString('{"t":[6002]}')

$Response = Invoke-RestMethod -Method Post `
  -Uri "http://${DeviceIp}:8080/rpc/Indevolt.GetData?config=${Config}" `
  -ContentType "application/json"

$Response | ConvertTo-Json -Compress
```

  </TabItem>
</Tabs>

`GetData` 的 `config` 对象只有一个必填字段：

```json
{
  "t": [6002]
}
```

|字段|类型|含义|
| --- | --- | --- |
|`t`|数组|本次请求需要读取的 cJSON 点位列表|

成功响应类似：

```json
{
  "6002": 76
}
```

响应是一个 JSON 对象：Key 是字符串形式的 cJSON 点位，Value 是设备当前值。这里表示电池 SOC 为 `76%`。

## 第二步：一次读取面板数据

`GetData` 支持在 `t` 数组中放入多个点位。设备面板需要读取：

|界面数据|点位|类型或单位|值说明|
| --- | ---: | --- | --- |
|设备序列号|`0`|字符串|设备 SN|
|电池直流功率|`6000`|W|正值表示放电，负值表示充电|
|充放电状态|`6001`|枚举|`1000` 静止、`1001` 充电、`1002` 放电|
|电池 SOC|`6002`|%|整机电池 SOC|
|前面板灯带状态|`7171`|枚举|`0` 关闭、`1` 开启|

用一个请求读取全部点位：

<Tabs groupId="terminal">
  <TabItem value="bash-zsh" label="Bash / Zsh" default>

```bash
DEVICE_IP="192.168.1.75"

curl --noproxy "${DEVICE_IP}" -g -X POST \
  -H "Content-Type: application/json" \
  "http://${DEVICE_IP}:8080/rpc/Indevolt.GetData?config={\"t\":[0,6000,6001,6002,7171]}"
```

  </TabItem>
  <TabItem value="powershell" label="PowerShell">

```powershell
$DeviceIp = "192.168.1.75"
$Config = [uri]::EscapeDataString('{"t":[0,6000,6001,6002,7171]}')

$Response = Invoke-RestMethod -Method Post `
  -Uri "http://${DeviceIp}:8080/rpc/Indevolt.GetData?config=${Config}" `
  -ContentType "application/json"

$Response | ConvertTo-Json -Compress
```

  </TabItem>
</Tabs>

下面是一个用于说明字段关系的响应示例；实际序列号和数值以设备返回为准：

```json
{
  "0": "YOUR_DEVICE_SN",
  "6000": -420,
  "6001": 1001,
  "6002": 76,
  "7171": 1
}
```

界面使用以下点位映射：

- `0` 直接作为设备序列号显示。
- `6000` 添加单位 `W`，不要丢失正负号。
- `6001` 按枚举表转换；遇到未知值时保留原始值，避免显示错误状态。
- `6002` 添加单位 `%`，并校验是否位于合理范围。
- `7171` 只有返回 `0` 或 `1` 时才更新灯带开关。

## 第三步：写入灯带控制点位

SolidFlex 2000 / PowerFlex 2000 使用写入点位 `7265` 控制前面板灯带：

|写入值|含义|
| ---: | --- |
|`0`|关闭灯带|
|`1`|开启灯带|

`SetData` 的 `config` 对象包含三个字段：

```json
{
  "f": 16,
  "t": 7265,
  "v": [1]
}
```

|字段|类型|含义|
| --- | --- | --- |
|`f`|数字|功能码，固定为 `16`|
|`t`|数字|需要写入的 cJSON 点位|
|`v`|数组|写入值，格式由目标点位定义|

以下请求把灯带设置为开启：

<Tabs groupId="terminal">
  <TabItem value="bash-zsh" label="Bash / Zsh" default>

```bash
DEVICE_IP="192.168.1.75"

curl --noproxy "${DEVICE_IP}" -g -X POST \
  -H "Content-Type: application/json" \
  "http://${DEVICE_IP}:8080/rpc/Indevolt.SetData?config={\"f\":16,\"t\":7265,\"v\":[1]}"
```

  </TabItem>
  <TabItem value="powershell" label="PowerShell">

```powershell
$DeviceIp = "192.168.1.75"
$Config = [uri]::EscapeDataString('{"f":16,"t":7265,"v":[1]}')

$Response = Invoke-RestMethod -Method Post `
  -Uri "http://${DeviceIp}:8080/rpc/Indevolt.SetData?config=${Config}" `
  -ContentType "application/json"

$Response | ConvertTo-Json -Compress
```

  </TabItem>
</Tabs>

设备接受写入时返回：

```json
{
  "result": true
}
```

`result: true` 表示写入请求已成功执行。应用还应读取状态点位，确认设备最终状态。

## 第四步：写入后读取状态

灯带的写入点位是 `7265`，状态读取点位是 `7171`。写入后按照建议请求间隔等待，再读取 `7171`：

<Tabs groupId="terminal">
  <TabItem value="bash-zsh" label="Bash / Zsh" default>

```bash
DEVICE_IP="192.168.1.75"

sleep 5
curl --noproxy "${DEVICE_IP}" -g -X POST \
  -H "Content-Type: application/json" \
  "http://${DEVICE_IP}:8080/rpc/Indevolt.GetData?config={\"t\":[7171]}"
```

  </TabItem>
  <TabItem value="powershell" label="PowerShell">

```powershell
$DeviceIp = "192.168.1.75"
$Config = [uri]::EscapeDataString('{"t":[7171]}')

Start-Sleep -Seconds 5
$Response = Invoke-RestMethod -Method Post `
  -Uri "http://${DeviceIp}:8080/rpc/Indevolt.GetData?config=${Config}" `
  -ContentType "application/json"

$Response | ConvertTo-Json -Compress
```

  </TabItem>
</Tabs>

灯带已开启时，响应应包含：

```json
{
  "7171": 1
}
```

关闭灯带时，把 `SetData` 中的 `v` 改为 `[0]`，随后再次读取 `7171`。只有读回值与目标值一致时，界面才显示操作成功。

## OpenData 调用规则

设备面板采用以下调用规则：

|类别|规则|本教程的处理方式|
| --- | --- | --- |
|接口建议|建议请求间隔 ≥ 5 秒|所有读取和写入共用 5 秒间隔|
|接口限制|最小支持间隔为 1 秒|不以 1 秒高频轮询设备|
|接口响应|成功读取返回“点位 → 当前值”的 JSON 对象|逐项检查点位是否存在、类型是否有效|
|接口响应|成功写入返回 `{"result":true}`|写入后再读取状态点位确认|
|客户端策略|局域网请求不应意外进入外部代理|OpenData 客户端不继承系统代理设置|
|客户端策略|设备无响应不能无限等待|示例客户端设置 10 秒超时|
|客户端策略|自动刷新、手动刷新和控制操作可能同时发生|示例客户端串行执行所有设备请求|
|客户端策略|设备地址不应被重定向替换|示例客户端不跟随 HTTP 重定向|

常见 HTTP 错误及完整说明见 [OpenData HTTP 错误码](../http/overview.md#errors)：

- `400`：`config` JSON、字段或点位格式错误。
- `404`：API 名称或请求路径错误。
- `405`：请求方法错误，或对不支持的资源执行操作。
- `408`：设备等待请求超时。
- `500`–`504`：设备当前无法正常完成请求。

## 设备面板调用流程

```text
设置 BASE_URL = http://{设备 IP}:8080/rpc

读取面板：
  POST /Indevolt.GetData
  config = {"t":[0,6000,6001,6002,7171]}
  校验 HTTP 200
  解析 JSON 对象
  按点位定义更新界面

控制灯带：
  校验用户目标值只能是 0 或 1
  POST /Indevolt.SetData
  config = {"f":16,"t":7265,"v":[目标值]}
  确认 result 为 true
  等待请求间隔
  POST /Indevolt.GetData
  config = {"t":[7171]}
  仅在读回值等于目标值时显示成功
```

完整交互顺序如下：

```mermaid
sequenceDiagram
    actor User as 用户
    participant App as 客户端
    participant Device as INDEVOLT 设备 :8080

    App->>Device: POST GetData {t:[0,6000,6001,6002,7171]}
    Device-->>App: 点位和值的 JSON 对象
    App-->>User: 显示设备状态
    User->>App: 开启或关闭灯带
    App->>Device: POST SetData {f:16,t:7265,v:[0/1]}
    Device-->>App: {result:true}
    Note over App,Device: 按请求间隔等待
    App->>Device: POST GetData {t:[7171]}
    Device-->>App: {7171:0/1}
    App-->>User: 显示最终确认状态
```

## 故障检查

|现象|优先检查|
| --- | --- |
|无法连接|设备 IP 是否正确；操作终端与设备是否在同一局域网；OpenData HTTP 是否启用；`8080` 端口是否可达|
|返回 `400`|`config` 是否为有效 JSON；`t` 是否为数组；`f/t/v` 是否使用正确类型|
|返回 `404`|路径是否为 `/rpc/Indevolt.GetData` 或 `/rpc/Indevolt.SetData`|
|响应缺少点位|当前型号是否支持该点位；请求中的 `t` 是否包含该点位|
|请求没有立即执行|客户端是否正在等待建议的 5 秒请求间隔|
|写入返回失败|目标点位是否可写；写入值是否在点位允许范围内|
|写入成功但读回不一致|等待请求间隔后重新读取状态点位，不要仅依据写入响应更新界面|

## 相关资料

- [INDEVOLT OpenData 介绍](../overview/introduction.md)
- [OpenData HTTP 请求格式、频率和错误码](../http/overview.md)
- [`Indevolt.GetData` 与 `Indevolt.SetData` API 参考](../http/api-reference.md)
