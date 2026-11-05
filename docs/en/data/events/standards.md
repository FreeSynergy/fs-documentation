# Appointments – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.**

## Core standard (updated 2026-11-05, `temp/research/events-standards.md`)

| Standard | Evidence | Role |
|----------|----------|------|
| **JSCalendar 2.0** — `draft-ietf-calext-jscalendarbis-22` (2026-10-05, IESG review, will obsolete RFC 8984) | ✅ | **stored model** (ADR 0026): `version: "2.0"` mandatory; incoming RFC 8984 data is upgraded on import |
| JSCalendar 1.0, RFC 8984 | ✅ | import/compatibility |

**What changes in 2.0 (✅):** new `version` (mandatory), `mainLocationId`, `organizerCalendarAddress`, `Participant.calendarAddress`, `Event.endTimeZone`; `@type` mostly optional; `recurrenceRules` → single `recurrenceRule`. **Obsolete:** `timeZones` (IANA IDs only), `excludedRecurrenceRules`, `Link.cid`, `Location.timeZone`/`relativeTo`, `Participant.language`/`locationId`, fractional seconds. **Reserved (taken out for now):** `replyTo`, `sendTo`, `localizations`, iTIP scheduling properties (`scheduleSequence`, `invitedBy`, `requestStatus`, …). `Event`, `Task`, `Group` and `title` stay.

The RFC 8984 property lists below remain valid as the 1.0 reference.

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
| JSCalendar ↔ iCalendar mapping draft (-29) | ✅ AD follow-up | conversion rules for import/export |
| **RFC 10051** Task Extensions to iCalendar (2026-10) | ✅ | richer task status (project management) — no JSCalendar form yet → vendor property `freesynergy.net:taskStatus` |
| RFC 9253 (relationships/links), RFC 7953 (availability) | ✅ | unchanged |
| **JMAP Calendars** (`draft-ietf-jmap-calendars-33`) | ✅ approved, RFC Editor queue (waits for JSCalendar 2.0) | calendar access protocol, built on JSCalendar 2.0 |
| JMAP Sharing, RFC 9670 (2024) | ✅ | sharing calendars |
| JMAP Tasks | ✅ expired 2023, WG plans IESG Mar 2027 | watch |
| **AS2 `Event`, `Invite`, `Accept`, `TentativeAccept`, `Reject`** | ✅ | envelope and invitation log (ADR 0020) |
| FEP-8a8e (events in the fediverse) | ✅ draft | `timezone` property, RSVP via `Join`/`Invite` + `Accept` |
| IANA tzdb **2026f** (2026-10-27); RFC 9557 IXDTF (2024) | ✅ | zones as IANA IDs; IXDTF for our APIs/logs only |
| expired: VPOLL, subscription-upgrade, series, itip-participants | ✅ | — |

## Why JSCalendar and not jCal

jCal is the JSON wrapper **over the iCalendar grammar** (property lists with parameters); JSCalendar is a real object model — for a database JSCalendar is the working representation, iCalendar/jCal are export (position from [standards.md](../standards.md)).

## Open standard points

- Naming conflict: JSCalendar `title` (display name) vs. `name` (JSContact/schema.org/AS2) — the rule is **open decision 1** in [standards.md](../standards.md).
- ~~Read jscalendarbis~~ → done 2026-11-05: we store 2.0 (risk: IESG review may still change details).
- **Gaps → own spec candidates:** delegation and counter-proposals, scheduling state (reserved in 2.0), task status, localization, polls/availability (VPOLL expired), time-zone policy.
