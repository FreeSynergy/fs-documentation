# Nextcloud Calendar – Keyboard shortcuts and direct workflows (v6.6.4)

The app registers **its own real keyboard shortcuts** through `useHotKey` (from `@nextcloud/vue`) — unlike many other tools, this list is genuinely implemented and not merely decorative. The app itself shows an overview list under **Calendar settings → ShortcutOverview** (`src/components/AppNavigation/Settings/ShortcutOverview.vue`). Locations in [index.md](../index.md#sources).

## Verified shortcuts (registration evidenced in the source)

### Navigation

| Key(s) | Function | Evidence |
|--------|----------|----------|
| `P` or `K` | previous period | `AppNavigationHeaderDatePicker.vue: useHotKey(['p','k'], …)` |
| `N` or `J` | next period | `AppNavigationHeaderDatePicker.vue: useHotKey(['n','j'], …)` |
| `T` | today | `AppNavigationHeaderTodayButton.vue: useHotKey('t', …)` |

### Views

| Key(s) | View | Evidence |
|--------|------|----------|
| `1` or `D` | day (`timeGridDay`) | `AppNavigationHeaderViewMenu.vue` |
| `2` or `W` | week (`timeGridWeek`) | ibid. |
| `3` or `M` | month (`dayGridMonth`) | ibid. |
| `4` or `Y` | year (`multiMonthYear`) | ibid. |
| `5` or `L` | list (`listMonth`) | ibid. |

### Actions

| Key | Function | Evidence |
|-----|----------|----------|
| `C` | create a new event | `AppNavigationHeaderNewEvent.vue: useHotKey('c', …)` |
| `H` | show the shortcut overview | **only listed in the overview list; in v6.6.4 no registration via `useHotKey` found in the source – function not verified** (the overview otherwise opens by clicking in the settings) |

### Event editor (only in the open editor; `src/mixins/EditorMixin.js`)

| Key | Function | Evidence |
|-----|----------|----------|
| `Escape` | close the editor | `useHotKey('Escape', …)` |
| `Ctrl` + `Enter` | save the event | `useHotKey('Enter', …, { ctrl: true, allowInInput: true })` |
| `Ctrl` + `Delete` | delete the event | `useHotKey('Delete', …, { ctrl: true })` |
| `Ctrl` + `D` | duplicate the event | `useHotKey('d', …, { ctrl: true })` |

Notes: outside the editor `useHotKey` ignores the shortcuts in text fields (editor shortcuts partly use `allowInInput`); on Mac ⌘ is used instead of Ctrl, since `ctrl: true` also covers the Cmd key — **not verified** in this detail, because the composable lives in `@nextcloud/vue` and not in the app repo.

## No command line of the app's own

There is **no OCC command and no CLI for this app** — the app only knows web routes and one automatic background job (`CleanUpOutdatedBookingsJob`). Server-wide DAV maintenance (e.g. birthday-calendar sync) belongs to the `dav` app of the Nextcloud server, not to Nextcloud Calendar.

## Direct-URL workflows (the app's "quick-start API")

All URLs relative to `{base}/index.php/apps/calendar/` (short form `{base}/apps/calendar/…`), valid after logging in in the browser:

| URL | Effect |
|-----|--------|
| `…/new` | open a new event |
| `…/new/{isAllDay}/{dtStart}/{dtEnd}` | open a pre-filled new event (e.g. `…/new/0/20261103T090000/20261103T100000`) |
| `…/edit/{objectId}` | edit an event; `objectId` = base64 of `/remote.php/dav/calendars/{user}/{kalender}/{objekt}.ics` |
| `…/object/{uid}` or `…/object/{uid}/{recurrenceId}` | permanent link by iCal UID alone (forwardable; `recurrenceId` = Unix timestamp or `next`) |
| `…/{view}/{timeRange}` | view + time window, `view` ∈ `timeGridDay`, `timeGridWeek`, `dayGridMonth`, `multiMonthYear`, `listMonth` |
| `…/p/{token}` | show a public calendar; `…/embed/{token}` without the Nextcloud interface (iframe-capable) |
| `…/appointments/{userId}` | the booking pages of a user |
| `{base}/calendar/proposal/{token}` | the poll page of a meeting proposal |

## Shortcuts of third-party clients (by way of distinction)

Thunderbird, Thunderbird Sonation, Merkuro, Apple Calendar, DAVx⁵ etc. have **their own client-side** shortcuts that have nothing to do with this app — they only work in the respective program, not in the Nextcloud web app. Anyone working over CalDAV (rather than the web UI) has no app shortcuts anyway; automation there runs through CalDAV requests (see [api.md](api.md)).
