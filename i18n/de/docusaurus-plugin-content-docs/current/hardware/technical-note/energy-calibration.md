---
title: Energiekalibrierung
description: Unterstützt die regelmäßige Kalibrierung des Batteriestands für eine genauere SOC-Anzeige
---

# Energiekalibrierung

## 1. Was ist eine Energiekalibrierung?

Im täglichen Betrieb wird der angezeigte Ladezustand (State of Charge, SOC) des Systems algorithmisch geschätzt. Im Laufe der Zeit kann es dabei zu Abweichungen kommen.

Die **Energiekalibrierung** sorgt dafür, dass das System regelmäßig einen vollständigen Ladevorgang durchführt, um den SOC neu zu referenzieren und die Anzeige des Ladezustands zu präzisieren.

:::info
Das System optimiert die SOC-Berechnung kontinuierlich durch verbesserte Algorithmen. Zukünftig wird zusätzlich ein Kalman-Filter eingesetzt, um die Genauigkeit der Ladezustandsbestimmung über längere Betriebszeiten weiter zu erhöhen.
:::

## 2. Was passiert während der Kalibrierung?

Sobald der konfigurierte Kalibrierintervall erreicht ist, führt das System automatisch eine Kalibrierung durch:

- Priorität: Laden über **PV (Photovoltaik)**
- Falls PV-Leistung nicht ausreicht, wird automatisch **AC-Netzstrom** zur Unterstützung verwendet
- Der Ladevorgang läuft, bis die Batterie **vollständig geladen** ist

👉 Einfach gesagt: Die Batterie wird einmal vollständig auf 100 % geladen, um den Referenzpunkt des SOC neu zu bestimmen.

## 3. Warum ist eine Kalibrierung notwendig?

Ohne regelmäßige Kalibrierung kann es zu folgenden Abweichungen kommen:

- Ungenaue SOC-Anzeige  
- Frühzeitiges Abschalten oder unerwartet schneller Ladeabfall  
- Beeinträchtigung der Nachladelogik (z. B. falscher Lade-/Entladezeitpunkt)  

## 4. So richtest du die Energiekalibrierung ein

👉 Schritte in der App: Geräteansicht → Gerät auswählen → <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/> → SoC-Einstellungen → Energiekalibrierung

<img src={require("../energy-mode/img/select_device.png").default} width="240"/>
<img src={require("../energy-mode/img/device_info.png").default} width="240"/>
<img src={require("../energy-mode/img/device_setting.png").default} width="240"/>
<img src={require("./img/soc_settings.png").default} width="240"/>

| Einstellung | Beschreibung | Empfehlung |
|------------|-------------|-------------|
| Kalibrierungsintervall | Zeitraum seit der letzten Vollladung (5–60 Tage) | Empfohlen: 14 Tage |
| Startzeitpunkt der Kalibrierung | Zeitpunkt, ab dem die Kalibrierung ausgeführt werden darf | Tagsüber mit hoher PV-Leistung oder nachts mit niedrigen Strompreisen |
| Ladeleistung | Aktuelle Nachladeleistung (AC-Leistung, Standardwert: 500 W) | Entsprechend der elektrischen Anschlusskapazität einstellen |

<img src={require("./img/calibration_interval.png").default} width="240"/>
<img src={require("./img/calibration_start_time.png").default} width="240"/>
<img src={require("./img/charging_power.png").default} width="240"/>