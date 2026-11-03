# Scroll Area - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `direction` | enum | `vertikal` | `vertikal`, `horizontal`, `beides` |
| `height` | number/string | `auto` | fixed height of the surface |
| `content` | array[] | - | the contents of the area |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `follow` | boolean | `false` | scroll to the end when new content is added |
| `scrollbar` | enum | `automatisch` | `automatisch`, `immer`, `nie` |
| `edges` | boolean | `true` | gradients at the edges |
| `snapTo` | string | `null` | row grid that the scrolling snaps to |
| `keepPosition` | boolean | `true` | keep the position when loading more at the top |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onScroll` | function | position changed |
| `onEndReached` | function | bottom or right end reached (loading more) |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `group` |
| `tabIndex` | number | required (`0`), so the keyboard can move the area |
| `aria-label` | string | name the area, e.g. "Messages" |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`,
`onClick`, `animation`, `gesture`, `aria-*` →
[base component](../../../primitives/basics/base.md)
