# Number Input

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `einfach`, `stepper`, `formatiert` |
| **States** | `error` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `press`, `highlight` |
| **Related** | `slider`, `rating`, `text-input`, `field` |
| **Status** | documented |

## Description
A number input is an input field for numbers.

## Purpose

- Giving an age
- Quantities
- Prices
- Values

## Variants

| Variant | Description |
|---------|-------------|
| **einfach** | number field only, keyboard without step buttons |
| **stepper** | field with `−` and `+` beside it, holding accelerates |
| **formatiert** | value with a unit and local grouping (`1,250 g`) |

## Features

- Min/max values
- Step size
- Validation
- Auto-formatting

## Distinction

- **Do not confuse with** [slider](../slider/): the slider chooses roughly and shows the value
  range, this field needs the exact value. Both share the value logic (`min`, `max`, `step`).
- **Do not confuse with** [text-input](../text-input/): sequences of digits that are not
  numbers (phone number, postcode, account number) belong in `text-input` with `type = text`.
- **Do not confuse with** [rating](../rating/): a rating is a scale, not number input.

## Best Practices

- Always set `min`, `max` and `step`; show values outside them as an error, do not
  silently clamp.
- Only use grouping characters in the display, the bare number is what gets stored.
- Put the unit as a fixed suffix outside the value, so it can be converted.
- For amounts, set the currency and precision instead of letting people type freely.

## See also

- [fields – overview](../index.md)
- [Slider](../slider/) — sliding value choice
- [Text Input](../text-input/) — strings instead of numbers
- [Base component](../../basics/base.md)
