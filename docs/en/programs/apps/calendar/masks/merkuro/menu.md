# Merkuro – Menu and navigation structure (Merkuro Calendar 26.08.2)

All entries come from the QML/C++ source code of the 26.08.2 tarball (`src/calendar/calendarapplication.cpp`, `src/components/…`, `src/calendar/qml/…`); the original labels are quoted in English. Locations in [index.md](index.md#sources).

## Desktop: menu bar (can be switched off, `showMenubar`)

The menus come from `src/components/qml/` and are filled by the centrally registered `QAction`s of `mainCollection()`:

- **File**: *Quit Merkuro*
- **Edit**: *Undo Text*, *Redo Text*, *Cut*, *Copy*, *Paste*, *Delete*, *Select All* (standard text-field actions)
- **Window**: *Enter/Exit Full Screen*
- **Settings**: among others *Show Menubar* (switch), *Manage Tags…*
- **Help**: *Merkuro Handbook*
- Plus the actions registered by the application class (below), which appear in the menu bar/toolbar; standard menu building blocks (theme, quick overview …) come from Kirigami Addons.

## Central actions (`CalendarApplication::setupActions`)

### Views (mutually exclusive group, shortcuts in [shortcuts.md](shortcuts.md))

| Action | Default shortcut |
|--------|------------------|
| *Month View* | Ctrl+1 |
| *Week View* | Ctrl+2 |
| *Work Week View* | Ctrl+2 (as in the source — same shortcut as Week View, a collision in the code) |
| *3 Day View* | Ctrl+3 |
| *Day View* | Ctrl+4 |
| *Schedule View* | Ctrl+5 |
| *Tasks View* | Ctrl+6 |

### Navigation

- *Backwards*, *Forwards* (disabled in task-view mode), *To Today*, *To Date…*

### Creating / importing / editing

- *New Event…*, *New Task…* (registered without a default shortcut), *Import Calendar…*
- *Undo*, *Redo* (event/task changes)

### Fine control of the task view

- Sorting: *Alphabetically*, *By Due Date*, *By Priority Level*
- Order: *Ascending order*, *Descending Order*
- Filters: *Show Completed Tasks*, *Show Today Only*

### Miscellaneous

- *Refresh All* (F5), *Manage Tags…*, switch the application language (*switch_application_language*)

## Mobile (Plasma Mobile / touch)

- **BottomToolBar** (`src/calendar/qml/BottomToolBar.qml`): switcher **Month / 3-Day / Day / Schedule / Tasks** + the "New Event" action.
- Navigation via the **Kirigami page stack** (`pageStack.layers`): editors and settings are pushed as layers on top of each other; swipe gestures between month/week grids (swipeable modes).
- No classic menu bar; actions reach the UI through the global drawer and toolbar menus.

## Sidebar / global drawer (`MainDrawer.qml`)

- Section **calendars/collections** (visibility per calendar, colours) and section **tags** (`collectionsSectionExpanded`, `tagsSectionExpanded` in `kalendarrc`).
- Below that the entry point to **settings** with the pages:
  - **ViewSettingsPage** (view fine-tuning),
  - **Configure Availability / FreeBusySettingsPage** ("Publish your availability information automatically", minimum interval in minutes),
  - **SourceSettingsPage** (calendar sources),
  - **ConfigurationsView** (overall overview),
  - account management via `SystemAccountsForm`/Akonadi resources.
- Event info appears as a **drawer** (`IncidenceInfoDrawer`) or pop-up (`useIncidenceInfoPopup`), editing as a dialog (desktop) or a page (mobile).

## External entry point

- Over D-Bus an event can be opened directly with `showIncidenceByUid` (see [api.md](api.md)); the filesystem invocation `merkuro-calendar datei.ics` opens the import dialog instead of a menu.
