# Menu

| Field | Value |
|-------|-------|
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `horizontal`, `vertical`, `dropdown`, `menubar`, `hamburger` |
| **States** | `open`, `expanded`, `selected` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `expand`, `collapse`, `fade-in` |
| **Related** | `context-menu`, `breadcrumb`, `tabs`, `bottom-navigation`, `sidebar` |
| **Role** | `menubar` |
| **Status** | documented |

!!! info "Standardisation"
    The former component `hamburger-menu` became a variant of `menu`:
    `dropdown`, `menubar`, `hamburger` (collapsed mobile menu).

## Description

A menu is an ordered list of menu items that trigger actions or switch views. Items can
have submenus. A menu is the shared superstructure for bars, drop-down menus and the
mobile menu.

## Purpose

- Program-wide navigation in a bar (`menubar`, `horizontal`)
- Offering actions bundled without cluttering the surface (`dropdown`)
- Navigation in the sidebar (`vertical`)
- Navigation on small screens (`hamburger`)

## Variants

| Variant | Description |
|---------|-------------|
| **horizontal** | bar above the content, standard on desktop |
| **vertical** | list next to the content, in sidebars |
| **dropdown** | items only appear when opened |
| **menubar** | several menus side by side, each with a submenu |
| **hamburger** | collapsed menu with an icon, mobile and narrow windows |

## Features

- Submenus with arbitrary depth
- Keyboard navigation (arrow keys, `Esc`, right arrow opens the submenu)
- Groups and separators between items (`separator`)
- Icons and labels individually toggleable
- Opens and closes with an animation; a click outside closes it

## Distinction

- **Do not confuse with** [context-menu](../../overlays/context-menu/): the context menu belongs to
  the clicked object and appears at the pointer position (different ARIA role).
- **Do not confuse with** [tabs](../tabs/): tabs switch within one view, a menu changes addresses
  or carries out actions.
- **Do not confuse with** [bottom-navigation](../bottom-navigation/): fixed main areas on mobile
  devices, always visible.

## Best Practices

- At most seven items per level; group anything more.
- Destructive actions do not belong in the main menu but in the context of the object.
- On mobile devices do not offer the menu twice (hamburger *or* sidebar).
- Menu items start with a verb; use `aria-current` or `activeItem` for the active item.

## See also

- [navigation – overview](../index.md)
- [Base component](../../../primitives/basics/base.md)
