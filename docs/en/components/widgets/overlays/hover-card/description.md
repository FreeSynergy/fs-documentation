# Hover Card

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base`, `popover` |
| **Variants** | `profil`, `dokument`, `vorschau` |
| **States** | `open`, `loading` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `fade-in`, `expand` |
| **Related** | `tooltip`, `popover`, `avatar` |
| **Role** | `tooltip` |
| **Status** | documented |

## Description

The preview card shows the most important information about the target of a reference —
without changing the address. It appears when the pointer is over the reference and
disappears again when the pointer moves away.

## Purpose

- Profile preview when a name is tapped in a chat or a list
- Short version of a wiki article or a task when hovering over the reference
- Making the target address of an external reference readable

## Variants

| Variant | Description |
|---------|-------------|
| **profil** | avatar, name, role, last activity |
| **dokument** | title, excerpt, editor, modification date |
| **vorschau** | image or first element of the target |

## Features

- Content is loaded after a delay, not on the first hover
- The card stays open when the pointer moves into the card (the content is operable)
- On touch devices the card appears after a long-press, closes with `Esc` or a tap

## Distinction

- **Do not confuse with** [tooltip](../tooltip/): a tooltip explains a control in one
  sentence, the card shows content.
- **Do not confuse with** [popover](../popover/): a popover contains actions, the card shows
  a summary.

## Best Practices

- At most five pieces of information per card.
- No scrolling inside the card; whoever wants to read everything follows the reference.
- Do not load cards in lists with many rows at the same time.

## See also

- [Tooltip](../tooltip/)
- [Popover](../popover/)
- [Base component](../../../primitives/basics/base.md)
