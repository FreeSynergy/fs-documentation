# Avatar - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | string | - | name of the user (for initials) |
| `src` | string | - | URL of the user image |
| `shape` | enum | `circular` | shape: `circular`, `square`, `pill` |
| `variant` | enum | `initials` | content: `image`, `initials`, `icon`, `placeholder` |
| `status` | enum | `offline` | status: `online`, `offline`, `away`, `busy`, `in-meeting` |

## Behaviour

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Presentation

| Attribute | Type | Description |
|-----------|------|-------------|
| `responsiveSize` | boolean | adjust the size to the screen size |
| `hideOnMobile` | boolean | hide on mobile |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `alt` | string | alt text for images |

## Status badge attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `showStatus` | boolean | show the status badge? |
| `statusPosition` | enum | position: `bottom-right`, `top-right`, `bottom-left`, `center` |
| `statusSize` | enum | size of the status badge: `small`, `medium`, `large` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
