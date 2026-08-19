---
title: Lade-/Entladeplan
description: Zeitgesteuertes Laden und Entladen zur präzisen Steuerung des Energieverbrauchs
---

# Lade-/Entladeplan

Der Modus „Lade-/Entladeplan“ ermöglicht es dir, für verschiedene Zeiträume eines Tages festzulegen, wann das System laden, entladen oder im Standby bleiben soll.

Nach der Konfiguration läuft das System automatisch entsprechend deinem Zeitplan, ohne dass tägliche manuelle Anpassungen erforderlich sind.

## Für welche Nutzer geeignet?

Dieser Modus ist besonders geeignet, wenn du:

- in einer Region mit **Zeit- / Spitzen- und Niedrigtarifen** lebst  
- deutliche Unterschiede zwischen Tages- und Nachtverbrauch hast  
- regelmäßige und stabile Nutzungsgewohnheiten besitzt  

## Funktionsweise des Systems

In diesem Modus kann ein Tag in mehrere Zeitintervalle unterteilt werden, wobei jedem Intervall ein Betriebsmodus zugewiesen wird:

- Laden: Das System lädt die Batterie mit der festgelegten Leistung  
- Entladen: Das System versorgt die Last basierend auf Verbrauch oder eingestellter Leistung  
- Standby: Keine aktive Lade- oder Entladeaktivität  

**Priorität des Energieverbrauchs**

- Haushaltsverbrauch wird **zuerst durch PV-Strom gedeckt**  
- Bei unzureichender PV-Leistung entlädt **die Batterie zur Unterstützung**  
- Nur wenn PV und Batterie nicht ausreichen, wird **Netzstrom bezogen**

## Lastauswahl

| Lastauswahl | Entladezeitraum | Ladezeitraum |
|-------------|----------------|--------------|
| Intelligente Steckdose | Das System regelt die Entladung basierend auf der tatsächlichen Leistung der angeschlossenen Geräte.<br/>Eine zusätzliche Leistungskompensation kann eingestellt werden:<br/>Effektive Entladeleistung = Lastleistung + Kompensationswert | Das System lädt gemäß der im Zeitplan festgelegten Leistung |
| Zähler | Das System regelt auf „0 Netzleistung“:<br/>- Positive Leistung → Entladung zur Kompensation<br/>- Negative Leistung → Laden von Überschussenergie | Laden gemäß geplanter Leistung |
| Schlüssel-Last | Versorgung erfolgt nur über den Bypass-Ausgang, keine Netzeinspeisung | Laden gemäß geplanter Leistung |
| Benutzerdefinierte (Lastkurve) | Entladung gemäß definierter Lastkurve | Laden gemäß geplanter Leistung |

:::info
Wenn Intelligente Steckdose oder Zähler offline sind, wechselt das System automatisch auf die Lastkurvensteuerung.
:::

:::info
Zur Vermeidung von Überlastungen verwendet das System automatisch den jeweils kleinsten Sicherheitswert:
- Beim Entladen: Minimum aus AC-Ausgangsleistung, Lastkurve und tatsächlicher Last  
- Beim Laden: Minimum aus AC-Eingangsleistung und Ladeleistung  
:::

## So richtest du den benutzerdefinierten Plan ein

**Schritte:**

1. Stelle sicher, dass das Gerät in der **INDEVOLT App** deinem Zuhause hinzugefügt wurde  
2. Öffne unten den Tab **Geräte** und wähle das entsprechende Gerät aus  
3. Tippe auf den Bereich „Energiemodus“ und öffne die Modusauswahl  
4. Wähle **Lade-/Entladeplan** und tippe auf **Einstellungen**  
5. Tippe auf **+ Plan hinzufügen**:  
   - Start- / Endzeit festlegen  
   - Betriebsmodus wählen: Laden / Entladen / Standby  
   - Entsprechende Betriebsparameter konfigurieren  
6. Tippe auf **Speichern**, die Einstellung wird sofort übernommen  

<img src={require("./img/select_device.png").default} width="240"/>
<img src={require("./img/select_energy_mode.png").default} width="240"/>
<img src={require("./img/charge_discharge_schedule.png").default} width="240"/>
<img src={require("./img/select_add_plan.png").default} width="240"/>
<img src={require("./img/add_plan.png").default} width="240"/>

## Empfohlene Geräteeinstellungen

Öffne in der Geräteansicht oben rechts das **⚙** Symbol, um die Konfiguration aufzurufen.

<img src={require("./img/device_info.png").default} width="240"/>
<img src={require("./img/device_setting.png").default} width="240"/>

Für eine stabile Nutzung werden folgende Einstellungen empfohlen:

| Einstellung | Empfehlung |
|-------------|-----------|
| Maximale AC-Ausgangsleistung (Entladen) | Nicht unterhalb der tatsächlichen Haushaltslast und gemäß lokalen Vorschriften |
| Maximale AC-Eingangsleistung (Laden) | Nicht unterhalb der gewünschten Ladeleistung |
| Einspeisebegrenzung | Empfohlen: `0` (Anti-Rückeinspeisung aktivieren) |
| Bypass | Ohne besonderen Bedarf deaktiviert lassen |
| Notstromreserve | Empfohlen: 20 % |