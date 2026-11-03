# Floating Action Button - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `icon` | string | - | icon name |
| `label` | string | - | button label (for the extended FAB) |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `position` | enum | `bottom-right` | position |
| `showBadge` | boolean | `false` | show a badge? |
| `badgeValue` | string/number | - | badge value |

## Presentation
| Attribute | Type | Default | Description |
|---|---|---|---|
| `size` | enum | `standard` | size: `standard`, `mini`, `extended` |
| Attribute | Type | Default | Description |
|---|---|---|---|
| `animate` | boolean | `true` | enable animations? |
| `rippleEffect` | boolean | `true` | ripple effect? |

| Attribute | Type | Default | Description |
|---|---|---|---|
| `responsive` | boolean | `true` | responsive layout? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `button` |

## Variant attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `color` | enum | `primary` | colour: `primary`, `secondary`, `danger` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
