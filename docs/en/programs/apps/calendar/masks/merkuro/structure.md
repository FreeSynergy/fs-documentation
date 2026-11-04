# Merkuro – Structure (Merkuro Calendar 26.08.2)

Locations for all statements in [index.md](index.md#sources) (source tarball 26.08.2).

## Request/program flow

1. **Start:** `merkuro-calendar` initialises Qt/KF (`KAboutData` "merkuro.calendar", icon `org.kde.merkuro.calendar`), registers itself as a single instance on the session D-Bus (`KDBusService::Unique`) and loads the QML module `org.kde.merkuro.calendar` (`Main.qml`).
2. **Data access:** the app connects to **Akonadi** (`Akonadi::ETMCalendar`). `CalendarManager` (a QML singleton) exposes collections (`collections`, `todoCollections`, `viewCollections`, `allCalendars` as an `Akonadi::CollectionFilterProxyModel`), an `Akonadi::IncidenceChanger` (the central place for all write operations incl. undo/redo) and factory methods for `IncidenceWrapper`.
3. **Models → views:** C++ Qt models (`monthmodel`, `multidayincidencemodel`, `hourlyincidencemodel`, `incidenceoccurrencemodel`, `holidaymodel`, `attendeesmodel`, `attachmentsmodel`, `itemtagsmodel`, `todosortfilterproxymodel`, `infinitemerkurocalendarviewmodel` …) feed the QML views (`MonthView`, `WeekView`, `DayView`, `ScheduleView`, `TodoView` with swipeable/basic variants).
4. **Writing:** the editor (`IncidenceWrapper` → `IncidenceEditorDialog`/`IncidenceEditorPage`) hands over to `IncidenceChanger`; Akonadi persists and synchronises (for online calendars via the relevant kdepim-runtime resource, e.g. CalDAV).
5. **Import:** `.ics` arguments/desktop invocations run through `Importer` into Akonadi.
6. **Reminders:** `RemindersModel` maintains VALARMs; triggering is handled by the KDE PIM infrastructure (Akonadi/notifications), not by the app at runtime.

## Directory structure (repo `pim/merkuro`)

```
CMakeLists.txt            Release Service version (26.08.2), Qt ≥6.9, KF ≥6.25, PIM libs 6.8.2
src/
├── org.kde.merkuro.desktop.in / org.kde.merkuro.metainfo.xml   suite entry point
├── launcher/             merkurolauncher (app chooser of the suite)
├── components/           shared suite building blocks
│   ├── abstractmerkuroapplication.{h,cpp}  base application class (actions, menu)
│   ├── accountsmodel, collectionutils, sortedcollectionproxymodel
│   └── qml/              BaseApplication, menus (File/Edit/Help/Settings/Window + Native-*),
│                         SystemAccountsForm, delegates, bars, controls, location …
├── calendar/             ← the core of this documentation (binary merkuro-calendar)
│   ├── main.cpp          CLI, D-Bus single instance, importer wiring
│   ├── calendarapplication.{h,cpp}  actions/shortcuts, D-Bus object /Calendar
│   ├── calendarmanager.{h,cpp}      Akonadi access, collections, IncidenceChanger
│   ├── datetimestate, filter, incidencewrapper, mousetracker, remindersmodel, utils
│   ├── models/           Month/MultiDay/Hourly/Occurrence/Holiday/Attendees/
│   │                     Attachments/Tags/TodoSortFilter/TimezoneList …
│   ├── calendarconfig.kcfg(c)       → kalendarrc
│   ├── importer.{h,cpp}             ICS import
│   ├── org.kde.calendar.Calendar.xml  D-Bus interface
│   ├── org.kde.merkuro.calendar.desktop / .metainfo.xml
│   └── qml/              Main.qml, BottomToolBar, drawers (MainDrawer, IncidenceInfoDrawer),
│                         MainViews/ (MonthView, WeekView, DayView, ScheduleView, TodoView,
│                         Swipeable*/Basic* grids), Dialogs/ (IncidenceEditorDialog/Page),
│                         incidenceeditor/, Settings/ (ViewSettings, FreeBusy, Source, Configurations),
│                         IncidenceEditorManager.qml (singleton)
├── contacts/             merkuro-contact (sister app)
└── mail/                 merkuro-mail (sister app, still work in progress)
po/                       translations
```

QML module URI: `org.kde.merkuro.calendar` (`qt_add_qml_module`).

## Configuration

- **`kalendarrc`** (KConfig, schema `calendarconfig.kcfg`): groups `General` (`showMenubar`, `forceCollapsedMainDrawer`, `enableMaps`, `enableMailIntegration`, `locationMarker`, `lastOpenedView`), `MainDrawer`, `Editor` (last used event/todo collection), `GeneralView` (holidays/regions, tasks on/off, pop-up vs. drawer), `MonthView`/`WeekView`/`ScheduleView` (grid modes, week numbers, headers), `TaskView` (sorting, direction, completed subtasks, dimming).
- **Accounts/folders:** live with Akonadi (`~/.config/akonadi/`, database under `~/.local/share/akonadi/`); resources are created via the KDE settings or `SystemAccountsForm`.
- Quick adjustment through the KDE shortcut settings (actions such as `open_month_view` are KAuthorized-based and overridable, stored among others in `actionentry.rc`).

## Data model

- **The master data store is Akonadi**, not the app: collections = calendars/task lists; items = incidences (VEVENT, VTODO, VJOURNAL) as KCalCore objects; tags/categories, attachments (Akonadi relations), attendees (CTA), reminders (VALARM).
- App-internal models: `IncidenceWrapper` (editor state incl. RRULE fields: Daily/Weekly/Monthly/Yearly/Custom, exceptions), `DateTimeState` (date navigation), occurrence/sorting proxy models.
- **No database/no cache of its own in the app**; every read/write path leads through Akonadi.

## Deployment

- **Distribution packages:** in most distributions the app was still called `kalendar` up to 23.08, since then `merkuro` (package `merkuro`, binaries `merkuro-*`); Flatpak/NEON via the KDE repositories.
- **Building it yourself:** CMake ≥ 3.29, Ninja recommended; current KDE PIM libraries are mandatory — the README expressly recommends **kdesrc-build**; before the first start install `kdepim-runtime` and run `akonadictl restart`, otherwise online resources are missing.
- **Runtime:** a KDE desktop environment is not required, but the Akonadi service must run; Qt 6.9+, KF 6.25+; the mobile variant is identical code (Kirigami adapts the UI).
- **Relationships:** the sister projects `pim/akonadi`, `pim/kdepim-runtime` (resources) and the `pim/merkuro` suite are coupled to one another; bug reports go through bugs.kde.org (product "merkuro").
