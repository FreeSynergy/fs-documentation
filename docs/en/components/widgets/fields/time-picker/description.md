# Time Picker

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `date-input` |
| **Variants** | `liste`, `ziffernblatt` |
| **States** | `open` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in` |
| **Related** | `date-picker`, `date-input`, `calendar-view` |
| **Role** | `listbox` |
| **Status** | documented |

## Description

The time picker selects a time of day from a list of possible times. It follows the
grid of the program (standard: 15-minute steps) and prevents unsuitable times.

## Purpose

- Start and end of an appointment
- Due dates of tasks
- Time grid in resource planning and room booking

## Variants

| Variant | Description |
|---------|-------------|
| **liste** | list of times, standard |
| **ziffernblatt** | hands on hour and minute, touch |

## Features

- Grid from `step` (5, 10, 15, 30 minutes)
- Free typing with correction onto the grid
- Hide times that are taken, from the context
- 12- or 24-hour display by language

## Distinction

- **Do not confuse with** [date-input](../../../primitives/fields/date-input/) with `type = "time"`:
  there you type, here you select.
- **Do not confuse with** [range-calendar](../range-calendar/): that one selects days,
  not times of day.

## Best Practices

- Match the step size to the use case: appointment 15 minutes, time tracking 6 minutes.
- Always show both directions (start and end) and pull the end along automatically.

## See also

- [Date Picker](../date-picker/)
- [Date Input](../../../primitives/fields/date-input/)
- [Base component](../../../primitives/basics/base.md)
