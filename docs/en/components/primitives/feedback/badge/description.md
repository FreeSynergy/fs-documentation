# Badge

| Field | Value |
|-------|-------|
| **Category** | `feedback` |
| **Inherits from** | `base` |
| **Variants** | `status`, `counter`, `dot`, `outline` |
| **States** | `versteckt` (count 0) |
| **Gestures** | none – not operable |
| **Animations** | `pop-in` (count change) |
| **Related** | `bottom-navigation`, `avatar`, `tags-input`, `alert`, `progress`, `base` |
| **Status** | documented |

## Description

A badge is a small display element for status, counts or category. It is placed
on or beside other elements and is not operable itself.

## Purpose

- Counts on navigation and toolbars (new messages, open tasks)
- Status on entries in lists and tables (open, done, blocked)
- Categorising entries (tags in the display, not in the input)

## Variants

| Variant | Description |
|---------|-------------|
| **status** | single-colour surface with text, e.g. "open" |
| **counter** | a count, e.g. on [bottom-navigation](../../../widgets/navigation/bottom-navigation/) |
| **dot** | only a dot, when the space is minimal |
| **outline** | border instead of fill, for weak hints |

## Features

- Count ceiling shown as "99+"
- Five status colours, readable independently of the theme
- Combinable with [avatar](../../../widgets/data/avatar/) and icons

## Distinction

- **Do not confuse with** [tags-input](../../fields/tags-input/): there tags are
  entered and deleted, a badge only displays.

- **Do not confuse with** [alert](../alert/): a message is a text block, a badge is
  a short marker.

- **Do not confuse with** [avatar](../../../widgets/data/avatar/): an avatar represents a
  person or an object.

## Best Practices

- At most 20 characters; long states as a word, not as colour alone.
- A count must never be the only hint at new content (screen readers need text).
- One status per entry; several statuses as a list below the entry.

## See also

- [Progress](../progress/)
- [Alert](../alert/)
- [Avatar](../../../widgets/data/avatar/)
- [Base component](../../basics/base.md)
