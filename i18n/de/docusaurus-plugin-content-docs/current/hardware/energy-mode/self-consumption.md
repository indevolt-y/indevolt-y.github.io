---
title: Eigenverbrauch
description: Bevorzugte Nutzung von Solarenergie zur Erhöhung des Eigenverbrauchsanteils
---

# Eigenverbrauch

Im Modus **Eigenverbrauch** passt das Indevolt Mikro-Energiespeichersystem die Lade- und Entladeleistung in Echtzeit an den Stromverbrauch des Haushalts an. Dabei wird die Solarenergie möglichst vorrangig genutzt, der Netzbezug reduziert und eine Rückeinspeisung ins Stromnetz vermieden.

Der gesamte Prozess erfolgt automatisch, ohne dass eine manuelle Steuerung erforderlich ist. Das System verteilt die Energie entsprechend der Konfiguration selbstständig.

## Für welche Nutzer geeignet?

Dieser Modus eignet sich für Nutzer, die:

- eine PV-Anlage installiert haben und ihren Eigenverbrauch maximieren möchten  
- die Stromkosten durch geringeren Netzbezug senken wollen  
- einen stabilen, regelmäßigen Energieverbrauch haben und keine häufigen Anpassungen wünschen  
- ein vollständig automatisiertes System bevorzugen  

## Funktionsweise des Systems

Im Modus „Eigenverbrauch“ verteilt das System die Energie automatisch basierend auf Erzeugung und Verbrauch.

**Priorität der Energieerzeugung**

- PV-Erzeugung versorgt **zuerst die Haushaltslasten**
- Überschüssige Energie lädt **den Akku**
- Erst wenn der Akku voll ist, kann überschüssige Energie ins Netz eingespeist werden (abhängig von den Einspeiseeinstellungen)

**Priorität des Energieverbrauchs**

- Haushaltsverbrauch wird **zuerst durch PV-Strom gedeckt**
- Bei unzureichender PV-Leistung entlädt **der Akku zur Unterstützung**
- Nur wenn PV und Akku nicht ausreichen, wird **Netzstrom bezogen**

## Lastauswahl

Um die Entladeleistung korrekt zu bestimmen, muss ein geeigneter Lasttyp ausgewählt werden:

**Intelligente Steckdose**

- Das System regelt die Entladung basierend auf der tatsächlich angeschlossenen Leistung
- Eine zusätzliche Leistungskompensation kann eingestellt werden
- Effektive Regelleistung = Lastleistung + Kompensationswert
- Geeignet für einzelne Geräte oder präzise Leistungssteuerung

**Zähler**

- Installation auf der **Netzeinspeiseseite**
- Das System regelt auf Zielwert „0 Netzleistung“:
  - Positiver Wert → Entladung zur Kompensation des Verbrauchs
  - Negativer Wert → Ladung zur Aufnahme überschüssiger Energie  
- Geeignet für Null-Einspeisung im gesamten Haushalt

**Schlüssel-Last**

- Versorgung erfolgt nur über den Bypass-Ausgang
- Keine Rückeinspeisung ins Netz
- Geeignet für wichtige Verbraucher, die priorisiert versorgt werden müssen

**Benutzerdefiniert (Lastkurve)**

- Der Tag kann in bis zu 48 Zeitintervalle unterteilt werden, jedes mit eigener Leistungsgrenze

:::info
Wenn die intelligente Steckdose oder der Zähler offline sind, wechselt das System automatisch auf die Leistung der Lastkurve.
:::

:::warning
Zu hohe oder falsch konfigurierte Lastkurven können zu Netzeinspeisung führen.
:::

## So richtest du den Eigenverbrauchsmodus ein

**Schritte:**

1. Stelle sicher, dass das Gerät in der **INDEVOLT App** deinem Zuhause hinzugefügt wurde  
2. Öffne unten den Tab **Geräte** und wähle das entsprechende Gerät aus  
3. Tippe auf den Bereich „Energiemodus“ und öffne die Modusauswahl  
4. Wähle **Eigenverbrauch** und tippe auf **Einstellungen**  
5. Wähle den passenden [Lasttyp](#lastauswahl) (Intelligente Steckdose / Zähler / Schlüssel-Last / Benutzerdefiniert)  
6. Tippe auf **Speichern**, die Einstellung wird sofort übernommen  

<img src={require("./img/select_device.png").default} width="240"/>
<img src={require("./img/select_energy_mode.png").default} width="240"/>
<img src={require("./img/self_consume_prioritized.png").default} width="240"/>
<img src={require("./img/load_settings.png").default} width="240"/>

## Empfohlene Geräteeinstellungen

Öffne in der Geräteansicht oben rechts das **⚙** Symbol, um die Einstellungen aufzurufen.

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