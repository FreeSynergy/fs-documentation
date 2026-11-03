# Toast - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `type` | enum | `info` | type: `info`, `success`, `warning`, `error` |
| `title` | string | - | title |
| `message` | string | - | message |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `autoDismiss` | boolean | `true` | close automatically? |
| `dismissDelay` | number | `3000` | delay in ms |
| `closable` | boolean | `true` | can be closed? |

## Presentation
| Attribute | Type | Default | Description |
|---|---|---|---|
| `position` | enum | `top-right` | position: `top-right`, `bottom-right`, `top-left`, `bottom-left`, `center` |

| Attribute | Type | Default | Description |
|---|---|---|---|
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `300` | duration in ms |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onClose` | function | runs when closing |
| `onDismiss` | function | runs on auto-close |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `alert` |

## Action attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `actionLabel` | string | action label |
| `onActionClick` | function | runs when the action is clicked |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
