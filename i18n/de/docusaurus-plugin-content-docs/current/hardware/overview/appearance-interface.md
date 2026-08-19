---
title: Geräteübersicht und Schnittstellen
description: Übersicht über die Geräteoptik, Schnittstellen, Tastenfunktionen und LED-Statusanzeigen von Indevolt
---

# Geräteübersicht und Schnittstellen

## Geräteoptik

<img src={require("./img/appearance.png").default} width="480"/>

| Nr. | Funktion                                                         |
| --- | ---------------------------------------------------------------- |
| 1   | Betriebsstatus-LED                                               |
| 2   | Ein-/Aus-Taste                                                   |
| 3   | Funkmodul                                                        |
| 4   | MC4-PV-Eingang 1                                                 |
| 5   | MC4-PV-Eingang 2                                                 |
| 6   | MC4-PV-Eingang 3                                                 |
| 7   | MC4-PV-Eingang 4                                                 |
| 8   | Netzanschluss (Grid)                                             |
| 9   | Backup-Stromanschluss                                            |
| 10  | Schutzleiter-Schraubanschluss (mind. 4 mm² Leiterquerschnitt)    |
| 11  | Befestigungsbohrungen für Halterung                              |

:::info
ECO-Modelle verfügen nicht über die Anschlüsse 4–7.
:::

## Tastenfunktionen

| Bedienung                     | Funktion                          |
| ---------------------------- | --------------------------------- |
| 2 Sekunden im Aus-Zustand halten | Einschalten                    |
| 2 Sekunden im Ein-Zustand halten | Ausschalten                   |
| 10 Sekunden im Ein-Zustand halten | Bluetooth- und WLAN-Reset   |

## LED-Anzeigen

| LED                                                                                         | Beschreibung                               | Status            |
| ------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------- |
| <div class="table-img-box"><img src={require("./img/led-starting.png").default} /></div>    | Blaue LED leuchtet von der Mitte nach außen | Startvorgang      |
| <div class="table-img-box"><img src={require("./img/led-charging.png").default} /></div>    | Grüne LED steigt entsprechend des Ladezustands | Laden           |
| <div class="table-img-box"><img src={require("./img/led-discharging.png").default} /></div> | Blaue LED erlischt entsprechend des Ladezustands | Entladen      |
| <div class="table-img-box"><img src={require("./img/led-iot-failure.png").default} /></div> | LED leuchtet gelb                          | IoT-Verbindungsfehler |
| <div class="table-img-box"><img src={require("./img/led-fault.png").default} /></div>       | LED leuchtet rot                           | Fehler            |
| <div class="table-img-box"><img src={require("./img/led-shutdown.png").default} /></div>    | Blaue LED leuchtet von beiden Seiten zur Mitte | Abschaltvorgang |
| <div class="table-img-box"><img src={require("./img/led-reset.png").default} /></div>       | Blaue LED blinkt dreimal                   | Erfolgreicher Reset |