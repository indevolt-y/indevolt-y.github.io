---
title: Bypass
description: Erfahren Sie mehr über die Funktionen, die Arbeitslogik und das Verhalten des Indevolt-Mikrospeichers Bypass-Anschlusses in verschiedenen Szenarien
---

# Bypass

Der Bypass-Anschluss (Backup) ist eine Schnittstelle mit automatischer Richtungsumschaltung, die keine manuelle Konfiguration erfordert. Er kann angeschlossen werden als:
- 🔌 Elektrische Verbraucher → als Ausgang (Stromversorgung)
- ☀️ PV-Mikro-Wechselrichter → als Eingang (Einspeisung)

---

## 1. Wie das Gerät automatisch erkennt

Das System erkennt den angeschlossenen Typ automatisch anhand von **Leistungsrichtung + Dauer**:

| Typ   | Erkennungskriterium |
|------|---------------------|
| Last | **Ausgangsleistung** über 30 W für mehr als 20 Sekunden |
| Mikro-Wechselrichter | **Eingangsleistung** über 30 W für mehr als 5 Sekunden |

> - Im Inselbetrieb bleibt das System bei 0 W am Bypass-Anschluss im zuletzt erkannten Zustand  
> - Nach einem Neustart wird standardmäßig der Lastbetrieb aktiviert  

---

## 2. Verhalten in verschiedenen Szenarien

Das Systemverhalten hängt von zwei Faktoren ab:
- Vorhandensein des Stromnetzes (netzgekoppelt / Inselbetrieb)
- Art des angeschlossenen Geräts (Last oder Mikro-Wechselrichter)

:::info

Die Leistungsfähigkeit des Bypass-Anschlusses hängt von der Anzahl der Batterieeinheiten ab. Eine einzelne Haupteinheit hat begrenzte Leistung und erreicht möglicherweise nicht die unten genannten Maximalwerte. Für höhere Leistungen müssen zusätzliche Batteriepacks hinzugefügt werden.

Empfohlene Mindestkonfiguration:
- 1 × SolidFlex 2000 + 2 × SFA1800  
- 1 × PowerFlex 2000 + 1 × PFA2000  
:::

---

### 2.1 Netzbetrieb mit Last

Die Last wird entweder vom Netz oder vom Wechselrichter des Systems versorgt.

Leistungsbereich:
- Bis **3600 W**: normaler Betrieb  
- Über **3600 W** (Strom ≤ 16 A) für mehr als 5 Sekunden: Schutz wird ausgelöst, Bypass wird getrennt, automatische Wiederherstellung nach 15 Minuten

Batterieschutz:
- Entladung wird bei SOC 5 % gestoppt  

---

### 2.2 Netzbetrieb mit Mikro-Wechselrichter

Die Energie des Mikro-Wechselrichters versorgt die Last und lädt die Batterie; überschüssige Energie kann innerhalb der Grenzen ins Netz eingespeist werden.

Leistungsbereich:
- Bis **2400 W**: normaler Betrieb  
- Über **2400 W** für mehr als 30 Sekunden: Schutz wird ausgelöst, Bypass wird getrennt, automatische Wiederherstellung nach 15 Minuten  

Einspeisebegrenzung:
- Wenn die Eingangsleistung des Bypass-Anschlusses die maximale Einspeisebegrenzung um mehr als 10 % überschreitet und dies länger als 30 Sekunden anhält, trennt das System den Bypass-Anschluss prioritär und stellt den Betrieb nach 15 Minuten wieder her  

---

#### 2.2.1 Verhalten im netzgekoppelten Energiemodus

Im Netzbetrieb verteilt das System die Energie automatisch je nach Betriebsmodus. Dabei gilt stets: Zuerst wird der Hausverbrauch gedeckt oder die Batterie geladen, erst danach erfolgt die Netzeinspeisung. Je nach Modus unterscheiden sich die Prioritäten zwischen „Last“ und „Batterie“.

Der **Mikro-Wechselrichter** wird im System als **zusätzliche PV-Quelle** behandelt. Die Hauptquelle bleibt die direkt angeschlossene PV. Beide Quellen werden automatisch koordiniert, ein manuelles Umschalten ist nicht erforderlich.


##### Umgang mit überschüssiger Energie

Wenn mehr Energie vorhanden ist als benötigt (Last gedeckt + Batterie voll):

| Einspeisegrenze überschritten | Systemverhalten |
|------------------------------|-----------------|
| Nicht überschritten | Überschuss wird ins Netz eingespeist |
| Überschritten | Systemregelung zur Begrenzung:<br />- Zu hohe Mikro-Wechselrichterleistung: Bypass wird getrennt<br />- Wenn nur die Direkt-PV die Grenze überschreitet: PV-Leistung wird reduziert |

> **Einstellung der Einspeisebegrenzung:**  
> INDEVOLT App: Geräte-Seite → Gerät auswählen → <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/> → Leistungseinstellungen → Einspeisebegrenzung

---

##### Modus 1: Eigenverbrauch priorisiert

1. Mikro-Wechselrichter versorgt zuerst die Last  
2. Danach wird die Batterie geladen  
3. Wenn Last gedeckt und Batterie voll ist, erfolgt Einspeisung gemäß [Regel für überschüssige Energie](#umgang-mit-überschüssiger-energie)

---

##### Modus 2: Benutzerdefinierter Lade-/Entladeplan

**(1) Laden**

- **A. Nur Solar laden**
  1. Mikro-Wechselrichter lädt zuerst die Batterie  
  2. Danach Versorgung der Last  
  3. Wenn Batterie voll und Last gedeckt: Einspeisung gemäß [Regel für überschüssige Energie](#umgang-mit-überschüssiger-energie)

- **B. Laden über Solar + Netz**
  1. Priorität für direkte PV zum Laden der Batterie:
     - Wenn PV-Leistung ausreichend ist (über der eingestellten Ladeleistung): Batterie wird durch PV geladen, Mikro-Wechselrichter versorgt die Last
     - Wenn PV nicht ausreicht: Mikro-Wechselrichter unterstützt das Laden der Batterie, Überschuss versorgt die Last
  2. Wenn Batterie voll ist, versorgt der Mikro-Wechselrichter zuerst die Last  
  3. Wenn Batterie voll und Last gedeckt ist: Einspeisung gemäß [Regel für überschüssige Energie](#umgang-mit-überschüssiger-energie)

**(2) Entladen**

1. Mikro-Wechselrichter versorgt zuerst die Last  
2. Danach wird die Batterie geladen  
3. Wenn Batterie voll und Last gedeckt: Einspeisung gemäß [Regel für überschüssige Energie](#umgang-mit-überschüssiger-energie)

---

##### Modus 3: Echtzeitsteuerung

**(1) Leerlauf / Laden**

1. Mikro-Wechselrichter lädt zuerst die Batterie  
2. Wenn Batterie voll:
   - Leistung ≤ 50 W: Zustand wird gehalten (Eigenverbrauch des Systems)
   - Leistung > 50 W für mehr als 30 Sekunden: Bypass wird getrennt und PV-Leistung reduziert, sodass die Systemleistung wieder unter 50 W fällt

**(2) Entladen**

1. Mikro-Wechselrichter versorgt zuerst die Last  
2. Danach wird die Batterie geladen  
3. Wenn Batterie voll:
   - Leistung ≤ <u>eingestellte Entladeleistung + Toleranz</u>: normaler Betrieb  
   - Leistung > <u>eingestellte Entladeleistung + Toleranz</u>: Bypass wird getrennt  

> *Toleranz = 50 W oder 10 % der Sollleistung (je nachdem, was größer ist)*  
>
> *Beispiel:*  
> - *Sollleistung 400 W → Schutz bei 450 W*  
> - *Sollleistung 800 W → Schutz bei 880 W*

---

### 2.3 Inselbetrieb mit Last

Nach Trennung vom Stromnetz wird die Last vom Systemwechselrichter versorgt.

Leistungsbereich:
- Bis 2400 W + 2 % (2448 W): stabiler Betrieb  
- 2448 W ~ 2640 W: 30 s Überlast möglich  
- 2640 W ~ 3000 W: 15 s Überlast möglich  
- Über 3000 W: 100 ms Überlast möglich  
- Wenn Überlast überschritten wird: Bypass wird getrennt, automatische Wiederherstellung nach 15 Minuten  

---

### 2.4 Inselbetrieb mit Mikro-Wechselrichter

- EMS < 1.01.05  
   ❌ Mikro-Wechselrichter wird nicht unterstützt (Bypass wird automatisch deaktiviert zum Schutz des Geräts)

- EMS ≥ 1.01.05  
   ✅ Unterstützung für Mikro-Wechselrichter  
  - Leistungsbereich: 30 W ~ 1200 W  
  - Wenn SOC unter 3 % fällt, reagiert der Systemwechselrichter nicht auf den Mikro-Wechselrichter, der Bypass bleibt jedoch aktiv. Sobald SOC wieder ≥ 3 % ist, wird der Betrieb automatisch fortgesetzt  

---

## 3. Ein-/Ausschalten des Bypass-Anschlusses

Steuerung abhängig vom Netzwerkstatus:

| Netzwerkstatus | Steuerung |
|--------------|-----------|
| Normal       | App / Bluetooth |
| Fehler       | Nur Bluetooth |


### Methode 1: Remote-Steuerung über App (Netzwerk aktiv)

INDEVOLT App → Gerät → <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/> → Bypass Socket → Aktivieren → Gerätetyp auswählen

<img src={require("../energy-mode/img/select_device.png").default} width="240"/>
<img src={require("../energy-mode/img/device_info.png").default} width="240"/>
<img src={require("../energy-mode/img/device_setting.png").default} width="240"/>
<img src={require("./img/bypass.png").default} width="240"/>


### Methode 2: Lokale Bluetooth-Verbindung (kein Netzwerk)

INDEVOLT App → Profil / Login → Direktverbindung zum Gerät → QR-Code scannen → Gerät verbinden → <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/> → Bypass Socket → Aktivieren  

<img src={require("./img/profile.png").default} width="240"/>
<img src={require("./img/login.png").default} width="240"/>
<img src={require("./img/scan_qr_code2.png").default} width="240"/>
<img src={require("./img/direct_connect.png").default} width="240"/>
<img src={require("./img/direct_connect_device_page.png").default} width="240"/>
<img src={require("./img/direct_connect_device_settings.png").default} width="240"/>

**Hinweis zum Inselbetrieb**

Wenn im Inselbetrieb der Schlafmodus aktiv ist und der Übergang von **Standby zu Abschaltung** erreicht wird, wechselt das Gerät in den **Ruhezustand**, und der Bypass-Anschluss wird **automatisch deaktiviert**. Er kann anschließend auf folgende Weise wieder aktiviert werden:

1. Power-Taste kurz drücken  
2. Je nach Netzwerkstatus die entsprechende Steuerungsmethode verwenden  