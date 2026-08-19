---
title: Echtzeit-Steuerung
description: Manuelle Steuerung von Laden, Entladen oder Standby des Geräts
---

# Echtzeit-Steuerung

Der Modus **Echtzeit-Steuerung** ermöglicht es dir, den Lade- und Entladezustand sowie die Leistung des Geräts jederzeit manuell zu steuern. Nach dem Setzen der Parameter setzt das System die Anweisung sofort um und stoppt automatisch, sobald die definierten Bedingungen erfüllt sind.

## Für welche Nutzer geeignet?

- Temporäre Anforderungen für schnelles Laden oder Entladen  
- Test-, Debug- oder Validierungsszenarien  
- Fortgeschrittene Nutzer mit Verständnis der Systemlogik  
- Kurzfristige manuelle Eingriffe in den Systembetrieb  

## Funktionsweise des Systems

Im Modus „Echtzeit-Steuerung“ müssen folgende Parameter manuell festgelegt werden:

- **Status**: Standby / Laden / Entladen  
- **Leistung**: 0–2400 W  
- **Ziel-SoC**: 5 %–100 %  

Nach dem Speichern wird das System sofort aktiv:

- **Laden**: Gerät lädt mit der eingestellten Leistung  
- **Entladen**: Gerät versorgt die Last mit der eingestellten Leistung  
- **Standby**: Gerät bleibt inaktiv (weder Laden noch Entladen)  

Sobald der Batteriestand den eingestellten **Ziel-SoC** erreicht, stoppt das System automatisch den Lade- oder Entladevorgang und wechselt in den Standby-Modus.

**Priorität des Energieverbrauchs**

- Der Haushaltsverbrauch wird **zuerst durch PV-Strom gedeckt**  
- Bei unzureichender PV-Leistung entlädt **der Akku zur Unterstützung**  
- Nur wenn PV und Akku nicht ausreichen, wird **Netzstrom bezogen**

## So richtest du die Echtzeit-Steuerung ein

**Schritte:**

1. Stelle sicher, dass das Gerät in der **INDEVOLT App** deinem Zuhause hinzugefügt wurde  
2. Öffne unten den Tab **Geräte** und wähle das entsprechende Gerät aus  
3. Tippe auf den Bereich „Energiemodus“ und öffne die Modusauswahl  
4. Wähle **Echtzeit-Steuerung** und tippe auf **Einstellungen**  
5. Konfiguriere die Parameter:  
   - Status: Standby / Laden / Entladen  
   - Leistung: 0–2400 W  
   - Ziel-SoC: 5 %–100 %  
6. Tippe auf **Speichern**, die Einstellung wird sofort übernommen  

<img src={require("./img/select_device.png").default} width="240"/>
<img src={require("./img/select_energy_mode.png").default} width="240"/>
<img src={require("./img/real_time_control.png").default} width="240"/>
<img src={require("./img/real_time_control_settings.png").default} width="240"/>
<img src={require("./img/real_time_control_status.png").default} width="240"/>
<img src={require("./img/real_time_control_power.png").default} width="240"/>
<img src={require("./img/real_time_control_soc.png").default} width="240"/>

## Empfohlene Geräteeinstellungen

Öffne in der Geräteansicht oben rechts das **⚙** Symbol, um die Konfiguration aufzurufen.

<img src={require("./img/device_info.png").default} width="240"/>
<img src={require("./img/device_setting.png").default} width="240"/>

Für eine stabile Nutzung werden folgende Einstellungen empfohlen:

| Einstellung | Empfehlung |
|------------|-----------|
| Max. AC-Ausgangsleistung (Entladung) | Nicht unterhalb der tatsächlichen Haushaltslast und entsprechend lokalen Vorschriften |
| Max. AC-Eingangsleistung (Ladung) | Nicht unterhalb der gewünschten Ladeleistung |
| Einspeisebegrenzung | Empfohlen: `0` (Anti-Rückeinspeisung aktivieren) |
| Bypass | Ohne besonderen Bedarf deaktiviert lassen |
| Notstromreserve | Empfohlen: 20 % |