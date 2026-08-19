---
title: CT-Multipositionsüberwachung für Dreiphasenstromzähler
description: Durch die Installation von drei CTs auf der PV-, Netz-, Last- oder Batterieseite können Leistungs- und Verbrauchsdaten an verschiedenen Systempositionen erfasst werden.
---

# CT-Multipositionsüberwachung für Dreiphasenstromzähler

In einem Dreiphasensystem werden die drei Phasenleiter L1, L2 und L3 üblicherweise jeweils mit einem CT ausgestattet, um die Gesamtleistung und Energiedaten des Systems zu messen.

Die drei CTs müssen jedoch nicht zwingend auf die drei Phasen verteilt werden. Je nach Anwendung können sie auch an unterschiedlichen Stromkreisen wie PV, Netz, Last oder Batterie installiert werden, um gleichzeitig Messdaten aus verschiedenen Systembereichen zu erfassen.

---

## 1. Unterstützte Stromzähler

| Marke     | Modell                                                         |
| --------- | -------------------------------------------------------------- |
| INDEVOLT  | SMD3                                                          |
| SOLARMAN  | MR3-D5-WR<br />MR3-D4-WE-B<br />MR3-D5-W<br />MR3-D4-WRE-B    |
| Shelly    | Shelly 3EM<br />Shelly Pro 3EM-400<br />Shelly Pro 3EM-3CT63  |

---

## 2. CT-Installationspositionen

Die Installationsposition des CT bestimmt die erfassten Daten.

| CT-Position | Zugeordnete Daten                     | Typische Anwendung |
|------------|---------------------------------------|--------------------|
| PV-Seite   | PV-Erzeugungsleistung                 | Überwachung der Stromerzeugung |
| Netzseite  | Import-/Exportleistung (je nach Richtung) | Netzüberwachung (Einspeise-/Bezugsanalyse) |
| Lastseite   | Verbrauchsleistung                    | Verbrauchsüberwachung |
| Batterie    | Lade-/Entladeleistung                 | Überwachung des Speicherstatus |

CTs an unterschiedlichen Positionen zeigen gleichzeitig unterschiedliche Werte, die gemeinsam den Gesamtzustand des Systems abbilden.

---

## 3. CT-Installationsrichtung

Der Pfeil auf dem CT-Gehäuse zeigt die Referenzrichtung des Stromflusses an. Eine falsche Installation beschädigt das Gerät nicht, führt jedoch zu invertierten Leistungswerten.

Beispielsweise kann Netzbezug als Einspeisung angezeigt werden oder Batterieladung als Entladung erscheinen.

Bei abweichenden Daten prüfen Sie bitte:
- Ob der CT in die richtige Richtung installiert wurde  
- Ob die CT-Richtungseinstellung in der App korrekt ist  

:::note
Falls die physische Installation nicht angepasst werden kann, lässt sich die CT-Richtung auch in der App korrigieren.
:::

---

## 4. App-Konfiguration

### 4.1 CT-Installationsposition einstellen

1. Öffnen Sie die Zählereinstellungen und wählen Sie **Zählerkonfiguration > Einphasensystem**.  
2. Ordnen Sie die drei CTs den tatsächlichen Installationspositionen zu (PV, Netz, Last oder Batterie).  
3. Stellen Sie die CT-Richtung entsprechend der physischen Pfeilrichtung ein. Prüfen Sie anhand der Abbildungen, ob die Richtung korrekt ist.

Nach der Konfiguration können Sie im Zählerbereich die Daten der drei CTs separat anzeigen, einschließlich Leistung, Energie, Strom und Spannung.

<img src={require("./img/ct_direction.png").default} width="240"/>
<img src={require("./img/ct_location.png").default} width="240"/>
<img src={require("./img/meter_data.png").default} width="240"/>

### 4.2 Lastquelle für Mikro-Energiespeicher konfigurieren (optional)

Wenn der Mikro-Energiespeicher automatisch auf Basis der Last geregelt werden soll, kann unter **Last-Einstellungen > Zähler** die entsprechende CT-Phase als Referenzquelle ausgewählt werden.

<img src={require("./img/load_settings.png").default} width="240"/>
<img src={require("./img/load_meter.png").default} width="240"/>

---

## 5. Prüfung der korrekten Konfiguration

Nach der Einrichtung kann die Funktion anhand des Betriebsverhaltens überprüft werden:

- Bei PV-Erzeugung sollte die PV-Leistung positiv angezeigt werden  
- Beim Netzbezug sollte der Import korrekt dargestellt werden  
- Beim Laden der Batterie sollte Ladeleistung angezeigt werden  
- Beim Einschalten der Last sollte die Verbrauchsleistung steigen  

Bei abweichenden oder invertierten Werten prüfen Sie:
- CT-Installationsposition  
- CT-Richtung  
- App-Konfiguration im Vergleich zur realen Installation  
- Ob der CT korrekt geschlossen und fest angebracht ist  