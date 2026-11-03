# Icon - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | string | - | icon name (e.g. "mdi:home", "fa:search") |
| `shape` | enum | `square` | shape: `circular`, `square`, `rectangular`, `hexagonal`, `pill` |
| `color` | string | `neutral` | colour: `primary`, `secondary`, `success`, `warning`, `error`, `neutral`, hex code |
| `interactive` | boolean | `false` | is the icon clickable? |
| `hoverEffect` | enum | `none` | hover effect: `zoom`, `border`, `shadow`, `none` |

## Behaviour

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Presentation
| Attribute | Type | Description |
|-----------|------|-------------|
| `spin` | boolean | let the icon rotate (e.g. for loading) |
| `pulse` | boolean | let the icon pulsate |
| `animationDuration` | number | duration of the animation in ms |

| Attribute | Type | Description |
|-----------|------|-------------|
| `responsiveSize` | boolean | adjust the size based on the screen size |
| `hideOnMobile` | boolean | hide on mobile |
| `hideOnDesktop` | boolean | hide on desktop |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role (e.g. `button`, `img`) |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
