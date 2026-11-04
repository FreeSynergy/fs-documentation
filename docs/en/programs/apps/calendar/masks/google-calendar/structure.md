# Google Calendar – Structure (as of 2026-11-02)

Google Calendar is closed source; internal process/server architecture is not public. This file documents the **officially evidenced** layout: the external request flow, the public resource/module structure of API v3, the data model, configuration surfaces and deployment reality. Sources: discovery v3 (revision 20261028) + official help pages (URLs in [index.md](index.md)).

## Request flow

### Use through the interface

Browsers/apps (Android, iOS, Wear OS, Apple Watch) → `https://calendar.google.com` or the Google-account sync of the apps → Google backend (internal, undocumented). Changes are immediately available on all Google channels; ICS addresses (public/secret per calendar) serve external clients for subscriptions.

### Use through API v3 (the documented path)

```
1. OAuth 2.0 handshake:
   consent screen (scope selection) → access/refresh token
   (alternatively: service account + domain-wide delegation; API key only for public calendars)

2. API calls:
   HTTPS + Authorization: Bearer → https://www.googleapis.com/calendar/v3/…
   responses as JSON, each resource carrying an etag (optimistic locking)

3. Synchronisation:
   full sync with events.list (timeMin/timeMax, singleEvents)
   → remember nextSyncToken
   → next change as a delta: events.list?syncToken=… (updatedMin, showDeleted)

4. Push instead of polling:
   POST …/events/watch {id, type:"web_hook", address:"https://…"}
   → Google sends header-only POSTs (X-Goog-Resource-State: sync|exists|not_exists)
   → the receiver answers with 200/201/202/204/102 and pulls the delta via syncToken
   → the channel expires and must be renewed with a new id; stop via POST /channels/stop

5. Batching:
   POST https://www.googleapis.com/batch/calendar/v3 (multipart of several calls)

6. Free/busy:
   POST /freeBusy {timeMin,timeMax,items:[{id:…}]} → busy intervals per calendar
   (groups are expanded along: groupExpansionMax)
```

## Module/resource structure (public API surface)

Eight resource groups according to discovery v3:

| Group | Purpose |
|-------|---------|
| `calendars` | calendar record (create/modify/delete/clear/transferOwnership) |
| `calendarList` | user-specific calendar list (`users/me`): visibility, colours, reminders, watch |
| `events` | events incl. import/quickAdd/move/instances/watch |
| `acl` | sharing rules per calendar incl. watch |
| `freebusy` | availability query (POST) |
| `colors` | colour palettes (calendars/events) |
| `settings` | user interface settings as key/value (`users/me/settings`, watch) |
| `channels` | terminate push channels (one stop endpoint for all watch resources) |

39 schemas, among others: `Event`, `EventAttendee`, `EventDateTime`, `EventReminder`, `EventAttachment`, `EventLabel`, `EventFocusTimeProperties`, `EventOutOfOfficeProperties`, `EventWorkingLocationProperties`, `EventBirthdayProperties`, `ConferenceData`/`EntryPoint` (Meet), `Calendar`, `CalendarListEntry`, `AclRule`, `Setting`, `Channel`, `Colors`, `FreeBusyRequest/Response`, `FreeBusyCalendar/Group`, `TimePeriod`.

## Data model

- **Calendar**: `summary`, `description`, `timeZone`, `location`, `conferenceProperties` (permitted conference types), `autoAcceptInvitations`, `dataOwner`, `labelProperties`.
- **CalendarListEntry** (the user-specific view of the same calendar): `primary`, `selected`, `hidden`, `colorId`/`backgroundColor`/`foregroundColor`, `defaultReminders`, `notificationSettings`, `summaryOverride`, `timeZone`, `deleted`, `accessRole`, `dataOwner`, `autoAcceptInvitations`.
  *Note, verified schema change:* the former fields `summaryVisibility` and `subscriptionType` **no longer appear** in discovery revision 20261028 — older third-party documentation is out of date here.
- **Access roles** (`accessRole`, `AclRule`): `freeBusyReader`, `reader`, `writerWithoutPrivateAccess` (new: write without private details), `writer`, `owner`; ACL scopes: `user`, `group`, `domain`, `default` (public). Important distinction according to the API: **owner role ≠ dataOwner** (several owners possible, one dataOwner; change via `calendars.transferOwnership`).
- **Event**:
  - Time: `start`/`end` as `EventDateTime` (`dateTime` with offset or `date` for all-day), `endTimeUnspecified`, `recurrence` (RRULE lines), `originalStartTime`, `recurringEventId`, `sequence`, `created`/`updated`
  - Identity: `id`, `iCalUID`, `etag`, `htmlLink`
  - Status/visibility: `status` (`confirmed`/`tentative`/`cancelled`), `transparency` (`opaque`/`transparent`), `visibility` (`default`/`public`/`private`), `locked`, `privateCopy`
  - Types (`eventType`): `default`, `birthday`, `focusTime`, `fromGmail` (cannot be created), `outOfOffice`, `workingLocation` — each with its own property block
  - Attendees: `attendees[]` (`email`, `displayName`, `optional`, `resource`, `organizer`, `self`, `responseStatus` needsAction/declined/accepted/tentative, `additionalGuests`, `comment`), `attendeesOmitted`, guest switches (`guestsCanInviteOthers`, `guestsCanModify`, `guestsCanSeeOtherGuests`)
  - Other: `reminders` + `reminderOverrides`, `attachments[]` (Drive/URL), `eventLabelId` (labels via eventLabelVersion=1), `conferenceData` (Meet conference, `createRequest`), `extendedProperties` (private/shared), `source`, `colorId`, `gadget` (legacy)
- **Setting**: `id`/`value` per user (the API docs give the time zone as an example; the full ID list is not published → **not verified**), changeable through the UI, readable/watchable via `users/me/settings`.
- **Channel**: `id`, `resourceId`, `resourceUri`, `address`, `expiration`, `token`, `params`.

## Configuration

| Level | Where | Evidenced examples |
|-------|-------|--------------------|
| User (UI) | gear → "Settings" | "Enable keyboard shortcuts", "View options" (start of week, custom view), "Import & export" |
| User (API) | `settings` resource | time zone among others (full list not published) |
| Calendar (record) | `calendars` + UI "Settings and sharing" | name, time zone, description, location, iCal addresses (public/secret), share list, export |
| Calendar (per user) | `calendarList` | colour, selected/hidden, default reminders, notifications |
| Appointment schedule | UI "Create → Appointment schedule" | appointment length, availability windows, buffer, max per day, guest rights, target calendar |
| Workspace admin | Admin console | payments for appointment schedules (Stripe) ON/OFF, Time Insights can be disabled, export can be restricted; the LSA/G-Sync switches were dropped in 2024/2025 |
| API usage | Google Cloud project | OAuth consent screen, scopes, quota management, API key |

## Deployment

- **Google SaaS only**: no server image, no own installation, no on-premises variant; data held in Google data centres (Google does not publish the exact region/redundancy for calendars → **not verified**).
- The UI and apps are rolled out continuously (the Workspace updates blog distinguishes "Rapid Release" and "Scheduled Release").
- API state is versioned through discovery revisions (currently 20261028); protection against breaking changes through ETags and version parameters (`conferenceDataVersion`, `eventLabelVersion`).
- Billing/quota: standard usage is free; quota model for projects from 1 May 2026, pricing above the daily limit announced for "later in 2026".

## Place in the FreeSynergy context

Unlike DAViCal (open request flow: PROPFIND/PUT/REPORT per RFC 4791 against your own server), Google Calendar can only be attached through the REST flow above: your own OAuth app, sync-token deltas and watch channels. Exchange with CalDAV clients is not officially provided; bridges must use the Calendar API v3 (or ICS subscriptions in read-only mode).
