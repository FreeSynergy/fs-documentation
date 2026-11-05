# Modal

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `Small`, `Medium`, `Large`, `Fullscreen` |
| **States** | `open`, `dirty` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `pop-in`, `slide-out` |
| **Related** | `alert-dialog`, `drawer`, `popover`, `wizard` |
| **Status** | documented |

## Description
A modal is an overlay window with focus on content.

## Purpose

- Confirmations
- Forms
- Editing dialogs

## Variants

| Variant | Size | Description |
|---------|------|-------------|
| **Small** | - | forms, confirmations |
| **Medium** | - | editing dialogs |
| **Large** | - | complete views |
| **Fullscreen** | - | complete view |

## Features

- Header
- Body
- Footer
- Close
- Dismissible

## Distinction

- **Do not confuse with** [alert-dialog](../alert-dialog/): the alert dialog asks for a
  decision, has hardly any content and cannot be closed by a click outside; the modal carries
  content or a form.
- **Do not confuse with** [drawer](../drawer/): the drawer comes from an edge and brings
  navigation; the modal sits centred and demands attention.
- **Do not confuse with** [popover](../popover/): a popover does not lock the rest of the page.
- **Do not confuse with** [wizard](../../containers/wizard/): several steps in a row are a
  wizard — even when it runs inside a modal.
- Locked focus and blocked background scroll are part of this component, not an extra library.

## Best Practices

- Clear content
- Close button
- Accessibility
- Feedback

## See also

- [overlays – overview](../index.md)
- [Alert Dialog](../alert-dialog/) — confirmation without content
- [Drawer](../drawer/) — overlay at the edge
- [Base component](../../../primitives/basics/base.md)
