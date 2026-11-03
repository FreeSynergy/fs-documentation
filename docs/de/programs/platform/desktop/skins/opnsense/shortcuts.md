# OPNsense - Tastatur-Shortcuts

## Übersicht

OPNsense dokumentiert **keine eigenen Tastatur-Shortcuts** für die Web-UI. Es gelten die Browser-Tasten sowie die Standard-Tastaturen der Formular- und Tabellenkomponenten (Ant-Design/Bootstrap-Mix). Effiziente Tastaturwege existieren nur in der **Konsole/Shell** des Geräts (Linux-artige BSD-Shell, vi, `opnsense-repl`). Diese Datei listet real Nutzbares und markiert verbreitet angenommene Shortcuts ausdrücklich als **nicht vorhanden**.

> Stand: OPNsense 24.x/25.x (22.7+ UI). Nach Major-Updates diese Liste prüfen.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Menüpunkte, Buttons, Felder ansteuern |
| `Enter` | Ausgewähltes Element auslösen, Dialog-Standardaktion |
| `Space` | Checkboxen/Schalter umschalten |
| `Esc` | Edit-Dialog abbrechen, Auswahllisten schließen |
| `F5` / `Strg+R` | Seite neu laden |
| `Alt+←` / `Alt+→` | Browser zurück/vor zwischen besuchten Seiten |
| `Strg+F` | Text auf der Seite suchen (Browser) |
| `Strg+P` | Seitendruck (z. B. Regel-Übersicht) |
| `F12` | Entwicklerwerkzeuge — offiziell empfohlen, um UI-calls (`/api/...`) für die API-Nutzung abzulesen |

---

## Menü und Navigation

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Top-Menü erreichen, mit `Enter` öffnen, Untermenü durchlaufen |
| `↑` / `↓` | In geöffneten Dropdowns blättern |
| `Esc` | Geöffnetes Menü schließen |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `/` für Suche | ❌ Nicht vorhanden — Suchfeld im Grid anklicken |
| `1`–`6` für Top-Menüs | ❌ Nicht vorhanden |
| Globale Befehlspalette (`Cmd+K`) | ❌ Nicht vorhanden |
| Sprung zu „Firewall ▸ Rules“ per Tastenkürzel | ❌ Nicht vorhanden |

---

## Grids (Regeln, Aliases, Logs)

| Shortcut | Funktion |
|----------|----------|
| Klick Suchfeld + Text | Serverseitige Suche (`searchPhrase`), Ergebnisliste neu geladen |
| `Enter` | Suche bestätigen (wo ein Suchbutton existiert) |
| `Tab` + `Enter` | `⋮`-Zeilenmenü öffnen und Punkt auslösen |
| `Esc` | Zeilenmenü schließen |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| Pfeiltasten zum Verschieben einer Regel | ❌ Nicht vorhanden — Drag & Drop am Griff |
| `Entf` Regel löschen | ❌ Nicht vorhanden — `⋮`-Menü Delete |
| `Strg+A` Mehrfachauswahl | ❌ Nicht vorhanden (kein Bulk-Editing in Standard-Grids) |
| `x` Regel deaktivieren | ❌ Nicht vorhanden — Deactivate im Menü |

---

## Formulare und Dialoge

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder und Accordion-Abschnitte durchlaufen |
| `Enter` | „Save“/Standardaktion auslösen |
| `Esc` | Dialog schließen (ungespeicherte Werte verwerfen) |
| `Space` | Schalter umschalten, Radio-Gruppen wechseln |
| `↑` / `↓` | Zahlenfelder und Auswahlen ändern |
| `Backspace` / `Entf` | Feldinhalt löschen |

Wichtig: **Save** speichert nur die Konfiguration — Regeln/Services werden erst über den **Apply**-Button am Seitenanfang aktiv (kein Tastaturweg dafür dokumentiert).

---

## Type-ahead-Selects (Auswahlfelder)

| Eingabe | Funktion |
|---------|----------|
| Text tippen | Filtert lange Auswahllisten (Interfaces, Aliases, Zertifikate) |
| `Enter` | Markierten Eintrag übernehmen |
| `Backspace` | Letzten Buchstaben der Filterkette löschen |
| Klick auf das `x` am Feld | Auswahl zurücksetzen (kein Key dokumentiert) |

---

## Konsole und Shell am Gerät

Das Konsolenmenü der Firewall ist zifferngesteuert (Nummern versionabhängig — Menütext lesen), danach gilt BSD-Shell-Standard:

| Eingabe | Funktion |
|---------|----------|
| Ziffer + `Enter` | Konsolenmenüpunkt (Interfaces, Shell, Neustart …) |
| `Strg+C` | Abbruch (Shell) |
| Tab-Vervollständigung | in `opnsense-repl` und modernen Shells |
| `opnsense-repl` | interaktiver Python-REPL mit Systemzugriff |
| `opnsense update` / Firmware-Menüpunkt | Updates (menügeführt, versionabhängig) |

Das ist keine Web-UI-Steuerung, sondern der reale Tastaturweg für Wartung.

---

## API-Workflows per Tastatur (Indirekt)

Der offiziell empfohlene Weg, API-Aufrufe zu lernen: **`F12` → Netzwerk-Tab → UI-Aktion auslösen → Request kopieren**. Das ersetzt kein Shortcut-System, ist aber der dokumentierte Lernpfad (Entwickler-Doku).

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Textsuche (Browser) |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang/-ende (Browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom |
| `Esc` | Dialog/Menü schließen |

**Nicht vorhanden:** `Cmd+S` (Speichern), `Cmd+/` (Suche), `Cmd+E` (Bearbeiten).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Top-Menü, Grid-Aktionen, Dialogfelder erreichbar |
| `Enter` / `Space` | Buttons und Schalter auslösen |
| `Esc` | Overlays verlassen |
| `↑` / `↓` | Auswahllisten und Dropdowns bedienen |
| `Shift+Tab` | Rückwärts navigieren |

---

## Zusammenfassung

OPNsense bietet **keine anwendungsspezifischen Shortcuts** in der Web-UI. Praktisch sind:

- **Browser-Tasten** plus `F12`-Netzwerktrace als offizielles API-Lernwerkzeug
- **`Tab`/`Enter`/`Esc`/Pfeiltasten** in Grids, Akkordeons und Dialogen
- **Konsolenmenü + Shell** (`opnsense-repl`) für Wartung ohne Browser

Wiederkehrende Regel-/Alias-Arbeiten gehören ohnehin in die API (siehe [api.md](api.md)) — dort ersetzt ein `curl` jede Klickfolge und jeden fehlenden Shortcut.
