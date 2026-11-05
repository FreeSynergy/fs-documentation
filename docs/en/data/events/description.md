# Appointments – description

**What this domain is:** calendar entries, recurring series, participants with invitation status — and **tasks**. Canonical model: **JSCalendar** (RFC 8984, ✅), whose object types `Event` **and** `Task` we manage both here (decision 1).

**What it covers:**

- `Event` with `start`, `duration`, `status`, `freeBusyStatus`, `privacy`
- Series via `recurrenceRules` / `recurrenceOverrides` (rule set like iCalendar `RRULE`)
- Participants (`participants`) with `roles`, `participationStatus`, `scheduleAgent`
- Invitation flow (request/reply/withdraw) via iTIP (RFC 5546, ✅)
- `Task` with `due`, `start`, `percentComplete`, `progress` — also for [projects/](../projects/index.md)
- Alarms/reminders (`alerts`, RFC 9074, ✅), rich-text descriptions (RFC 9073, ✅)

**Differentiation from other domains:**

| Topic | Where it lives | Why |
|-------|----------------|-----|
| Board/list/relationship structure | [projects/](../projects/index.md) | projects only adds structure around the task objects of **this** domain |
| People/organisations of the participants | [contacts/](../contacts/index.md) | a JSCalendar `Participant` is an **appointment copy** with `sendTo`/`email` as the bridge |
| Places | [geodata/](../geodata/index.md) | the appointment only references places (`locations`) |
| Chat arrangements about the invitation | [messages/](../messages/index.md) | iTIP replies are protocol messages, not chat posts |

**No separate `tasks/` domain:** as long as JSCalendar `Task` suffices, tasks live here (see [index.md](index.md)).
