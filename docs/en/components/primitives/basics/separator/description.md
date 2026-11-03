# Separator

| Field | Value |
|-------|-------|
| **Category** | `basics` |
| **Inherits from** | `base` |
| **Variants** | `horizontal`, `vertical`, `mit-beschriftung`, `dekorativ`, `inset` |
| **States** | none – not operable |
| **Gestures** | none – not operable |
| **Animations** | `cross-fade` (switching `vertical` → `horizontal`) |
| **Related** | `card`, `panel`, `label`, `menu`, `toolbar`, `base` |
| **Status** | documented |

## Description

A separator separates content from each other: horizontally between blocks,
vertically between columns or tool groups. It can carry a caption or be purely
decorative.

## Purpose

- Separating groups in menus and toolbars
- Structuring sections in forms and detail views
- An "or" divider between paths of equal value

## Variants

| Variant | Description |
|---------|-------------|
| **horizontal** | line across the full width |
| **vertical** | line between two columns or groups |
| **mit-beschriftung** | text centred in the line (e.g. "or") |
| **dekorativ** | pure appearance without structural effect |
| **inset** | indented, matching lists with an icon column |

## Features

- The gap (`spacing`) to the left/right or above/below is adjustable
- A caption continues the line automatically
- `inset` follows the indent width of the list

## Distinction

- **Do not confuse with** the border of a [card](../../../widgets/containers/card/) or
  [panel](../../../widgets/containers/panel/): their frame belongs to the container.

- **Do not confuse with** spacers: those separate without a line.
- A divider in a menu is a separator with role `separator` in the menu group.

## Best Practices

- In menus, separate groups, not every single entry.
- At most one separator per section; too many look fragmented.
- Decorative lines get `aria-hidden="true"`.
- Keep the caption short ("or", "then").

## See also

- [Label](../label/)
- [Menu](../../../widgets/navigation/menu/)
- [Toolbar](../../../widgets/navigation/toolbar/)
- [Base component](../base.md)
