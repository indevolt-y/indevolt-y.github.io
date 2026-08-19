---
title: Schnellstart
description: Installations- und Ersteinrichtungsanleitung für Indevolt-Energiespeichersysteme
---

# Schnellstart

Dieses Dokument gilt für die Energiespeichersysteme SolidFlex 2000 und PowerFlex 2000 und beschreibt den vollständigen Ablauf von der Inbetriebnahme nach dem Auspacken bis zur ersten Nutzung. Es umfasst die Überprüfung vor der Installation, die Montage des Geräts, das erstmalige Einschalten sowie das Hinzufügen des Geräts in der App.

:::warning

Lesen Sie vor der Installation unbedingt die **[Sicherheitshinweise](./safety.md)**, um eine sichere Verwendung zu gewährleisten.

:::

## Benötigte Werkzeuge

Bitte halten Sie vor der Installation die folgenden Werkzeuge bereit:

<img src={require("./img/tools.png").default} width="480"/>

---

## Auspacken und Lieferumfang prüfen

1. Stellen Sie sicher, dass die Verpackung unbeschädigt ist.
2. Öffnen Sie die Verpackung und entnehmen Sie das Gerät sowie alle Zubehörteile.
3. Vergleichen Sie den Inhalt mit der Packliste und prüfen Sie, ob Teile fehlen oder beschädigt sind.

   <img src={require("./img/power-packing-list.png").default} width="720"/>

   > Wenn Sie zusätzlich Batteriemodule erworben haben, prüfen Sie bitte auch die folgende Packliste.
   <img src={require("./img/battery-packing-list.png").default} width="720"/>

---

## Montage des Geräts

:::info
- Installieren Sie die Module nicht in Bereichen mit direkter Sonneneinstrahlung, in der Nähe von offenem Feuer oder in der Nähe von brennbaren bzw. explosiven Materialien.
- Stellen Sie sicher, dass der Installationsort vor möglichen Gefahren wie Überschwemmungen geschützt ist.
- Die Verwendung wird in Höhenlagen unter 2000 m empfohlen.
- Sorgen Sie für eine gute Belüftung am Installationsort, damit die Wärme zuverlässig abgeführt werden kann.
:::

**Schritt 1: Installationsabstände bestimmen**

Berechnen Sie anhand Ihrer tatsächlichen Systemkonfiguration den erforderlichen Platzbedarf und stellen Sie sicher, dass nach der Installation ausreichend Freiraum für Wärmeabfuhr und elektrische Sicherheit vorhanden ist.

<img src={require("./img/system-size.png").default} width="720"/>
<img src={require("./img/device-size.png").default} width="600"/>

**Schritt 2: Gerät befestigen**

Das folgende Beispiel zeigt eine Konfiguration mit **einem Leistungsmodul und zwei Batteriemodulen**:

1. Montieren Sie vier Standfüße an der Unterseite des untersten Erweiterungsbatteriemoduls.
   <img src={require("./img/installation-step1.png").default} width="360"/>

2. An der Rückseite des Geräts (Kühlkörperbereich) muss ein Mindestabstand von 30 mm eingehalten werden, um eine ausreichende Belüftung und eine effiziente Wärmeableitung sicherzustellen.
   <img src={require("./img/installation-step2.png").default} width="360"/>

3. Passen Sie die Höhe der vier Standfüße an, bis das Gerät waagerecht ausgerichtet ist, und überprüfen Sie dies mit einer Wasserwaage.
   <img src={require("./img/installation-step3.png").default} width="480"/>

4. Entfernen Sie die Schutzabdeckungen an folgenden Positionen:
   - Schutzabdeckung an der Unterseite des Leistungsmoduls
   - Schutzabdeckungen an der Ober- und Unterseite des mittleren Batteriemoduls

   :::warning
   Entfernen Sie nicht die Schutzabdeckung des untersten Erweiterungsbatteriemoduls, da dies zu Schäden am Gerät führen kann.
   :::

   <img src={require("./img/installation-step4.png").default} width="600"/>

5. Richten Sie die Erweiterungsbatteriemodule an den entsprechenden Anschlüssen aus, stapeln Sie sie nacheinander und setzen Sie das Leistungsmodul ganz oben auf.
   <img src={require("./img/installation-step5.png").default} width="240"/>

6. Befestigen Sie die L-förmigen Wandhalterungen mit M4-Kreuzschlitzschrauben an beiden Seiten des ersten Erweiterungsbatteriemoduls unterhalb des Leistungsmoduls.
   <img src={require("./img/installation-step6.png").default} width="240"/>

7. Nachdem Leistungs- und Batteriemodule gestapelt wurden, verbinden Sie beide Module mit M4-Kreuzschlitzschrauben fest miteinander.
   <img src={require("./img/installation-step7.png").default} width="480"/>

8. Markieren Sie die Bohrpositionen an der Wand, bohren Sie mit einem Ø8-mm-Bohrer Löcher mit einer Tiefe von etwa 60 mm.
   <img src={require("./img/installation-step8.png").default} width="480"/>

9. Schlagen Sie die Kunststoffdübel für die M5×60-Selbstschneideschrauben mit einem Hammer in die Bohrlöcher ein und befestigen Sie anschließend die L-förmigen Wandhalterungen mit einem Kreuzschlitzschraubendreher sicher an der Wand.
   <img src={require("./img/installation-step9.png").default} width="480"/>

:::info

Dieses Produkt verfügt über einen integrierten Doppel-Trenntransformator und erfüllt die entsprechenden Sicherheitsanforderungen. Daher ist weder die Messung des Erdungsisolationswiderstands der PV-Anlage noch die Überprüfung auf Fehlerströme erforderlich.

Das Hauptgerät muss an eine ordnungsgemäß geerdete Steckdose angeschlossen werden, da andernfalls Stromschlaggefahr besteht. Falls keine geerdete Steckdose verfügbar ist, muss das Gerätegehäuse geerdet werden. Die Position des Erdungsanschlusses ist in der folgenden Abbildung dargestellt.

<img src={require("./img/installation-step10.png").default} width="240"/>

:::

---

## Elektrischer Anschluss

:::info
- Die Installation des AC-Netzanschlusses muss den geltenden örtlichen Vorschriften entsprechen. Falls die Installation die zulässigen Rahmenbedingungen überschreitet, wird empfohlen, eine qualifizierte Elektrofachkraft zu beauftragen.
:::

Die folgenden Anschlussbeispiele basieren auf einer Standardinstallation mit vier Solarmodulen.

<img src={require("./img/connect-cables.png").default} width="960"/>

**Schritt 1: Netzanschluss herstellen**

1. Verwenden Sie das mitgelieferte Netzkabel mit Sicherheitsstecker (5 m).
2. Verbinden Sie ein Ende des Netzkabels mit dem Anschluss **GRID IN/OUT** am Hauptgerät.
3. Stecken Sie das andere Ende in eine Haushalts- oder Baustellensteckdose.

<img src={require("./img/connect-grid.png").default} width="720"/>

**Schritt 2: Solarmodule anschließen**

:::info
Die ECO-Modelle verfügen über keine PV-Anschlüsse. Dieser Schritt ist daher nicht anwendbar.
:::

Verbinden Sie mit den PV-Verlängerungskabeln die positiven und negativen Ausgänge jeder Solarmodulgruppe mit den entsprechenden PV-Eingängen des Hauptgeräts (gekennzeichnet mit PV1, PV2 usw.).

<img src={require("./img/connect-pv.png").default} width="480"/>

:::warning
Es ist strengstens untersagt, zwei oder mehr Solarmodule in Reihe zu schalten. Andernfalls kann die Eingangsspannung 60 V überschreiten und das Gerät beschädigen.
:::

:::info
Tritt am Hauptgerät eine Störung auf, versucht das System innerhalb von 15 Minuten automatisch einen Neustart. Falls die Wiederherstellung fehlschlägt, ist eine Überprüfung durch qualifiziertes Servicepersonal erforderlich. Die Systemfunktionen können erst nach entsprechender Freigabe durch den Kundendienst wiederhergestellt werden.
:::

---

## Einschalten

Suchen Sie die Taste **ON/OFF** auf der linken Seite des Hauptgeräts und halten Sie sie zwei Sekunden lang gedrückt. Beim Starten leuchtet die blaue LED-Anzeige an der Vorderseite des Geräts auf und zeigt eine Animation an, die sich von der Mitte nach oben und unten ausbreitet.

<img src={require("./img/power-on.png").default} width="360"/>
<img src={require("./img/power-on-led-state.png").default} width="240"/>

---

## Verwendung der App

Mit der INDEVOLT App können Sie:

- den Betriebsstatus und die aktuelle Leistung des Geräts in Echtzeit überwachen,
- den Ladezustand der Batterie sowie Lade- und Entladevorgänge anzeigen,
- Tages-, Wochen-, Monats- und Jahresstatistiken zur Stromerzeugung und zum Stromverbrauch einsehen,
- Energiestrategien konfigurieren, Zeitpläne festlegen oder Firmware-Updates durchführen.

📥 Wenn Sie die App zum ersten Mal verwenden, führen Sie zunächst die [Installation, Registrierung und das Hinzufügen des Geräts](../app/installation.md) durch.