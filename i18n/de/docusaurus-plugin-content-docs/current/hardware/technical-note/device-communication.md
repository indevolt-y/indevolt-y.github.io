---
title: Kommunikation mit externen Geräten
description: Erfahren Sie, wie der Mikrospeicher mit Stromzählern, Steckdosen und anderen Geräten kommuniziert und wie die Datenaktualisierung erfolgt
---

# Kommunikation mit externen Geräten

Wenn Sie einen Stromzähler, eine Steckdose oder ein anderes Gerät in das Mikrospeicher-System integrieren, kommuniziert das System automatisch mit diesen Geräten, um Verbrauchs- oder Erzeugungsdaten zu erfassen.

- **Lokale Kommunikation (LAN)**: zur Erfassung von Echtzeitdaten (schnelle Reaktion)
- **Cloud-Kommunikation (Remote)**: für App-Anzeige und historische Datenaufzeichnung

Die Kommunikationsmethoden unterscheiden sich je nach Hersteller leicht, das System passt sich jedoch automatisch an – eine manuelle Konfiguration ist nicht erforderlich.

| Marke       | Lokale Kommunikation | Cloud-Kommunikation |
| ---------- | -------------------- | ------------------- |
| Shelly     | HTTP                 | Mikrospeicher-Cloud |
| Ecotracker | HTTP                 | Mikrospeicher-Cloud |
| Stromleser | HTTP                 | Mikrospeicher-Cloud |
| HomeWizard | HTTP                 | Mikrospeicher-Cloud |
| SOLARMAN   | UDP-Broadcast       | Direkte Cloud-Übertragung  |
| INDEVOLT   | proprietäres Protokoll | Mikrospeicher-Cloud |

:::tip
„Mikrospeicher-Cloud“ bedeutet, dass die Daten zuerst an den Mikrospeicher gesendet und anschließend zentral in die Cloud hochgeladen werden.
:::

## 1. Lokale Kommunikation

Die lokale Kommunikation dient der Erfassung von **Echtzeitdaten**. Die Aktualisierungsrate kann je nach Gerät variieren.

:::info
Die Funktion zur Anpassung der Datenaktualisierungsrate ist derzeit noch nicht verfügbar und wird in zukünftigen App-Versionen bereitgestellt.
:::

### 1.1 Geräte mit HTTP-Kommunikation

Daten werden über eine lokale HTTP-Schnittstelle im LAN abgerufen. Diese Methode ist stabil und weit verbreitet.

- **Standard-Intervall**: 2 Sekunden  
- **Einstellbarer Bereich**:
  - SolidFlex 2000 / PowerFlex 2000: ≥ 1 Sekunde  
  - BK1600 / BK1600 Ultra: ≥ 2 Sekunden  

- **Unterstützte Geräte**

  <table><thead>
    <tr>
      <th>Marke</th>
      <th>Typ</th>
      <th>Modell</th>
    </tr></thead>
  <tbody>
    <tr>
      <td rowspan="3">Shelly</td>
      <td>Einphasen-Stromzähler</td>
      <td>Shelly Pro EM</td>
    </tr>
    <tr>
      <td>Dreiphasen-Stromzähler</td>
      <td>Shelly 3EM<br />Shelly Pro 3 EM (400)<br />Shelly Pro 3EM 3CT 63</td>
    </tr>
    <tr>
      <td>Smart-Steckdosen</td>
      <td>Shelly Plug<br />Shelly Plug S Gen3</td>
    </tr>
    <tr>
      <td>Ecotracker</td>
      <td>IR-Zählerausleser</td>
      <td>EcoTracker IR</td>
    </tr>
    <tr>
      <td>Stromleser</td>
      <td>IR-Zählerausleser</td>
      <td>stromleser.one</td>
    </tr>
    <tr>
      <td>Homewizard</td>
      <td>P1-Zählerausleser</td>
      <td>HWE-P1</td>
    </tr>
  </tbody>
  </table>

:::note

Die folgenden Geräte sind derzeit noch nicht in das Mikrospeicher-System integriert und werden noch nicht unterstützt:

<table><thead>
  <tr>
    <th>Marke</th>
    <th>Typ</th>
    <th>Modell</th>
  </tr></thead>
<tbody>
  <tr>
    <td rowspan="3">Shelly</td>
    <td>Einphasen-Stromzähler</td>
    <td>Shelly EM<br />Shelly EM Gen3</td>
  </tr>
  <tr>
    <td>Dreiphasen-Stromzähler</td>
    <td>Shelly 3EM-63T Gen3</td>
  </tr>
  <tr>
    <td>Smart-Steckdosen</td>
    <td>Shelly Wave Plug S<br />Shelly Plus Plug S<br />Shelly Outdoor Plug S Gen3</td>
  </tr>
</tbody>
</table>

:::


### 1.2 SOLARMAN-Geräte

SOLARMAN-Geräte senden Daten im LAN aktiv über **Broadcast**, ohne Polling. Dadurch ist die Echtzeitfähigkeit höher.

| Typ | Modell | Standardintervall | Mindestintervall |
| ---- | ------ | ----------------- | ---------------- |
| Einphasen-Stromzähler | MR1-D5-WR<br />MR1-D5-W | 150 ms | ≥150 ms |
| Dreiphasen-Stromzähler | MR3-D5-WR<br />MR3-D5-W<br />MR3-D4-WRE<br />MR3-D4-WE | 150 ms | ≥150 ms |
| IR-Zählerausleser | NIR-12-EU<br />NIR-32-EU | 150 ms | ≥150 ms |
| P1-Zählerausleser | P1-2W<br />P1-2W-C | 500 ms | ≥150 ms |
| Smart-Steckdose | SP-2W-EU | 500 ms | ≥150 ms |

:::note
Die folgenden Geräte befinden sich derzeit in der Anpassungsentwicklung und werden in zukünftigen Versionen unterstützt:
- P1-2WR
:::


### 1.3 INDEVOLT-Geräte

Kommunikation über ein proprietäres Protokoll.

- **Standardintervall**: 2 Sekunden  
- **Einstellbarer Bereich**: ≥ 1 Sekunde  

- **Unterstützte Geräte**

  | Typ | Modell |
  | ---- | ------ |
  | Einphasen-Stromzähler | SMD1 |
  | Dreiphasen-Stromzähler | SMD3 |
  | Smart-Steckdose | SP16 |

---

## 2. Cloud-Kommunikation

Cloud-Daten dienen der Fernüberwachung, z. B. zur Anzeige von Gerätestatus oder historischen Daten in der App.

Alle Geräte folgen denselben Regeln:
- **Standardintervall**: 300 Sekunden (5 Minuten)  
- **Bei aktivierter Schnellaktualisierung**: 1 Sekunde Aktualisierung