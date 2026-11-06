# Appointments – technical explanation

## Storage perspective

- **Original + envelope + log (ADR 0020, 0030):** the incoming iTIP/iMIP message, ICS, jCal or ActivityPub object is kept **as received** (with hash and the tzdb version used); envelope = AS2 **`Event`** (`name` ← JSCalendar `title`, `startTime`/`endTime`, `location`); content = **JSCalendar 2.0** JSON.
- **One table `calobj`** for both JSCalendar types (`Event`, `Task`). Extracted columns: `id` (UUIDv7), `uid` (JSCalendar `uid`), `type` (`event`/`task`), `start_min`/`end_min` (index over the time range; `due_min` for tasks), `calendar_id` (which calendar), `sequence`, `updated_at`, `sync_token`.
- **Series:** the master object with `recurrenceRules` is **not** stored expanded; expanding it into individual occurrences happens at query time (respect the iCalendar half-open interval rules). Changes to a single occurrence are stored as a `recurrenceOverrides` entry on the master (✅). JSCalendar 2.0 has a single `recurrenceRule`.

## Keys and links

- Externally: `https://<instance>/events/<uuid>` (decision 3).
- `participants[].email` follows RFC 5322 §3.4.1 (✅) and is the **link to [people/](../people/index.md)**: when rendering, the card is looked up, but the participant fields stay the appointment-binding copy (otherwise the invitation would change when someone moves house).
- `participants[].locationId` ↔ ` Participant.kind = "location"` refers to [geodata/](../geodata/index.md).
- `relatedTo` connects task ↔ event (the task "write the minutes" hangs on an appointment).

## Log mapping (AS2, ✅)

| Action | Activity | iTIP |
|--------|----------|------|
| publish / create | `Create` | PUBLISH |
| invite | `Invite` | REQUEST |
| reply | `Accept` / `TentativeAccept` / `Reject` | REPLY |
| change | `Update` | REQUEST (sequence +1) |
| cancel | `Delete` or status `cancelled` | CANCEL |

## Flow (invitation)

1. Organizer stores the `Event` with `participants` → `Create` in the envelope.
2. iTIP (RFC 5546, ✅): requests to `sendTo` (`imip`/`other`), replies write `participationStatus` (`needs-action` → `accepted`/`declined`/`tentative`/`delegated`).
3. Partial patches via the RFC 8984 path form (`participants/<id>/participationStatus`, ✅) instead of replacing the whole object.
4. Sync for clients via `sync_token` (evidence: RFC 6578, ✅).

## Projections

| Target | Projection |
|--------|------------|
| File exchange | iCalendar (RFC 5545) / jCal (RFC 7265) — export/import |
| Server interoperability | CalDAV + Scheduling (RFC 6638, ✅) |
| [projects/](../projects/index.md) | task objects unchanged, structure references as an extension |
| Webhooks/webhook feed | `Create`/`Update`/`Delete` (decision 2) |

## Open technical points

- **Time zones:** JSCalendar 2.0 allows IANA IDs only (`timeZones` obsolete); we ship tzdb (2026f) and record its version with each original.
- iTIP scheduling properties are only *reserved* in 2.0 → keep them in the original and as vendor properties until a scheduling extension exists (gap).
