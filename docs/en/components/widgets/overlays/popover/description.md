# Popover

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `inhalt`, `aktionen`, `formular` |
| **States** | `open` |
| **Gestures** | `tap` |
| **Animations** | `expand`, `fade-in` |
| **Related** | `tooltip`, `modal`, `select`, `context-menu`, `base` |
| **Status** | documented |

## Description

A popover is a small overlay with interactive content: actions, a preview or a short
form. It is docked to a trigger element but – unlike a modal – does not take over the
whole screen.

## Purpose

- Secondary actions on an entry (more-menu with buttons)
- Quick input without changing the page (setting a date, assigning a label)
- Detailed preview of an entry (short version before opening it)

## Variants

| Variant | Description |
|---------|-------------|
| **inhalt** | text, images or preview, no form input |
| **aktionen** | list of actions (distinction from context-menu: fixed trigger) |
| **formular** | small form, e.g. setting a date or colour |

## Features

- Focus moves into the popover and returns to the trigger after closing
- Closes on a click outside, Escape, or an action inside the popover
- Docking position as in the [tooltip](../tooltip/)

## Distinction

- **Do not confuse with** [tooltip](../tooltip/): tooltip = text only, never interactive.

- **Do not confuse with** [modal](../modal/): a modal blocks and is centred; a popover stays
  at the trigger and leaves the rest operable.

- **Do not confuse with** [dropdown](../../../primitives/fields/select/): a dropdown picks a
  value from a list, a popover carries arbitrary content.

- **Do not confuse with** [context-menu](../context-menu/): the context menu follows the
  right-click, a popover follows a fixed trigger.

## Best Practices

- Escape and a click outside must close it; focus returns to the trigger.
- `aria-expanded` on the trigger is mandatory.
- No replacement for a full dialog: use a `modal` for more than ~5 input fields.

## See also

- [Tooltip](../tooltip/)
- [Modal](../modal/)
- [Context Menu](../context-menu/)
- [Base component](../../../primitives/basics/base.md)
