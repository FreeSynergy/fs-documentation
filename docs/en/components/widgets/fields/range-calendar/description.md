# Range Calendar

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base`, `date-picker` |
| **Variants** | `zwei-monate`, `ein-monat` |
| **States** | `open`, `selecting` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `slide-in` |
| **Related** | `date-picker`, `calendar-view`, `table` |
| **Role** | `dialog` |
| **Status** | documented |

## Description

The range calendar selects one continuous period of time. It shows two months
next to each other so the start can be in the left month and the end in the right month.

## Purpose

- Vacation and absence periods
- Reporting and filter periods ("last 30 days")
- Booking periods for rooms and resources

## Variants

| Variant | Description |
|---------|-------------|
| **zwei-monate** | two months side by side, standard on desktop |
| **ein-monat** | one month, month change by swiping |

## Features

- The selection starts with the first click, the second click sets the end
- Prediction of the range while the pointer moves
- Preset ranges (`presets`): today, 7 days, 30 days, this quarter
- Day counter ("14 days") below the grid

## Distinction

- **Do not confuse with** [date-picker](../date-picker/) with `bereich`: there the
  selection sits on a field, the range calendar is a surface of its own in filter bars.
- **Do not confuse with** [calendar-view](../../data/calendar-view/): the view shows
  appointments, this one selects a period.

## Best Practices

- Set a maximum length when analyses would otherwise become too large.
- Show the selected period as text, not only in the calendar.

## See also

- [Date Picker](../date-picker/)
- [Calendar View](../../data/calendar-view/)
- [Base component](../../../primitives/basics/base.md)
