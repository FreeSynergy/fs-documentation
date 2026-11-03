# Label

| Field | Value |
|-------|-------|
| **Category** | `basics` |
| **Inherits from** | `base` |
| **Variants** | `ueber-feld`, `inline`, `versteckt`, `pflicht` |
| **States** | none compared to `base` |
| **Gestures** | `tap` (the label focuses the field) |
| **Animations** | none – caption only |
| **Related** | `field`, `base`, `separator` |
| **Status** | documented |

## Description

A label is the caption of a control or a field. It says what the user enters or
triggers at this place – visibly, or only for screen readers.

## Purpose

- Caption every input field (together with [field](../../fields/field/))
- Name controls that have no text of their own
- Mark access keys

## Variants

| Variant | Description |
|---------|-------------|
| **ueber-feld** | standard: label above the field |
| **inline** | label to the left of the element |
| **versteckt** | visually hidden, still active for screen readers |
| **pflicht** | with a required marking and the text "required" |

## Features

- Linked to the element via `for`/`id`
- Access key (`shortcut`) shown underlined
- The required marking always comes with text, never as an asterisk alone

## Distinction

- **Do not confuse with** [field](../../fields/field/): the wrapper adds the help
  text and the error; the label is only the text.

- **Do not confuse with** `placeholder`: a placeholder is an example, not a
  replacement for a label.

- **Do not confuse with** an image caption: that one describes an image.

## Best Practices

- Short, in the singular, no colon at the end.
- No label as an icon or emoji.
- `versteckt` only when the context replaces the label for sighted users (e.g. a
  search field with an icon) – for screen readers it must stay active.

## See also

- [Field](../../fields/field/)
- [Base component](../base.md)
- [Separator](../separator/)
