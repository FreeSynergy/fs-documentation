# Outlook calendar – Features (verified against Microsoft Graph v1.0 + official help, 2026-11-02)

Basis: the `event`/`calendar` resources of Microsoft Graph v1.0, the official keyboard shortcuts page (covering the new Outlook, classic Outlook and Outlook on the web) and official help articles. Locations in [index.md](index.md#sources). Items marked as UI elements inferred solely from the shortcut list are evidence of a function, not invented menus.

## Events and series

- Events with title, body (HTML/text), location (plus multiple `locations`), categories (`categories`), priority (`importance`), all-day (`isAllDay`), **own time zone per event** (`DateTimeTimeZone`, `start`/`end`).
- **Recurrence series** (`recurrence`, type `PatternedRecurrence`; event type field `type`: singleInstance/occurrence/exception/seriesMaster) with single-instance management: list instances (`instances`), change/delete single occurrences, `cancelledOccurrences` and `seriesMasterId` for booking by series; `iCalUId` as the RFC 5545 UID.
- **Reminders** per event (`isReminderOn`, minutes before start) with snooze/dismiss as actions (`snoozeReminder`, `dismissReminder`); in classic Outlook additionally a reminder window (shortcut `Alt+V,M`) and a configurable reminder sound.
- **Attachments** on events (`attachments` collection: add/list).
- Drafts for meeting updates (`isDraft` – changes not yet sent to participants).
- Privacy/confidentiality: `sensitivity` (`normal`/`personal`/`private`/`confidential`) and the `showAs` status (`free`/`tentative`/`busy`/`oof`/`workingElsewhere`/`unknown`) as free/busy camouflage, `hideAttendees` (each attendee sees only themselves).

## Participants and meetings

- **Invitations** to users with RSVP: accept / tentative / decline (`accept`, `tentativelyAccept`, `decline`); the organiser can cancel (`cancel`) and forward (`forward`).
- **Time proposals by participants** (`allowNewTimeProposals`) — the counterpart to the meeting polls of other products.
- **Free/busy:** `getSchedule` (query occupancy of several users/resources/distribution lists) and **`findMeetingTimes`** (automatic meeting suggestions from participant availability); in classic Outlook the **scheduling assistant** (`Alt+X`).
- **Online meetings:** `isOnlineMeeting` + `onlineMeeting` (join link via `onlineMeeting.joinUrl`; the old `onlineMeetingUrl` is a deprecation candidate), the provider of your choice is **no longer switchable**; permitted providers per calendar via `allowedOnlineMeetingProviders` — in practice **Teams** (`teamsForBusiness`); no Zoom/Meet integration in the product.
- **Resources:** rooms/equipment as CalDAV-less Exchange resources through the same mailbox model (`getSchedule` supports resource types).
- Limit: max. **500 attendees** per event.

## Calendar management and sharing

- Several calendars per mailbox, calendar folders/groups, colours (11 theme colours + `hexColor`), a default calendar can be marked, `changeKey` as versioning; shares can be read on the API side through the **`calendarPermissions`** association (`isSharedWithMe` marks received shares).
- **Sharing** with permission levels (canViewPrivateItems/canEdit/canShare as the API reflection): evidenced by shortcuts in classic Outlook — "Add to calendar" for a shared calendar (`Alt+H,O,C`), "Share calendar" (`Alt+H,S,C`), edit folder sharing rights (`Alt+H,F,P`), **publish calendar online** (`Alt+H,P,O`).
- **Classic Outlook:** send the calendar by e-mail (`Alt+H,E`).
- **Scheduling links/booking:** the product line solves public booking through the separate app **Microsoft Bookings** — the calendar app itself has no booking page of its own like Nextcloud Calendar or Google's appointment scheduling (booking is external, therefore noted here as a boundary).
- **To Do/tasks:** its own To Do view in the client (`Ctrl+5` in the navigation list of classic Outlook) — tasks live with Microsoft To Do, not as VTodo in the calendar mailbox as with CalDAV servers.

## Clients and views

- **New Outlook / Outlook on the web:** views day, work week, week, month, 3 days, list view (from the official shortcut table: `Ctrl+Alt+1` day, `Ctrl+Alt+2` week/work week, `Ctrl+Alt+4`/`Alt+ =` month, `Alt+3` 3 days; list view without a shortcut); "Today" `Alt+Shift+Y/Home`.
- **Classic Outlook (Windows):** finer day grids of 1–10 days (`Alt+1`…`Alt+0`), whole week/full week, month view, date navigator, "Next 7 days".
- **Sync across devices:** Exchange mailbox sync (EAS/mobile Outlook apps); Outlook for iOS/Android as separate apps.
- **Live updates:** push-like refresh of the clients over the Exchange protocols; for third-party systems real **webhooks** via Graph change notifications (see api.md).
- **Calendar sharing modernisation (2026):** switching calendar sharing from MAPI to a REST model is rolling out tenant by tenant (secondary sources office365itpros.com 2026-05, admin365.blog 2026-07 — marked as secondary sources).

## What the Outlook calendar does NOT offer

- **No CalDAV/CardDAV** in the Outlook clients: "Outlook for Mac doesn't support the CalDAV or CardDAV Internet standards" (official help article, location in index.md). For Outlook.com/Exchange Online there is no official access for external CalDAV clients; third-party connectors (e.g. Outlook CalDav Synchronizer) are unofficial.
- **Private-account accesses withdrawn:** for free Outlook.com accounts the protocols EAS/MAPI/CalDAV were shut down in January 2025 (a technical move to the new Outlook; the primary source, the support page, was unreachable on the research day — marked as secondary information from a techcommunity post, **not verified in detail**).
- **No self-hosting:** Outlook.com is a pure service; a self-operated counterpart would be Exchange Server (on-prem) or a CalDAV server (davical in this series).
- **No appointment booking page of its own** (like Google's appointment scheduling / Nextcloud booking) — instead the separate Bookings app.
- **No meeting poll as a calendar feature** in the Doodle style: the Outlook calendar lacks an equivalent "put proposals up for a vote" object (Nextcloud Calendar offers that as proposals, Google Calendar "polls"); the Outlook event has no voting model — `allowNewTimeProposals` is only the single counter-proposal of one participant. (Formulated as a boundary according to the state of the resource-page sources.)
- **No third-party conference providers** besides Teams (see `allowedOnlineMeetingProviders`).
- **No open ICS API for third parties:** events are mailbox objects (MAPI/Graph), not an ICS object store as with CalDAV servers; import/export is a client feature (ICS files can be imported), not the standard object format of the server API.
- **EWS dependencies break** (shutdown in Exchange Online Oct 2026–Apr 2027).
- **No client API for own add-ins in the new Outlook as in the classic one:** COM add-ins/VBA/macro shortcuts (`Alt+F11`, `Alt+F8`) exist only in classic Outlook (the official shortcuts page lists them under "classic Outlook").
