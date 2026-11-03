# Panel

| Field | Value |
|-------|-------|
| **Category** | `containers` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `einklappbar`, `verschiebbar`, `filter` |
| **States** | `geöffnet`, `geschlossen` |
| **Gestures** | `tap`, `drag`, `long-press` |
| **Animations** | `expand`, `collapse`, `reorder` |
| **Related** | `card`, `split-view`, `scroll-area`, `accordion`, `dashboard` |
| **Status** | documented |

## Description
A panel is a large container with a header, content and footer. It differs from
a card by its larger size and its use in layouts.

## Purpose

- Large content blocks
- Layout containers
- Filter panel
- Dashboard widget

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | standard panel with a header |
| **einklappbar** | the header collapses and expands the content |
| **verschiebbar** | can be moved |
| **filter** | with filter options |

## Features

- Collapsible (collapse/expand)
- Draggable (moving)
- Resize (changing the size)
- Custom header

## Distinction

- **Do not confuse with** [card](../card/): the card shows one content with a title and actions,
  the panel gathers controls or a work area (plan section 4, row 16 —
  both stay, with a common container base).
- **Do not confuse with** [split-view](../split-view/): the split view breaks the surface
  into areas, the panel is one of those areas.
- **Do not confuse with** [drawer](../../overlays/drawer/) or [modal](../../overlays/modal/):
  a panel stays in the layout and covers nothing.
- **Do not confuse with** [accordion](../accordion/): the accordion is a group of
  headers, the panel a single area.

## Best Practices

- The header names the area, not the action.
- Keep the size and inner spacing consistent within one application.
- Remember the state of a collapsible panel, set `aria-expanded`.
- The panel body scrolls itself, do not let the page scroll along.

## Structure

```
┌─────────────────────────────────────────┐
│ Header / title                          │  ← header
├─────────────────────────────────────────┤
│                                         │
│   Content                               │
│   ...                                   │
│                                         │  ← body
├─────────────────────────────────────────┤
│ Footer / actions                        │  ← footer
└─────────────────────────────────────────┘
```

## See also

- [containers – overview](../index.md)
- [Base component](../../../primitives/basics/base.md)
