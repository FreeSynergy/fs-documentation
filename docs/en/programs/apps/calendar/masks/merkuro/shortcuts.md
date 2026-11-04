# Merkuro – Keyboard shortcuts and workflows (Merkuro Calendar 26.08.2)

The app registers shortcuts centrally as **default shortcuts of its QAction collection** (`setDefaultShortcut` in `src/calendar/calendarapplication.cpp` and `src/components/abstractmerkuroapplication.cpp`) — the list below is therefore evidenced in the source code. Shortcuts can be adjusted through the KDE curtorrc (`KAuthorized` mechanism); the default state is as follows. Locations in [index.md](index.md#sources).

## Verified shortcuts

| Shortcut | Action | Evidence |
|----------|--------|----------|
| `Ctrl` + `1` | month view | `open_month_view` |
| `Ctrl` + `2` | week view **and** work-week view | both actions receive `Ctrl+2` in the code — **collision in the source code**; which menu/UI element wins is not verified |
| `Ctrl` + `3` | 3-day view | `open_threeday_view` |
| `Ctrl` + `4` | day view | `open_day_view` |
| `Ctrl` + `5` | schedule view | `open_schedule_view` |
| `Ctrl` + `6` | task view | `open_todo_view` |
| `F5` | refresh all calendars (*Refresh All*) | `QKeySequence::Refresh` |
| `Ctrl` + `M` | show/hide the menu bar (*Show Menubar*) | `toggle_menubar` |

## Explicitly NOT present (checked, 26.08.2)

- **No default shortcuts** for *New Event…*, *New Task…*, *Import Calendar…*, *Backwards/Forwards/To Today/To Date…* and *Undo/Redo* — the actions are registered but without `setDefaultShortcut` (usable in menus/the interface; a custom assignment is possible via the KDE settings).
- **No editor shortcuts in the app source** (no Ctrl+S/Ctrl+N found in the editor QMLs); standard QML field actions (text editing) excepted.
- Kirigami Addons basics (e.g. fullscreen, theme switcher) bring their own shortcuts — those live outside this repo and are **not verified** here.

## Workflows without shortcuts (direct CLI/URL)

Since the app offers no UI shortcut for everything, the alternative entry points are:

| Workflow | Command / path |
|----------|----------------|
| Import ICS | `merkuro-calendar /path/to/calendar.ics` (the argument is passed through to the running instance) or double-click on `.ics` (`MimeType=text/calendar`) |
| Open an event by UID | `qdbus org.kde.merkuro.calendar /Calendar org.kde.calendar.Calendar.showIncidenceByUid "<uid>" "" ""` (argument marshalling see [api.md](api.md)) |
| Manage accounts/resources | `SystemSettings`/Akonadi settings or `kcm_akonadi` — not in the app itself |
| Restart the Akonadi service | `akonadictl restart` (after installing `kdepim-runtime`) |
| Edit the configuration | KConfig file `kalendarrc` (groups in [structure.md](structure.md)) |

## Note on third-party shortcuts

Shortcuts from **KOrganizer**, Thunderbird or web calendars only apply there — Merkuro uses its own, considerably smaller set of shortcuts (see above).
