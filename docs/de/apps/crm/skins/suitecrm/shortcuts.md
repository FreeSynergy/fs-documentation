# SuiteCRM - Tastatur-Shortcuts

## Übersicht

SuiteCRM veröffentlicht **keine offizielle Liste eigener Tastatur-Shortcuts**. Bedient wird über Maus, Touch und die üblichen Browser-Tasten; Formulare, Listen und Dialoge folgen den Standard-Tastaturen des Browsers. Diese Datei dokumentiert, was tatsächlich funktioniert, und markiert verbreitet erwartete Kurzzeichen ausdrücklich als **nicht vorhanden**.

> Stand: SuiteCRM 7.14.x (LTS) und SuiteCRM 8.x. Die Oberfläche ändert sich zwischen den Major-Versionen; nach Updates sollte diese Liste geprüft werden.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen (Menü, Feld, Button) |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Fokussierten Button auslösen, Formular absenden |
| `Space` | Checkbox oder Kästchen in der Liste umschalten |
| `Esc` | Offenes Popup oder Auswahlfenster schließen (versionsabhängig) |
| `F5` / `Strg+R` | Seite neu laden (Liste wird erneut abgerufen) |
| `Alt+←` / `Alt+→` | Browser zurück/vor (Backpfad durch Listen und Details) |
| `Strg+P` | Aktuelle Ansicht drucken |
| `Strg+F` | Text auf der Seite suchen (Browser, nicht SuiteCRM) |
| `Strg+A` | Text im fokussierten Feld markieren |

---

## Navigation

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Hauptmenüpunkte der Menüleiste erreichen |
| `Enter` | Menüpunkt öffnen (Modulliste) |
| `↑` / `↓` | In Auswahllisten und Dropdown-Feldern blättern |
| `Enter` | Ausgewählte Zeile öffnet die Detailansicht |
| `Tab` | Subpanel-Buttons (Eintrag hinzufügen, Bearbeiten) erreichen |
| `Esc` | Abbrechen-Schaltfläche entspricht der Browser-Abbruchlogik (versionsabhängig) |

**Nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `Strg+K` Befehlspalette / Modulsuche | ❌ Nicht vorhanden — Modul über Menü oder Admin-Suche erreichen |
| `/` für Suchfokus | ❌ Nicht vorhanden — Suchfeld muss angeklickt oder per `Tab` erreicht werden |
| `1`–`9` für Modulwechsel | ❌ Nicht vorhanden |
| `Alt+L` für Leads, `Alt+O` für Opportunities | ❌ Nicht vorhanden |
| `g` dann `l` (zu Leads springen) | ❌ Nicht vorhanden |
| Function-Keys (`F2` umbenennen, `F9` speichern) | ❌ Nicht vorhanden |

---

## Bearbeitung (Formulare, Listen)

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder des Formulars in Reihenfolge durchlaufen |
| `Enter` | Standardaktion des fokussierten Dialogs (meist Speichern) |
| `Esc` | Auswahlfenster (Person, Firma) ohne Übernahme schließen |
| `Backspace` / `Entf` | Feldinhalt löschen |
| `Strg+Z` | Rückgängig **innerhalb eines Textfeldes** (Browser-Funktion) |
| `Space` | Auswahlkästchen in der Liste setzen (für Mass Actions) |
| `↑` / `↓` | Mehrzeilige Felder und Auswahllisten bedienen |

**Nicht vorhanden:**

| Erwarteter Shortcut | Status |
|---------------------|--------|
| `Strg+S` Datensatz speichern | ❌ Nicht dokumentiert — Speichern-Schaltfläche nutzen |
| `Strg+Enter` Speichern im Formular | ❌ Nicht dokumentiert — gilt nur für wenige Textfelder des Browsers |
| `Strg+Z` Änderungen am Datensatz rückgängig | ❌ Nicht vorhanden — gespeicherte Änderungen nur über den Feldverlauf nachvollziehbar |
| `Entf` Datensatz in der Liste löschen | ❌ Nicht vorhanden — Auswahlkästchen plus Mass Action "Löschen" |
| Pfeiltasten zum Verschieben von Dashlets | ❌ Nicht vorhanden — Drag & Drop auf dem Dashboard |
| Inline-Bearbeitung per Doppelklick in jeder Spalte | ❌ Nicht überall vorhanden — nur in dafür eingerichteten Feldern (versionsabhängig) |

---

## Suche und Filter

| Shortcut | Funktion |
|----------|----------|
| Klick in das Schnellsuchfeld oben + Text | Volltextsuche über Module hinweg |
| `Enter` | Suche absenden, Trefferliste öffnen |
| `Esc` | Autocomplete-Vorschläge schließen |
| `Backspace` | Suchtext löschen, wenn das Feld fokussiert ist |
| `Tab` | Filterpanel-Felder ansteuern, Filter anwenden-Button erreichen |

Kurzbefehle im Suchfeld (etwa Operatoren-Shortcuts) sind **nicht** dokumentiert; die Suche arbeitet mit Texteingabe und Filterfeldern.

---

## Dialoge und Assistenten

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Felder im Dialog durchlaufen (Import, Konvertieren, Module Loader) |
| `Enter` | Nächster Schritt im Assistenten, sofern das Eingabefeld fokussiert ist |
| `Esc` | Abbrechen, sofern der Dialog das unterstützt |
| `Space` | Optionsfelder und Kontrollkästchen umschalten |
| `↑` / `↓` | Auswahllisten (Sprache, Team, Modul) bedienen |

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Strg`.

| Shortcut | Funktion |
|----------|----------|
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+Z` | Rückgängig im Textfeld |
| `Cmd+A` | Alles markieren |
| `Cmd+↑` / `Cmd+↓` | Seitenanfang / Seitenende (Browser) |
| `Cmd+Plus` / `Cmd+Minus` | Zoom der Oberfläche |
| `Cmd+0` | Zoom zurücksetzen |
| `Cmd+W` | Tab schließen |

**Nicht vorhanden:** `Cmd+K` (Befehlspalette), `Cmd+S` (Speichern), `Cmd+E` (Bearbeiten), `Cmd+/` (Suchfokus).

---

## Barrierefreie Tastaturbedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Kopfzeile, Filterpanel, Tabellenzeilen und Buttons in Lesereihenfolge |
| `Enter` / `Space` | Aktion des fokussierten Elements auslösen |
| `Esc` | Overlay schließen und zum Inhalt zurückkehren |
| `↑` / `↓` | Auswahlfelder und Vorschlagslisten bedienen |
| `Shift+Tab` | Rückwärts navigieren |

---

## Betriebskommandos (CLI, keine Shortcuts)

Wartung und Update laufen über Kommandozeilen-Aufrufe auf dem Server. Diese Kommandos sind **keine** Tastatur-Shortcuts, sondern Betriebsschritte; die genauen Namen sind versionsabhängig und in der offiziellen Dokumentation nachzulesen.

| Kommando | Funktion |
|----------|----------|
| `php -f cron.php` | Scheduler ausführen (Workflows, Kampagnen, Bereinigung); typisch per Cron-Job |
| Admin ▸ "Reparieren" / "Cache leeren" | Metadaten-Cache neu aufbauen (Oberfläche, kein CLI-Kommando) |
| `php -f bin/suitecrm-cli/suitecrm cache:clear` | Cache-Wartung über das CLI-Werkzeug (ab 7.11, Namen versionsabhängig) |
| `php -f bin/suitecrm-cli/suitecrm db:repair` | Reparatur-Aktionen der Datenbank (Namen versionsabhängig) |
| `composer install` / `bin/console` (SuiteCRM 8) | Abhängigkeiten und Symfony-Kommandos der 8er-Shell |

Wer kurze Wege sucht, arbeitet mit gespeicherten Filtern, Favoriten auf dem Dashboard und einem persönlichen Theme; SuiteCRM selbst bietet dafür keine Tastenkombinationen.

---

## Zusammenfassung

SuiteCRM bringt **keine anwendungsspezifischen Shortcuts** mit. Nutzbar sind:

- **Browser-Tasten** für Neu laden, Drucken, Zoom und Textsuche
- **`Tab`, `Enter`, `Space`, `Esc`, `↑`/`↓`** in Formularen, Listen, Filtern und Dialogen
- **Drag & Drop** ausschließlich für Dashlets auf der Startseite
- **CLI- und Admin-Wartung** für Cache, Datenbankreparatur und Scheduler
