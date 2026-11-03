# Field

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `vertikal`, `horizontal`, `inline` |
| **States** | `error` (error message below the field) |
| **Gestures** | `tap` (the label focuses the field) |
| **Animations** | `expand` |
| **Related** | `label`, `search-field`, `text-input`, `base` |
| **Status** | documented |

## Description

A field is the wrapper around an input field: it joins the label, help text,
error message and required marking into one accessible unit. The actual field
stays a component of its own.

## Purpose

- An accessible frame around every input field
- Showing help text and errors in the right place
- Consistent spacing and label position in forms

## Variants

| Variant | Description |
|---------|-------------|
| **vertikal** | label above the field (standard) |
| **horizontal** | label to the left of the field (dense forms) |
| **inline** | only the label, without help text (e.g. in toolbars) |

## Features

- Error and help text get their own line space (nothing overlaps)
- Required marking with text, not just an asterisk
- Character counter (`counter`) for text fields
- Label and error text linked via `id`/`aria-describedby`

## Distinction

- **Do not confuse with** [label](../../basics/label/): the label is only the
  caption; the field adds help, error and spacing.

- **Do not confuse with** [search-field](../search-field/): that is
  a complete input component, not a wrapper.

- **Do not confuse with** [description-list](../../../widgets/data/description-list/): label-value pairs
  in detail views, without input.
- **Do not confuse with** [input-group](../input-group/): the group sits inside the field next
  to the value, this wrapper outside it (label, help, error).

## Best Practices

- Every field needs a visible label – a `placeholder` does not replace it.
- Name the error message concretely ("the date is in the past").
- Mark errors additionally with an icon and text, not only by colour.
- Help text only when it genuinely helps with decisions.

## See also

- [Label](../../basics/label/)
- [Text Input](../text-input/)
- [Base component](../../basics/base.md)
- [Standardised data](../../../widgets/data/)
