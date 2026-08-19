---
title: Standby-Verbrauch
description: Überblick über den Eigenverbrauch des Systems in verschiedenen Betriebszuständen und dessen Einfluss auf den Energiebedarf
---

# Standby-Verbrauch

Im täglichen Betrieb kann es vorkommen, dass die Batterie langsam entladen wird, obwohl weder geladen noch entladen wird. In den meisten Fällen handelt es sich dabei um ein normales Betriebsverhalten des Systems.

**Warum verbraucht das Gerät auch im „inaktiven“ Zustand Energie?**

Ein Energiespeichersystem arbeitet nicht nur während des Lade- oder Entladevorgangs. Auch im Ruhezustand müssen interne Komponenten aktiv bleiben, z. B. das Steuerungssystem im Bereitschaftsmodus, das Batteriemanagementsystem (BMS) zur kontinuierlichen Überwachung sowie Kommunikationsmodule, die dauerhaft verbunden bleiben.

Solange das Gerät eingeschaltet ist, verbrauchen diese Module eine geringe Menge an Energie. Dieser Verbrauch kann als „Betriebserhaltungsenergie“ verstanden werden. Ein geringer Standby-Verbrauch ist daher normal.

## Hauptfaktoren, die den Standby-Verbrauch beeinflussen

Der Standby-Verbrauch ist kein fester Wert, sondern hängt von Systemkonfiguration und Betriebsbedingungen ab. Die wichtigsten Einflussfaktoren sind:

### 1. Netzanschluss (On-Grid / Off-Grid)

**Netzbetrieb (On-Grid)**  
Wenn das Gerät an das Stromnetz angeschlossen ist, können bestimmte Funktionen über das Netz betrieben werden. Dadurch ist der Energieverbrauch in der Regel geringer.

**Inselbetrieb (Off-Grid)**  
Im Inselbetrieb muss das System die Versorgung eigenständig sicherstellen. Daher bleiben mehr Module aktiv, was zu einem höheren Standby-Verbrauch führt.

Kurz gesagt:

- On-Grid: Nutzung des Stromnetzes → geringerer Verbrauch  
- Off-Grid: Eigenständige Versorgung → höherer Verbrauch  


### 2. Bypass-Funktion

Ist der Bypass aktiviert, kann die Last direkt über das Stromnetz oder die Batterie versorgt werden. In diesem Fall bleiben hauptsächlich Steuer-, Mess- und Bypass-Schaltungen aktiv. Der Verbrauch liegt typischerweise unter dem eines aktiven Inselbetriebs, aber über dem eines Tiefer Standby.

Ist der Bypass deaktiviert und das System im Inselbetrieb, kann das Gerät in einen tieferen Standby-Zustand wechseln und dadurch Energie sparen.

Kurz gesagt:

- Bypass aktiv: Netz versorgt die Last direkt, System im Bereitschaftsmodus  
- Bypass deaktiviert: höhere Systemaktivität erforderlich  


### 3. Tiefer Standby

Wenn der Tiefer Standby aktiviert ist, arbeitet das System im Energiesparmodus. Bei fehlender Lade- oder Entladeanforderung werden hochverbrauchende Komponenten (z. B. der Wechselrichter) in den Ruhezustand versetzt. Nur Basisfunktionen wie Überwachung und Kommunikation bleiben aktiv.

Kurz gesagt:

- Tiefer Standby aktiviert: Energiesparmodus  
- Tiefer Standby deaktiviert: jederzeit betriebsbereit, höherer Verbrauch  


### 4. AC-Hilfsversorgung

Die AC-Hilfsversorgung dient zur Stromversorgung der internen Steuerelektronik. Die neueren Geräte PowerFlex / SolidFlex 2000 sind mit einer **AC-Hilfsversorgung** ausgestattet.

Wenn das Gerät am Netz angeschlossen ist und eine AC-Hilfsversorgung vorhanden ist, können bestimmte interne Module direkt über das Stromnetz betrieben werden, wodurch der Batterieverbrauch reduziert wird.

Kurz gesagt:

- Mit AC-Hilfsversorgung: Teil des Verbrauchs wird vom Netz übernommen  
- Ohne AC-Hilfsversorgung: Verbrauch erfolgt aus der Batterie  

---

## Leistungsaufnahme in verschiedenen Betriebszuständen

Abhängig vom Netzanschluss und Betriebsmodus ergeben sich unterschiedliche Systemzustände.

:::note
- Die folgenden Angaben gelten nur für die Serien PowerFlex / SolidFlex 2000 und nicht für PowerFlex / SolidFlex 1200 und 3000.
- Es handelt sich um typische Werte; tatsächliche Werte können je nach Umgebungstemperatur, Kommunikationsstatus und Anzahl der Batteriemodule leicht variieren.
- Gesamtverbrauch = Hauptgerät + Anzahl der Batteriemodule × Verbrauch pro Batteriemodul
:::

### Netzbetrieb (On-Grid)

**🔌 Bypass aktiviert**

In diesem Zustand wird die Last in der Regel direkt vom Netz versorgt. **Der Verbrauch ist unabhängig davon, ob der Tiefer Standby aktiviert ist oder nicht.**

| Modell | Hauptgerät-Leistungsaufnahme (W) | Batteriemodul-Leistungsaufnahme (W) |
|--------|--------------------------|--------------------|
| PowerFlex 2000 | 20 | 0 |
| SolidFlex 2000 | 20 | 0 |
| PowerFlex 2000 (mit AC-Hilfsversorgung) | 20 | 0 |
| SolidFlex 2000 (mit AC-Hilfsversorgung) | 20 | 0 |


**🔌 Bypass deaktiviert**

<table>
<thead>
<tr>
  <th></th>
  <th colspan="2">Tiefschlaf aktiviert</th>
  <th colspan="2">Tiefschlaf deaktiviert</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Modell</td>
  <td>Hauptgerät-Leistungsaufnahme (W)</td>
  <td>Batteriemodul-Leistungsaufnahme (W)</td>
  <td>Hauptgerät-Leistungsaufnahme (W)</td>
  <td>Batteriemodul-Leistungsaufnahme (W)</td>
</tr>
<tr>
  <td>PowerFlex 2000</td>
  <td>7</td>
  <td>2</td>
  <td>20</td>
  <td>0</td>
</tr>
<tr>
  <td>SolidFlex 2000</td>
  <td>7</td>
  <td>2</td>
  <td>20</td>
  <td>0</td>
</tr>
<tr>
  <td>PowerFlex 2000 (mit AC-Hilfsversorgung)</td>
  <td>7 (AC-Hilfsversorgung aktiv)</td>
  <td>2</td>
  <td>20</td>
  <td>0</td>
</tr>
<tr>
  <td>SolidFlex 2000 (mit AC-Hilfsversorgung)</td>
  <td>7 (AC-Hilfsversorgung aktiv)</td>
  <td>2</td>
  <td>20</td>
  <td>0</td>
</tr>
</tbody>
</table>


### Inselbetrieb (Off-Grid)

Im Inselbetrieb kann das System nicht auf das Stromnetz zurückgreifen und muss die Versorgung selbst aufrechterhalten. Daher ist der Standby-Verbrauch in der Regel höher als im Netzbetrieb.

**🔌 Bypass aktiviert**

Das System muss den Wechselrichter betriebsbereit halten, um jederzeit Lasten versorgen zu können. **Der Verbrauch ist unabhängig vom Tiefer Standby gleich.**

:::note
Wenn nach Aktivierung des Bypass der Off-Grid-„Sleep Timer / Standby-Abschalt-Timer“ abläuft, entspricht der Verbrauch dem Zustand bei deaktiviertem Bypass.
:::

| Modell | Hauptgerät-Leistungsaufnahme (W) | Batteriemodul-Leistungsaufnahme (W) |
|--------|--------------------------|--------------------|
| PowerFlex 2000 | 29 | 5 |
| SolidFlex 2000 | 29 | 5 |
| PowerFlex 2000 (mit AC-Hilfsversorgung) | 29 | 5 |
| SolidFlex 2000 (mit AC-Hilfsversorgung) | 29 | 5 |


**🔌 Bypass deaktiviert**

Im Inselbetrieb mit deaktiviertem Bypass wechselt das System automatisch in den Tiefer Standby.

| Modell | Hauptgerät-Leistungsaufnahme (W) | Batteriemodul-Leistungsaufnahme (W) |
|--------|--------------------------|--------------------|
| PowerFlex 2000 | 7 | 2 |
| SolidFlex 2000 | 7 | 2 |
| PowerFlex 2000 (mit AC-Hilfsversorgung) | 7 | 2 |
| SolidFlex 2000 (mit AC-Hilfsversorgung) | 7 | 2 |