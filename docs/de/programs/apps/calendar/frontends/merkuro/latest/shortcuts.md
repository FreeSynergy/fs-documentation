# Merkuro – Tastenkürzel und Workflows (Merkuro Calendar 26.08.2)

Die App registriert Kürzel zentral als **Default-Shortcuts ihrer QAction-Sammlung** (`setDefaultShortcut` in `src/calendar/calendarapplication.cpp` und `src/components/abstractmerkuroapplication.cpp`) – die Liste unten ist damit im Quelltext belegt. Kürzel sind über die KDE-Curtorrc anpassbar (`KAuthorized`-Mechanismus), Standardzustand ist wie folgt. Fundstellen in [index.md](../index.md#quellen).

## Verifizierte Kürzel

| Kürzel | Aktion | Beleg |
|--------|--------|-------|
| `Strg` + `1` | Monatsansicht | `open_month_view` |
| `Strg` + `2` | Wochenansicht **und** Arbeitswochenansicht | beide Aktionen erhalten im Code `Ctrl+2` – **Kollision im Quelltext**, welches Menü-/UI-Element gewinnt, ist nicht verifiziert |
| `Strg` + `3` | 3-Tage-Ansicht | `open_threeday_view` |
| `Strg` + `4` | Tagesansicht | `open_day_view` |
| `Strg` + `5` | Terminplan-Ansicht | `open_schedule_view` |
| `Strg` + `6` | Aufgabenansicht | `open_todo_view` |
| `F5` | Alle Kalender aktualisieren (*Refresh All*) | `QKeySequence::Refresh` |
| `Strg` + `M` | Menüleiste ein-/ausblenden (*Show Menubar*) | `toggle_menubar` |

## Ausdrücklich NICHT vorhanden (geprüft, 26.08.2)

- **Keine Default-Kürzel** für *New Event…*, *New Task…*, *Import Calendar…*, *Backwards/Forwards/To Today/To Date…* und *Undo/Redo* – die Aktionen sind registriert, aber ohne `setDefaultShortcut` (in Menüs/Oberfläche nutzbar; eigene Zuordnung über KDE-Einstellungen möglich).
- **Keine Editor-Kürzel im App-Quelltext** (kein Ctrl+S/Ctrl+N in den Editor-QMLs gefunden); Standard-QML-Feldaktionen (Textbearbeitung) ausgenommen.
- Kirigami-Addons-Grundlagen (z. B. Vollbild-, Theme-Umschalter) bringen eigene Kürzel mit – die liegen außerhalb dieses Repos und sind hier **nicht verifiziert**.

## Workflows ohne Kürzel (Direct-CLI/URL)

Da die App keine UI-Kürzel für alles bietet, sind die alternativen Einstiege:

| Workflow | Kommando / Weg |
|----------|----------------|
| ICS importieren | `merkuro-calendar /pfad/zum/kalender.ics` (Argument wird an laufende Instanz durchgereicht) oder Doppelklick auf `.ics` (`MimeType=text/calendar`) |
| Termin per UID öffnen | `qdbus org.kde.merkuro.calendar /Calendar org.kde.calendar.Calendar.showIncidenceByUid "<uid>" "" ""` (Argument-Marshalling siehe [api.md](api.md)) |
| Konten/Ressourcen verwalten | `SystemSettings`/Akonadi-Einstellungen bzw. `kcm_akonadi` – nicht in der App selbst |
| Akonadi-Dienst neu starten | `akonadictl restart` (nach Installation von `kdepim-runtime`) |
| Konfiguration editieren | KConfig-Datei `kalendarrc` (Gruppen in [structure.md](layout.md)) |

## Hinweis zu fremden Kürzeln

Kürzel von **KOrganizer**, Thunderbird oder Webkalendern gelten nur dort – Merkuro nutzt eine eigene, deutlich kleinere Kürzelmenge (siehe oben).
