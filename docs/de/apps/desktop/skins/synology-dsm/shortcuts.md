# Synology DSM - Tastatur-Steuerung

## Übersicht

DSM führt **keine öffentliche Shortcut-Liste**. Das Portal ist auf Maus und Touch ausgelegt; verfügbar sind die Browser-Standardtasten sowie die Feld- und Listen-Tastatur der Dialoge. Diese Datei listet, was tatsächlich funktioniert, kennzeichnet verbreitet angenommene Kombinationen ausdrücklich als **nicht vorhanden** und ergänzt die **Systembefehle**, die statt virtueller Kurzschlüsse verwendet werden.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Ausgewählte Schaltfläche, Dialogaktion oder markierte Datei öffnen |
| `Space` | Auswahl umschalten, Schalter auslösen |
| `Esc` | Dialog, Kontextmenü oder Suche abbrechen |
| `F5` / `Ctrl+R` | Portal neu laden |
| `Alt+←` / `Alt+→` | Browser zurück/vor (innerhalb einer Anwendung) |
| `Strg+P` | Druckansicht (Protokolle, Berichte) |
| `F12` | Entwicklerwerkzeuge (nützlich für `entry.cgi`-Beobachtungen) |

---

## Navigation im Portal

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Obere Leiste, Menüpunkte und Fenster ansteuern |
| `Enter` | Menüpunkt bzw. Symbol auslösen, Fenster aktivieren |
| `↑` / `↓` | In Listen und Auswahlfeldern blättern |
| `←` / `→` | Baumansicht zu-/aufklappen (File Station) |
| `Home` / `Ende` | Listenanfang / -ende |
| `Esc` | Hauptmenü, Kontextmenü oder Suche schließen |
| `Backspace` | Im Suchfeld löschen; in manchen Listen eine Ebene zurück |

**Nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `/` für die globale Suche | ❌ Nicht vorhanden – Suchfeld oben muss angeklickt werden |
| `1`–`9` für Pakete | ❌ Nicht vorhanden |
| Alt+Tab zwischen DSM-Fenstern | ❌ Nicht vorhanden – Fensterwechsel über App-Leiste oder Fensterliste |
| `Win`-Taste als „Hauptmenü“ | ❌ Nicht vorhanden – Symbol oben links |
| Springen zu einem Desktop-Widget | ❌ Nicht vorhanden |

---

## Dateien und Ordner (File Station)

| Shortcut | Funktion |
|----------|----------|
| `Enter` | Markierte Datei öffnen bzw. Ordner betreten |
| `Strg+A` | Alle Einträge der aktuellen Liste markieren |
| `Strg+Klick` | Einzelne Einträge zur Auswahl hinzufügen |
| `Umschalt+Klick` | Bereich auswählen |
| `Entf` | Markierte Datei in den Papierkorb verschieben (Bestätigungsdialog) |
| `Esc` | Umbenennungs- oder Auswahlvorgang abbrechen |
| Text eingeben | In der Liste zum passenden Namen springen |

**Nicht eindeutig dokumentiert / nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `F2` umbenennen | nicht offiziell dokumentiert – Kontextmenü „Umbenennen“ verwenden |
| `Strg+C` / `Strg+V` kopieren/einfügen | ❌ Nicht vorhanden – Kontextmenü oder Zielordner-Dialog nutzen |
| `Strg+Z` Aktion rückgängig | ❌ Nicht vorhanden – Papierkorb bzw. Snapshot-Recovery nutzen |
| `Strg+X` verschieben | ❌ Nicht vorhanden – „Verschieben“-Dialog verwenden |

---

## Aufgaben, Fenster und Dialoge

| Shortcut | Funktion |
|----------|----------|
| `Enter` | Standardaktion des aktiven Dialogs („OK“, „Weiter“) |
| `Esc` | Dialog abbrechen, Aufgaben-Overlay schließen |
| `Tab` / `Shift+Tab` | Felder im Dialog durchlaufen |
| `Space` | Auswahlliste öffnen, Schalter umschalten |
| `↑` / `↓` | Werte in Zahlenfeldern und Auswahlen ändern |
| `Page Up` / `Page Down` | Listenabschnitte wechseln |

**Nicht vorhanden:** `Ctrl+W` Fenster schließen (Browser schließt den Tab), `Ctrl+Q` Abmelden, dedizierte Tasten für „Alle Fenster minimieren“.

---

## Suche und Filter

| Shortcut | Funktion |
|----------|----------|
| Klick ins Suchfeld + Text | Universal Search starten |
| `Enter` | Suche ausführen, markierten Treffer öffnen |
| `Esc` | Suchfeld leeren bzw. Ergebnispanel schließen |
| `↑` / `↓` | Trefferliste durchlaufen |
| Filterfelder (Typ, Freigabe) | per Klick setzen – keine Tastenkürzel |

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Portal neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+A` | Alle Einträge markieren |
| `Cmd+Klick` | Mehrfachauswahl in Listen |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang / -ende |
| `Cmd+Plus` / `Cmd+Minus` | Zoom |
| `Cmd+0` | Zoom zurücksetzen |
| `Fn+Entf` | Löschen (entspricht `Entf`) |

**Nicht vorhanden:** `Cmd+E` (Datei-Dialog), `Cmd+/` (Suchfeld), `Cmd+Z` (Operation rückgängig).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Leiste, Menü, Fenster und Dialoge erreichen |
| `Enter` / `Space` | Aktionen auslösen |
| `Esc` | Overlays und Menüs verlassen |
| `↑` / `↓` / `←` / `→` | Listen und Bäume bedienen |
| `Shift+Tab` | Rückwärts navigieren |
| Browser-Zoom | ohne Funktionsverlust nutzbar |

**Einschränkung**: Fenster-Anordnen, Drag-&-Drop-Upload und Mehrfachauswahl per Rahmen sind nur mit Zeigegerät möglich.

---

## Systembefehle statt Kurzschlüsse (SSH, Admin)

Für wiederkehrende Arbeiten nutzt DSM Kommandozeilenwerkzeuge statt Tastenkombinationen. Zugang: **Systemsteuerung → Terminal & SNMP → SSH-Dienst aktivieren** (Port 22).

| Befehl | Funktion |
|--------|----------|
| `sudo -i` | zur Root-Shell wechseln |
| `synopkglist` | installierte Pakete auflisten |
| `synopkg status <paket>` / `start` / `stop` | Paket steuern |
| `synoservice --status` | Systemdienste ansehen |
| `synosharectl --list` | Freigegebene Ordner auflisten (Parameter je DSM-Version) |
| `synouser --enum priv` | lokale Konten auflisten |
| `synogroup --enum` | Gruppen auflisten |
| `synodsmnotify @administrators Nachricht "Text"` | Portal-Benachrichtigung senden |
| `smartctl -a /dev/sataX` | SMART-Werte eines Laufwerks |
| `df -h`, `free -m`, `top` | Auslastung und Speicherplatz |

**Hinweis**: Befehle können Systemzustand ändern; vor Eingriffen Sicherung anlegen und Änderungen im **Protokoll-Center** nachhalten.

---

## Zusammenfassung

DSM bietet **keine anwendungsspezifischen Shortcuts**. Nutzbar sind:

- **Browser-Tasten** für Neuladen, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Esc`, Pfeiltasten, `Strg/Cmd+A`** in Fenstern, Listen und Dialogen
- **Systembefehle** (`synopkg`, `synosharectl`, `synouser`, `synodsmnotify`) für wiederkehrende Aufgaben
- **Aufgabenplanung** und **Ereignisskripte** als eigentlicher Automatisierungsweg
