# Calendar View

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `Monthly View`, `Weekly View`, `Daily View`, `Agenda View` |
| **States** | `dragging`, `leer` |
| **Gestures** | `tap`, `drag`, `swipe`, `long-press`, `pinch` |
| **Animations** | `slide-in`, `expand` |
| **Related** | `list-view`, `timeline`, `date-picker`, `range-calendar` |
| **Status** | documented |

## Description
A calendar view shows appointments in a calendar.

## Purpose

- Showing appointments
- Calendars
- Planning
- Scheduling

## Variants

| Variant | Description |
|---------|-------------|
| **Monthly View** | month view |
| **Weekly View** | week view |
| **Daily View** | day view |
| **Agenda View** | list view |

## Features

- Navigation (forward/back)
- Drag and drop (moving appointments)
- Resize (changing the length of an appointment)
- Showing events

## Distinction

- **Do not confuse with** [date-picker](../../fields/date-picker/): this view shows appointments,
  it does not pick a date. The core on display is the same — grid, markers, entries by
  type and colour — the view is only larger and has room for periods of time.
- **No menu, no export.** The view is a widget (level 2). A calendar app
  (level 4) embeds it in a whole screen and brings the menu, views, editing, export
  and output formats with it — the view itself stays the same, it is not
  built a second time.
- **Do not confuse with** [range-calendar](../../fields/range-calendar/): there you select a period
  as a filter, here the period is the view.
- **Do not confuse with** [timeline](../timeline/): a timeline explains sequences,
  the calendar shows occupancy.
- Anyone who does not need a time scale is better served by [list-view](../list-view/).

## Best Practices

- Mark today's date and the current time consistently.
- Split overlapping appointments sideways, never stack them.
- Let a `drag` snap to a grid (15 minutes) and offer undo.
- At most six category colours; above that the view is no longer readable.
- On narrow screens switch to the agenda view automatically.

## See also

- [data – overview](../index.md)
- [List View](../list-view/) — agenda without a time scale
- [Range Calendar](../../fields/range-calendar/) — selecting a period
- [Base component](../../../primitives/basics/base.md)
