---
title: FAQ und Fehlerbehebung
description: Häufig gestellte Fragen und Hinweise zur Nutzung der INDEVOLT-Energiespeichergeräte
---

# FAQ und Fehlerbehebung

## I. Anwendungsbereich und grundlegende Kompatibilität

<details className="custom-details" open>
  <summary className="custom-details__summary">
  1. Frage: Welche Spezifikationen von Solarmodulen werden unterstützt?
  </summary>

  Antwort: Es wird empfohlen, Solarmodule mit einer Leerlaufspannung (Voc) im Bereich von 10–60 V und einem Kurzschlussstrom (Isc) von maximal 20 A zu verwenden.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  2. Frage: Kann das Gerät bei Temperaturen unter 0 °C betrieben werden? Welcher Temperaturbereich ist für den Akku ideal?
  </summary>

  Antwort: Das Gerät kann auch unter 0 °C normal laden und entladen. Auch die Photovoltaik-Erzeugung funktioniert weiterhin. Aufgrund der winterlichen Lichtverhältnisse kann die Energieerzeugung jedoch geringer ausfallen; in diesem Fall wird der erzeugte Solarstrom in der Regel direkt selbst verbraucht, ohne nennenswerte Energieverluste.

  Der ideale Betriebstemperaturbereich des Akkus ist wie folgt:
    - Laden: -20 bis 55 °C  
    - Entladen: -20 bis 55 °C  
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  3. Frage: Mit welchen Marken ist das Gerät kompatibel?
  </summary>

  Antwort: Derzeit werden Produkte der Marken Shelly, SOLARMAN und INDEVOLT unterstützt.
</details>

---

## II. Installation, Verkabelung und Nutzung

<details className="custom-details" open>
  <summary className="custom-details__summary">
  1. Frage: Wird ein zusätzlicher Mikro-Wechselrichter benötigt?
  </summary>

  Antwort: Je nach Modell gilt Folgendes:
  - Nicht-ECO-Modelle: Ein Mikro-Wechselrichter ist bereits integriert, sodass keine zusätzliche Installation erforderlich ist. Außerdem sind 4 MPPT-Kanäle (Maximum Power Point Tracking) enthalten. Zur Leistungssteigerung kann optional ein zusätzlicher Mikro-Wechselrichter angeschlossen werden.
  - ECO-Modelle: MPPT wird nicht unterstützt.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  2. Frage: Was ist beim Einsetzen oder Hinzufügen eines Erweiterungsakkus zu beachten?
  </summary>

  Antwort: Arbeiten dürfen ausschließlich im vollständig spannungsfreien Zustand durchgeführt werden. Ein Ein- oder Ausstecken unter Last ist strengstens verboten, da dies zu Geräteschäden oder Sicherheitsrisiken führen kann. Vorgehensweise:

      1. PV-Eingang und AC-Stecker trennen;  
      2. Ein-/Ausschalter ca. 2 Sekunden gedrückt halten, um das Gerät auszuschalten;  
      3. Nach dem Ausschalten den Erweiterungsakku einsetzen;  
      4. Solarmodule erneut anschließen und das Gerät wieder in Betrieb nehmen.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  3. Frage: Funktioniert das Gerät bei einem Stromausfall?
  </summary>

  Antwort: Bei einem Stromausfall im Haushalt kann das Gerät weiterhin betrieben werden. Es kann über Photovoltaik geladen werden. Die maximale Ausgangsleistung im Inselbetrieb variiert je nach Modell.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  4. Frage: Kann der Netzanschluss bei einem Stromausfall weiterhin verwendet werden?
  </summary>

  Antwort: Aufgrund der geltenden Netzanschlussnormen muss das Gerät über eine Anti-Islanding-Funktion verfügen, um eine Einspeisung ins Netz während eines Stromausfalls zu verhindern und die Sicherheit von Wartungspersonal zu gewährleisten. Daher ist bei Netzausfall keine Einspeisung über den Netzanschluss möglich; die Versorgung erfolgt ausschließlich über den Inselbetrieb-Ausgang.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  5. Frage: Was ist der Bypass-Modus?
  </summary>

  Antwort: Der Bypass-Modus ist ein spezieller Betriebsmodus zur Unterstützung externer Geräte. Wenn er aktiviert ist, können z. B. Mikro-Wechselrichter oder kritische Verbraucher angeschlossen werden. Je nach angeschlossenem Gerät kann der entsprechende Schalter am Gerät oder in der App aktiviert werden. Anschließend zeigt die App die angeschlossenen Geräte sowie den Energiefluss in Echtzeit an.

  👉 Detaillierte Beschreibung: [Anleitung zum Bypass-Anschluss](./technical-note/bypass.md)
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  6. Frage: Wie kann ich Gerätedaten und Parameter bei einem Netzausfall oder Verbindungsabbruch einsehen?
  </summary>

  Antwort: Auch bei unterbrochener Internetverbindung bleibt die Grundfunktion des Geräts aktiv. Die Daten können lokal über Bluetooth abgerufen werden:

    - Option 1: Im Login-Bildschirm „Direktverbindung zum Gerät“ auswählen und per Bluetooth verbinden;  
    - Option 2: In der App im Bereich „Profil“ die Funktion „Direktverbindung zum Gerät“ verwenden.
</details>

## III. Lade-/Entladeverhalten und Energiemanagement-Strategien

<details className="custom-details" open>
  <summary className="custom-details__summary">
  1. Frage: Ist es ein Problem, wenn mehrere Batteriemodule unterschiedliche SOC-Werte haben?
  </summary>

  Antwort: Nein, das ist völlig normal.

  Jedes Batteriemodul verfügt über einen eigenen DC-DC-Optimierer. Das System kann automatisch Unterschiede im Ladezustand zwischen den einzelnen Batterien ausgleichen. Auch Batteriemodule mit unterschiedlicher Kapazität oder unterschiedlichem SOC können gemeinsam betrieben werden. Der SOC wird automatisch synchronisiert, eine manuelle Anpassung ist nicht erforderlich.

  👉 Detaillierte Erklärung: [SOC-Balancing](./technical-note/soc-balancing.md)
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  2. Frage: Wie kann ich einstellen, dass kein Strom ins Hausnetz eingespeist wird?
  </summary>

  Antwort: In der App unter „Leistungseinstellungen“ die maximale Einspeiseleistung auf 0 setzen.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  3. Frage: Kann die Entladung anhand von „Zeit + SOC“ gesteuert werden?
  </summary>

  Antwort: Ja. Über Home Assistant können entsprechende Bedingungen definiert werden. Im Echtzeit-Steuermodus lassen sich Zeitregeln und SOC-Grenzwerte kombinieren, um eine gekoppelte Steuerung zu realisieren.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  4. Frage: Wie stelle ich ein, dass die Batterie ausschließlich über Solarmodule geladen wird?
  </summary>

  Antwort: In der App einen Lade-/Entladeplan einstellen und die Ladequelle „nur Solar-Laden“ auswählen.

  > **Hinweis:** Um die Batterielebensdauer zu schützen, lädt das System automatisch aus dem Stromnetz, wenn der Ladezustand sehr niedrig ist (SOC ≤ 3 %) und die PV-Leistung nicht ausreicht.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  5. Frage: Ab welcher PV-Leistung beginnt das Gerät mit dem Laden?
  </summary>

  Antwort: Das System beginnt mit dem Laden der Batterie, sobald die PV-Leistung über 50 W liegt. Der Eigenverbrauch des Geräts beträgt ca. 35 W, zusätzlich treten Umwandlungsverluste auf. Unterhalb von 50 W reicht die verbleibende Leistung in der Regel nicht zum Laden aus.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  6. Frage: Warum wird bei niedriger PV-Leistung kein „Laden“ angezeigt?
  </summary>

  Antwort: Bei geringer PV-Leistung wird ein Teil der Energie zunächst für den Eigenverbrauch und die Umwandlung genutzt. Daher kann die tatsächlich in die Batterie eingespeiste Leistung sehr gering sein.

  Liegt die effektive Ladeleistung unter dem Anzeigeschwellenwert, zeigt die App „Standby“ an, obwohl die Batterie möglicherweise weiterhin langsam geladen wird. Dies ist normal.

  Anzeigeschwellen:

  - Laden wird angezeigt ab ≥ 30 W  
  - Entladen wird angezeigt ab ≥ 60 W  
  - Darunter wird „Standby“ angezeigt
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  7. Frage: Muss die Batterie vor der ersten Nutzung vollständig geladen werden?
  </summary>

  Antwort: Es wird empfohlen, die Batterie vor der ersten Nutzung einmal vollständig aufzuladen. Dadurch wird der SOC kalibriert und die Anzeige im App-System besser an den tatsächlichen Ladezustand angepasst.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  8. Frage: Stoppt das Solarmodul die Stromerzeugung, wenn die Batterie voll ist? Ist das sicher?
  </summary>

  Antwort: Das Gerät verfügt über einen Überladeschutz. Sobald der SOC 100 % erreicht, wird der Ladevorgang automatisch gestoppt. Dies ist ein normaler Betriebszustand.

  Ob die PV-Module weiterhin Energie erzeugen, hängt vom Systemzustand und den App-Einstellungen ab:

  - Wenn Verbraucher aktiv sind, versorgt die PV-Anlage weiterhin die Lasten direkt.
  - Bei aktivierter Einspeisung wird überschüssige Energie gemäß der eingestellten maximalen Einspeiseleistung ins Netz eingespeist.
  - Ohne Verbrauch reduziert oder stoppt das System die PV-Abnahme automatisch.

  Der gesamte Prozess ist vollständig automatisiert und sicher für Gerät, Batterie und PV-Anlage.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  9. Frage: Warum hat der Backup-Anschluss nach einer Netztrennung keinen Strom?
  </summary>

  Antwort: Mögliche Ursachen:

  - Bei EMS-Firmware-Versionen unter 1.01.08 wird der Backup-Anschluss im Mikrowechselrichter-Modus aus Sicherheitsgründen im Inselbetrieb deaktiviert.
  - Wenn der Batteriestand unter 5 % fällt, kann die Ausgangsversorgung ebenfalls deaktiviert werden.

  Empfehlungen:
  - EMS-Firmware auf Version 1.01.08 oder höher aktualisieren;
  - Prüfen, ob der Batterieladezustand zu niedrig ist.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  10. Frage: Wie hoch ist der Eigenverbrauch des SolidFlex 2000?
  </summary>

  Antwort: Der Stromverbrauch hängt vom Betriebszustand ab:

  - Normalbetrieb (Laden, Entladen oder Versorgung der Last): ca. 30 W  
  - Tief-Standby-Modus (kein Laden/Entladen, reduzierte Leistung): abhängig von den Systemeinstellungen; siehe [Standby-Verbrauch](./technical-note/standby-power.md)
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  11. Frage: Wird der Verbraucher immer aus der Batterie versorgt oder auch direkt über PV?
  </summary>

  Antwort: Nicht immer.

  - Wenn die PV-Leistung ausreichend ist, versorgt das System die Verbraucher bevorzugt direkt über Solarenergie. Überschüsse werden zur Batterieladung genutzt.
  - Wenn die PV-Leistung nicht ausreicht, übernimmt die Batterie die Versorgung.
  - Bei Geräten ab Produktion Dezember 2025 wird im Tief-Standby zusätzlich eine AC-Hilfsversorgung aus dem Netz genutzt.
</details>

## IV. Erweiterung, Batterien und Parallelbetrieb

<details className="custom-details" open>
  <summary className="custom-details__summary">
  1. Frage: Was ist der Cluster-Modus und wie wird er verwendet?
  </summary>

  Antwort: Der Cluster-Modus bezeichnet den Zusammenschluss mehrerer Mikro-Speichergeräte zu einem einheitlich arbeitenden System, bei dem mehrere Geräte gemeinsam die Stromversorgung, Energiespeicherung und das Energiemanagement übernehmen.

  Vorgehensweise: Nachdem alle Geräte in der App hinzugefügt und mit dem Netzwerk verbunden wurden, öffnen Sie die Geräteeinstellungen. Wählen Sie dort „Cluster“ und fügen Sie die zu koppelnden Geräte gemäß den Anweisungen hinzu. Nach erfolgreicher Kopplung wird der Cluster-Modus aktiviert. In dieser Ansicht können außerdem Leistungszuweisungen, SOC-Schwellenwerte und weitere Parameter konfiguriert werden.

  👉 Detaillierte Beschreibung: [Cluster](./technical-note/cluster.md)
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  2. Frage: Können PowerFlex- und SolidFlex-Systeme im Cluster-Modus gemeinsam betrieben werden?
  </summary>

  Antwort: Ja, PowerFlex- und SolidFlex-Systeme werden im Cluster-Modus gemeinsam unterstützt.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  3. Frage: Wenn zwei Batteriesysteme parallel betrieben werden, beträgt die Ausgangsleistung dann 2 × 2400 W oder weiterhin nur 2400 W?
  </summary>

  Antwort: Die maximal einstellbare AC-Ausgangsleistung kann in der App im Bereich „Leistungseinstellungen“ des Parallelbetriebs eingesehen werden.

  Je nach Betriebsart unterscheidet sich die Ausgangsleistung:
  - Kooperativer Parallelbetrieb: Jedes Gerät ist unabhängig an das Stromnetz angeschlossen und übernimmt eigene Ein- und Ausgangsleistung. Daher kann jedes Batteriesystem bis zu 2400 W liefern.
  - Zentralisierter Parallelbetrieb: Alle AC-Ein- und Ausgänge werden über das Hauptgerät geführt, das die Netzanbindung und Leistungssteuerung übernimmt. In diesem Fall kann die Gesamtleistung des Hauptgeräts bis zu 2 × 2400 W betragen.

  Die tatsächlich zulässige Leistung muss den lokalen Netz- und Sicherheitsvorschriften entsprechen.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  4. Frage: Wie wird die Leistung bei mehreren parallel geschalteten Geräten verteilt?
  </summary>

  Antwort: Das System verwendet eine gestufte Leistungszuweisung basierend auf SOC und Lastleistung:

  - Entladeleistung < 200 W: nur das Gerät mit dem höchsten SOC übernimmt die gesamte Last  
  - 200 W ≤ Entladeleistung < 500 W: zwei Geräte mit höherem SOC teilen sich die Last  
  - Entladeleistung > 500 W: alle Slave-Geräte beteiligen sich an der Entladung, die Leistungsaufteilung erfolgt proportional zum SOC
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  5. Frage: Obwohl die maximale Leistung im Batteriemodul 2400 W beträgt, ist standardmäßig nur 800 W eingestellt. Kann die Leistung auf 2400 W erhöht werden?
  </summary>

  Antwort: Die Entladeleistung wird durch die Anzahl der Batteriemodule bestimmt. Um die Leistung auf 2400 W zu erhöhen, müssen zusätzliche Batteriemodule installiert werden. Eine reine Parameteranpassung reicht nicht aus. Nach Erweiterung der Batteriemodule erhöht sich die Systemleistung entsprechend. Dabei muss die elektrische Auslegung der Leitungen beachtet werden, um Überlastungen zu vermeiden.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  6. Frage: Wie viele SolidFlex-2000-Geräte und SFA1800-Batteriemodule werden maximal unterstützt und wie hoch ist die Gesamtleistung?
  </summary>

  Antwort:
  - Maximale Erweiterung: Pro SolidFlex 2000 können bis zu 5 SFA1800-Batteriemodule angeschlossen werden. Die maximale Energiekapazität pro Gerät beträgt 10,8 kWh (5 × SFA1800).
  - Maximale Gesamtleistung: Die Nennleistung eines SolidFlex 2000 beträgt 2400 W. Das System unterstützt bis zu 3 SolidFlex-2000-Geräte im drahtlosen Clusterbetrieb, mit einer maximalen Gesamtleistung von 7200 W (3 × 2400 W).
</details>

## V. Systeminteraktion

<details className="custom-details" open>
  <summary className="custom-details__summary">
  1. Frage: Kann das System mit Energiespeichern anderer Hersteller gekoppelt werden?
  </summary>

  Antwort: Ja. Über Home Assistant kann eine Kopplung und gemeinsame Steuerung mit anderen Systemen realisiert werden. Voraussetzung ist, dass beide Systeme in Home Assistant eingebunden und entsprechend autorisiert sind.
</details>

## VI. Garantiefragen

<details className="custom-details" open>
  <summary className="custom-details__summary">
  1. Frage: Wie lange gilt die Produktgarantie und welche Komponenten sind abgedeckt?
  </summary>

  Antwort: Für das Produkt gilt eine **10-jährige eingeschränkte Garantie**. Der Garantieumfang umfasst die Batterie, den AC-Wechselrichter sowie das Gesamtsystem (maßgeblich sind die Bestimmungen des Garantievertrags; Verschleißteile sind ausgeschlossen).
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  2. Frage: Hat die Angabe von 8000 Ladezyklen vertragliche Garantie-Wirkung oder handelt es sich nur um einen theoretischen Nennwert?
  </summary>

  Antwort: Die Angabe von 8000 Ladezyklen basiert auf tatsächlichen Tests. Das Gerät verwendet zwei große Zellen, wodurch die Zyklusstabilität verbessert wird. Diese Angabe hat vertragliche Garantie-Wirkung.
</details>
 
 <details className="custom-details" open>
  <summary className="custom-details__summary">
  3. Frage: Welchen verbleibenden Batteriezustand (SOH) garantiert das System am Ende der Garantiezeit?
  </summary>

  Antwort: Nicht weniger als 70 % (SOH).
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  4. Frage: Wie hoch ist die maximal zulässige Entladetiefe (DOD) der Batterie?
  </summary>

  Antwort: Im Rahmen der Garantiebedingungen beträgt die maximal zulässige Entladetiefe der Batterie 100 %. Für den täglichen Gebrauch wird jedoch empfohlen, die Entladetiefe je nach Bedarf anzupassen und häufige Vollentladungen zu vermeiden.
</details>

<details className="custom-details" open>
  <summary className="custom-details__summary">
  5. Frage: Begrenzt das System die Lade- und Entladerate (C-Rate) automatisch, um die Lebensdauer der Batterie zu verlängern?
  </summary>

  Antwort: Das System unterstützt die manuelle Anpassung der Lade- und Entladeleistung und begrenzt die Lade- und Entladerate außerdem automatisch anhand des Batteriezustands (z. B. SOC und Temperatur), um Schäden durch zu hohe C-Raten zu vermeiden und die Lebensdauer der Batterie zu verlängern.
</details>