# Dashy - Tastatur-Shortcuts

## Übersicht

Dashy ist auf Tastaturbedienung ausgelegt: Es gibt **keinen Aktivierungs-Key für die Suche** — einfach tippen genügt. Dazu kommen Tasten zum Navigieren, Öffnen und Leeren sowie optionale **Hotkeys pro Kachel** (`0`–`9`). Die hier gezeigten Kombinationen entsprechen der offiziellen Dokumentation; darüber hinausgehende Tasten sind nicht vorhanden.

---

## Allgemein

| Shortcut | Funktion |
|----------|----------|
| *einfach tippen* | Suche starten, ohne ein Feld zu fokussieren; Treffer filtern in Echtzeit |
| `Esc` | Suchbegriff leeren, geöffnete Modal-Fenster schließen |
| `Enter` | Ersten Treffer öffnen oder Websuche starten |
| `Tab` | Kacheln oder Treffer durchlaufen |
| `Shift+Tab` | Rückwärts durch Kacheln/Treffer |
| `↑` `↓` `←` `→` | Zwischen Kacheln und Treffern navigieren |
| `0` – `9` | Kachel mit hinterlegtem `hotkey` starten (muss in der Konfiguration gesetzt sein) |
| `F5` / `Ctrl+R` | Neu laden, Statuspunkte werden neu geprüft |

---

## Kacheln starten

| Shortcut | Funktion |
|----------|----------|
| `Enter` | Kachel mit der eingestellten Öffnungsart starten (`target`: neuer Tab, gleicher Tab, Modal, Workspace …) |
| `Alt+Enter` | Kachel im Modal-Fenster öffnen |
| `Ctrl+Enter` | Kachel in einem neuen Tab öffnen |
| Ziffer (`0`–`9`) | Kachel mit diesem Hotkey sofort öffnen (ersetzt das Suchen) |
| Rechtsklick | Kontextmenü mit allen Öffnungsarten (Maus, kein Shortcut) |

---

## Suche

| Shortcut | Funktion |
|----------|----------|
| Tippen | Filtert nach Titel, URL, Anbieter, Beschreibung, Alias und `tags` |
| `Enter` | Websuche mit der eingestellten Suchmaschine starten |
| `/w Begriff` | Kurzkommando (`searchBangs`): Begriff bei Wikipedia suchen |
| `:git Begriff` | Beispiel für ein eigenes Kurzkommando aus der Konfiguration |
| `https://…` eingeben | Bei aktivierter Option direkt zur Adresse springen statt zu suchen |
| `Esc` | Suchtext löschen, Ansicht zurücksetzen |
| `Backspace` | Einzelne Zeichen aus dem Suchtext entfernen |
| `Strg+A` | Suchtext markieren (Standard im Eingabefeld) |

**Hinweis zu URL-Aliasen**: Ein `alias` in der Konfiguration erlaubt den Sprung über die Adresse (`dashy.local/jelly`) — das ist kein Shortcut, sondern eine Route.

---

## Navigation

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zwischen Kopfzeilen-Elementen, Suchleiste und Kacheln wechseln |
| `↑` / `↓` | In Trefferlisten und Auswahlfeldern blättern |
| `←` / `→` | Kacheln in der Zeile anspringen |
| `Enter` | Ausgewähltes Element auslösen |
| `Esc` | Offene Dialoge schließen, Filter zurücknehmen |
| `Alt+←` | Zurück zur vorherigen Ansicht (Browser) |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `/` für Suchfeld | ❌ Nicht nötig und nicht belegt — Tippen funktioniert ohne Fokus |
| `g` dann `s` (Seite wechseln) | ❌ Nicht vorhanden — Seiten-Menü oder Adresse nutzen |
| Sprung zur Minimalansicht per Taste | ❌ Nicht vorhanden — Ansicht über Menü oder URL |

---

## Bearbeitung (Bearbeitungsmodus)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Bearbeitungs- und Löschungssymbole einer Kachel erreichen |
| `Enter` | Bearbeitungsdialog öffnen bzw. im Dialog speichern |
| `Esc` | Dialog ohne Speichern schließen |
| `Tab` / `Shift+Tab` | Felder im Kachel-Dialog durchlaufen |
| `↑` / `↓` | Werte in Zahlen- und Auswahlfeldern ändern |
| `Enter` (Feld „URL“) | Feld bestätigen |

### Verschieben und Anordnen

| Geste | Funktion |
|-------|----------|
| Ziehen an der Kachel | Kachel im Raster verschieben (nur im Bearbeitungsmodus) |
| Ziehen an der Sektions-Griffzone | Sektion umsortieren |
| Kontextmenü → Bearbeiten | Felder der Kachel ändern |
| Speichern | schreibt die Änderung in die Konfigurationsdatei |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `e` für Bearbeitungsmodus | ❌ Nicht dokumentiert — Schaltfläche im Kopfbereich nutzen |
| `Entf` zum Löschen einer Kachel | ❌ Nicht vorhanden — Lösch-Symbol im Bearbeitungsmodus |
| `Strg+Z` Rückgängig | ❌ Nicht vorhanden — es gibt zeitgestempelte Sicherungen im `user-data`-Ordner |
| Pfeiltasten zum Verschieben | ❌ Nicht vorhanden — nur Drag & Drop |

---

## Ansichten und Einstellungspanel

| Shortcut | Funktion |
|----------|----------|
| `Esc` | Einstellungspanel und Dialoge schließen |
| `Tab` | Bereiche des Einstellungspanels durchlaufen |
| `Enter` | Ausgewählten Bereich öffnen, Speichern auslösen |
| `Strg+F` | Text in der Seite suchen (Browser), nicht Dashy-eigen |

---

## Mac-Varianten

Die offizielle Dokumentation nennt die Kombinationen mit `Ctrl` und `Alt`. Auf macOS gelten die üblichen Entsprechungen; die `Cmd`-Varianten sind nicht separat dokumentiert.

| Shortcut | Funktion |
|----------|----------|
| `Esc` | Suche leeren, Dialog schließen |
| `Option+Enter` | Kachel im Modal öffnen (Entsprechung zu `Alt+Enter`) |
| `Cmd+Enter` | Kachel in neuem Tab öffnen (Entsprechung zu `Ctrl+Enter`) |
| `Cmd+R` | Neu laden |
| `Cmd+F` | Textsuche im Browser |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+Plus` / `Cmd+Minus` | Zoom |
| `0` – `9` | Hotkeys der Kacheln (identisch) |

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Alle Kacheln, Links und Dialogelemente erreichbar |
| `Enter` | Kachel öffnen, Dialog speichern |
| `↑` `↓` `←` `→` | Raster und Ziele ansteuern |
| `Esc` | Filter und Overlays verlassen |
| Tippen | Suche ohne Mausklick |

Die Tastatursteuerung deckt Suche, Navigation und Starten vollständig ab; Layout-Änderungen bleiben Maus- oder Touch-Aufgaben.

---

## Zusammenfassung

Dashy bietet als einziges der vier Dashboard-Programme eine **durchgängige Tastaturbedienung**:

- **Tippen** startet die Suche ohne Fokus-Key
- **`Tab`, `Shift+Tab`, Pfeiltasten** bewegen durch Kacheln und Treffer
- **`Enter`, `Alt+Enter`, `Ctrl+Enter`** öffnen mit unterschiedlichen Öffnungsarten
- **`Esc`** setzt Suche und Overlays zurück
- **`0`–`9`** starten per `hotkey` hinterlegte Kacheln
- **Keine Shortcuts** existieren für den Bearbeitungsmodus, für Rückgängig und für das Umsortieren
