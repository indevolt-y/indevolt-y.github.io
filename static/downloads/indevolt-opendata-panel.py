"""INDEVOLT OpenData HTTP API device panel example."""

from __future__ import annotations

import asyncio
import json
import sys
from collections.abc import Callable, Sequence
from datetime import datetime
from ipaddress import AddressValueError, IPv4Address
from queue import Empty, SimpleQueue
from time import perf_counter
from typing import Any

import flet as ft
import requests

PORT = 8080
TIMEOUT_SECONDS = 10.0
REQUEST_INTERVAL_SECONDS = 5.0

READ_POINTS = ("0", "6000", "6001", "6002", "7171")
LIGHT_STATE_POINT = "7171"
LIGHT_WRITE_POINT = "7265"

STATE_NAMES = {
    1000: "Idle",
    1001: "Charging",
    1002: "Discharging",
}


class OpenDataError(RuntimeError):
    """OpenData transport or response error."""


class OpenDataClient:
    """Call the OpenData GetData and SetData HTTP APIs."""

    def __init__(
        self,
        host: str,
        logger: Callable[[str], None] | None = None,
    ) -> None:
        self._base_url = f"http://{host}:{PORT}/rpc"
        self._logger = logger
        self._session = requests.Session()

        # Local device requests must not use HTTP_PROXY, HTTPS_PROXY or ALL_PROXY.
        self._session.trust_env = False
        self._session.headers.update(
            {
                "Content-Type": "application/json",
                "Connection": "close",
            }
        )

    def _log(self, message: str) -> None:
        if self._logger is not None:
            self._logger(message)

    def _post(self, api: str, config: dict[str, Any]) -> dict[str, Any]:
        url = f"{self._base_url}/{api}"
        config_json = json.dumps(config, separators=(",", ":"))
        started = perf_counter()

        self._log(f"REQUEST POST {url}")
        self._log(f"CONFIG {config_json}")

        try:
            with self._session.post(
                url,
                params={"config": config_json},
                timeout=TIMEOUT_SECONDS,
                allow_redirects=False,
            ) as response:
                elapsed = perf_counter() - started
                response_body = response.text or "<empty>"
                self._log(f"RESPONSE HTTP {response.status_code} ({elapsed:.2f}s)")
                self._log(f"BODY {response_body}")

                if response.status_code != 200:
                    raise OpenDataError(f"Device returned HTTP {response.status_code}")
                payload = response.json()
        except ValueError as error:
            self._log("ERROR Device response is not valid JSON")
            raise OpenDataError("Device response is not valid JSON") from error
        except requests.RequestException as error:
            elapsed = perf_counter() - started
            self._log(f"ERROR after {elapsed:.2f}s: {error}")
            if sys.platform == "emscripten" and "Failed to fetch" in str(error):
                self._log(
                    "BROWSER The online preview could not access the local device. "
                    "Browser access requires the device to allow cross-origin "
                    "requests; run the downloaded Python file locally instead."
                )
            raise OpenDataError(f"OpenData request failed: {error}") from error

        if not isinstance(payload, dict):
            self._log("ERROR Device response is not a JSON object")
            raise OpenDataError("Device response is not a JSON object")
        return payload

    def get_data(self, points: Sequence[str]) -> dict[str, Any]:
        return self._post(
            "Indevolt.GetData",
            {"t": [int(point) for point in points]},
        )

    def set_data(self, point: str, value: int) -> bool:
        payload = self._post(
            "Indevolt.SetData",
            {"f": 16, "t": int(point), "v": [value]},
        )
        return payload.get("result") is True

    def close(self) -> None:
        self._session.close()


class RequestGate:
    """Serialize requests and enforce the recommended five-second interval."""

    def __init__(self, logger: Callable[[str], None] | None = None) -> None:
        self._logger = logger
        self._lock = asyncio.Lock()
        self._last_started = 0.0

    async def run(self, request: Callable[[], Any]) -> Any:
        async with self._lock:
            loop = asyncio.get_running_loop()
            delay = REQUEST_INTERVAL_SECONDS - (loop.time() - self._last_started)
            if delay > 0:
                if self._logger is not None:
                    self._logger(f"WAIT {delay:.1f}s for the request interval")
                await asyncio.sleep(delay)
            self._last_started = loop.time()

            # Flet Studio runs Python in a browser worker without native threads.
            if sys.platform == "emscripten":
                return request()
            return await asyncio.to_thread(request)


def integer_value(
    data: dict[str, Any],
    point: str,
    low: int | None = None,
    high: int | None = None,
) -> int | None:
    try:
        value = int(data[point])
    except (KeyError, TypeError, ValueError):
        return None
    if low is not None and value < low:
        return None
    if high is not None and value > high:
        return None
    return value


async def main(page: ft.Page) -> None:
    page.title = "INDEVOLT OpenData Panel"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    client: OpenDataClient | None = None
    pending_logs: SimpleQueue[str] = SimpleQueue()
    log_lines: list[str] = []
    stop = asyncio.Event()
    confirmed_light: bool | None = None

    def enqueue_log(message: str) -> None:
        timestamp = datetime.now().astimezone().strftime("%H:%M:%S.%f")[:-3]
        pending_logs.put(f"[{timestamp}] {message}")

    gate = RequestGate(enqueue_log)

    host_input = ft.TextField(label="Device IPv4 address", width=240)
    port_input = ft.TextField(
        label="Port",
        value=str(PORT),
        read_only=True,
        width=110,
    )
    connect_button = ft.Button("Connect")
    refresh_button = ft.Button("Refresh", disabled=True)
    serial_text = ft.Text("Serial number: —")
    soc_text = ft.Text("SOC: —")
    state_text = ft.Text("State: —")
    power_text = ft.Text("Battery power: —")
    light_switch = ft.Switch(label="Front panel light", disabled=True)
    updated_text = ft.Text("Last updated: —")
    status_text = ft.Text("Connection: Not connected")
    log_field = ft.TextField(
        label="Request log",
        helper="Ctrl+A / Command+A selects all logs",
        value="",
        multiline=True,
        min_lines=8,
        max_lines=8,
        read_only=True,
        expand=True,
        enable_interactive_selection=True,
        can_request_focus=True,
        text_style=ft.TextStyle(font_family="monospace", size=12),
    )

    def flush_logs() -> None:
        changed = False
        while True:
            try:
                message = pending_logs.get_nowait()
            except Empty:
                break
            log_lines.append(message)
            changed = True
        if changed:
            log_field.value = "\n".join(log_lines)

    async def run_request(request: Callable[[], Any]) -> Any:
        try:
            return await gate.run(request)
        finally:
            flush_logs()
            page.update()

    def show(data: dict[str, Any]) -> None:
        nonlocal confirmed_light

        serial = str(data.get("0", "")).strip()
        if not serial:
            raise OpenDataError("Response does not include the serial number")

        power = integer_value(data, "6000")
        state = integer_value(data, "6001")
        soc = integer_value(data, "6002", 0, 100)
        light = integer_value(data, LIGHT_STATE_POINT, 0, 1)

        serial_text.value = f"Serial number: {serial}"
        power_text.value = f"Battery power: {'—' if power is None else f'{power} W'}"
        state_text.value = (
            f"State: {STATE_NAMES.get(state, f'Unknown ({state})')}"
            if state is not None
            else "State: —"
        )
        soc_text.value = f"SOC: {'—' if soc is None else f'{soc}%'}"
        updated_text.value = (
            datetime.now().astimezone().strftime("Last updated: %H:%M:%S")
        )

        confirmed_light = None if light is None else bool(light)
        light_switch.value = confirmed_light or False
        light_switch.disabled = confirmed_light is None

    async def refresh(_=None) -> bool:
        if client is None:
            return False

        refresh_button.disabled = True
        light_switch.disabled = True
        page.update()

        try:
            data = await run_request(lambda: client.get_data(READ_POINTS))
            show(data)
        except OpenDataError as error:
            enqueue_log(f"PANEL Read failed: {error}")
            status_text.value = "Connection: Not connected"
            success = False
        else:
            status_text.value = "Connection: Connected"
            success = True

        refresh_button.disabled = False
        light_switch.disabled = not success or confirmed_light is None
        flush_logs()
        page.update()
        return success

    async def auto_refresh() -> None:
        while not stop.is_set():
            try:
                await asyncio.wait_for(stop.wait(), timeout=5.0)
            except TimeoutError:
                await refresh()

    async def connect(_=None) -> None:
        nonlocal client

        try:
            host = str(IPv4Address(str(host_input.value or "").strip()))
        except AddressValueError:
            enqueue_log("INPUT Invalid device IPv4 address")
            status_text.value = "Connection: Not connected"
            flush_logs()
            page.update()
            return

        enqueue_log(f"TARGET http://{host}:{PORT}")
        candidate = OpenDataClient(host, enqueue_log)
        client = candidate
        connect_button.disabled = True
        status_text.value = "Connection: Connecting"
        page.update()

        if await refresh():
            host_input.disabled = True
            page.run_task(auto_refresh)
        else:
            candidate.close()
            enqueue_log("SESSION Closed after connection failure")
            client = None
            connect_button.disabled = False
            refresh_button.disabled = True
            status_text.value = "Connection: Not connected"
            flush_logs()
        page.update()

    async def change_light(event) -> None:
        nonlocal confirmed_light

        if client is None:
            return

        target = int(bool(event.control.value))
        light_switch.disabled = True
        page.update()

        try:
            accepted = await run_request(
                lambda: client.set_data(LIGHT_WRITE_POINT, target)
            )
            if not accepted:
                raise OpenDataError("Device rejected the write")

            data = await run_request(lambda: client.get_data((LIGHT_STATE_POINT,)))
            confirmed = integer_value(data, LIGHT_STATE_POINT, 0, 1)
            enqueue_log(
                f"VERIFY point {LIGHT_STATE_POINT}: "
                f"expected={target}, received={confirmed}"
            )
            success = confirmed == target
        except OpenDataError as error:
            enqueue_log(f"PANEL Light control failed: {error}")
            success = False

        if success:
            confirmed_light = bool(target)
        else:
            light_switch.value = confirmed_light or False

        light_switch.disabled = confirmed_light is None
        flush_logs()
        page.update()

    async def window_event(event: ft.WindowEvent) -> None:
        if event.type == ft.WindowEventType.CLOSE:
            stop.set()
            if client is not None:
                client.close()
            await page.window.destroy()

    connect_button.on_click = connect
    refresh_button.on_click = refresh
    light_switch.on_change = change_light
    page.window.prevent_close = True
    page.window.on_event = window_event

    page.add(
        ft.Column(
            [
                ft.Row(
                    [host_input, port_input, connect_button, refresh_button],
                    wrap=True,
                ),
                serial_text,
                ft.Row([soc_text, state_text, power_text], wrap=True),
                light_switch,
                updated_text,
                status_text,
                ft.Row([log_field]),
            ]
        )
    )

    enqueue_log(f"READY OpenData endpoint port: {PORT}")
    flush_logs()
    page.update()


if __name__ == "__main__":
    ft.run(main)
