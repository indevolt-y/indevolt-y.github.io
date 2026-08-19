---
title: SoC-Ausgleich von Batterien
description: Erfahren Sie, wie das System bei unterschiedlichem Ladezustand der Batterien automatisch reguliert und schützt
---

# SoC-Ausgleich von Batterien

## 1. Was ist SoC-Ausgleich

SoC (State of Charge) bezeichnet den Ladezustand einer Batterie in Prozent. Wenn mehrere Batteriepacks in das Mikrospeicher-System eingebunden sind, können sich deren Ladezustände trotz gleicher Bauart im Laufe der Zeit unterscheiden – z. B. durch unterschiedliche Nutzungsdauer, Temperatur oder Lastverteilung.

In diesem Fall führt das System automatisch einen **SoC-Ausgleich** durch, um die Ladezustände der Batteriepacks anzugleichen.

Einfach gesagt: Batterien mit höherem SoC liefern mehr Leistung, Batterien mit niedrigerem SoC weniger – bis sich die Unterschiede ausgleichen.

---

## 2. Warum ist SoC-Ausgleich notwendig

- Verlängerung der Batterielebensdauer: Vermeidung ungleichmäßiger Zyklen
- Höhere Betriebseffizienz: stabilerer Systembetrieb bei ähnlichen Ladezuständen
- Mehr Sicherheit: geringeres Risiko von Überhitzung oder Schäden

---

## 3. Warum entstehen Ungleichgewichte

Selbst Batteriepacks desselben Modells sind nie vollständig identisch.

Häufige Ursachen:
- Fertigungstoleranzen bei Kapazität und Innenwiderstand
- Unterschiedliche Lade-/Entladeleistungen im Betrieb
- Mischung aus neuen und gealterten Batterien
- Eigenverbrauch des Systems ([Standby-Leistung](./standby-power.md)), der unterschiedlich verteilt sein kann
- Ungenauigkeiten der SoC-Berechnung bei niedriger Leistung über längere Zeit
- Systemstrategien, bei denen bestimmte Batterien bevorzugt entladen oder nachgeladen werden

Mit der Zeit summieren sich diese Effekte und führen zu SoC-Abweichungen.

---

## 4. Probleme klassischer Batteriesysteme

In traditionellen Speichersystemen werden mehrere Batterien meist in Serie, parallel oder als Mischform verbunden. Dabei sind die Batterien direkt gekoppelt, was hohe Anforderungen an ihre Gleichmäßigkeit stellt.

### Serienverschaltung

Die Gesamtkapazität wird durch die „schwächste Batterie“ begrenzt. Eine stärker gealterte Batterie bestimmt dadurch Lade- und Entladeende des gesamten Systems.

### Parallelschaltung

Bei Spannungsunterschieden fließt Ausgleichsstrom zwischen den Batterien. Dies führt zu internen Umlaufströmen, zusätzlicher Wärmeentwicklung und beschleunigter Alterung.

---

## 5. Wie DCDC diese Probleme löst

Das Mikrospeicher-System nutzt eine **DCDC-Architektur**. Jeder Batteriepack ist über einen eigenen DCDC-Wandler angebunden.

Man kann dies als „intelligenten Regler“ pro Batterie verstehen – die Batterien sind nicht direkt miteinander verbunden.

| Klassische Verbindung | DCDC-Architektur |
|----------------------|------------------|
| Direkte Batterieverbindung | Einzelne Anbindung jeder Batterie |
| Hohe Anforderungen an Gleichheit | Geringere Abhängigkeit von Gleichheit |
| Gegenseitige Beeinflussung | Elektrische Trennung der Batterien |
| Schwierige Leistungsaufteilung | Präzise Leistungsregelung möglich |
| Schwierige Mischung alter und neuer Batterien | Hohe Kompatibilität unterschiedlicher Zustände |

Dadurch sind SoC-Abweichungen zulässig, und das System gleicht diese im Betrieb schrittweise aus.

---

## 6. Wie der SoC-Ausgleich erfolgt

Das System nutzt DCDC-Module und das EMS (Energiemanagementsystem), um automatisch zu regeln:

- Leistungsaufteilung je nach SoC-Unterschieden
- Höherer SoC → mehr Entladung / weniger Laden
- Niedrigerer SoC → weniger Entladung / mehr Laden

Im Betrieb bleibt eine SoC-Differenz typischerweise im Bereich von **3 % bis 15 %** bestehen.

> **Beispiel:**
> - Batterie 1: SoC 80 %
> - Batterie 2: SoC 40 %
> - Last: 900 W
>
> Verteilung durch EMS:
> - Batterie 1 (höherer SoC): ca. 600 W Entladung
> - Batterie 2 (niedriger SoC): ca. 300 W Entladung
>
> Mit der Zeit verringert sich die Differenz und die Batterien gleichen sich an.

---

## 7. Ausgleich bei niedrigem Ladezustand

Bei niedrigem SoC priorisiert das System Sicherheit und Grundversorgung.

<details className="custom-details">
  <summary className="custom-details__summary">Notstromreserve anzeigen / einstellen</summary>

  Schritte in der App: Geräte-Seite → entsprechendes Mikrospeichergerät auswählen → <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/> → SoC-Einstellungen → Notstromreserve (5 %–100 %)

  <img src={require("../energy-mode/img/select_device.png").default} width="240"/>
  <img src={require("../energy-mode/img/device_info.png").default} width="240"/>
  <img src={require("../energy-mode/img/device_setting.png").default} width="240"/>
  <img src={require("./img/soc_settings.png").default} width="240"/>
  <img src={require("./img/backup_reserve.png").default} width="240"/>
</details>

### 7.1 Entladung

- Wenn ein Batteriepack die Notstromreserve erreicht, stoppt das System die Entladung und geht in den Standby-Modus
- Andere Batterien mit höherem SoC versorgen weiterhin die Last

### 7.2 Laden

**◽ Bei PV vorhanden (PV / PV+AC)**  
Alle Batteriepacks werden gleichzeitig geladen

**◽ Nur Netzladung (AC)**

| EMS-Version | Verhalten |
|------------|----------|
| < 1.01.05 | Wenn Gesamt-SoC unter Notstromreserve liegt: alle Batterien werden gemeinsam geladen; Stop bei Erreichen |
| ≥ 1.01.05 | Batterien unterhalb des Notstromreserve werden bevorzugt geladen; Stop bei Erreichen |

📌 Details: [Erklärung zum Nachladeverhalten](./recharge.md)

### 7.3 Standby

**◽ Eigenverbrauch des Hauptgeräts**

Ob ein AC-Hilfsmodul vorhanden ist, beeinflusst die Standby-Versorgung. Diese Information wird später in der App angezeigt.

Deep-Standby des Hauptgeräts: ca. 6 W

* **Ohne AC-Hilfsmodul**: Versorgung über den **eigenen Akku**, wodurch der SoC der Haupteinheit schneller sinkt als der der Batteriepacks
* **Mit AC-Hilfsmodul**: Versorgung über das **AC-Hilfsmodul** (bei Netzanschluss über das Stromnetz), wodurch der Batterieverbrauch reduziert wird


**◽ Verbrauch des Batteriepacks**

ca. 2 W, wird stets aus der eigenen Batterie gespeist

📌 Detaillierte Informationen zum Standby-Verbrauch finden Sie unter: [Standby-Verbrauch](./standby-power.md)