# Proxmox VE - Tastatur-Shortcuts

## Übersicht

Proxmox VE dokumentiert **keine eigenen globalen Tastatur-Shortcuts** für die Weboberfläche. Bedient wird über Baum, Reiter, Buttons und Dialoge mit den üblichen Browser- und Formular-Tasten. Eigene Tastaturwege gibt es nur **innerhalb der Konsolen** (Node-Shell, VM-Serial, noVNC/xterm.js) — dort gelten Terminal- und Gast-System-Normen. Diese Datei trennt beides sauber und markiert verbreitet angenommene Shortcuts als **nicht vorhanden**.

> Stand: Proxmox VE 8.x. Die Konsolentechnik wechselt mit den Versionen (noVNC → xterm.js); nach Updates diese Liste prüfen.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Bedienelemente ansteuern (Baum, Reiter, Buttons, Felder) |
| `Enter` | Ausgewähltes Element öffnen/Bestätigen (Standardaktion im Dialog) |
| `Space` | Checkboxen/Schalter umschalten, markierten Button auslösen |
| `Esc` | Dialog, Dropdown oder Overlay ohne Änderung schließen |
| `F5` / `Strg+R` | Seite neu laden (State wird aus der API frisch geladen) |
| `Alt+←` / `Alt+→` | Browser zurück/vor (Objekt-/Reiter-Historie) |
| `Strg+F` | Text auf der Seite suchen (Browser) |
| `Strg+P` | Druckansicht (z. B. Summary) |

---

## Navigation im Baum und in Reitern

| Shortcut | Funktion |
|----------|----------|
| `↑` / `↓` | Im Ressourcenbaum und in Auswahllisten blättern |
| `←` / `→` | Baumknoten zu-/aufklappen |
| `Enter` | Markierten Baumknoten öffnen |
| `Tab` | Reiterleiste erreichen, mit `Enter` Reiter wechseln |
| `Strg+F` + Suchtext | In langen Tabellen suchen (Browser-Funktion) |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `/` für Sprung in die Suchleiste | ❌ Nicht vorhanden — Suchfeld anklicken oder per `Tab` erreichen |
| `1`–`9` für Reiter | ❌ Nicht vorhanden |
| VM per VMID + Enter starten | ❌ Nicht vorhanden — Suchfeld + Buttons nutzen |
| `g` dann `n` (zu Nodes) | ❌ Nicht vorhanden |

---

## Dialoge und Assistenten

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder und Reiter des Dialogs durchlaufen |
| `Enter` | Standardaktion („Create“, „OK“) auslösen |
| `Esc` | Dialog abbrechen |
| `Space` | Schalter umschalten, Radio-Gruppen wechseln |
| `↑` / `↓` | Zahlenfelder und Auswahlen ändern |
| `Backspace` / `Entf` | Feldinhalt löschen |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `Strg+S` Speichern | ❌ Nicht vorhanden — Speichern heißt „OK/Create/Apply“ per Klick |
| `Strg+Z` Rückgängig | ❌ Nicht vorhanden — Aktionen wirken sofort, Undo existiert nicht |
| `Entf` VM/Regel löschen | ❌ Nicht vorhanden — Aktionsmenü (`⋮`) bzw. Delete-Button |
| Pfeiltasten zum Umsortieren der Boot-Reihenfolge | ❌ Nicht vorhanden — Drag & Drop |

---

## Tabellen (Grids)

| Shortcut | Funktion |
|----------|----------|
| `↑` / `↓` | Zeile markieren (Grid-Standard) |
| `Enter` | Standardaktion der markierten Zeile (objektabhängig) |
| `Tab` | In Zeilen auf Aktionsmenüs/Buttons navigieren |
| `Esc` | Geöffnete Aktionsmenüs (`⋮`) wieder schließen |

Der Rest läuft über Mausklicks: `⋮`-Menüs, Edit-Dialoge, Task-Panel.

---

## Konsolen: Node-Shell und Terminal

Die Browser-Shell (`xterm.js`) ist eine echte Linux-Shell — es gelten Shell-Normen, keine Proxmox-Keys:

| Shortcut | Funktion |
|----------|----------|
| `Strg+C` | Vordergrundprozess abbrechen |
| `Strg+D` | Shell beenden |
| `Strg+L` | Bildschirm leeren |
| `Pfeil hoch/runter` | Kommandoverlauf |
| `Tab` | Kompletter/Autovervollständigung (bash) |

Nützliche reale Befehle statt Shortcuts: `pvesh get /version`, `qm list`, `pct list`, `pvesm status`.

---

## Konsolen: noVNC / xterm.js-Grafikkonsole von VMs

Tastatureingaben gehen an den **Gast** — Proxmox sendet keine Sonderkombinationen per Direkttaste:

| Aktion | Weg |
|--------|-----|
| `Strg+Alt+Entf` (Gast) | Über das Konsolen-Menü (Zahnrad/Tasten-Menü) senden — Tastenkombination löst im Browser sonst Browser-Aktionen aus (versionabhängig) |
| Sonderzeichen/F-Tasten | Konsolen-Menü „Sondertasten“ oder Gast-treue Eingabe nach Klick in die Konsole |
| Clipboard/Paste | Über Konsolen-Menü (versionabhängig) |

**Nicht vorhanden:** Kein Proxmox-Key zum Wechseln zwischen Konsolen-Typen (noVNC/xterm.js/SPICE) — das erledigt das Dropdown am Objektkopf.

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`; Konsolen leiten `Cmd`-Kombinationen je nach Einstellungen an den Gast weiter (versionabhängig).

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Textsuche (Browser) |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang/-ende (Browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom |
| `Esc` | Dialog schließen |

**Nicht vorhanden:** `Cmd+S` (Speichern), `Cmd+/` (Suche), `Cmd+E` (Bearbeiten).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Baum, Reiter, Buttons, Dialogfelder erreichbar |
| `Enter` / `Space` | Aktionen auslösen |
| `Esc` | Overlays verlassen |
| `↑` / `↓` / `←` / `→` | Baum, Listen, Auswahlen bedienen |
| `Shift+Tab` | Rückwärts navigieren |

---

## Zusammenfassung

Proxmox VE bietet **keine anwendungsspezifischen Kurzbefehle** in der Web-UI. Effizient arbeiten heißt:

- **Suchleiste** (VMID/Name/Tag) statt Baumklicken, **`Tab`/`Enter`/`Esc`** in Dialogen
- **Browser-Tasten** für Neuladen, Suche und Zoom
- **Shell/Konsole** mit Linux-Standardtasten und `pvesh`/`qm`/`pct` für Wiederkehraufgaben

Wer echte Abkürzungen braucht, verlagert sie in die API oder CLI (siehe [api.md](api.md)) — dort ersetzt ein Befehl jede Mausklick-Kette.
