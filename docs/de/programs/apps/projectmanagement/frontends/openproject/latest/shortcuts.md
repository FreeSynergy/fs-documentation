# OpenProject - Tastatur-Shortcuts

## Übersicht

OpenProject veröffentlicht **keine zentrale Liste eigener Tastatur-Shortcuts**. Bedient wird über Maus, Touch und die üblichen Browser-Tasten; Formularfelder folgen den Standard-Tastaturen des Browsers, der Rich-Text-Editor folgt gängigen Editor-Konventionen. Diese Datei listet, was tatsächlich funktioniert, und markiert verbreitet angenommene Kurzzeichen ausdrücklich als **nicht vorhanden**.

> Stand: aktuelle OpenProject-Versionen (13.x/14.x-Linie). Details können sich je Version ändern; nach Updates diese Liste prüfen.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen (Leiste, Filter, Tabelle) |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Ausgewählte Schaltfläche oder Formularaktion auslösen |
| `Space` | Checkboxen/Zellen der Mehrfachauswahl markieren |
| `Esc` | Offene Overlay-Elemente (Autocomplete, Picker) schließen |
| `F5` / `Ctrl+R` | Seite neu laden |
| `Alt+←` / `Alt+→` | Browser zurück/vor (Modulwechsel verläuft über URLs) |
| `Ctrl+P` | Aktuelle Ansicht drucken |
| `Ctrl+F` | Text auf der Seite suchen (Browser, nicht OpenProject) |

---

## Navigation

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Modul-Leiste, Projektauswahl und Tabellenzeilen ansteuern |
| `Enter` | Markierte Tabelle-Zeile öffnen (Detail-Split) oder Link folgen |
| `↑` / `↓` | In Auswahllisten blättern (Projekt-, Benutzer-, Versions-Autocomplete) |
| `Esc` | Autocomplete-Vorschläge schließen |
| `Backspace` | Suchtext im Auswahlfeld löschen, wenn fokussiert |
| Leertaste + Pfeile | Scrollen großer Tabellen/Gantt ohne Mauszeiger (Browser) |

**Nicht vorhanden:**

| Gewünschtes Shortcut | Status |
|----------------------|--------|
| `/` für Suche | ❌ Nicht vorhanden - Suchfeld muss angeklickt oder per `Tab` erreicht werden |
| `Ctrl+K` / Befehlspalette | ❌ Nicht vorhanden |
| `g` + Buchstabe (Modulsprung) | ❌ Nicht vorhanden |
| `J` / `K` (nächstes/vorheriges Element) | ❌ Nicht vorhanden |
| Zifferntasten für Module | ❌ Nicht vorhanden |

---

## Bearbeitung

| Shortcut | Funktion |
|----------|----------|
| `Enter` | Inline-Feld bestätigen und speichern (Inline-Bearbeitung, versionsabhängig) |
| `Esc` | Inline-Bearbeitung abbrechen, Wert zurücksetzen |
| `Tab` | Nächstes Inline-Feld erreichen (wie Tabulator im Formular) |
| `Ctrl+A` | Text im Feld/Editor alles markieren (Browser) |
| `Ctrl+C` / `Ctrl+V` / `Ctrl+X` | Kopieren, Einfügen, Ausschneiden (Browser) |
| `Ctrl+Z` / `Ctrl+Y` | Rückgängig/Wiederholen **innerhalb** eines noch offenen Textfeldes; kein globales Undo für gespeicherte Änderungen |

### Rich-Text-Editor (Beschreibungen, Kommentare)

Die Editoren folgen gängigen Konventionen; eine offizielle Kurzzeichenliste existiert nicht (versionsabhängig):

| Shortcut | Funktion |
|----------|----------|
| `Ctrl+B` | Fett |
| `Ctrl+I` | Kursiv |
| `Ctrl+U` | Unterstreichen |
| `Ctrl+K` | Link einfügen/Bearbeitungsbubble öffnen |
| `Ctrl+Shift+7` | Nummerierte Liste (Editor-Konvention, nicht garantiert) |
| `Ctrl+Shift+8` | Aufzählung (Editor-Konvention, nicht garantiert) |
| `Ctrl+Z` | Rückgängig im Editor-Text |

---

## Suche

| Shortcut | Funktion |
|----------|----------|
| Klick auf das Lupen-Symbol | Globale Suche öffnen |
| `Enter` | Suchbegriff ausführen |
| `Esc` | Offene Vorschlagsliste schließen |
| `Ctrl+F` | Seitentext durchsuchen (Browser) |

**Nicht vorhanden:**

| Gewünschtes Shortcut | Status |
|----------------------|--------|
| Zentraler Such-Hotkey (`/`, `s`, `Ctrl+K`) | ❌ Nicht dokumentiert |
| `Ctrl+H` Ersetzen in Feldern | ❌ Nicht vorhanden (nur Browser-Ersetzen in Adress-/Textfeldern) |

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Ctrl`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+A` / `Cmd+C` / `Cmd+V` | Alles markieren, kopieren, einfügen |
| `Cmd+Z` | Rückgängig im aktiven Textfeld |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang/-ende (Browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom der Oberfläche |
| `Cmd+B` / `Cmd+I` / `Cmd+K` | Fett, Kursiv, Link im Rich-Text-Editor |

**Nicht vorhanden:** `Cmd+K` als Befehlspalette der Anwendung (Editor-Link-Konvention siehe oben), `Cmd+E` für Bearbeiten, `Cmd+S` als globaler Speicherknopf (Speichern erfolgt über Buttons oder Inline-Bestätigung).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Komplette Bedienoberfläche rückwärts/vorwärts erreichen |
| `Enter` / `Space` | Buttons, Links und Markierungen auslösen |
| `Esc` | Picker, Autocomplete und Menüs verlassen |
| `↑` / `↓` | Auswahlen und Vorschlagslisten bedienen |
| `Ctrl+Plus` | UI vergrößern ohne Funktionsverlust |

---

## Zusammenfassung

OpenProject bietet **keine anwendungsspezifischen Kurzzeichen**. Nutzbar sind:

- **Browser-Tasten** für Neu laden, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Esc`, `↑`/`↓`** in Formularen, Autocompletes und der Inline-Tabelle
- **Editor-Konventionen** (`Ctrl+B/I/K`) in Rich-Text-Feldern, je Version unterschiedlich gedeckt

Tempo erreicht man stattdessen über gespeicherte Abfragen, Inline-Bearbeitung und die Tastaturbestätigung von Tabellenfeldern - nicht über Hotkeys.
