# Appointments – technical explanation

## Storage perspective

- **One table `calobj`** for both JSCalendar types (`Event`, `Task`): canonical payload = JSCalendar JSON (decision 4). Extracted columns: `id` (ULID), `uid` (JSCalendar `uid`), `type` (`event`/`task`), `start_min`/`end_min` (index over the time range; `due_min` for tasks), `calendar_id` (which calendar), `sequence`, `updated_at`, `sync_token`.
- **Series:** the master object with `recurrenceRules` is **not** stored expanded; expanding it into individual occurrences happens at query time (respect the iCalendar half-open interval rules). Changes to a single occurrence are stored as a `recurrenceOverrides` entry on the master (RFC 8984, ✅).

## Keys and links

- Externally: `https://<instance>/events/<ulid>` (decision 3).
- `participants[].email` follows RFC 5322 §3.4.1 (✅) and is the **link to [contacts/](../contacts/index.md)**: when rendering, the card is looked up, but the participant fields stay the appointment-binding copy (otherwise the invitation would change when someone moves house).
- `participants[].locationId` ↔ ` Participant.kind = "location"` refers to [geodata/](../geodata/index.md).
- `relatedTo` connects task ↔ event (the task "write the minutes" hangs on an appointment).

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

- **Time zone representation:** `timeZone`/`timeZones` exist (✅); which IANA version we ship is an operational, not a data decision.
- Watch the revision `draft-ietf-calext-jscalendarbis` (✅ found, content unread): it will obsolete RFC 8984.
