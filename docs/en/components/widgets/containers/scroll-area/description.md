# Scroll Area

| Field | Value |
|-------|-------|
| **Category** | `containers` |
| **Inherits from** | `base` |
| **Variants** | `vertikal`, `horizontal`, `beides` |
| **States** | `atTop`, `atBottom` |
| **Gestures** | `swipe`, `drag` |
| **Animations** | `fade-in` |
| **Related** | `split-view`, `list-view`, `sidebar` |
| **Role** | `group` |
| **Status** | documented |

## Description

A scroll area is a surface with a fixed measure whose content scrolls. It adds
scrollbar indicators, edge gradients and keyboard navigation, and holds content
at a constant height.

## Purpose

- Chats and histories at a fixed height inside a column
- Long lists inside a card or a panel
- Horizontal areas such as toolbars or rows of images

## Variants

| Variant | Description |
|---------|-------------|
| **vertikal** | height limited only, standard |
| **horizontal** | width limited only |
| **beides** | surface with both scroll directions |

## Features

- An edge gradient shows that there is more
- Scrolling follows the content automatically (`follow`), e.g. for new messages
- The scrollbar fades in while scrolling and fades out at rest
- Keyboard: `arrow keys`, `Page Up/Down`, `Home`/`End`

## Distinction

- **Do not confuse with** [list-view](../../data/list-view/): the list arranges content,
  the scroll area only governs the scrolling.
- **Do not confuse with** `overflow: auto`: no gradients, no indicators,
  no follow behaviour.

## Best Practices

- At most two independently scrolling areas per screen area.
- Keep the scroll position when loading more at the top, otherwise the content jumps.
- Respect reduced motion: no smooth following with `respectReducedMotion`.

## See also

- [Split View](../split-view/)
- [List View](../../data/list-view/)
- [Base component](../../../primitives/basics/base.md)
