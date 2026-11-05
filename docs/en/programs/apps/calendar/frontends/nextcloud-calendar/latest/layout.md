# Nextcloud Calendar – Structure (v6.6.4)

Locations for all statements in [index.md](../index.md#sources) (source tag v6.6.4).

## Request/program flow

1. **Invocation:** the browser loads `{base}/apps/calendar/…` → the PHP route `calendar.view.index` (`ViewController`) renders `templates/main.php` and hands **initial state** to the frontend (`CalendarInitialStateService`: `app_version`, `initial_view`, `show_weekends`, `show_week_numbers`, `event_limit`, `skip_popover`, `talk_enabled`, `hide_event_export`, `disable_appointments`, …).
2. **SPA start:** the entry `src/main.js` initialises Vue 3 + router + Pinia; `src/services/caldavService.js` builds a `@nextcloud/cdav-library` client on `rootUrl = {base}/remote.php/dav/` and connects (`connect({ enableCalDAV: true })`).
3. **Loading data:** the calendar list via `PROPFIND` on the calendar home; events per view via `REPORT calendar-query` for the visible time window (the store `fetchedTimeRanges.js` avoids duplicate queries); changes in the tabs made by other clients are pulled in through the Notify-Push message `calendar_sync` (`NotifyPushListener`).
4. **Writing:** event changes are `PUT`/`DELETE` on the ICS objects in DAV (ETag-based); attendee invitations are processed by the server (iTIP/schedule in the `dav` backend).
5. **Special features:** booking, proposal, autocomplete and configuration actions run through the app's own controllers (see [api.md](api.md)); booking finally writes the event via `BookingCalendarWriter` back into the target calendar over CalDAV.
6. **Public views:** `/p/{token}` and `/embed/{token}` render `templates/public.php`; the CalDAV client opens the server's public calendar collection (`_createPublicCalendarHome`), without a user login.

## Directory and module structure (repo)

```
appinfo/            info.xml (metadata, navigation entry order 5), routes.php
templates/          main.php, public.php, appointments/
lib/                PHP backend of the app (AppFramework)
├── AppInfo/        Application.php (bootstrap: widgets, listeners, notifier), Capabilities.php
├── Controller/     View, PublicView, Appointment, Booking, AppointmentConfig,
│                   Contact (autocomplete), Email, Settings, Object (deep-link resolver),
│                   Proposal, ProposalPublic
├── Service/
│   ├── Appointments/  config service, slot logic (AvailabilityGenerator, SlotExtrapolator,
│   │                  DailyLimitFilter, EventConflictFilter, TimezoneGenerator),
│   │                  BookingService, BookingCalendarWriter, MailService
│   ├── Proposal/      ProposalService (proposals, votes, conversion into an event)
│   └── CalendarInitialStateService, JSDataService, ContactsService, ObjectResolverService
├── Db/             mappers/entities for bookings, configs and proposals
├── Objects/        JSON models of the proposal domain (Collection/Object/Vote/…)
├── Listener/       AppointmentBooked, CalendarReference, NotifyPush, UserDeleted
├── BackgroundJob/  CleanUpOutdatedBookingsJob
├── Migration/      DB schema (2040, 3000, 3010, 4050, 5050 ×4, 6060)
├── Dashboard/ Profile/ Reference/ Notification/ UserMigration/
└── Http/ Exception/
src/                Vue 3 frontend (rspack bundles)
├── main.js, appointments/main-*.js, proposal-public.ts   ← bundle entries
├── views/          Calendar.vue, EditSimple/EditFull, Appointments/, Proposal/,
│                   ContactsMenuAvailability.vue
├── components/     AppNavigation/ (calendar list, settings, import, shortcuts),
│                   Editor/ (Properties, Repeat, Alarm, Invitees, Resources, Talk,
│                   Attachments, FreeBusy), AppointmentConfigModal/, Appointments/,
│                   Proposal/, Shared/, Subscription/
├── store/          Pinia: calendars, calendarObjects, calendarObjectInstance, settings,
│                   appointmentConfigs, proposalStore, delegation, unscheduledTasks,
│                   importFiles, principals, contacts, davRestrictions, fetchedTimeRanges
├── services/       caldavService (cdav-library), proposalService, appointmentService,
│                   autocompleteService, freeBusyService, attachmentService, talkService …
├── fullcalendar/   view configuration, event sources, interaction (eventDrop …)
└── models/ types/ utils/ mixins/
```

Build entry points (`rspack.config.js`): `main` (main app), `reference` (link preview), `contacts-menu` (availability in the contacts menu, loaded globally from `Application::boot()`), `appointments-booking`, `appointments-confirmation`, `appointments-overview`, `proposal-public`.

## Configuration

- **Administrative (app values, via `occ config:app:set calendar …`):**
  - `hideEventExport=yes` hides the ICS export of individual events;
  - `disableAppointments=yes` switches the booking feature off.
- **Per user** (stored through the UI, endpoint `POST /v1/config/{key}`; keys among others from `src/store/settings.js`): `view` (default view), `timezone`, `showWeekends`, `showWeekNr`, `showTasks`, `tasksSidebar`, `eventLimit`, `skipPopover`, `slotDuration`, `defaultReminder`, `defaultReminderPartDay`, `defaultReminderFullDay`, `attachmentsFolder`.
- **Runtime dependencies:** Nextcloud app `dav` (CalDAV backend, mandatory), optionally `talk` (conferences), `contacts` (autocomplete, birthdays), Circles, Tasks/Deck (VTODO sources), `notify_push` (live sync), the Notifications app (reminders/bookings).

## Data model

- **The calendar domain does not live in the app database** but as ICS objects (VEVENT/VTODO/VJOURNAL) in the CalDAV backend of the server; calendar properties are WebDAV properties (displayname, `{http://nextcloud.com/ns}calendar-color` …), shares are CalDAV ACLs.
- **Own tables** (`lib/Db`, migrations):
  - `calendar_appt_configs` – appointment booking configurations (owner, token, target calendar, visibility, availability JSON, durations/limits)
  - `calendar_appt_bookings` – booked/provisional bookings (token, slot, status)
  - `calendar_proposal_dts` – meeting proposals (UID, UUID/token, title, description, location, duration, `response_notify`), plus
  - `calendar_proposal_pts` (participants incl. realm/status/attendance),
  - `calendar_proposal_dats` (candidate appointments),
  - `calendar_proposal_vts` (votes per participant/appointment)
- **No sync table/caches:** the app keeps no mirrors of events; `fetchedTimeRanges` is only a runtime cache in the browser.

## Deployment

- **Standard route:** installation through the Nextcloud App Store (`apps.nextcloud.com/apps/calendar`) or directly in the instance; release tarballs (built signed) are hosted at `github.com/nextcloud-releases/calendar`. App v6.6.4 needs Nextcloud **32–35** and PHP **8.1–8.5**; the CalDAV backend is already part of the server.
- **Developer build:** `composer install` + `npm ci`, frontend built with rspack (Node required); the artifact is deployed like an ordinary Nextcloud app under `apps/calendar`.
- **Browser support** according to the README: Chrome/Chromium ≥ 76, Edge ≥ 40, Firefox ≥ 60, Safari ≥ 12.1 (IE 11 is still named there — doubt it for current 6.x versions, not separately verified).
- **Operations note:** only behind HTTPS; CalDAV basic/app passwords and the tokens of the public pages are unprotected without TLS. The server's cron determines when booking cleanup, subscription refresh and e-mail reminders run.
