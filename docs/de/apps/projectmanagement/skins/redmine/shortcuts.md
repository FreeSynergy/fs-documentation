# Redmine - Tastatur-Shortcuts

## Übersicht

Redmine bringt nur **ein einziges eigenes Kurzzeichen** mit: `/` setzt den Fokus in das Suchfeld der Kopfzeile (seit mehreren Major-Versionen enthalten; ältere Installationen ohne dieses Verhalten: versionsabhängig). Daneben gelten die Browser-Tastatur und die Standard-Navigation in Formularen. Verbreitet angenommene Kurzbefehle (`c`, `j/k`, `Ctrl+Enter`) existieren im Kern **nicht**; einige Plugins ergänzen Shortcuts.

> Stand: Redmine 5.x/6.x-Linie. Nach Updates oder Plugin-Installationen Liste prüfen.

---

## Allgemein (Browser-Standard)

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Zum nächsten Bedienelement springen |
| `Shift+Tab` | Zum vorherigen Bedienelement springen |
| `Enter` | Schalter, Link oder Formularstandardaktion auslösen |
| `Space` | Checkboxen/Häkchen umschalten (Filter, Modulauswahl) |
| `F5` / `Ctrl+R` | Seite neu laden |
| `Alt+←` / `Alt+→` | Browser zurück/vor (Reiternavigation folgt URLs) |
| `Ctrl+P` | Drucken (Redmine liefert eigenes Druck-Stylesheet) |
| `Ctrl+F` | Text auf der Seite suchen (Browser) |
| `Strg+Klick` | Issue-Link in neuem Tab öffnen |

---

## Redmine-eigene Shortcuts

| Shortcut | Funktion |
|----------|----------|
| `/` | Fokus in das Suchfeld der Kopfzeile legen (Tippen startet Suche) |
| `Esc` | Geöffnete Autocomplete-/Vorschlags-Popups schließen (Formular-Standard) |

**Nicht vorhanden:**

| Gewünschtes Shortcut | Status |
|----------------------|--------|
| `c` Neues Issue anlegen | ❌ Nicht im Kern - „Neues Issue"-Button benutzen |
| `j` / `k` Nächste/vorherige Position | ❌ Nicht im Kern |
| `Ctrl+Enter` Notiz/Speichern absenden | ❌ Nicht im Kern - Speichern-Button oder `Enter` im Feld |
| `Ctrl+S` Speichern | ❌ Nicht abgefangen - Browser speichert die Seite |
| `g` + Buchstabe (Sprung zu Modulen) | ❌ Nicht vorhanden |
| `?` Shortcut-Übersicht | ❌ Nicht vorhanden |
| `Alt` + Ziffer für Reiter | ❌ Nicht im Kern (nur Browser-/OS-Landeskürzel) |

---

## Navigation

| Shortcut | Funktion |
|----------|----------|
| `Tab` | Kopfzeile, Reiter, Breadcrumb und Tabelle ansteuern |
| `Enter` | Issue-Link öffnen, Reiter auslösen |
| `↑` / `↓` | In Auswahlfeldern (Tracker, Status, Zugewiesene) blättern |
| `Esc` | Autocomplete-Vorschläge schließen |
| `Backspace` | Suchfeldtext löschen, wenn fokussiert |

Tipp: Die Breadcrumb- und Reiterleisten sind normale Links - `Tab` + `Enter` ersetzt jeden Navigations-Hotkey.

---

## Bearbeitung

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Formularfelder durchlaufen (Status, Priorität, Notiz) |
| `Enter` | Standard-Speichern-Aktion im fokussierten Formular |
| `Ctrl+A` / `Ctrl+C` / `Ctrl+V` / `Ctrl+X` | Alles markieren, kopieren, einfügen, ausschneiden |
| `Ctrl+Z` | Rückgängig **innerhalb** eines Textfeldes; gespeicherte Änderungen lassen sich nicht per Undo zurücknehmen |
| `Shift+Klick` | Text in Wiki-/Kommentarfeldern in Blöcken markieren (Browser) |

### Wiki- und Kommentarfelder (Textile/Markdown)

Redmine formatiert per Syntax, nicht per Hotkey:

| Eingabe | Funktion |
|---------|----------|
| `**text**` | Fett |
| `*text*` | Kursiv |
| `h2.` / `##` | Überschrift (Textile / Markdown) |
| `[[WikiPage]]` | Interner Wiki-Link |
| `#1234` | Issue-Referenz (verlinkt automatisch) |
| `{{...}}` | Inline-Code (Textile) |

**Nicht vorhanden:** `Ctrl+B`/`Ctrl+I` im Wiki-Editor (es sei denn, ein Plugin stellt sie bereit).

---

## Suche

| Shortcut | Funktion |
|----------|----------|
| `/` | Suchfeld fokussieren (Redmine-eigenes Kurzzeichen) |
| `Enter` | Suche ausführen |
| `Ctrl+F` | Seitentext durchsuchen (Browser) |

---

## Mac-Varianten

Unter macOS gelten die Browser-Tasten mit `Cmd` statt `Ctrl`.

| Shortcut | Funktion |
|----------|----------|
| `/` | Suchfeld fokussieren (wie unter Windows/Linux) |
| `Cmd+R` | Neu laden |
| `Cmd+P` | Drucken (Druck-Stylesheet) |
| `Cmd+F` | Text auf der Seite suchen (Browser) |
| `Cmd+A` / `Cmd+C` / `Cmd+V` | Alles markieren, kopieren, einfügen |
| `Cmd+Z` | Rückgängig im aktiven Textfeld |
| `Cmd+Klick` | Link in neuem Tab öffnen |
| `Cmd+Plus` / `Cmd+Minus` / `Cmd+0` | Zoom der Oberfläche |

**Nicht vorhanden:** `Cmd+E` (Bearbeiten), `Cmd+S` (Speichern), `Cmd+K` (Palette).

---

## Wartung auf der Kommandozeile (kein UI, aber real)

Redmine-Administration nutzt `rake`/`bundle` im Installationsverzeichnis; das ersetzt keine Shortcuts, gehört aber zum schnellen Arbeiten:

| Kommando | Funktion |
|----------|----------|
| `bundle exec rake db:migrate` | Datenbank-Migrationen ausführen |
| `bundle exec rake redmine:load_default_data` | Standarddaten (Tracker, Status) laden |
| `bundle exec rake generate_secret_token` | Session-Secret erzeugen |
| `bundle exec rails server -e production` | Entwicklungsserver starten (Produktion: Puma/Passenger) |

---

## Barrierefreie Bedienung

| Shortcut | Funktion |
|----------|----------|
| `Tab` / `Shift+Tab` | Komplette Navigation ohne Maus |
| `Enter` / `Space` | Links und Schalter auslösen |
| `Esc` | Popups und Vorschläge verlassen |
| `↑` / `↓` | Auswahlfelder bedienen |
| `Ctrl+Plus` | UI vergrößern ohne Funktionsverlust |

---

## Zusammenfassung

Redmine bietet exakt **ein eigenes Kurzzeichen**: `/` für die Suche. Alles Weitere läuft über:

- **Browser-Tasten** (Neu laden, Drucken, Zoom, Textsuche)
- **`Tab`/`Enter`/`Esc`/Pfeiltasten** in Formularen und Auswahlfeldern
- **Syntax-Kürzel** (Textile/Markdown, `#1234`-Issue-Referenzen) statt Formatierungs-Hotkeys

Plugin-Erweiterungen können zusätzliche Shortcuts liefern - dann ersetzt die Plugin-Doku diese Liste nicht, sie ergänzt sie nur.
