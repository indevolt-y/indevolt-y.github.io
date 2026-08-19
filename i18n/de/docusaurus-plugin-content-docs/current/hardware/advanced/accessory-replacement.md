---
title: Zubehör Austauschen
description: Austausch des WiFi+LAN-Moduls sowie Migration von Geräteeinstellungen und historischen Daten.
---

# Zubehör Austauschen

Diese Anleitung gilt für folgende Modelle:

- PowerFlex 2000  
- PowerFlex 2000 Eco  
- PowerFlex 3000 AC  
- PowerFlex 3000 Hybrid  
- SolidFlex 2000  
- SolidFlex 2000 Eco  
- SolidFlex 3000 AC  

---

## Vorbereitung

Bitte stellen Sie sicher, dass die Verpackung unbeschädigt ist. Öffnen Sie die Verpackung und entnehmen Sie alle Komponenten. Prüfen Sie anhand der Packliste, ob Menge und Modell korrekt sind.

<img src={require("./img/packing_list.png").default} width="960"/>

---

## Schritt 1: Altes Modul entfernen

:::warning
Stellen Sie vor dem Austausch sicher, dass das Gerät spannungsfrei ist.
:::

**1. Befestigungsschrauben entfernen**

Entfernen Sie die 6 Befestigungsschrauben des Moduls mit dem im Lieferumfang enthaltenen Schraubendreher.

> Hinweis: Bewahren Sie die Schrauben sorgfältig auf, da sie für die Montage des neuen Moduls wiederverwendet werden.

<img src={require("./img/remove_screws.png").default} width="360"/>

**2. Altes Modul entfernen**

Ziehen Sie das Modul vorsichtig entlang der Steckrichtung aus dem Steckplatz.

<img src={require("./img/remove_module.png").default} width="360"/>

**3. Kommunikationskabel trennen**

Drücken Sie die Verriegelung am Stecker und ziehen Sie das Kommunikationskabel vorsichtig heraus.

<img src={require("./img/unplug_cable.png").default} width="360"/>

:::tip
Nach dem Entfernen des Moduls prüfen Sie bitte, ob die Schraubpositionen des Geräts mit dem neuen Modul übereinstimmen.
<img src={require("./img/model_confirmation.png").default} width="360"/>
:::

---

## Schritt 2: Neues Modul installieren

**1. Kommunikationskabel anschließen**

Stecken Sie das Kommunikationskabel in den entsprechenden Anschluss der neuen PCB-Platine und stellen Sie sicher, dass es fest sitzt.

<img src={require("./img/connect_cable.png").default} width="360"/>

**2. Neues Modul einsetzen**

Richten Sie das neue Modul am Steckplatz aus und schieben Sie es vorsichtig hinein, bis es vollständig sitzt.

<img src={require("./img/install_module.png").default} width="360"/>

**3. Modul befestigen**

Verwenden Sie die zuvor entfernten 6 Schrauben, um das Modul wieder zu befestigen, und ziehen Sie diese mit dem Schraubendreher fest.

<img src={require("./img/fasten_screws.png").default} width="360"/>

**4. Installation überprüfen**

Stellen Sie sicher, dass:

- das Modul vollständig eingesetzt ist  
- alle Schrauben fest angezogen sind  
- die Abdeckung sicher sitzt und keine Lockerheit aufweist  

<img src={require("./img/check_installation.png").default} width="360"/>

**5. Neues Seriennummern-Etikett anbringen**

Kleben Sie das neue SN-Etikett aus der Verpackung über das alte Seriennummernlabel. Das Gerät wird anschließend über die neue Seriennummer in der App erkannt.

Bitte stellen Sie sicher, dass beide folgenden Etiketten korrekt überklebt werden:

- Original-SN-Etikett oben rechts am Gerät  

  <img src={require("./img/cover_sn1.png").default} width="720"/>

- Typenschild an der Geräte-Seite  

  <img src={require("./img/cover_sn2.png").default} width="600"/>

---

## Schritt 3: Geräteinformationen in der App aktualisieren

:::tip
Bitte stellen Sie vor dem Start sicher:
- Bluetooth am Smartphone ist aktiviert  
- Das Gerät ist eingeschaltet  
- Das Smartphone befindet sich während des gesamten Vorgangs möglichst nah am Gerät  
:::

### 1. Geräteinformationen aktualisieren

1. Öffnen Sie die Geräteeinstellungen und tippen Sie auf **Zubehör Austauschen**.  
2. Scannen Sie den QR-Code auf dem neuen Zubehör.  
3. Tippen Sie auf **Weiter**, prüfen Sie die Informationen unter **Bestätigung des Austauschs** und bestätigen Sie mit **OK**.  
4. Warten Sie, bis der Austausch abgeschlossen ist.  

   > Während dieses Vorgangs werden Zubehörinformationen automatisch aktualisiert und Geräteeinstellungen migriert, einschließlich Cluster-Konfiguration, Lastquelle und verknüpfter Geräte.

5. Nach erfolgreicher Aktualisierung tippen Sie auf **Weiter**, um fortzufahren.

<img src={require("./img/accessory_replacement.png").default} width="240"/>
<img src={require("./img/scan_qr_code.png").default} width="240"/>
<img src={require("./img/accessory_info.png").default} width="240"/>
<img src={require("./img/confirm_replacement.png").default} width="240"/>
<img src={require("./img/connect_accessory.png").default} width="240"/>
<img src={require("./img/connect_accessory_success.png").default} width="240"/>

### 2. Historische Daten migrieren

Tippen Sie auf **Migration Starten**, um die historischen Daten zu übertragen.

Wenn Sie die Migration derzeit nicht durchführen möchten, können Sie auf **Überspringen** tippen. Die Migration kann später auch unter [Austauschverlauf](#4-austauschverlauf-anzeigen) gestartet werden.

<img src={require("./img/data_sync.png").default} width="240"/>
<img src={require("./img/skip_data_sync.png").default} width="240"/>


### 3. Gerät erneut mit dem Netzwerk verbinden

1. Geben Sie WLAN-Name (SSID) und Passwort ein und tippen Sie auf **Einrichten**.  
2. Warten Sie, bis die Netzwerkverbindung erfolgreich hergestellt wurde.  

<img src={require("./img/wifi_settings.png").default} width="240"/>
<img src={require("./img/wifi_connected.png").default} width="240"/>


### 4. Austauschverlauf anzeigen

Um frühere Austauschvorgänge anzuzeigen, gehen Sie zu: **Einstellungen > Zubehör Austauschen**.

Im Bereich **Austauschverlauf** können Sie:

- Austauschhistorie anzeigen, einschließlich Zeitpunkt, Migrationsstatus der Einstellungen und Datenmigration  
- In einem Eintrag auf **Migration Starten** tippen, um den Migrationsprozess zu starten, falls die Datenmigration noch nicht begonnen wurde  

<img src={require("./img/accessory_replacement.png").default} width="240"/>
<img src={require("./img/replacement_history.png").default} width="240"/>
<img src={require("./img/device_migration.png").default} width="240"/>

:::info
Die Migration historischer Daten erfolgt nach dem Start automatisch über die Cloud. Währenddessen ist kein Verbleib auf der Migrationsseite erforderlich.

Sie können den Fortschritt und Status jederzeit im Bereich **Austauschverlauf** einsehen.
:::