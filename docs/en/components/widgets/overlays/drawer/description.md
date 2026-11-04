# Drawer

| Field | Value |
|-------|-------|
| **Category** | `overlays` |
| **Inherits from** | `base` |
| **Variants** | `Left Drawer`, `Right Drawer`, `Bottom Drawer`, `Full Drawer` |
| **States** | `open`, `peek` |
| **Gestures** | `swipe`, `tap`, `drag` |
| **Animations** | `slide-in`, `slide-out` |
| **Related** | `sidebar`, `modal`, `split-view`, `menu` |
| **State** | documented |

## Description
A drawer is a side overlay window (collapsible).

## Purpose

- Navigation
- Filters
- Profiles

## Variants

| Variant | Position | Description |
|---------|----------|-------------|
| **Left Drawer** | left | left |
| **Right Drawer** | right | right |
| **Bottom Drawer** | bottom | bottom |
| **Full Drawer** | full | full screen |

!!! info "Classification"
    The `sheet`, kept separate in libraries, is not a component of its own but the bottom
    drawer with reduced height and a grab handle.

## Features

- Header
- Body
- Footer
- Close
- Dismissible

## Distinction

- **Do not confuse with** [sidebar](../../navigation/sidebar/): the sidebar permanently belongs
  to the layout; the drawer comes on demand and covers the content.
- **Do not confuse with** [modal](../modal/): the modal sits in the middle and wants a decision;
  the drawer brings navigation or filters to the edge.
- **Do not confuse with** [popover](../popover/): a popover is small, attached to an element and
  explains exactly that element.
- The bottom drawer with a grab handle is the `sheet` form — a variant, not a component of its own.
- On a wide surface the drawer can stay open permanently; it then behaves like a sidebar but
  remains the same component.

## Best Practices

- Clear content
- Close button
- Accessibility
- Feedback

## See also

- [overlays – overview](../index.md)
- [Sidebar](../../navigation/sidebar/) — permanent sidebar
- [Modal](../modal/) — centred overlay
- [Base component](../../../primitives/basics/base.md)
