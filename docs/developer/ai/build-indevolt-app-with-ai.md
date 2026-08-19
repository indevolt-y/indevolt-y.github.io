---
title: Build an INDEVOLT App with AI, Step by Step
id: build-indevolt-app-with-ai
description: Follow a complete AI-assisted workflow to plan, build, run, and troubleshoot a local App that connects to an INDEVOLT device
sidebar_label: Build an INDEVOLT App with AI
slug: /developer/guides/build-indevolt-app-with-ai
---

# Build an INDEVOLT App with AI, Step by Step

This guide shows you how to use an AI coding tool to build a local App that connects to an INDEVOLT device. It provides a complete workflow you can follow directly, from downloading the expert instructions, describing your goal, and approving the plan to running the App, copying logs, and resolving problems.

:::note What “INDEVOLT App” means in this guide

Here, “INDEVOLT App” means a small App you build yourself to connect to an INDEVOLT device. It does not refer to the official INDEVOLT App.

:::

![AI tutorial diagram: the five steps from downloading the expert instructions to completing a local INDEVOLT App](/img/developer/ai/en/app-development-flow.svg)

*The whole process has five parts: download, upload, describe, approve, and run.*

## What you will build

The first version is a simple local device panel that can:

- Accept a device IP address and connect through port `8080`.
- Display the serial number, battery state of charge, battery power, and operating state.
- Refresh automatically and display the last update time.
- Show a scrollable request log that can be selected and copied.

This first version only reads data. It does not control the device or publish anything to the Internet. A first attempt usually takes 30–60 minutes, depending on your AI tool and computer environment.

![AI tutorial diagram: layout of the finished local INDEVOLT device panel](/img/developer/ai/en/local-device-panel-layout.svg)

## Before you start

Prepare the following:

- A SolidFlex or PowerFlex device with [OpenData HTTP enabled](https://docs.indevolt.com/docs/hardware/open-data/http/#enable-api).
- A computer connected to the same local network as the device.
- The device IP address, for example `192.168.8.247`.
- An AI coding tool that can read attachments and webpages, create files, run commands, and check results.
- A new empty folder for the App.

If you do not know the device IP address or whether OpenData is enabled, you can simply tell the AI that you do not know.

## Step 1: Download the expert instructions

Download this Markdown file:

<a className="button button--primary" href="/downloads/indevolt-software-development-expert-instructions-en.md" download="INDEVOLT-Software-Development-Expert-Instructions.md">Download the INDEVOLT Software Development Expert Instructions</a>

The download is a `.md` file. Start a new task in your AI coding tool, then drag this file into the conversation or upload it as an attachment.

If your AI tool does not support file uploads, open the [web version of the expert instructions](./expert-instructions.md), copy the complete document, and send it to the AI.

**You have completed this step when:** the expert-instructions attachment appears in the conversation, or the AI has received the full text.

![AI tutorial diagram: upload the INDEVOLT Software Development Expert Instructions and send the App request in the same AI conversation](/img/developer/ai/en/upload-expert-instructions.svg)

## Step 2: Send the App request to the AI

After uploading the expert instructions, copy the complete message below. You only need to fill in the last four fields.

Every blue card titled “Send to AI” or “Reply to AI” contains text that belongs in the AI conversation.

:::info Send to AI — Create the App request

```text
Please read the attached INDEVOLT Software Development Expert Instructions in full. Do not write code yet.

I want to build a local App that connects to an INDEVOLT device. The first version must only read data; it must not control the device, publish, or deploy anything.

The App must:
- Accept a device IPv4 address and display the fixed port 8080;
- Display the device serial number, battery state of charge, charge/discharge power, and operating state;
- Display the last update time and refresh automatically within the official INDEVOLT request limits;
- Provide a full-width request log that is scrollable, selectable, and easy to copy;
- Bypass the system HTTP proxy when requesting a device on the local network;
- Run directly on my computer.

Success criteria: the App connects to a real device and displays real data. The log shows the request URL, port, HTTP status, and response content. Detailed errors appear only in the log and are not repeated elsewhere in the interface.

First inspect the INDEVOLT documentation and the current computer environment, then recommend the simplest suitable implementation. Give me the plan and an Implementation Confirmation Sheet. Wait until I reply with exactly “Confirm implementation” before creating files or running tests.

Computer operating system: [macOS, Windows, or Linux]
Device model: [Enter the model, or “I don't know”]
Device IP address: [Enter the IP address, or “I don't know”]
OpenData HTTP: [Enabled, or “I don't know”]
```

:::

**You have completed this step when:** the AI is reading documentation, asking for missing information, or preparing a plan instead of immediately writing code.

## Step 3: Answer the AI's questions

The AI may ask for the device model, IP address, computer operating system, or OpenData status. Answer what you know. If you do not know, reply with:

:::info Reply to AI — When you do not know device information

```text
I don't know. Tell me exactly where I can find it. Please investigate anything else that can be determined from the INDEVOLT documentation, attachments, project, or computer environment.
```

:::

You do not need to decide:

- Which programming language to use.
- Whether to use HTTP, MQTT, or Modbus.
- Which user-interface framework to use.
- How many source files the App should contain.

If the AI asks you to make these choices, reply with:

:::info Reply to AI — Ask for a direct recommendation

```text
Use the expert instructions, the INDEVOLT documentation, and the current environment to recommend the simplest suitable approach directly.
```

:::

## Step 4: Review the plan

Before writing code, the AI should provide an Implementation Confirmation Sheet. Check only these five items:

- [ ] The first version only reads data and does not control the device.
- [ ] It displays the serial number, battery state of charge, power, operating state, and request log.
- [ ] The App runs only on your computer and will not be published automatically.
- [ ] The plan lists the files that will be created and explains how the App will be started and verified.
- [ ] The AI is waiting for you to reply with “Confirm implementation.”

If everything is correct, send only:

:::info Reply to AI — Approve implementation

```text
Confirm implementation
```

:::

Do not add anything before or after those two words.

If the plan is not correct, state exactly what needs to change. For example:

:::info Reply to AI — Request a simpler plan

```text
The first version is too complex. Remove device control and publishing. Keep only the local read-only panel, then provide a revised Implementation Confirmation Sheet. Do not start writing code.
```

:::

## Step 5: Let the AI complete the work

After you reply with “Confirm implementation,” the AI should create the files, install dependencies, run the required checks, and tell you how to start the App.

If the AI only pastes code into the conversation without creating and running the project, reply with:

:::info Reply to AI — Complete the actual implementation

```text
Continue with the approved implementation scope. Write the code into the project files, run the required checks, and start the App. Do not only display code in the conversation.
```

:::

**You have completed this step when:** the App is open, or the AI has provided a startup command that it actually verified.

## Step 6: Test the App yourself

After the App opens, check the following in order:

1. The interface shows “Device IPv4 address” and port `8080`.
2. Enter the device IP address and select **Connect**.
3. The serial number, battery state of charge, power, and operating state appear.
4. The “Last updated” time changes.
5. The log area spans the full width of the interface and can be scrolled.
6. Select the log and press `Ctrl+A` or `Command+A` to copy everything.
7. The log shows the request address, `HTTP 200`, and the device response.

When every check passes, the first version is complete.

## Step 7: If something fails, send the log to the AI

You do not need to diagnose the code yourself. Copy the observed behavior and the complete log into this message:

:::info Send to AI — Report a problem with the complete log

```text
Current behavior: [Example: the App still shows “Not connected” after I select Connect]
What I just did: [Example: entered 192.168.8.247 and selected Connect]
Expected result: [Example: display the device state of charge and power]

Complete request log:
[Paste the log here]

Use the log to identify the cause. Fix only this problem, then repeat the same verification. Do not add unrelated features.
```

:::

Before sharing a log, remove any device information you do not want to disclose. Never send passwords, tokens, or secret keys to the AI.

If the log contains `Failed to fetch`, also state whether you are using an online browser preview or a local program downloaded to your computer. Browser previews are subject to cross-origin and local-network permission restrictions.

## Step 8: Keep the finished App

After the App works, send:

:::info Send to AI — Produce the Delivery Report

```text
Follow the expert instructions and provide the final Delivery Report. Include the source-code location, how to start the App next time, actual verification results, known limitations, and rollback method. Do not include the work process in the delivery document.
```

:::

Confirm that you received:

- [ ] The complete source code.
- [ ] Instructions for starting the App again.
- [ ] The checks the AI actually ran and their results.
- [ ] Known limitations and the rollback method.
- [ ] Confirmation that the first version contains no unapproved device control or publishing functionality.

## Add features later

Keep the read-only version working before starting a new task to add charts, historical data, alerts, or device control.

If a new feature needs to control a physical device, the AI must first provide a Device Write Confirmation Sheet. Only an exact reply of `Confirm device write` authorizes the single device operation listed in that sheet. `Confirm implementation` does not authorize a device write.

To understand the OpenData HTTP calls behind this App, continue with the official [HTTP/HTTPS Overview](https://docs.indevolt.com/docs/hardware/open-data/http/) and [API Reference](https://docs.indevolt.com/docs/hardware/open-data/http-api/).
