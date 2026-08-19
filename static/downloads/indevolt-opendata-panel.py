"""INDEVOLT OpenData HTTP API device panel example."""

from __future__ import annotations

import asyncio
import json
import sys
from collections.abc import Callable, Sequence
from datetime import datetime
from ipaddress import AddressValueError, IPv4Address
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

    def __init__(self, host: str) -> None:
        self._base_url = f"http://{host}:{PORT}/rpc"
        self._session = requests.Session()

        # Local device requests must not use HTTP_PROXY, HTTPS_PROXY or ALL_PROXY.
        self._session.trust_env = False
        self._session.headers.update(
            {
                "Content-Type": "application/json",
                "Connection": "close",
            }
        )

    def _post(self, api: str, config: dict[str, Any]) -> dict[str, Any]:
        try:
            with self._session.post(
                f"{self._base_url}/{api}",
                params={"config": json.dumps(config, separators=(",", ":"))},
                timeout=TIMEOUT_SECONDS,
                allow_redirects=False,
            ) as response:
                if response.status_code != 200:
                    raise OpenDataError(f"Device returned HTTP {response.status_code}")
                payload = response.json()
        except requests.RequestException as error:
            raise OpenDataError(f"OpenData request failed: {error}") from error
        except ValueError as error:
            raise OpenDataError("Device response is not valid JSON") from error

        if not isinstance(payload, dict):
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

    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._last_started = 0.0

    async def run(self, request: Callable[[], Any]) -> Any:
        async with self._lock:
            loop = asyncio.get_running_loop()
            delay = REQUEST_INTERVAL_SECONDS - (loop.time() - self._last_started)
            if delay > 0:
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
    gate = RequestGate()
    stop = asyncio.Event()
    confirmed_light: bool | None = None

    host_input = ft.TextField(label="Device IPv4 address", width=240)
    connect_button = ft.Button("Connect")
    refresh_button = ft.Button("Refresh", disabled=True)
    serial_text = ft.Text("Serial number: —")
    soc_text = ft.Text("SOC: —")
    state_text = ft.Text("State: —")
    power_text = ft.Text("Battery power: —")
    light_switch = ft.Switch(label="Front panel light", disabled=True)
    updated_text = ft.Text("Last updated: —")
    status_text = ft.Text("Not connected")

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
            data = await gate.run(lambda: client.get_data(READ_POINTS))
            show(data)
        except OpenDataError as error:
            status_text.value = f"Read failed: {error}"
            success = False
        else:
            status_text.value = "Connected"
            success = True

        refresh_button.disabled = False
        light_switch.disabled = confirmed_light is None
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
            status_text.value = "Enter a valid device IPv4 address"
            page.update()
            return

        candidate = OpenDataClient(host)
        client = candidate
        connect_button.disabled = True

        if await refresh():
            host_input.disabled = True
            page.run_task(auto_refresh)
        else:
            candidate.close()
            client = None
            connect_button.disabled = False
        page.update()

    async def change_light(event) -> None:
        nonlocal confirmed_light

        if client is None:
            return

        target = int(bool(event.control.value))
        light_switch.disabled = True
        status_text.value = "Setting light"
        page.update()

        try:
            accepted = await gate.run(
                lambda: client.set_data(LIGHT_WRITE_POINT, target)
            )
            if not accepted:
                raise OpenDataError("Device rejected the write")

            data = await gate.run(lambda: client.get_data((LIGHT_STATE_POINT,)))
            confirmed = integer_value(data, LIGHT_STATE_POINT, 0, 1)
            success = confirmed == target
        except OpenDataError:
            success = False

        if success:
            confirmed_light = bool(target)
            status_text.value = "Light turned on" if target else "Light turned off"
        else:
            light_switch.value = confirmed_light or False
            status_text.value = "Light state not confirmed"

        light_switch.disabled = confirmed_light is None
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
                    [host_input, connect_button, refresh_button],
                    wrap=True,
                ),
                serial_text,
                ft.Row([soc_text, state_text, power_text], wrap=True),
                light_switch,
                updated_text,
                status_text,
            ]
        )
    )


if __name__ == "__main__":
    ft.run(main)
