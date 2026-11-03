# Text Input

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `floating label`, `underline` |
| **States** | `filled`, `error` |
| **Gestures** | `tap`, `double-tap`, `long-press` |
| **Animations** | `highlight` |
| **Related** | `textarea`, `search-field`, `number-input`, `field`, `input-group` |
| **Status** | documented |

## Description
A text input is a single-line input field for text.

!!! info "Standardisation"
    The former components `email-input`, `url-input` and `phone-input` were merged into
    this component as `type` values: `text`, `email`, `url`, `phone`, `password`.

## Purpose

- Names
- Addresses
- Messages

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | normal |
| **floating label** | the label floats above |
| **underline** | only an underline |

## Features

- Placeholder
- Error state
- Validation

## Distinction

- **Do not confuse with** [textarea](../textarea/): this field is a single line; paragraphs
  belong in the multi-line field.
- **Do not confuse with** [search-field](../search-field/): a search field triggers something
  on input, this field takes a value.
- **Do not confuse with** [number-input](../number-input/): phone numbers, postcodes and
  account numbers are text, not values to calculate with.
- The label, help text and error line come from [field](../field/) – the field itself is only
  the input line.

## Best Practices

- The label stays visible; the placeholder does not replace it (it disappears while typing).
- Assign autofill answers (`name`, `email`, `tel`), otherwise passwords and addresses
  do not work in password managers.
- Validate only after the field was left, errors in text form directly below the field.
- For `password`, offer a show button and state the requirements up front instead of
  showing them on submit.
- `maxlength` only where needed; then show a counter.

## Types (`type`)

| Type | Description |
|------|-------------|
| `text` | free text (standard) |
| `email` | email address with validation |
| `url` | web address with validation |
| `phone` | phone number with a country code |
| `password` | masked input |

## See also

- [fields – overview](../index.md)
- [Field](../field/) — label, help and error message
- [Textarea](../textarea/) — multi-line
- [Base component](../../basics/base.md)
