# Date Picker

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `date-input` |
| **Variants** | `einzeln`, `bereich`, `wiederkehrend` |
| **States** | `open`, `outOfRange`, `loading` |
| **Gestures** | `tap`, `swipe`, `drag`, `long-press` |
| **Animations** | `fade-in`, `slide-in` |
| **Related** | `date-input`, `time-picker`, `range-calendar`, `calendar-view`, `list-view` |
| **Role** | `dialog` |
| **Status** | documented |

## Description

The date picker opens a calendar overlay in which a date or a range is
selected. It complements the [date-input](../../../primitives/fields/date-input/), which allows
entering by typing.

Beyond pure selection, the picker is **connected to the data**: it reads the
standardised data set (see [Standardized Data](../../data/)) and shows in the days the
entries that fall on that day — appointments, tasks with a due date, documents with a
creation date. The selected day opens the day list, and through the quick entry entries
are created there directly or moved by dragging onto another day. Anything that has a
date can be shown, selected and written; which date is meant is decided by `dateField`.

## Purpose

- Selecting appointment, task and due dates
- Selecting ranges (from/to), for instance for reports
- Setting repetitions (weekly, monthly)
- Seeing what is already planned for a day before selecting it
- Creating, changing or moving an appointment or task directly in the overlay
  without leaving the form

## Variants

| Variant | Description |
|---------|-------------|
| **einzeln** | one date |
| **bereich** | start and end, marked in between |
| **wiederkehrend** | date plus rules for repetition |

## Features

- Month, year and decade view in one overlay
- Quick selection: today, tomorrow, next week
- Free typing in the overlay field stays possible
- Days with entries are visibly marked: one dot per entry, colour by type, counter when there
  are many
- Day list below the grid: title, time and status of the entries of the selected day
- Quick entry: a title and a time are enough, save without leaving the overlay
- Dragging an entry onto another day moves it (write permission assumed)
- Series (`recurrenceRule` after RFC 5545) are shown resolved and marked as a series

## Distinction

- **Do not confuse with** [date-input](../../../primitives/fields/date-input/): the field accepts typed input,
  the picker shows the calendar.
- **Do not confuse with** [calendar-view](../../data/calendar-view/): both show
  entries on days — the core is the same, the size is not. The picker stays
  a selection overlay that only shows entries **compactly** (dots, day list,
  quick entry) and delivers a date as its result; the view is the planning tool
  with week and day grid, timeline and wrapping of periods. Menu, views,
  export and settings belong to neither of them — that is what the
  calendar app brings, which takes both building blocks.
- **Do not confuse with** [list-view](../../data/list-view/): a list shows
  entries without a focus on dates, the day list of the picker hangs on the selected day.

## Best Practices

- Set the preset to the date that is most likely.
- Always set the allowed range limits (`min`, `max`) when the domain knows them.
- On mobile devices offer the list of upcoming dates, not just the grid.
- Never load the whole data set: only the window with `loadWindow`, at most
  `entryLimit` entries per day, the rest as "+ n more".
- Times with timezone offsets, all-day dates with `allDay = true`
  (see [standard fields](../../../../data/fields.md)).
- Only switch on `creatable` and `movable` when the write permission exists; otherwise the
  picker stays read-only and the day list is pure information.
- Without context (`sources` empty) the picker behaves like a plain calendar —
  not every date field needs a connection.

## Data connection

The picker reads through the unified data pattern
([data API](../../../../data/api.md)) and writes back by the same pattern
(`POST` to create, `PATCH` when moving). What gets bound is one model plus the field
that supplies the day — which is why the picker is not limited to appointments:

| Model | Date field (`dateField`) | Display on the day |
|-------|--------------------------|--------------------|
| `Event` | `start`, end in `end` | dot filled, colour by calendar |
| `Task` | `dueAt` | dot with a tick when `status = done` |
| `Document` | `createdAt`, `updatedAt` | dash at the lower edge of the day |
| `Message` | `createdAt` | collective counter per day |
| `Revision` | `createdAt` | only on explicit request |
| own model | any `date` or `datetime` field | like `Event`, the label comes from `type` |

Only the visible window plus `loadWindow` months is ever loaded; changes to the data set
follow the window through `updatedSince` or webhooks
(`event.created`, `task.updated`). The permissions of the record apply: what the
person may see decides the source — blocked entries are missing from grid and counter
entirely.

## See also

- [Date Input](../../../primitives/fields/date-input/)
- [Range Calendar](../range-calendar/)
- [Calendar View](../../data/calendar-view/)
- [Appointments — date domain](../../../../data/events/)
- [Standard fields](../../../../data/fields.md)
- [Data API](../../../../data/api.md)
- [Base component](../../../primitives/basics/base.md)
