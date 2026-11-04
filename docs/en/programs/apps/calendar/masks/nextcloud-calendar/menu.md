# Nextcloud Calendar – Menu and navigation structure (v6.6.4)

All entries are taken from the source code of tag v6.6.4 (components under `src/views/Calendar.vue`, `src/components/AppNavigation/…`, `src/views/EditFull.vue`; the original English labels are quoted). Locations in [index.md](index.md#sources).

## Overall layout of the web app

```
Nextcloud header (server: app list, avatar, search)
└── Calendar app (NcContent)
    ├── left sidebar (NcAppNavigation)
    │   ├── head: event filter, date picker, new event, today, view menu
    │   ├── list: calendars, subscriptions, proposals, bookings, trash
    │   └── footer: calendar settings
    ├── main area: calendar grid (FullCalendar) + "Unscheduled tasks" switch
    └── editor layer: quick editor / detail editor / modals
```

## Sidebar – header (`AppNavigationHeader.vue`)

- Search field **"Filter events …"** (filters events in the current view)
- **Date picker** (`AppNavigationHeaderDatePicker`)
- **"New event"** (`AppNavigationHeaderNewEvent`, logged-in users only)
- **"Today"** (today button)
- **View menu** (`AppNavigationHeaderViewMenu`): **Day / Week / Month / Year / List** — exactly the five FullCalendar views of the routes (`timeGridDay`, `timeGridWeek`, `dayGridMonth`, `multiMonthYear`, `listMonth`)

## Sidebar – list (`CalendarList.vue`)

- Section **"My calendars"** with the "Add new" menu (`CalendarListNew.vue`):
  - **New calendar**
  - **New calendar with task list**
  - **New subscription from link (read-only)** (WebCal subscription from an `http(s)://`, `webcal(s)://` link)
  - **Add public holiday calendar**
  - **Add custom public calendar**
- **Calendar entries** (`CalendarListItem.vue`, context menu per calendar):
  - **Disable/Enable calendar** (show/hide)
  - Labels **"Shared with you by …"** / **"Delegated to you by …"**
  - **Copy public link**
  - **Edit and share calendar** or **Edit calendar** (`EditCalendarModal`: details, sharing with users/groups/Circles, **PublishCalendar** for the public share, internal link, delete)
- Section **public calendars** (`PublicCalendarListItem.vue`)
- **Meeting proposals**: `ProposalEditor` + `ProposalList` (logged in only)
- **Appointment bookings**: `AppointmentConfigList.vue` (entry point "New appointment config", manage booking links)
- **Trash** (`Trashbin.vue`, appears when objects/calendars have been deleted)

## Sidebar – footer (`Settings.vue`)

Entry point **"Calendar settings"**, below it the groups:

- **General**: default calendar for incoming invitations, **Availability settings** (your own availability), a **CalDAV** block with copyable URLs: **CalDAV URL** and **Server Address for iOS and macOS**
- **Appearance**: **Birthday calendar**, **Tasks in calendar**, **Weekends**, **Week numbers**, **Limit number of events shown in Month view**, **Density in Day and Week View**
- **Editing**: **Default reminder for part-day events**, **Default reminder for full-day events**, **Simple event editor** (option: "More details" opens the detail editor)
- **Files**: attachment folder for event attachments (`SettingsAttachmentsFolder.vue`)
- **Delegation**: manage delegators/delegations with read/write rights (`SettingsDelegationSection.vue`)
- **ICS import** (`SettingsImportSection.vue`, import screen with per-file progress)
- **Keyboard shortcut overview** (`ShortcutOverview.vue`)

## Main area

- **Calendar grid** (`CalendarGrid.vue`): FullCalendar with next/previous and time jump (the date picker sits in the sidebar header), events can be moved/resized by drag & drop.
- The **"Show unscheduled tasks"** switch (NcActions button) opens the right sidebar **"Unscheduled tasks"** (`UnscheduledTasksList.vue`).
- Empty view `EmptyCalendar.vue` when no calendar exists.

## Event editor

**Quick editor** (`EditSimple.vue`): title, start/end/duration, calendar, all-day, the "More details" transition.

**Detail editor** (`EditFull.vue`, title **"Detailed event editor"**):

- Actions menu top right: **Copy link**, **Export** (ICS download, can be blocked server-side via `hideEventExport`), **Duplicate**, **Delete** — for series also **Delete this occurrence** / **Delete this and future occurrences** / **Delete entire series**
- Head: title, calendar picker with colour, all-day switch
- Sections (component folder `src/components/Editor/`):
  - **Properties** (time/time zone, location, resources/rooms, description, category flags)
  - **Repeat** (recurrence editor)
  - **Alarm** (reminders, several, time units)
  - **Invitees** (manage attendees; section heading **"Managing shared access"**; free/busy display, slot suggestions)
  - **Attachments** (attachments from Files)
  - **Add Talk conversation** (create/link a conference room)
  - Invitation acceptance buttons (**InvitationResponseButtons**: accept/tentative/decline)
- Save buttons (`SaveButtons.vue`), discard confirmation (**Discard changes?**)

## Public/embedded views (their own navigation)

- `/p/{token}`: Nextcloud header with the calendar name + view menu (no sidebar editing).
- `/embed/{token}`: `EmbedTopNavigation.vue`/`EmbedHeader.vue` – a slim bar with title, view switcher, an "Open in Nextcloud" entry point.
- **Booking page** (`/appointments/{userId}`, `/appointment/{token}`): slot list + form, no calendar navigation.
- **Poll page** (`/calendar/proposal/{token}`): the proposal with candidate appointments and a voting UI, its own minimal navigation (`ProposalPublic.vue`).

## Server-side entry points outside the app

- Nextcloud **dashboard**: widget "upcoming events" (`CalendarWidget.php`).
- **Contacts menu/avatar**: availability display (`ContactsMenuAvailability.vue`).
- **Profile page**: link "book appointments" (profile link action `AppointmentsAction.php`).
