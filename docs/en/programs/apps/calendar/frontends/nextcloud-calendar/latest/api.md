# Nextcloud Calendar – API (app version 6.6.4, as of 2026-11-02)

## Version state and development

- **App `calendar`, version 6.6.4** (released 2026-10-26, repo `github.com/nextcloud/calendar`). The project is active: last tags in October 2026, daily commit activity, no announced end of life.
- `appinfo/info.xml` v6.6.4 requires **PHP 8.1–8.5** and **Nextcloud Server 32–35** and explicitly declares `<backend>caldav</backend>`.
- **Basic architecture with regard to the API question:** the app is only the web frontend (Vue.js). Actual data access to calendars and events runs through the **CalDAV backend of the Nextcloud server** (sabre/dav), which is not part of this app. The app additionally ships its own HTTP routes: HTML views, a small internal JSON API (`/v1/...`), the appointment booking API and — new in the 6.x series — an OCS API for meeting proposals (Doodle-style polls).

| API level | Base URL | Status |
|-----------|----------|--------|
| CalDAV (events, calendars, sync) | `{base}/remote.php/dav/` | server backend, IETF standards RFC 4791/5995, stable |
| App routes (views, public, booking) | `{base}/index.php/apps/calendar/` | from the app's `appinfo/routes.php`, tied to the version |
| App JSON API (`/v1/...`) | `{base}/index.php/apps/calendar/v1/` | internal API of the frontend, not promised as a public API |
| Meeting proposals | `{base}/ocs/v2.php/calendar/proposal/...` | defined in the source via the `#[ApiRoute]` attribute |
| Webhooks | – | not present (see below) |

## CalDAV backend (the actual data access level)

The app's own frontend uses the official client **`@nextcloud/cdav-library`** with `rootUrl = generateRemoteUrl('dav')`, i.e. `{base}/remote.php/dav/` (`src/services/caldavService.js`). So for any integration exactly the path the app itself takes applies:

- **Discovery:** `/.well-known/caldav` → redirects to the user principal.
- **Principal:** `PROPFIND {base}/remote.php/dav/principals/users/{user}/` (returns `calendar-home-set`).
- **Calendar home:** `{base}/remote.php/dav/calendars/{user}/` — your own calendars; `PROPFIND` (Depth 1) to list, `MKCALENDAR` to create, `PROPPATCH` for displayname/colour/time zone, `DELETE` to delete.
- **Events:** `PUT`/`GET`/`DELETE` on `{base}/remote.php/dav/calendars/{user}/{calendar}/{object}.ics` (ICS per RFC 5545; concurrency via `ETag`/`If-Match`).
- **Queries:** `REPORT calendar-query` (time-range search), `REPORT calendar-multiget`, `REPORT sync-collection` (incremental sync, RFC 5995), `REPORT free-busy-query`.
- **Public calendars:** token-based collection under `/remote.php/dav/public-calendars/{token}`; export as ICS via `POST ...?export`. The app builds its public/embed view on the same public CalDAV collection (`_createPublicCalendarHome` in `caldavService.js`).
- **Nextcloud-specific header:** the app sends `X-NC-CalDAV-Webcal-Caching: On` (or `Off` to explicitly list WebCal subscriptions) — a server extension header, not a standard.
- Birthday calendars and other server-side calendar sources appear in the same calendar home.

The CalDAV endpoints belong to the Nextcloud server (admin manual → groupware); details such as `getctag` for change detection are documented there.

## App routes according to `appinfo/routes.php` (v6.6.4)

Base `{base}/index.php/apps/calendar/` (short form `{base}/apps/calendar/…`).

### HTML/deep-link routes (GET)

| URL | Purpose |
|-----|---------|
| `/` | app start |
| `/new` or `/new/{isAllDay}/{dtStart}/{dtEnd}` | open the editor for a new event (direct link) |
| `/edit/{objectId}` or `/edit/{objectId}/{recurrenceId}` | edit an event; `objectId` is the **base64 of the DAV path** `/remote.php/dav/calendars/{user}/{calendarUri}/{objectUri}` (verified in the source `ObjectController`/`ViewController`) |
| `/{view}/{timeRange}` | view + time window; `view` exactly: `timeGridDay`, `timeGridWeek`, `dayGridMonth`, `multiMonthYear`, `listMonth` |
| `/{view}/{timeRange}/new/{mode}/{isAllDay}/{dtStart}/{dtEnd}` or `…/edit/{mode}/{objectId}/{recurrenceId}` | editor from within a view |
| `/object/{uid}` and `/object/{uid}/{recurrenceId}` | **permanent deep link** by iCal UID alone; resolves the event and redirects to `/edit/…` (`recurrenceId`: Unix timestamp or `next`) |
| `/p/{token}`, `/p/{token}/{view}/{timeRange}`, `/p/{token}/{fancyName}` | public, branded calendar view |
| `/embed/{token}…` | public view without Nextcloud chrome (embedding) |
| `/public/{token}` | legacy alias |
| `/appointments/{userId}` | the appointment booking page of a user |
| `/appointment/{token}` | the concrete booking page of an appointment configuration |
| `/appointment/confirm/{token}` | confirmation page after an appointment booking (GET form, POST confirm) |
| `{base}/calendar/proposal/{token}` | public poll page of a meeting proposal (`#[FrontpageRoute]` with `root: '/calendar'` in `ProposalPublicController`) |

### Internal JSON API `/v1/…` (used by the frontend)

| Method | Endpoint | Parameters (from the controllers) |
|--------|----------|-----------------------------------|
| POST | `/v1/autocompletion/attendee` | `search` – attendee completion from Contacts/Circles |
| POST | `/v1/autocompletion/location` | `search` – room/location suggestions (resources) |
| POST | `/v1/autocompletion/photo` | `search` – photo hits |
| POST | `/v1/autocompletion/groupmembers` | `groupName` – members of a contact group |
| GET | `/v1/circles/getmembers` | `circleId` – members of a Circles team |
| POST | `/v1/config/{key}` | save the user's app setting (keys from `SettingsController`) |
| POST | `/v1/public/sendmail` | `recipient` among others – e-mail a public calendar link |

All `/v1/` endpoints require a logged-in Nextcloud session (`@NoAdminRequired`); they are not documented as a stable external API and may change between app versions.

### Appointment booking (booking, PublicPage + token)

| Method | Endpoint | Rate limit (attributes in the code) |
|--------|----------|-------------------------------------|
| GET | `/appointment/{appointmentConfigToken}/slots` | – |
| POST | `/appointment/{appointmentConfigToken}/book` | anonymous 10/1200 s, user 10/300 s |
| POST | `/appointment/confirm/{token}` | – |

Booking flow: `slots` returns bookable intervals (computed from the config's `availability` minus occupancy), `book` reserves provisionally, `confirm` after the confirmation e-mail writes the event into the target calendar (`BookingCalendarWriter`). The background job `CleanUpOutdatedBookingsJob` clears abandoned reservations.

### Appointment configurations (REST resource, logged-in users)

Resource `appointmentConfig` on `/v1/appointment_configs`:

- `GET /v1/appointment_configs` – your own configurations
- `GET /v1/appointment_configs/{id}` – single item
- `POST /v1/appointment_configs` – create (rate limit 10/1200 s)
- `PUT /v1/appointment_configs/{id}` – change
- `DELETE /v1/appointment_configs/{id}` – delete

Field schema `create` (validated in `AppointmentConfigController::create`): `name`, `description`, `location`, `visibility` (`PUBLIC`/`CONFIRMED`), `targetCalendarUri`, `availability` = `{ timezoneId, slots: { MO…SU: [ {start,end} ] } }`, `length`, `increment`, `preparationDuration`, `followupDuration`, `timeBeforeNextSlot`, `dailyMax`, `calendarFreeBusyUris`, `start`, `end`, `futureLimit` (seconds or Unix timestamps), `createTalkRoom` (optional bool, creates a Talk room directly).

### Meeting proposals (OCS API, 6.x series)

All calls are **POST in OCS format** (`OCS-APIRequest: true`), base `{base}/ocs/v2.php/calendar/proposal/` – verified through `#[ApiRoute(root: '/calendar')]` in `ProposalController` and `generateOcsUrl('/calendar/proposal/…')` in the frontend:

| Endpoint | Payload | Access / rate limit |
|----------|---------|---------------------|
| `/list` | `{ user? }` | logged in (own data only; admins others' via `user`), 10/60 s |
| `/fetch` | `{ token }` | PublicPage, anonymous 10/300 s |
| `/create` | `{ proposal }` | logged in, 10/60 s |
| `/modify` | `{ proposal }` | logged in, 10/60 s |
| `/destroy` | `{ id, user? }` | logged in, 10/60 s |
| `/convert` | `{ proposalId, dateId, options }` | logged in, 10/60 s; converts the chosen proposal into a real event (optional Talk room, invitations to participants) |
| `/response` | `{ response }` | PublicPage (voting by token), anonymous 10/300 s |

Proposal data model (`src/types/proposals/proposalInterfaces.ts`): `proposal` with `id`, `uid`, `uuid` (token), `title`, `description`, `location`, `duration`, `responseNotify`, `participants[]` (`address`, `attendance`, `status`, `realm`), `dates[]` (`date`), `votes[]` (`date`, `participant`, `vote`).

## Authentication and permissions

- **Typical Nextcloud, no granular scopes:** every access inherits the full rights of the user.
- **Browser:** Nextcloud session cookie + `RequestToken` (CSRF) for the JSON/write routes.
- **CalDAV and OCS:** HTTP Basic with an **app password** (recommended), bearer token or Nextcloud session; OCS additionally `OCS-APIRequest: true`.
- **PublicPages (public/embed views, booking, proposal fetch/response):** authorised solely through the token in the path; optional password protection of public calendars is a server feature.
- The server's brute-force protection (staggered delays, IP bans) also applies to the DAV routes.

## Limits

- No documented global rate limits; the app defines `#[UserRateLimit]`/`#[AnonRateLimit]` **per endpoint** (tabulated above: 10 requests per 60–1200 s depending on the endpoint).
- Server-side: brute-force throttling, PHP/web server settings, reverse-proxy limits you have to set yourself.
- The practical limit of large rollouts: every event is a separate `PUT` object under CalDAV.

## Push / webhooks

- **No outgoing webhooks.**
- The app listens for the server events `CalendarObjectCreated/Updated/Deleted` and pushes the message `calendar_sync` (with the calendar URL) into the queue of the **Notify-Push app** (`lib/Listener/NotifyPushListener.php`) — but only if that app is installed; it only refreshes the user's own browser tabs and is no third-party hook.
- Notifications about bookings/invitations go out as e-mails and through the Nextcloud **Notifications** app (notifier of the calendar app).
- Pull alternative for integrations: the `sync-collection` REPORT or a `getctag` comparison.

## SDKs and clients

- **No SDK for the app's own endpoints** (deliberately internal).
- JS libraries maintained by the vendor that the app itself uses: `@nextcloud/cdav-library` (CalDAV client), `ical.js` (ICS parsing), FullCalendar (rendering), `@nextcloud/calendar-js` (recurrence rules).
- Server-side reference implementation: **sabre/dav** (PHP).
- External integration: any standard CalDAV client (Thunderbird, GNOME Evolution, Apple Calendar, DAVx⁵, python-caldav …) speaks to the same data basis.

## Distinctions / warnings

- Earlier app versions had different internal endpoints (e.g. `timeobjects`, `schedule`, `comment`) — in v6.6.4 these routes **no longer** exist (`appinfo/routes.php`). Scripts built on them break with modern versions.
- Everything under `/v1/` and `/ocs/v2.php/calendar/…` is not versioned as a public API; stability across app major versions is not promised. The stable integration rail is **CalDAV**.

## Sources (locations, all v6.6.4)

- Source tag `v6.6.4` (tarball `github.com/nextcloud/calendar/archive/refs/tags/v6.6.4.tar.gz`, retrieved 2026-11-02): `appinfo/routes.php`, `appinfo/info.xml`, `lib/Controller/{AppointmentConfig,Booking,Contact,Email,Object,Proposal,ProposalPublic,PublicView,Settings,View}Controller.php`, `lib/Listener/NotifyPushListener.php`, `lib/Migration/Version6060Date20260801000000.php`, `src/services/{caldavService.js,proposalService.ts,appointmentConfigService.js}`, `src/types/proposals/proposalInterfaces.ts`, `CHANGELOG.md`.
- GitHub API tag list `nextcloud/calendar` (newest tag `v6.6.4`, 2026-10-26).
- Nextcloud server documentation on groupware (CalDAV base paths `/remote.php/dav/`, app passwords): docs.nextcloud.com, admin/user manual (referenced in `info.xml` as the official documentation).
