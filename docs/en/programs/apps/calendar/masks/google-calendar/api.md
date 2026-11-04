# Google Calendar – API (Calendar REST API v3, as of discovery revision 2026-10-28)

## Version state and development

- **Current and only officially documented version: Calendar REST API v3.** The machine-readable discovery document (`https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest`) carries **revision 20261028**; the developer documentation was last updated in autumn 2026. The service is being actively developed (in 2026 among other things a new quota model as of 1 May 2026, event labels, focus-time/out-of-office/working-location fields).
- Google Calendar is in heavy use (consumer and Workspace accounts); nothing suggests the API is being discontinued.
- **Self-hosting the API is not possible** – the service runs exclusively in the Google Cloud. A Calendar API v2 (legacy) is no longer contained in the current official documentation.

| Property | Value |
|----------|-------|
| Base URL | `https://www.googleapis.com/calendar/v3/` |
| Batch endpoint | `https://www.googleapis.com/batch/calendar/v3` |
| Discovery | `https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest` (revision 20261028) |
| Format | JSON over HTTPS; `alt` (e.g. `json`), `fields` (partial response), `prettyPrint` as global parameters |
| Auth | OAuth 2.0 (`Authorization: Bearer …`), service accounts, API key only for public calendars |

## Authentication and scopes

- **OAuth 2.0** is the standard route (access token as a bearer header, refresh token for long-term integrations). Public apps with sensitive scopes must go through Google's verification process.
- **Service account + domain-wide delegation**: server-to-server access to the calendars of a Workspace domain; Workspace administrators can act within the organisation's calendars using `useAdminAccess`.
- **API key** (`?key=…`): only for read access to public calendars without a user context.
- **Calendar IDs**: `primary` (default calendar of the signed-in user), an e-mail address (private/group/resource calendar), a calendar ID from `calendarList.list`.

Complete official scope list (scopes page, as of 2026-09; base `https://www.googleapis.com/auth/`):

| Scope | Permission |
|-------|------------|
| `calendar` | view, change, share and permanently delete all accessible calendars |
| `calendar.readonly` | only view/download all accessible calendars |
| `calendar.events` | view and change events in all your own calendars |
| `calendar.events.readonly` | only view events of all calendars |
| `calendar.events.owned` | view/change/delete events in calendars you own |
| `calendar.events.owned.readonly` | only view events in your own calendars |
| `calendar.events.public.readonly` | only view events of public calendars |
| `calendar.events.freebusy` | see availability (free/busy) of accessible calendars |
| `calendar.freebusy` | view your own availability |
| `calendar.calendars` | view/change calendar properties, create secondary calendars |
| `calendar.calendars.readonly` | only view calendar properties |
| `calendar.calendarlist` | view your own calendar list, add/remove calendars |
| `calendar.calendarlist.readonly` | only view your own calendar list |
| `calendar.acls` | view/change shares of your own calendars |
| `calendar.acls.readonly` | only view shares of your own calendars |
| `calendar.app.created` | manage secondary calendars created by the app |
| `calendar.settings` | view and change calendar settings |
| `calendar.settings.readonly` | only view calendar settings |
| `calendar.addons.execute` / `.addons.current.event.read` / `.addons.current.event.write` | for Calendar add-ons only |

There is **no** scope called `calendar.push` (push channels are created with the ordinary resource scopes).

## Resources and endpoints (exact, discovery v3 rev. 20261028)

| Resource | Method | HTTP | Path |
|----------|--------|------|------|
| `calendars` | insert | POST | `/calendars` |
| | get | GET | `/calendars/{calendarId}` |
| | update / patch | PUT / PATCH | `/calendars/{calendarId}` |
| | delete | DELETE | `/calendars/{calendarId}` |
| | clear (delete all events) | POST | `/calendars/{calendarId}/clear` |
| | transferOwnership (`newDataOwner`, `useAdminAccess`) | POST | `/calendars/{calendarId}/transferOwnership` |
| `calendarList` | list | GET | `/users/me/calendarList` |
| | insert | POST | `/users/me/calendarList` |
| | get | GET | `/users/me/calendarList/{calendarId}` |
| | update / patch | PUT / PATCH | `/users/me/calendarList/{calendarId}` |
| | delete (unsubscribe only) | DELETE | `/users/me/calendarList/{calendarId}` |
| | watch | POST | `/users/me/calendarList/watch` |
| `events` | list | GET | `/calendars/{calendarId}/events` |
| | insert | POST | `/calendars/{calendarId}/events` |
| | get | GET | `/calendars/{calendarId}/events/{eventId}` |
| | update / patch | PUT / PATCH | `/calendars/{calendarId}/events/{eventId}` |
| | delete | DELETE | `/calendars/{calendarId}/events/{eventId}` |
| | import (adopt an event without invitation e-mails) | POST | `/calendars/{calendarId}/events/import` |
| | quickAdd (`text` parameter) | POST | `/calendars/{calendarId}/events/quickAdd` |
| | move (`destination`) | POST | `/calendars/{calendarId}/events/{eventId}/move` |
| | instances | GET | `/calendars/{calendarId}/events/{eventId}/instances` |
| | watch | POST | `/calendars/{calendarId}/events/watch` |
| `acl` | list/insert | GET/POST | `/calendars/{calendarId}/acl` |
| | get/update/patch/delete | GET/PUT/PATCH/DELETE | `/calendars/{calendarId}/acl/{ruleId}` |
| | watch | POST | `/calendars/{calendarId}/acl/watch` |
| `freebusy` | query | POST | `/freeBusy` |
| `colors` | get (calendar/event colour palette) | GET | `/colors` |
| `settings` | list | GET | `/users/me/settings` |
| | get | GET | `/users/me/settings/{setting}` |
| | watch | POST | `/users/me/settings/watch` |
| `channels` | stop | POST | `/channels/stop` |

Notes: `calendarList` and `settings` are hard-wired to `users/me` — other people's calendar lists cannot be viewed through the API. An `events.freeBusy` endpoint does not exist in v3; free/busy runs exclusively through `POST /freeBusy`.

## Important method parameters

- **`events.list`**: `timeMin`/`timeMax` (RFC 3339), `singleEvents` (expand series into single events), `orderBy` (`startTime`), `q` (free text over summary, description, location, attendees among others), `updatedMin`, `showDeleted`, `showHiddenInvitations`, `eventTypes` (repeatable), `privateExtendedProperty`/`sharedExtendedProperty`, `maxResults` (default 250), `pageToken`, **`syncToken`** (delta sync via `nextSyncToken`), `timeZone`, `maxAttendees`, `iCalUID`.
- **`events.insert`/`update`/`patch`/`import`**: `sendUpdates` (`all` / `externalOnly` / `none`; `sendNotifications` deprecated), `conferenceDataVersion` (0–1, Meet conferences via `createRequest`), `supportsAttachments` (attachments), `eventLabelVersion` (0 = `colorId`, 1 = `eventLabelId`). `update` always replaces the whole resource object (no patch semantics); for partial updates `get` + modify + `patch`, atomicity via ETags.
- **`events.instances`**: pages of the recurring series (`timeMin`/`timeMax`, `originalStart`, max. 250 per page).
- **`freebusy.query`**: request `FreeBusyRequest` with `timeMin`/`timeMax`, `timeZone`, `items` (calendars/groups), `calendarExpansionMax`, `groupExpansionMax`; response per calendar `busy` intervals and optionally `errors`, for groups `groups`.
- **`calendars.*`**: `useAdminAccess` for Workspace admins.
- **Optimistic locking**: every resource carries an `etag`; the official reference recommends `get` + `update`/`patch` with the ETag for atomic changes.

## Data model (short form, details in structure.md)

Resources according to discovery: `Calendar`, `CalendarListEntry`, `Event`, `EventAttendee`, `EventReminder`, `EventDateTime`, `AclRule`, `Setting`, `Channel`, `Colors`, `FreeBusyRequest/Response`, `ConferenceData` (Meet), `EventAttachment`, `EventLabel`, `FocusTimeProperties`, `OutOfOfficeProperties`, `WorkingLocationProperties`, `BirthdayProperties`.

## Push notifications (webhooks)

- Watchable resources: **Acl, CalendarList, Events, Settings** — each with its own `…/watch` endpoint, one shared stop endpoint `POST /channels/stop` (at least `id` + `resourceId`).
- Channel request: `id` (unique within the project, max. 64 characters), `type: "web_hook"`, `address` (**HTTPS with a valid, non-self-signed certificate**), optionally `token` (max. 256 characters) and `expiration` (Unix ms).
- Responses deliver `resourceId` (version-independent) and `resourceUri`; every notification is an HTTPS POST (user agent `APIs-Google`) with the headers `X-Goog-Channel-ID`, `-Token`, `-Expiration`, `X-Goog-Resource-ID`, `-URI`, `-State` (`sync` | `exists` | `not_exists`), `-Message-Number`.
- **The message contains no event content** — afterwards you pull the change yourself via `events.list` with `syncToken`.
- The receiver must answer 200/201/202/204/102; on 500/502/503/504 Google retries with exponential backoff, all other codes count as a delivery failure.
- **No automatic renewal**: replace channels before they expire with a new `watch` request and a new `id`.

## Limits and quotas (official usage-limits page, as of the model in force since 1 May 2026)

| Limit | Value |
|-------|-------|
| Requests per minute per Cloud project | 10,000 |
| Requests per minute per user per project | 600 |
| Daily threshold per project (planned fees afterwards) | 1,000,000 |
| Error code when exceeded | HTTP 403/429 `usageLimits` (sliding window; exponential backoff recommended) |

Additionally **operational limits** that Google may adjust at any time (e.g. writing to a single calendar too fast). Standard usage is free; exceeding the daily limit is to become chargeable "later in 2026" (with ≥ 90 days notice). Quota increases can be requested in the Google Cloud console; service-account traffic counts as one user. Side note from the help: more than **400 subscribed calendars** in one account cause performance problems.

## Batching

Several calls per HTTP request via `POST https://www.googleapis.com/batch/calendar/v3` (multipart, each sub-request with its own auth/parameters).

## Client libraries (official downloads page)

Stable: **Java, JavaScript, .NET, Objective-C (REST), PHP, Python (v1/v2)**. Early stage: **Dart (beta), Go, Node.js (alpha), Ruby (alpha)**. All libraries support bearer OAuth and push-channel helpers.

## Other official interfaces

- **Google Tasks API** (`https://tasks.googleapis.com/tasks/v1/…`): tasks that appear in the calendar UI next to events; a separate service, not part of v3.
- **Apps Script service `CalendarApp`** and **Workspace add-ons for Calendar**: script/extension control inside the Google account (`calendar.addons.*` scopes).
- **Google Workspace Events API** (`https://workspaceevents.googleapis.com/v1/subscriptions`, Pub/Sub-based): the official Workspace Pub/Sub mechanism; whether calendar resources can currently be subscribed is not evidenced on the reference page checked (**not verified**).

## What does NOT exist at the API level

- **No documented CalDAV/CardDAV offering.** Google switched off CalDAV/CardDAV access with a password (Less Secure Apps) for Workspace from 2024-09-30 and account-wide from 2025; the official developer documentation names only the REST API. Community tools (DAVx⁵) still address Google endpoints over OAuth — according to DAVx⁵ "not officially supported by either Google or DAVx⁵" — as a support, not a guarantee.
- No GraphQL, no OData, no server/self-hosting variant of its own, no API for public booking pages ("appointment schedules") — in the current discovery v3 (rev. 20261028) neither a dedicated resource nor an `appointment` value for `eventType` exists; booking pages are a pure UI feature.
- No access to calendar lists other than `users/me`, no calendar search API (sharing works via IDs/e-mail).
