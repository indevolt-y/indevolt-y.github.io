---
title: Geräte verknüpfen
description: Verknüpfen Sie Ihr INDEVOLT-Mikro-Energiespeichersystem mit Ihren Haushaltsgeräten, um ein intelligenteres und sichereres Energiemanagement zu ermöglichen.
---

# Geräte verknüpfen

Durch die Verknüpfung des Mikro-Energiespeichersystems mit anderen Geräten im Haushalt, wie z. B. Smart-Steckdosen, intelligenten Stromzählern oder Zählerauslesegerätn, können Verbrauchsdaten sicher innerhalb des lokalen Netzwerks ausgetauscht werden. Dadurch erkennt das System den aktuellen Energiebedarf präziser und passt die Lade- und Entladeleistung automatisch an.

## Warum andere Geräte verknüpfen?

Ist kein weiteres Gerät mit dem Mikro-Energiespeicher verknüpft, kann dieser Änderungen des Stromverbrauchs nicht erkennen und arbeitet ausschließlich nach festen Regeln:

- Der aktuelle Stromverbrauch im Haushalt ist nicht bekannt, sodass die Leistung nicht automatisch an den tatsächlichen Verbrauch angepasst werden kann.
- Laden und Entladen erfolgen ausschließlich mit einer festen Leistung oder nach einem Zeitplan.

Dies kann in der Praxis zu folgenden Situationen führen:

- **Zu hohe Entladeleistung** → Überschüssige Energie wird ins öffentliche Stromnetz eingespeist.
- **Zu geringe Entladeleistung** → Der Haushalt muss weiterhin Strom aus dem Netz beziehen und die Batterie wird nicht optimal genutzt.

:::tip
Der Hauptzweck der Geräteverknüpfung besteht darin, dem Mikro-Energiespeicher **Rückmeldungen zum aktuellen Stromverbrauch bereitzustellen**, sodass Laständerungen in Echtzeit erkannt und Lade- bzw. Entladeleistung dynamisch angepasst werden können.
:::

## Welche Geräte können verknüpft werden?

Je nach Anwendungsszenario können folgende Gerätetypen mit dem Mikro-Energiespeicher verknüpft werden:

### Smart-Steckdose

Geeignet für Anwendungen, bei denen **einzelne Verbraucher oder bestimmte Geräte** gezielt überwacht und versorgt werden sollen.

**Funktionen**

- Erfasst den Stromverbrauch der angeschlossenen Geräte in Echtzeit.
- Der Mikro-Energiespeicher passt seine Entladeleistung exakt an den Verbrauch dieser Steckdose an.
- Nur die an dieser Steckdose angeschlossenen Geräte werden mit Energie versorgt, ohne andere Stromkreise zu beeinflussen.

### Intelligenter Stromzähler

Ideal für Nutzer, die den **gesamten Stromverbrauch des Haushalts** verwalten möchten.

**Funktionen**

- Erfasst den gesamten Stromverbrauch des Haushalts in Echtzeit.
- Erkennt, ob Strom aus dem Netz bezogen oder ins Netz eingespeist wird.
- Passt die Leistung des Mikro-Energiespeichers automatisch an, um eine **Nulleinspeisung** oder einen maximalen Eigenverbrauch zu erreichen.

### Zählerauslesegerät

Eine Alternative, wenn der Stromzähler selbst keine Netzwerkverbindung unterstützt.

**Funktionsweise**

- Der Mikro-Energiespeicher kommuniziert nicht direkt mit dem Stromzähler.
- Der Zählerauslesegerät liest die Daten des Stromzählers aus.
- Anhand dieser Verbrauchsdaten wird die Leistung des Mikro-Energiespeichers indirekt geregelt.

## Geräte verknüpfen

:::info Voraussetzungen
Stellen Sie vor dem Verknüpfen sicher, dass folgende Voraussetzungen erfüllt sind:

- Der Mikro-Energiespeicher und das zu verknüpfende Gerät (z. B. Smart-Steckdose, Stromzähler oder Zählerauslesegerät) wurden **demselben Zuhause hinzugefügt**.
- Alle zu verknüpfenden Geräte sind **eingeschaltet und mit dem Netzwerk verbunden**.

👉 Falls Geräte noch nicht hinzugefügt wurden, lesen Sie zunächst: [Gerät hinzufügen](../../app/add-device.md)
:::

1. Öffnen Sie in der INDEVOLT App die Seite **Gerät** und tippen Sie auf die Gerätekarte des Mikro-Energiespeichers, um die **Gerätedetails** zu öffnen.
2. Tippen Sie unten auf der Seite auf **+ Untergerät hinzufügen**.
3. Wählen Sie in der Liste **Verfügbare Geräte** das gewünschte Gerät aus.
4. Tippen Sie auf **Verknüpfen** und warten Sie, bis die Konfiguration abgeschlossen ist.

<img src={require("../energy-mode/img/select_device.png").default} width="240"/>
<img src={require("./img/device_info.png").default} width="240"/>
<img src={require("./img/link_device.png").default} width="240"/>

Nach erfolgreicher Verknüpfung wird das verknüpfte Gerät als Karte im unteren Bereich der Gerätedetailseite angezeigt. Tippen Sie auf die Karte des Untergeräts, um Echtzeit-Leistung, Betriebsstatus und Verlaufsdaten anzuzeigen.

<img src={require("./img/device_linked.png").default} width="240"/>