# Merkuro – Features (verified against Merkuro 26.08.2)

Currently documented version: **Merkuro Calendar 26.08.2** (Kalendar has been called "Merkuro" since KDE Gear 23.08). Every item comes from the source code of the release tarball; locations in [index.md](../index.md#sources).

## Views

- Seven operating modes according to the `CalendarApplication::Mode` enum: **month, week, 3 days, day, schedule, tasks, work week**; switched via menu/shortcuts, forward/back/today.
- **Swipeable month/week/schedule grids** (swipeable and basic variants can be switched in `kalendarrc`), week numbers, alignable/named weekday headers.
- **Schedule view** as a list of upcoming events (week headers, empty days can be hidden).
- **Task view** as a tree (subtasks), sorting by due date/alphabet/priority, ascending/descending, show or hide completed items.
- Event info optionally as a **pop-up or drawer** (`useIncidenceInfoPopup`).
- Dismissable sidebar with calendar/tag sections (`MainDrawer`), on mobile a bottom toolbar.

## Events, tasks, journals

- **Event editor** (a dialog on desktop, a page on mobile): title, description, start/end, **all-day**, **time zone per event**, calendar/collection selection.
- **Recurrences**: never/daily/weekly/monthly/yearly/**custom** (RRULE), "Every" interval, "On" rule, end (never/date/after n occurrences), **exceptions (EXDATE)**.
- **Attendees** from contacts or entered manually (name/e-mail), status, **request RSVP**.
- **Reminders** (reminders with a time unit), **priority 1–9**, **progress %** (tasks), **tags/categories**, **attachments**.
- Also **journal entries (VJOURNAL)** and **subtasks** in the editor.
- **Undo/redo** for changes (signals of the application class).
- **ICS import**: files/URLs as arguments, double-click on `.ics` (`MimeType=text/calendar`), import confirmation.

## Calendars and sources

- Data storage through **Akonadi**: local calendars + online calendars (**Nextcloud, Google Calendar, Outlook, CalDAV and many more**) through resources from `kdepim-runtime`; account maintenance partly via `SystemAccountsForm`/Akonadi settings.
- **Public holidays by region** (KF6::Holidays; `showHolidaysInCalendarViews`, `holidayRegions`), a holiday line in the week view.
- Tasks (VTodos) can be shown in all calendar views, including subtasks.
- **Availability publication (Free/Busy)**: configurable automatic publication with an adjustable minimum interval (minutes) (`FreeBusySettingsPage`) — the basis so that others see occupancy when invited.
- **Location maps** optional (QtLocation; `enableMaps`, marker type circle/pin) for event locations.
- **Mail integration** as an optional bridge to the mail component of the suite (`enableMailIntegration`).

## Configuration and integration

- KConfig file **`kalendarrc`** with fine view options (grid modes, headers, week numbers, margin widths, dimming of past events, last opened view …).
- **D-Bus**: `showIncidenceByUid` for opening a specific event (details in [api.md](api.md)); single-instance.
- Convergent UI: identical app on desktop and **Plasma Mobile** (Kirigami, `Kirigami.Settings.isMobile` switches).
- Complete translations (AppData for dozens of languages).

## What Merkuro does NOT offer

- **No server, no web interface** — a pure desktop/mobile app; public sharing, embedding or booking for outsiders only exists via the respective calendar server (e.g. Nextcloud Calendar).
- **No webhooks/REST API** and no SDK for third parties; automation only via D-Bus, CLI arguments and the Akonadi libraries.
- **No appointment booking pages / no scheduling polls** (Doodle-style suggestions do not exist; nor is there a slot finder for shared availability — a "find a common free time" feature was not found in 26.08.2).
- **No push notifications of its own beyond local reminders** — reminders run over Akonadi/KDE notifications; browser-based alarms as with a web calendar are not applicable.
- **No calendar server synchronisation to third-party servers beyond CalDAV** (no Exchange-MAPI/Google-API special features such as calendar delegation or resource booking; those hang on the kdepim-runtime resources, not on Merkuro).
- **No team features** (comments on events, graduated sharing and the like are not in the app; whatever the server offers, Merkuro only shows as far as Akonadi represents it — **not verified**, no corresponding UI elements found in 26.08.2).
