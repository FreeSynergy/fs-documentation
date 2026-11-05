# Appointments – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.**

## Core standard

| Standard | Evidence | Role |
|----------|----------|------|
| **JSCalendar, RFC 8984** | ✅ | canonical model (decision 1): object types `Event`, `Task`, `Group` |

**Verified properties (RFC 8984, ✅):** `@type`, `uid`, `relatedTo`, `prodId`, `created`, `updated`, `sequence`, `method`, `title`, `description`, `descriptionContentType`, `showWithoutTime`, `locations`, `virtualLocations`, `links`, `locale`, `keywords`, `categories`, `color`, `recurrenceId`, `recurrenceRules`, `excludedRecurrenceRules`, `recurrenceOverrides`, `excluded`, `priority`, `freeBusyStatus`, `privacy`, `replyTo`, `sentBy`, `participants`, `requestStatus`, `useDefaultAlerts`, `alerts`, `localizations`, `timeZone`, `timeZones` — Event: `start`, `duration`, `status`; Task: `due`, `start`, `estimatedDuration`, `percentComplete`, `progress`, `progressUpdated`.

**Participant model (RFC 8984, ✅):** `name`, `email`, `description`, `sendTo` (`imip`, `other`), `kind` (`individual`, `group`, `location`, `resource`), `roles` (required, at least one: `owner`, `attendee`, `optional`, `informational`, `chair`, `contact`), `locationId`, `language`, `participationStatus` (`needs-action`, `accepted`, `declined`, `tentative`, `delegated`), `participationComment`, `expectReply`, `scheduleAgent`, `scheduleForceSend`.

## Surrounding standards (all ✅)

| Standard | Evidence | Role |
|----------|----------|------|
| iCalendar, RFC 5545 | ✅ | file export/import; `RRULE` rule set |
| jCal, RFC 7265 | ✅ | JSON wrapper over the iCalendar grammar (export variant) |
| iTIP, RFC 5546 | ✅ | invitation protocol |
| CalDAV Scheduling, RFC 6638 | ✅ | server integration |
| CalDAV SYNC, RFC 6578 | ✅ | sync mechanism (`sync_token`) |
| RFC 9073 | ✅ | `STYLED-DESCRIPTION` (rich text), `STRUCTURED-DATA` |
| RFC 9074 | ✅ | VALARM extensions (`alerts`/reminders) |
| RFC 6868 | ✅ | shared escaping rules iCal/vCard |
| RFC 5322 §3.4.1 | ✅ | format of `Participant.email` |
| `draft-ietf-calext-jscalendarbis` | ✅ found, content unread ⚠️ | will obsolete RFC 8984 — watch it |

## Why JSCalendar and not jCal

jCal is the JSON wrapper **over the iCalendar grammar** (property lists with parameters); JSCalendar is a real object model — for a database JSCalendar is the working representation, iCalendar/jCal are export (position from [standards.md](../standards.md)).

## Open standard points

- Naming conflict: JSCalendar `title` (display name) vs. `name` (JSContact/schema.org/AS2) — the rule is **open decision 1** in [standards.md](../standards.md).
- Read jscalendarbis as soon as it is decided to replace RFC 8984.
