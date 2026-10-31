# Request Tracker - Tastatur-Shortcuts

## Übersicht

RT bietet **keine dokumentierten Tastatur-Shortcuts** in der Web-UI. Die effiziente „Kurzbefehl-Schicht“ ist die Query-Sprache und das CLI.

> Stand: RT 5.x.

## Web-UI

| Shortcut | Funktion |
|----------|----------|
| `Tab`/`Enter` | Formulare |
| `Strg+F` | Browser-Suche |
| `Alt+…` | Access-Keys einzelner Buttons (versionsabhängig, nicht garantiert) |

## Query-Sprache als „Power-Shortcuts“

| Muster | Beispiel |
|--------|----------|
| Queue + Status | `Queue = "netz" AND Status = "open"` |
| Owner | `Owner = "anna"` / `Owner = "Nobody"` |
| Zeit | `Updated > "2026-10-01"` |
| Wiedervorlage | `StartsBefore = "2026-11-01"` |

## CLI („echte“ Shortcuts)

```
rt show ticket/4711
rt ls "Queue=hw AND Status=new"
rt edit ticket/4711 set-status resolved
rt correspond ticket/4711 -m "Erledigt, Kabel getauscht."
```

## Ausdrücklich nicht vorhanden

- Palette, Vim-Maps, Ein-Tasten-Statuswechsel

## Mac

entfällt (Web/CLI plattformneutral).
