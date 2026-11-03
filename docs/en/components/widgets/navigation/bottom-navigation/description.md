# Bottom Navigation

| Field | Value |
|-------|-------|
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `Active Icon`, `Text Labels`, `Icon Only` |
| **States** | `aktiv` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `highlight`, `press` |
| **Related** | `tabs`, `menu`, `sidebar`, `toolbar`, `floating-action-button` |
| **Status** | documented |

## Description
Bottom navigation is a navigation at the bottom of the screen, typical for
mobile-first design.

## Purpose

- Main navigation on mobile
- 3–5 main items
- Fast access with the thumb

## Variants

| Variant | Description |
|---------|-------------|
| **Active Icon** | the active item is highlighted |
| **Text Labels** | with text |
| **Icon Only** | icons only (less space) |

!!! info "Classification"
    The navbar that libraries keep separate (`navigation-menu`) is a variant here:
    docked at the top with `placement = "top"`. The horizontal menu bar is
    [`menu`](../menu/) with the variant `menubar`.

## Features

- Maximum 5 main items
- Clear indicator (active item)
- Animation (on switching)
- Accessibility

## Distinction

- **Do not confuse with** [tabs](../tabs/): tabs switch content **inside** one view,
  this bar switches the view itself.
- **Do not confuse with** [sidebar](../sidebar/): the sidebar sits permanently at the edge,
  this bar belongs at the bottom edge of small screens.
- **Do not confuse with** [toolbar](../toolbar/): a toolbar holds actions,
  this bar holds destinations.
- A single main action belongs to the [floating-action-button](../../../primitives/actions/floating-action-button/).

## Best Practices

- Only main functions; put secondary things on the first level of the view, not in the bar.
- At most five items, each in plain text when there is room.
- The active item must stay recognisable, not by colour alone.
- The bar stays above the keyboard and respects the gesture control of the device.

## See also

- [navigation – overview](../index.md)
- [Tabs](../tabs/) — content inside one view
- [Sidebar](../sidebar/) — navigation at the edge
- [Base component](../../../primitives/basics/base.md)
