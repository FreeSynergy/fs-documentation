# Date Input

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `date`, `time`, `datetime` |
| **States** | `open`, `error` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `slide-in` |
| **Related** | `date-picker`, `time-picker`, `range-calendar`, `calendar-view` |
| **Status** | documented |

!!! info "Standardisation"
    The former components `datetime-input` and `time-input` were merged into `date-input`
    as `type` values: `date`, `time`, `datetime`.

## Description
A date input is a date selection field with a calendar.

## Purpose

- Date of birth
- Choosing an appointment
- Giving a date

## Variants

| Variant (`type`) | Description |
|------------------|-------------|
| **date** | date only, a calendar is enough |
| **time** | time only, a time grid instead of a calendar |
| **datetime** | date and time together in one field |

## Features

- Calendar
- Formatting
- Validation

## Distinction

- **Do not confuse with** [date-picker](../../../widgets/fields/date-picker/): the date field also
  accepts typed values and is part of the form; the picker is the pure selection
  overlay without text input.
- **Do not confuse with** [calendar-view](../../../widgets/data/calendar-view/): the calendar view shows
  appointments, it does not select a date.
- **Do not confuse with** [range-calendar](../../../widgets/fields/range-calendar/): there you choose the
  start **and** the end, not a single value.

## Best Practices

- Always display in the local format, store internally in ISO 8601.
- Reject nonsensical values (`min`/`max`), but do not silently correct mistyped text –
  show the error state and leave the text standing.
- For `time`, take the 12/24-hour format from the language, do not hard-set it.
- Offer keyboard operation: arrow keys change the marked segment, PageUp/PageDown the month.

## See also

- [fields – overview](../index.md)
- [Date Picker](../../../widgets/fields/date-picker/) — selection via overlay
- [Time Picker](../../../widgets/fields/time-picker/) — time selection
- [Base component](../../basics/base.md)
