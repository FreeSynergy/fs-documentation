# TrueNAS - Tastatur-Shortcuts

## Übersicht

TrueNAS dokumentiert **keine eigenen Tastatur-Shortcuts** für die Web-UI. Es gelten die Browser-Tasten und die Standard-Tastaturen der Angular-/NG-ZORRO-Komponenten (Formulare, Dialoge, Menüs). Einzig das **Konsolenmenü** am Server selbst ist tastaturgesteuert (Ziffern zum Auswählen). Diese Datei listet, was real funktioniert, und markiert verbreitet angenommene Shortcuts ausdrücklich als **nicht vorhanden**.

> Stand: TrueNAS SCALE 24.x/25.x sowie CORE 13. Menüpunkte und Konsolennummern ändern sich über Versionen; nach Updates prüfen.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Bedienelemente ansteuern (Sidebar, Buttons, Felder) |
| `Enter` | Ausgewähltes Element auslösen, Standardaktion im Dialog |
| `Space` | Checkboxen/Schalter umschalten, Button auslösen |
| `Esc` | Dialog, Dropdown oder Job-Panel schließen |
| `F5` / `Strg+R` | Seite neu laden (SPA lädt den aktuellen Bereich nach) |
| `Alt+←` / `Alt+→` | Browser zurück/vor zwischen besuchten Bereichen |
| `Strg+F` | Text auf der Seite suchen (Browser) |
| `Strg+P` | Druckansicht (z. B. Reports) |

---

## Suche und Navigation

| Shortcut | Funktion |
|----------|----------|
| Klick auf Suchfeld + Text | Globale Suche: Seiten, Datasets, Freigaben, Apps |
| `↑` / `↓` | In Suchvorschlägen und Auswahllisten blättern |
| `Enter` | Markierten Suchvorschlag öffnen |
| `Esc` | Suchfeld leeren / Vorschläge schließen |
| `Tab` | Sidebar-Punkte nacheinander ansteuern |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `/` oder `Strg+K` für die globale Suche | ❌ Nicht dokumentiert — Suchfeld per Klick/`Tab` fokussieren |
| `1`–`9` für Sidebar-Bereiche | ❌ Nicht vorhanden |
| Schnellsprung zu einem Dataset per Kürzel | ❌ Nicht vorhanden |
| `g` dann `d` (zu Datasets) | ❌ Nicht vorhanden |

---

## Formulare und Assistenten

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder eines Assistenten durchlaufen |
| `Enter` | Standardaktion („CREATE“, „SAVE“) auslösen |
| `Esc` | Dialog abbrechen |
| `Space` | Kontrollkästchen und Schalter umschalten |
| `↑` / `↓` | Zahlenfelder und Auswahllisten ändern |
| `Backspace` / `Entf` | Feldinhalt löschen |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `Strg+S` Speichern | ❌ Nicht vorhanden — Speichern heißt „SAVE“ per Klick |
| `Strg+Z` Rückgängig | ❌ Nicht vorhanden — Aktionen wirken sofort |
| `Entf` Dataset/Snapshot löschen | ❌ Nicht vorhanden — Drei-Punkte-Menü nutzen |
| Autovervollständigung in Dataset-Namensfeldern | ❌ Nicht vorhanden (Autocomplete nur in ausgewählten Auswahlfeldern, versionabhängig) |

---

## Tabellen (Datasets, Snapshots, Apps)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zeilenaktion (Drei-Punkte-Menü) erreichen, mit `Enter` öffnen |
| `↑` / `↓` | In geöffneten Menülisten blättern |
| `Esc` | Menü schließen |

Sortieren und Filtern laufen ausschließlich über Mausklicks auf Spaltenköpfe und Filterfelder.

---

## Bestätigungsdialoge

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Buttons „CANCEL“/bestätigenden Button erreichen |
| `Enter` | Bestätigungsbutton auslösen (bei Gefahr oft erst nach Texteingabe scharf) |
| `Esc` | Abbrechen, ohne die Aktion auszuführen |

---

## App-Konsolen und VM-VNC

| Kontext | Verhalten |
|---------|-----------|
| App-Console (Docker-Logs/TTY in der UI) | Terminal-Standard (`Strg+C` etc.), Fokus anklicken |
| VM-VNC-Konsole (ab 24.10) | Tasten gehen an den Gast; Sonderkombis (Strg+Alt+Entf) über das VNC-Menü der Konsole, nicht per Direkttaste (versionabhängig) |
| Web Shell (frühere Versionen/alternativ) | Shell-Standard, keine TrueNAS-Keys |

---

## Konsolenmenü am Server (tastaturgesteuert)

Am lokalen Bildschirm/Serial der Appliance erscheint ein Menü, das per Ziffer bedient wird (Nummern versionabhängig — Menüpunkt ankündigender Text entscheidet):

| Eingabe | Typische Funktion |
|---------|-------------------|
| Ziffer + `Enter` | Menüpunkt wählen (Netzwerk, Shell, Import, Reset UI …) |
| `Enter` | Menü zurück / Auswahl bestätigen |
| `Strg+C` | laufende Abfrage abbrechen (Shell-Ebene) |

Nach der Wahl **„Shell“** gilt normale Linux-Bash (CORE: FreeBSD-Shell): `midclaw call` bzw. `midclt call` für API-Aufrufe (siehe [api.md](api.md)).

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
| `Esc` | Dialog schließen |

**Nicht vorhanden:** `Cmd+S` (Speichern), `Cmd+K` (Suche in TrueNAS), `Cmd+E` (Bearbeiten).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Sidebar, Tabellen, Dialoge erreichbar |
| `Enter` / `Space` | Aktionen auslösen |
| `Esc` | Overlays und Menüs verlassen |
| `↑` / `↓` / `←` / `→` | Auswahlen, Bäume, Menüs bedienen |
| `Shift+Tab` | Rückwärts navigieren |

---

## Zusammenfassung

TrueNAS bietet **keine anwendungsspezifischen Shortcuts** in der Web-UI. Effizient arbeitet man mit:

- **Globaler Suche** (Klick + Tippen) statt Sidebar-Klicken
- **`Tab`/`Enter`/`Esc`/Pfeiltasten** in Assistenten und Menüs
- **Konsolenmenü und `midclaw`/`midclt`** für wiederkehrende Wartungsschritte

Wer Tastenkürzel vermisst, automatisiert über die API (siehe [api.md](api.md)) — dort ersetzt ein JSON-RPC-Aufruf jede Klickfolge.
