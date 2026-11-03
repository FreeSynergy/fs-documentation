# Date Picker - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

The picker hangs on a [date-input](../../../primitives/fields/date-input/). Typing in the field opens the
overlay; the selected date then sits in the field.

When `sources` is set, the picker is additionally a small calendar: when opening and
when changing the month it requests the entries of the visible window, marks
days that are taken and shows the day list for the selected day. From there entries
are opened, created, changed, dragged onto another day or deleted — the
result still stays a date (or a range) that lands in the field.

## Examples

### Selecting a due date (without a connection)

```jsx
<DatePicker label="Due date" value={due} min={today} onChange={setDue} />
```

### Period for a report

```jsx
<DatePicker variant="bereich" rangeStart={from} rangeEnd={to} closeOnSelect={false} />
```

### Taken days in the team calendar

```jsx
<DatePicker label="Appointment" value={day}
            sources={[events]} scopeId={teamCalendar}
            showEntries="beides" onEntryClick={openEvent} />
```

### Due dates of tasks

```jsx
<DatePicker label="Due date" value={due}
            sources={[tasks]} dateField="dueAt" filter="status:eq:open"
            movable onEntryMove={(task, day) => reschedule(task, day)} />
```

### Everything with a date from one project

Each source may count a different date field; the setting per source overrides
`dateField`.

```jsx
<DatePicker label="Cut-off date" value={at} entryLimit={3}
            sources={[{resource: events, dateField: "start"},
                      {resource: tasks, dateField: "dueAt"},
                      {resource: documents, dateField: "createdAt"}]} />
```

### Create an entry directly in the overlay

```jsx
<DatePicker label="Appointment" value={day} sources={[events]}
            creatable createFields={[title, start, end]}
            onEntryCreate={(data) => client.events.create(data)} />
```

### Move an entry by dragging

```jsx
<DatePicker label="Appointment" value={day} sources={[events]} movable
            onEntryMove={(appointment, day) => client.events.update(appointment.id, {start: day, end: day})} />
```

## Loading and writing data

| Operation | Request per [data API](../../../../data/api.md) |
|-----------|------------------------------------------------|
| Overlay opens | `GET /api/v1/events?filter=start:gte:2026-11-01;start:lte:2026-12-31&fields=id,title,start,end,type&limit=100` |
| Month change | the same request for the new window, triggered through `onMonthChange` |
| Data set changes | delta query with `updatedSince`, or the webhooks `event.created`, `task.updated` |
| Quick entry | `POST /api/v1/events` with an `Idempotency-Key` |
| Drag onto another day | `PATCH /api/v1/events/{id}` with a new `start` and `end`, `If-Match` from the ETag |
| Delete from the list | `DELETE /api/v1/events/{id}` (soft delete) |

A loaded slice looks per entry as described in
[standard fields](../../../../data/felder.md):

```json
{
  "id": "event_01HZY9",
  "title": "Review",
  "start": "2026-11-14T15:00:00+01:00",
  "end": "2026-11-14T16:00:00+01:00",
  "allDay": false,
  "timezone": "Europe/Berlin",
  "type": "event"
}
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Appointment in a task | `einzeln`, `quickPick` with today and tomorrow |
| Reporting period | `bereich`, `closeOnSelect = false` |
| Only the future allowed | `min = heute` |
| Finding an appointment in the team | `sources = [events]`, `showEntries = beides`, `creatable = false` |
| Rescheduling due dates | `sources = [tasks]`, `dateField = dueAt`, `movable = true` |
| Chronicle of a project | several sources each with its own `dateField`, `entryLimit = 3` |
| Plain date field without context | `sources = []` — the picker stays an empty calendar |
