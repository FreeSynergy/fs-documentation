# Description List

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `zweispaltig`, `gestapelt`, `inline` |
| **States** | `empty` |
| **Gestures** | `tap` |
| **Animations** | `fade-in` |
| **Related** | `table`, `field`, `card` |
| **Role** | `list` |
| **Status** | documented |

## Description

A description list shows pairs of a label and a value — the detail view of a data
record. It is optimised for reading and not for editing.

## Purpose

- Detail view of a contact, an appointment or a task
- Metadata below a document or image
- Comparative blocks in overviews

## Variants

| Variant | Description |
|---------|-------------|
| **zweispaltig** | label on the left, value on the right (desktop) |
| **gestapelt** | label above the value (narrow surface) |
| **inline** | pairs in the text flow, separated by delimiters |

## Features

- Values may contain their own building blocks: [avatar](../avatar/),
  [badge](../../../primitives/feedback/badge/), [link](../../../primitives/basics/link/), [tag](../../../primitives/fields/tags-input/)
- Missing values stay visible as a placeholder or are hidden
- Groups with subheadings for long detail views
- Copying a value through an icon per row

## Distinction

- **Do not confuse with** [table](../table/): a table compares many records
  by the same fields, the description list shows one object.
- **Do not confuse with** [field](../../../primitives/fields/field/): fields edit values,
  this list presents them.

## Best Practices

- Order by readability, not by database columns.
- Hide empty values unless they carry meaning ("no due date").
- At most two columns; more becomes busy.

## See also

- [Table](../table/)
- [Field](../../../primitives/fields/field/)
- [Base component](../../../primitives/basics/base.md)
