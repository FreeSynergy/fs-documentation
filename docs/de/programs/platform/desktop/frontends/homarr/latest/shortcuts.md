# Homarr - Tastatur-Shortcuts

## Übersicht

Homarr dokumentiert **keine eigenen Tastatur-Shortcuts**. Bedient wird über Maus, Touch und die üblichen Browser-Tasten; Dialoge und Formulare folgen den Standard-Tastaturen der Mantine-Komponenten. Diese Datei listet deshalb, was tatsächlich funktioniert, und markiert verbreitet angenommene Shortcuts ausdrücklich als **nicht vorhanden**.

> Stand: aktuelle Homarr-Versionen (v1.x). Kurzfristige Änderungen sind möglich; nach Updates sollte diese Liste geprüft werden.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Ausgewählte Schaltfläche oder Liste auslösen |
| `Space` | Schalter/Checkbox umschalten, markierte Kachel aktivieren |
| `Esc` | Dialog, Dropdown oder Menü schließen |
| `F5` / `Ctrl+R` | Seite neu laden (Board wird neu abgerufen) |
| `Alt+←` / `Alt+→` | Browser zurück/vor (Board-Wechsel, Dialog-Historie) |
| `Strg+P` | Board ausdrucken (Browser-Druckdialog) |

---

## Navigation im Board

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Kacheln und Links in Lesereihenfolge ansteuern |
| `Enter` | Aktivierte App-Kachel öffnet die Ziel-URL |
| `↑` / `↓` | In Dropdowns (Board-Auswahl, Integrations-Auswahl) blättern |
| `↑` / `↓` | In der Autocomplete-Liste der Suche blättern |
| `Enter` | Suchvorschlag ausführen |
| `Esc` | Suchvorschläge schließen, Fokus verlassen |
| `Backspace` | Suchtext löschen, wenn das Suchfeld fokussiert ist |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `/` für Suche | ❌ Nicht vorhanden — Suchfeld muss angeklickt oder per `Tab` erreicht werden |
| `1`–`9` für Boards/Kacheln | ❌ Nicht vorhanden |
| Schnellstart einer App per Buchstabe | ❌ Nicht vorhanden |
| `g` dann `b` (Board wechseln) | ❌ Nicht vorhanden |

---

## Bearbeitung (Board, Widgets)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Schwebende Kachel-Werkzeuge (Bearbeiten, Entfernen) erreichen |
| `Enter` | Bearbeiten-Dialog der fokussierten Kachel öffnen |
| `Esc` | Widget-Dialog ohne Speichern schließen |
| `Enter` (im Dialog) | Standardaktion „Speichern“ auslösen |
| `Esc` (im Bearbeitungsmodus) | Bearbeitungsmodus verlassen, sofern kein Dialog offen ist |
| `Z` / `X` | ❌ Nicht vorhanden — kein Umschalten des Modus per Taste, nur über die Schaltfläche |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `e` für Bearbeitungsmodus | ❌ Nicht vorhanden |
| `Ctrl+Z` Rückgängig im Board | ❌ Nicht vorhanden — Layoutänderungen werden sofort gespeichert |
| `Entf` Kachel löschen | ❌ Nicht vorhanden — Werkzeuge-Symbol oder Rechtsklick nutzen |
| Pfeiltasten zum Verschieben einer Kachel | ❌ Nicht vorhanden — Drag & Drop mit der Maus oder per Touch |

### Kachel verschieben und vergrößern

| Geste | Funktion |
|-------|----------|
| Ziehen an der Griffzone | Kachel im Raster verschieben, Zielbereich rastet ein |
| Ziehen an Unterkante/Ecke | Breite/Höhe in Rasterschritten ändern |
| Langes Drücken (Touch) | Kachel aufnehmen (Mobil-Layout) |
| Board-Optionen → Spaltenanzahl | Rasterdichte ändern, statt einzelne Kacheln zu stapeln |

---

## Suche und Websuche

| Shortcut | Funktion |
|----------|----------|
| Klick auf Suchfeld + Text | Filtern der Board-Treffer |
| `↑` / `↓` | Trefferliste durchlaufen |
| `Enter` | Ersten/hervorgehobenen Treffer öffnen oder Websuche starten |
| `Esc` | Suchfeld leeren bzw. Vorschläge schließen |

Kurzkommandos im Suchtext (sogenannte Bangs) sind möglich und werden in [features.md](features.md) beschrieben; sie ersetzen keine Shortcuts.

---

## Dialoge und Formulare

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder innerhalb des Dialogs durchlaufen |
| `Enter` | Aktives Feld bestätigen, Standardaktion auslösen |
| `Esc` | Dialog abbrechen |
| `Space` | Auswahlliste öffnen, Schalter umschalten |
| `↑` / `↓` | Values in Zahlenfeldern und Auswahlen ändern |
| `Backspace` / `Entf` | Feldinhalt löschen |

---

## Instanz- und Nutzerverwaltung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Tabellenzeilen und Aktionen ansteuern (Nutzer, Integrationen) |
| `Enter` | Bearbeiten-Dialog des ausgewählten Eintrags öffnen |
| `Esc` | Dialog schließen |
| `/` in Suchfeldern | ❌ Nicht vorhanden — Filterfelder manuell fokussieren |

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser, nicht Homarr) |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang/-ende (Browser) |
| `Cmd+Plus` / `Cmd+Minus` | Zoom der Oberfläche |
| `Cmd+0` | Zoom zurücksetzen |
| `Esc` | Dialog schließen |

**Nicht vorhanden:** `Cmd+E` (Bearbeiten), `Cmd+/` (Suche), `Cmd+Z` (Layout rückgängig).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Komplette Kopfzeile, Kacheln und Dialoge erreichbar |
| `Enter` / `Space` | Kachelaktionen auslösen |
| `Esc` | Overlays und Menüs verlassen |
| `↑` / `↓` | Auswahlen und Vorschlagslisten bedienen |
| `Shift+Tab` | Rückwärts navigieren |

---

## Zusammenfassung

Homarr bietet **keine anwendungsspezifischen Shortcuts**. Nutzbar sind:

- **Browser-Tasten** für Neuladen, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in Dialogen, Menüs und Vorschlagslisten
- **Drag & Drop und Touch-Gesten** für Layout-Arbeiten

Wer Abkürzungen erwartet, erreicht sie über die Board-Organisation: wenige Boards, klare Kachelnamen und eine gewählte Standard-Suchmaschine machen die Maus überflüssiger als jede Tastenkombination.
