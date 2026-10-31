# Unraid - Tastatur-Shortcuts

## Übersicht

Unraid bringt **keine eigenen Tastatur-Shortcuts** mit. Die Weboberfläche folgt den üblichen Browser-Tasten; Formulare, Dialoge und Tabellen nutzen die Standard-Tastaturen der HTML-Elemente. Diese Datei listet, was tatsächlich funktioniert, und markiert verbreitet angenommene Shortcuts ausdrücklich als **nicht vorhanden**.

> Stand: aktuelle Unraid-Versionen (6.12/7.x). Kleinere Änderungen sind möglich; nach Updates sollte diese Liste geprüft werden.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen (Buttons, Felder, Links) |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Fokussierten Button/Link auslösen, Formular abschicken |
| `F5` / `Strg+R` | Seite neu laden (Status wird frisch abgerufen) |
| `Alt+←` / `Alt+→` | Browser zurück/vor zwischen bereits besuchten Tabs/Seiten |
| `Strg+F` | Text auf der Seite suchen (Browser, nicht Unraid) |
| `Strg+P` | Seite ausdrucken (z. B. Array-Übersicht) |
| `F12` | Entwicklerwerkzeuge öffnen (nützlich für API-/Formularanalysen) |
| `Alt+F4` / Tab schließen | Seite schließen — Session bleibt serverseitig bis Timeout offen |

---

## Navigation zwischen Tabs

| Shortcut | Funktion |
|----------|----------|
| `Tab` + `Enter` | Tab-Link in der Kopfzeile anspringen und öffnen |
| Browser-Chronik (`Alt+←`) | Zum zuletzt besuchten Tab zurückkehren |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `1`–`9` für Tabs (Main, Shares, Docker …) | ❌ Nicht vorhanden |
| `g` dann `s` (zu Settings) | ❌ Nicht vorhanden |
| `/` für Suche | ❌ Nicht vorhanden — App-Store-Suche muss angeklickt werden |
| Schnellstart eines Containers per Buchstabe | ❌ Nicht vorhanden |

---

## Formulare und Dialoge

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder eines Dialogs durchlaufen |
| `Enter` | Standardaktion des Dialogs (meist „Apply“) auslösen |
| `Esc` | Manche Overlay-Dialoge schließen (nicht überall umgesetzt) |
| `Space` | Checkboxen/Schalter umschalten, Buttons auslösen |
| `↑` / `↓` | In Auswahllisten (Disk-Zuweisung, Vorlagenliste) blättern |
| `Backspace` / `Entf` | Feldinhalt löschen |

**Nicht vorhanden:**

| Gewünschter Shortcut | Status |
|----------------------|--------|
| `Strg+S` Speichern | ❌ Nicht vorhanden — Speichern heißt immer „Apply“ per Klick |
| `Strg+Z` Rückgängig | ❌ Nicht vorhanden — Änderungen wirken sofort |
| `Entf` Share/Container löschen | ❌ Nicht vorhanden — Button im Dialog nutzen |
| Autovervollständigung im Terminalfeld | ❌ Nicht vorhanden (Web-terminal-Plugin: Browser-Standard) |

---

## Docker- und VM-Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` + `Enter` | Aktionen in der Container-/VM-Tabelle erreichen (Start, Logs, …) |
| `Esc` | webVNC-/Console-Overlay verlassen, sofern UI-Fokus aktiv |
| `Strg+C` (im Web-terminal) | Prozess im eingebetteten Terminal abbrechen (Terminal-Standard) |

### webVNC-Konsole einer VM

In der Browser-VNC-Konsole gelten die Tasten der **Gast-VM**, nicht von Unraid:

| Kombination | Funktion |
|-------------|----------|
| Tasten direkt | An die Gast-VM durchgereicht |
| `Strg+Alt` | Kann Browser-Kurzkeys auslösen — im Zweifel VNC-Fokus anklicken |
| Sonderaktionen (Strg+Alt+Entf) | Über die webVNC-Werkzeugleiste senden, nicht per Tastatur (versionabhängig) |

**Nicht vorhanden:** Kein Unraid-Key, der die VM-Konsole wechselt, stoppt oder den Vollbildmodus umschaltet.

---

## App-Store und Suche

| Shortcut | Funktion |
|----------|----------|
| Klick ins Suchfeld + Text | Apps/Plugins im Apps-/Docker-Tab filtern |
| `Enter` | Suche ausführen |
| `Esc` | Suchtext teilweise löschen (feldabhängig) |

---

## Terminal/CLI auf dem Server

Auf der Konsole (Schirm am Server) oder per SSH gilt die normale Linux-Shell — keine Unraid-eigenen Keys. Praktische, reale Befehle:

| Befehl | Funktion |
|--------|----------|
| `unraid-api status` | Status der API-Komponente prüfen (aktuelle Versionen) |
| `unraid-api developer --sandbox true` | GraphQL-Sandbox aktivieren |
| `diagnostics` | Diagnosepaket für den Support erzeugen |

Das sind keine Shortcuts, sondern Konsolenbefehle — der Vollständigkeit halber aufgeführt.

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+K` | Adressleiste fokussieren (Browser) |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang/-ende (Browser) |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom der Oberfläche |
| `Esc` | Dialog schließen (sofern umgesetzt) |

**Nicht vorhanden:** `Cmd+S` (Speichern), `Cmd+/` (Suche), `Cmd+E` (Bearbeiten).

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Tabs, Tabellenaktionen und Dialogfelder erreichbar |
| `Enter` / `Space` | Buttons und Links auslösen |
| `Esc` | Overlays verlassen (nicht überall implementiert) |
| `↑` / `↓` / `←` / `→` | Auswahlfelder und Radio-Gruppen bedienen |
| `Shift+Tab` | Rückwärts navigieren |

---

## Zusammenfassung

Unraid bietet **keine anwendungsspezifischen Shortcuts**. Nutzbar sind:

- **Browser-Tasten** für Neuladen, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in Formularen und Dialogen
- **Linux-Shell-Befehle** (inkl. `unraid-api`) auf Konsole oder SSH

Wer Abkürzungen erwartet, erreicht sie über die Struktur: feste Tab-Reihenfolge, aussagekräftige Share- und Containernamen sowie API-Keys für Wiederkehraufgaben ersetzen jede Tastenkombination.
