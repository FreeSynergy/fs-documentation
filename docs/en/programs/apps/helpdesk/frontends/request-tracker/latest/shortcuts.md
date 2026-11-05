# Request Tracker - Keyboard shortcuts

## Overview

RT offers **no documented keyboard shortcuts** in the web UI. The efficient "shortkey layer" is the query language and the CLI.

> State: RT 5.x.

## Web UI

| Shortcut | Function |
|----------|----------|
| `Tab`/`Enter` | Forms |
| `Ctrl+F` | Browser search |
| `Alt+…` | Access keys of individual buttons (version-dependent, not guaranteed) |

## Query language as "power shortcuts"

| Pattern | Example |
|---------|---------|
| Queue + status | `Queue = "netz" AND Status = "open"` |
| Owner | `Owner = "anna"` / `Owner = "Nobody"` |
| Time | `Updated > "2026-10-01"` |
| Follow-up date | `StartsBefore = "2026-11-01"` |

## CLI ("real" shortcuts)

```
rt show ticket/4711
rt ls "Queue=hw AND Status=new"
rt edit ticket/4711 set-status resolved
rt correspond ticket/4711 -m "Erledigt, Kabel getauscht."
```

## Explicitly not present

- Palette, vim maps, single-key status change

## Mac

Not applicable (web/CLI are platform-neutral).
