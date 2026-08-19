---
title: Temperatur-Derating PV/Batterie
description: Überblick über Leistungsbegrenzungen bei hohen und niedrigen Temperaturen
---

# Temperatur-Derating von PV- und Batteriesystemen

Das System kann innerhalb eines definierten Temperaturbereichs mit voller Leistung betrieben werden. Bei zu hohen oder zu niedrigen Temperaturen reduziert das System automatisch die Leistung. Dieses Verhalten wird als **Derating** bezeichnet.

Derating ist ein normaler Schutzmechanismus. Ziel ist es, den Betrieb in einem sicheren Zustand zu gewährleisten, Schäden durch Überhitzung oder Unterkühlung zu vermeiden und die Lebensdauer der Geräte zu verlängern. Sobald die Temperatur wieder in den zulässigen Bereich zurückkehrt, wird die Nennleistung automatisch wiederhergestellt. Eine manuelle Intervention ist nicht erforderlich.

---

## PV-Temperatur-Derating

Im Normalbetrieb maximiert das System die PV-Erzeugung. Steigt jedoch die Temperatur, kann ein dauerhafter Betrieb unter Volllast zu zusätzlicher thermischer Belastung führen. Wenn die Temperatur des internen PV-Leistungswandlers (MPPT) zu hoch wird, reduziert das System automatisch die PV-Leistung, um das Gerät zu schützen.

:::info
Die ECO-Serie verfügt nicht über einen PV-Gleichstromeingang und unterstützt keine direkte PV-Anbindung. Dieser Abschnitt ist für diese Serie nicht relevant.
:::

### Warum kommt es zum Derating?

Der PV-Leistungswandler (DC/DC-Konverter) erzeugt während der Energieumwandlung kontinuierlich Wärme. Mit steigender Leistung nimmt die Wärmeentwicklung zu. Zusätzlich können äußere Bedingungen die Temperatur weiter erhöhen, z. B.:

- hohe Umgebungstemperaturen am Mittag im Sommer  
- unzureichende Belüftung des Installationsortes  

Bei anhaltend hohen Temperaturen kann ein Betrieb unter Volllast zu Überhitzung, Effizienzverlust oder Geräteschäden führen. Daher reduziert das System aktiv die Ausgangsleistung, um einen sicheren Betrieb sicherzustellen.

### Auswirkungen im Betrieb

Im praktischen Einsatz äußert sich PV-Derating wie folgt:

- Die PV-Leistung erreicht nicht die theoretische Spitzenleistung  
- Die Leistungskurve wird zur Mittagszeit sichtbar „abgeschnitten“  

Diese Effekte sind normal und stellen keinen Fehler dar.

### Derating-Logik

Wenn die Temperatur des PV-Leistungswandlers (MPPT) ansteigt, wird die maximale PV-Leistung stufenweise reduziert. Nach Abkühlung erfolgt eine automatische Rückkehr zur Nennleistung:

* **Bei Temperaturen über 93 °C** wird die maximale Leistung auf **80 % der Nennleistung** reduziert

  * Beispiel: Gesamtleistung sinkt auf `2400 W × 80 % = 1920 W`; pro PV-Eingang auf `600 W × 80 % = 480 W`
  * Rückkehr zur Nennleistung bei Temperaturen unter **75 °C**

* **Bei Temperaturen über 96 °C** wird die maximale Leistung auf **60 % der Nennleistung** reduziert

  * Beispiel: Gesamtleistung sinkt auf `2400 W × 60 % = 1440 W`; pro PV-Eingang auf `600 W × 60 % = 360 W`
  * Rückkehr zur Nennleistung bei Temperaturen unter **80 °C**

:::note
Die MPPT-Temperatur wird in der aktuellen App-Version nicht angezeigt.
:::

---

## Batterie-Temperatur-Derating

Im Vergleich zum PV-System reagiert die Batterie deutlich empfindlicher auf Temperaturänderungen. Daher gelten strengere Schutzmechanismen. Sowohl hohe als auch niedrige Temperaturen können zu einer Leistungsreduzierung führen.

### Warum kommt es zum Derating?

Batterien basieren auf elektrochemischen Prozessen, die stark temperaturabhängig sind:

- **Hohe Temperaturen**: beschleunigen die Alterung und können Sicherheitsrisiken verursachen  
- **Niedrige Temperaturen**: verlangsamen die chemischen Reaktionen und können Ladeprozesse schädigen  

Daher begrenzt das System die Lade- und Entladeleistung, um einen sicheren Betrieb sicherzustellen.

### Auswirkungen im Betrieb

- reduzierte Ladegeschwindigkeit oder kein Laden möglich  
- reduzierte Entladeleistung  
- Nennleistung kann nicht erreicht werden  

### Derating-Logik

Die maximale Lade- und Entladeleistung wird temperaturabhängig dynamisch angepasst:

- **Hohe Temperaturen**: Reduzierung der Ladeleistung und Begrenzung der Entladeleistung; bei weiterem Temperaturanstieg wird der Betrieb vollständig gestoppt, um Überhitzung zu vermeiden.  
- **Niedrige Temperaturen**: vorrangige Begrenzung der Ladeleistung, da das Laden bei Kälte zu irreversiblen Zellschäden führen kann. Auch die Entladeleistung wird reduziert. Im Winter kann es daher vorkommen, dass Entladen möglich ist, Laden jedoch nicht.

Die Tabellenwerte beziehen sich jeweils auf ein einzelnes Hauptgerät bzw. Batteriemodul. Die tatsächliche Systemleistung ergibt sich aus:
**Einzelwert × Anzahl der Module**, darf jedoch die maximale Systemleistung nicht überschreiten.

<table>
<thead>
  <tr>
    <th></th>
    <th colspan="2">SolidFlex 2000 / SolidFlex 2000 Eco / SFA1800</th>
    <th colspan="2">PowerFlex 2000 / PowerFlex 2000 Eco / PFA2000</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Temperatur (°C)</td>
    <td>Max. Ladeleistung (W)</td>
    <td>Max. Entladeleistung (W)</td>
    <td>Max. Ladeleistung (W)</td>
    <td>Max. Entladeleistung (W)</td>
  </tr>
  <tr>
    <td>≤ -20</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>-20 < T ≤ -10</td>
    <td>0</td>
    <td>304</td>
    <td>0</td>
    <td>341</td>
  </tr>
  <tr>
    <td>-10 < T ≤ 0</td>
    <td>0</td>
    <td>380</td>
    <td>0</td>
    <td>426</td>
  </tr>
  <tr>
    <td>0 < T ≤ 4</td>
    <td>179</td>
    <td>761</td>
    <td>200</td>
    <td>853</td>
  </tr>
  <tr>
    <td>4 < T ≤ 10</td>
    <td>537</td>
    <td>761</td>
    <td>602</td>
    <td>853</td>
  </tr>
  <tr>
    <td>10 < T ≤ 52</td>
    <td>896</td>
    <td>1075</td>
    <td>1004</td>
    <td>1205</td>
  </tr>
  <tr>
    <td>52 < T ≤ 53 (Rückkehr zur Nennleistung unter 51 °C)</td>
    <td>448</td>
    <td>380</td>
    <td>502</td>
    <td>426</td>
  </tr>
  <tr>
    <td>&gt; 53</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
</tbody>
</table>

<img src={require("./img/bat_charging_power.png").default} width="960"/>
<img src={require("./img/bat_discharging_power.png").default} width="960"/>


### So wird die Batterietemperatur angezeigt

Schritte in der INDEVOLT App: Geräteansicht → Micro-Energy-Storage-Gerät auswählen → Einstellungen <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/> → **Temperatur** → Anzeige der Temperaturen von Hauptgerät und Batteriemodulen

<img src={require("../energy-mode/img/select_device.png").default} width="240"/>
<img src={require("../energy-mode/img/device_info.png").default} width="240"/>
<img src={require("./img/device_setting2.png").default} width="240"/>
<img src={require("./img/temperature.png").default} width="240"/>