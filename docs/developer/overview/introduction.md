---
title: Introduction
id: introduction
description: Overview of the INDEVOLT device local and cloud data communication framework
sidebar_label: Introduction
slug: /developer
---

# OpenData Overview

OpenData is an open data communication framework designed for INDEVOLT micro energy storage devices. It allows users to connect micro storage systems to custom-developed Apps or energy management systems to view device data, monitor status, and perform remote control.

Without relying on the INDEVOLT Server, users can still access micro storage device functions directly through local interfaces even without an Internet connection, ensuring flexible operation in different application scenarios.

With OpenData, you can:

- 📡 View real-time device data, such as state of charge (SOC), power, voltage, temperature, and operating status.
- 🎛️ Remotely control devices, such as setting charging and discharging modes, adjusting power, and controlling operating strategies.
- 🔗 Integrate with third-party systems, such as Home Assistant or cloud platforms.

## Supported communication methods

OpenData supports multiple common industrial and IoT protocols for different application scenarios:

- [**HTTP / HTTP Digest / HTTPS**](../http/overview.md)
  - Suitable for API calls from cloud platforms and applications.
  - Supports on-demand device data queries.

- [**Modbus TCP / RTU**](../modbus/overview.md)
  - Suitable for local systems and home energy management systems (HEMS).
  - Reads or writes device data through registers.

- [**MQTT**](../mqtt/overview.md)
  - Suitable for real-time data publishing and IoT scenarios.
  - Enables efficient data synchronization using the publish/subscribe model.

## Device connection methods

Devices can connect to the network through:

- Wi-Fi
- Ethernet
- RS485 (for Modbus RTU; not supported yet)

After the device connects to the network, it can exchange data and receive control commands from external systems through OpenData.

## How it works

The device generates and uploads data, while external systems read data or send control commands.

```text
INDEVOLT Device
   ↓
OpenData Communication Layer
   ↓
HTTP / MQTT / Modbus
   ↓
External System (App / Cloud Platform / HEMS)
```
