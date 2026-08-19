---
title: LoRa-Anbindungsanleitung
description: Benutzeranleitung zur Anbindung von Mikrospeichergeräten an LoRa-Endgeräte
---

# LoRa-Anbindungsanleitung

## Was ist LoRa

LoRa (Long Range, große Reichweite) ist eine energiearme Funktechnologie für Weitbereichsnetzwerke (LPWAN), die auf Spread-Spectrum-Modulation basiert. Dabei wird das Signal über ein breiteres Frequenzband verteilt übertragen, wodurch eine hohe Störfestigkeit und eine sehr hohe Empfangsempfindlichkeit erreicht wird.

Einfach gesagt: LoRa ist eine Technologie, die es Geräten ermöglicht, über große Distanzen drahtlos miteinander zu kommunizieren. Im Gegensatz zu Wi-Fi oder Bluetooth ist sie nicht auf ein Heimnetzwerk angewiesen und erfordert keine komplexe Konfiguration. Man kann sie sich wie einen dedizierten Funkkanal zwischen Geräten vorstellen.

Mit LoRa können Geräte automatisch Informationen austauschen. Beispielsweise übermittelt ein Stromzähler Verbrauchsdaten an das Mikrospeichersystem, das darauf basierend Lade- und Entladevorgänge automatisch steuert. Dieser gesamte Prozess läuft im Hintergrund und ist für den Nutzer nahezu unsichtbar.

**Kernmerkmale**

- Sehr große Reichweite: In idealen Umgebungen (z. B. ländliche oder offene Gebiete) bis zu 10–20 km oder mehr  
- Sehr geringer Energieverbrauch: Batterielaufzeiten von mehreren Jahren bis zu zehn Jahren möglich  
- Hohe Kapazität: Ein Gateway kann Tausende von Endgeräten verbinden  
- Geringe Kosten: Hardware- und Netzwerkinfrastruktur vergleichsweise günstig  

---

## Unterschied zwischen LoRa und Wi-Fi

Wi-Fi kann man sich als schnelles Heimnetzwerk vorstellen, das für Internetzugang, Video-Streaming usw. genutzt wird. Es ist schnell, verbraucht jedoch mehr Energie und ist stark von der Netzverfügbarkeit abhängig.

LoRa hingegen ist speziell für die Übertragung kleiner Datenmengen gedacht, wie z. B. Stromverbrauch oder Gerätestatus. Die Datenrate ist geringer, dafür ist die Reichweite deutlich größer und der Energieverbrauch sehr niedrig. Zudem ist LoRa unabhängig vom Heimnetzwerk – auch bei Internetausfall bleibt die Kommunikation zwischen Geräten bestehen.

Kurz gesagt: Wi-Fi ist für das Internet da, LoRa für die direkte Kommunikation zwischen Geräten, um das System intelligenter und zuverlässiger zu machen.

---

## Anwendungsbereiche

- Orte mit schlechter Netzwerkabdeckung oder schwachem Wi-Fi-Signal, z. B. Keller oder Dachboden  
- Umgebungen mit starken Störungen, z. B. Serverräume oder Energieanlagen  

---

## Unterstützte Geräte

Wenn die Firmware-Version eines Geräts unter der in der Tabelle angegebenen Mindestversion liegt, aktualisieren Sie diese bitte in der INDEVOLT-App im Gerätebereich.

<table><thead>
  <tr>
    <th>Gerät</th>
    <th>Modell</th>
    <th>Mindest-Firmwareversion</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Mikrospeicher</td>
    <td>SolidFlex 2000<br />PowerFlex 2000<br />SolidFlex 2000 Eco<br />PowerFlex 2000 Eco<br />PowerFlex 3000 Hybrid<br />PowerFlex 3000 AC<br />SolidFlex 3000 Hybrid<br />SolidFlex 3000 AC</td>
    <td>CMS: V1406.07.002B <br/>Pfile: V0D.00.11</td>
  </tr>
  <tr>
    <td rowspan="2">Stromzähler</td>
    <td>MR1-D5-WR</td>
    <td>V1.4.09_R00B.082_M051A_00000037</td>
  </tr>
  <tr>
    <td>MR3-D5-WR</td>
    <td>V1.4.09_R01C.0D2_M0515_00000016</td>
  </tr>
  <tr>
    <td>Nah-Infrarot-Zählerausleser</td>
    <td>NIR-3</td>
    <td>V1.4.09_R016.082_M0000_0000001E</td>
  </tr>
</tbody>
</table>

---

## Bedienungsschritte

### Verbindung mit LoRa-Endgerät herstellen

:::info Vorbereitung
Bitte stellen Sie sicher, dass folgende Bedingungen erfüllt sind:
- Das Mikrospeichergerät wurde bereits in der INDEVOLT-App hinzugefügt, ist eingeschaltet und online  
- Das LoRa-fähige Endgerät ist installiert und mit Strom versorgt  
:::

1. Öffnen Sie die INDEVOLT-App, tippen Sie auf der Geräteseite oben rechts auf „**+**“ und wählen Sie das hinzuzufügende Gerät aus (z. B. Stromzähler).

   <img src={require("./img/click_add_device.png").default} width="200"/>
   <img src={require("./img/select_lora_device.png").default} width="200"/>

2. Scannen Sie den QR-Code auf dem Stromzähler und tippen Sie nach erfolgreicher Erkennung auf **Mit Gerät verbinden**.

   <img src={require("./img/connect_device.png").default} width="200"/>

3. Wählen Sie als Verbindungsmethode **LoRa-Funkverbindung** aus, wählen Sie anschließend das zu bindende Mikrospeichergerät und tippen Sie auf **Binden**, dann warten Sie auf den Abschluss der Verbindung.

   <img src={require("./img/select_lora.png").default} width="210"/>
   <img src={require("./img/select_bind_device.png").default} width="200"/>
   <img src={require("./img/connected_device.png").default} width="200"/>

4. Überprüfen Sie die Verbindung

   Öffnen Sie die Geräteseite, tippen Sie auf den Stromzähler, gehen Sie zur Detailseite und wählen Sie oben rechts das Einstellungsmenü <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/>, dann **Netzwerk-Einstellungen**. Prüfen Sie, ob die aktuelle Verbindung **LoRa-Funkverbindung** ist.

   <img src={require("./img/tap_device.png").default} width="210"/>
   <img src={require("./img/device_setting.png").default} width="200"/>
   <img src={require("./img/network_setting.png").default} width="200"/>
   <img src={require("./img/network_info_lora.png").default} width="200"/>

   Zusätzlich wird in der Geräteliste oben rechts ein Symbol angezeigt, das die aktuelle Verbindung (Wi-Fi oder LoRa) kennzeichnet.

   <img src={require("./img/lora_icon.png").default} width="210"/>

---

### Verbindungsart wechseln (Wi-Fi / LoRa)

Falls Sie die Verbindungsmethode ändern möchten, gehen Sie wie folgt vor:

1. Öffnen Sie die Geräteseite des Stromzählers, tippen Sie auf das Einstellungsmenü <img src={require("./img/settings_icon.png").default} width="30" style={{verticalAlign: "middle"}}/>, wählen Sie **Netzwerk-Einstellungen** und tippen Sie auf **Verbindungsart Wechseln**.

   <img src={require("./img/tap_device.png").default} width="210"/>
   <img src={require("./img/device_setting.png").default} width="200"/>
   <img src={require("./img/network_setting.png").default} width="200"/>
   <img src={require("./img/switch_connection_method.png").default} width="200"/>

2. Tippen Sie auf **Mit Gerät verbinden** und wählen Sie **Wi-Fi-Verbindung**.

   <img src={require("./img/connect_device.png").default} width="200"/>
   <img src={require("./img/select_wifi.png").default} width="210"/>

3. Wählen Sie das gewünschte Wi-Fi-Netzwerk aus, schließen Sie die Konfiguration ab und warten Sie auf die erfolgreiche Verbindung.

   <!-- <img src={require("./img/configure_wifi.png").default} width="200"/> -->

4. Kehren Sie zur Gerätedetailseite zurück und prüfen Sie in den **Netzwerk-Einstellungen**, ob die Verbindung auf Wi-Fi umgestellt wurde.

   <!-- <img src={require("./img/network_info_wifi.png").default} width="200"/> -->