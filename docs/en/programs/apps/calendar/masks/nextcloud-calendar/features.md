# Nextcloud Calendar – Features (verified against v6.6.4, 2026-10-26)

Every item is evidenced in the source code of release tag v6.6.4; locations in [index.md](index.md#sources).

## Views and navigation

- Five main views, hard-defined as route requirements: **day** (`timeGridDay`), **week** (`timeGridWeek`), **month** (`dayGridMonth`), **year/multi-month** (`multiMonthYear`), **list** (`listMonth`); time windows can be addressed directly by URL (`/{view}/{timeRange}`).
- **Resource timeline** (FullCalendar resource-timeline) in the room-availability dialog.
- Sidebar with the calendar list (colours, ticks, sorting by drag), public calendars, appointment booking configurations, the proposal list and "Unscheduled tasks".
- **Trash view** for deleted calendars and objects (`CalendarList/Trashbin.vue`).
- Search, day/week/year navigation, "Today" jump; event legend in the settings.
- **Permanent deep links**: `/apps/calendar/object/{uid}` resolves events by iCal UID; `/new`, `/edit/{objectId}` as direct create/edit via link.

## Events (editor)

- Two editors: **quick editor** (timeline/click) and **full editor** (`EditSimple.vue`/`EditFull.vue`).
- Fields: title, calendar assignment, colour, start/end, all-day, **own time zone per event**, description, location, **resources/rooms** (room-availability modal with free/busy timeline).
- **Recurrences** (RRULE editor incl. exceptions/series handling), **reminders/alarms** (several, selectable time units; browser notification and e-mail according to the official app description; default reminder configurable).
- **Attachments** from the Nextcloud Files folder (configurable attachment folder).
- **Attendees** with autocomplete (users, groups, Circles, e-mail contacts), **free/busy view** of attendees, availability slot suggestions, invitation-acceptance buttons (accept/tentative/decline) directly in the editor.
- **Conferences only through Nextcloud Talk**: create/link a Talk room when booking an appointment (`AddTalkModal.vue`); no other conference providers in the source code.
- Download events as **ICS** (can be switched off on the server via `hideEventExport`); move/resize via **drag & drop** in calendar views (`fullcalendar/interaction/eventDrop.js`).
- Comments/dialog fields for objects: **not verified** — in v6.6.4 no comment endpoint of its own in `routes.php`.

## Calendar management

- Create/edit (name, colour, description, time zone), delete with **restoration from the trash**, sharing with users/groups/Circles (`EditCalendarModal/SharingSearch.vue`).
- **Public share** via token link: read/write levels, **publish** (`PublishCalendar.vue`), own **embed view without the Nextcloud interface** (`/embed/{token}`), internal link.
- **WebCal subscriptions** (`/components/Subscription`): subscribe to external calendars (read-only; the subscriptions are managed in the UI).
- **Birthday calendar** (from Contacts, a switch in the settings) and **tasks/Deck calendars** (VTODO components; due dates from Tasks/Deck appear in the calendar).
- **Delegation** (`store/delegation.ts`): manage proxy read/write rights over CalDAV principals (view and revoke delegators and delegations).
- **ICS import** through the settings (`SettingsImportSection.vue`, import screen with progress).

## Appointment booking

- Booking configurations with name, description, location, visibility (`PUBLIC`/`CONFIRMED`), target calendar, **weekly availability** (slots per weekday + time zone), slot duration, increment, lead/trailing time, minimum distance to the next slot, daily limit, start/end date, future limit.
- A public booking page per user (`/appointments/{userId}`) and per configuration (`/appointment/{token}`), slot selection, **confirmation e-mail step** (optional), cleanup of outdated bookings via a background job.
- The booking page is linked in the **Nextcloud profile** (profile link action).
- Note: the separate older app "appointments" is an alternative; the calendar app can book by itself.

## Meeting proposals (polls, 6.x series)

- Create/edit/delete a proposal with title, description, location, duration, **candidate appointments** and participants.
- **Voting link** for outsiders (`{base}/calendar/proposal/{token}`, anonymous voting), replies with a vote status per participant, **notification of the organiser** upon a reply (`responseNotify`).
- **Converting** an appointment proposal into a real calendar entry (options, optional Talk room, invitations to participants).

## Miscellaneous

- Dashboard widget "Upcoming events" (the earliest objects).
- **Reference provider**: calendar links generate preview cards in Talk, Text and the like.
- **Live sync of the tabs** through the Notify-Push app (`calendar_sync` message on object changes).
- **Availability in the contacts menu** of the server UI (`ContactsMenuAvailability.vue`).
- Settings: time zone, start-of-week and default view options, weekend/calendar-week-number switches, event-limit popover, birthday/tasks/popover switches, attachment folder.
- Localised into German and many other languages (folder `l10n`, 185 languages).
- Permission model: no rights of the app's own — Nextcloud user rights + CalDAV ACLs; public areas are token-based.

## What Nextcloud Calendar does NOT offer

- **No webhooks/push API** for third-party systems; integration remains pull over CalDAV (`sync-collection`, `getctag`).
- **No offline mode and no native app** — a pure web app (mobile devices use CalDAV clients such as DAVx⁵).
- **No synchronisation with Google/Exchange/EWS**: no write-back sync to external services; external calendars are only readable via a WebCal subscription.
- **No write rights on WebCal subscriptions** (subscriptions are read-only).
- **No other conference providers** besides Nextcloud Talk (no Zoom/Teams/Meet).
- **No resource management of its own**: rooms/equipment must be created server-side as CalDAV resources; the UI only represents them.
- **No recurring-appointment booking**: booking configures weekly slots, but recurring single appointments cannot be booked as a series.
- **No organisation-wide room-booking workflow engine** (no approval workflow beyond CalDAV ACLs).
- **No chat bots/task automation of its own** — automation is left to the Nextcloud ecosystem (workflow apps, OCC).
