---
title: Dynamischer Tarifmodus
description: Automatisches Laden und Entladen basierend auf Strompreisen zur Senkung der Energiekosten
---

# Dynamischer Tarifmodus

Der dynamische Tarifmodus ist ein intelligenter Energiemodus. Das System entscheidet anhand der von dir definierten Strompreisgrenzen automatisch, wann geladen oder entladen wird. Dadurch werden die Stromkosten minimiert, ohne den normalen Energieverbrauch zu beeinträchtigen.

## Für welche Nutzer geeignet?

- Regionen mit **Zeitstromtarifen / dynamischen Strompreisen / Echtzeitpreisen**  
- Nutzer, die durch „günstig laden, teuer entladen“ Stromkosten sparen möchten  
- Nutzer, die keine täglichen Lade- und Entladepläne manuell einstellen möchten  
- Anwender, die eine automatische, preisbasierte Steuerung bevorzugen  

## Funktionsweise des Systems

Im Modus des dynamischen Tarifmodus wechselt das System automatisch zwischen drei Betriebszuständen:

### **Laden (bei niedrigen Strompreisen)**

Die tatsächliche Ladeleistung wird durch die maximale Eingangsleistung des Wechselrichters bestimmt:

- PV-Strom wird bevorzugt zum Laden der Batterie genutzt  
- Wenn PV-Leistung nicht ausreicht, wird automatisch Netzstrom zur Unterstützung verwendet  
- Sobald die Batterie vollständig geladen ist, wird der Ladevorgang beendet  

### **Entladen (bei hohen Strompreisen oder hoher Last)**

Die tatsächliche Entladeleistung hängt von der aktuellen Lastquelle ab (Intelligente Steckdose / Zähler / Standardlast):

- PV-Strom wird zuerst zur Versorgung der Verbraucher genutzt  
- Wenn die PV-Leistung nicht ausreicht, übernimmt die Batterie die Versorgung  
- Sobald der Batteriestand den Notfall-SoC erreicht, wird das Entladen automatisch gestoppt  

### **Standby (außerhalb der Preisstrategie)**

Im Standby-Modus lädt oder entlädt die Batterie nicht aktiv:

- PV-Erzeugung versorgt zuerst die Haushaltslasten  
- Wenn PV-Leistung den Verbrauch übersteigt und der SOC unter 100 % liegt, wird der Überschuss zur Batterie geladen  
- Ist die Batterie voll, wird die PV-Leistung entsprechend begrenzt  

## So richtest du den dynamischen Tarifmodus ein

👉 Detaillierte Einstellungen findest du in der [INDEVOLT App – Beschreibung des Smart-Modus](../../app/smart.md)