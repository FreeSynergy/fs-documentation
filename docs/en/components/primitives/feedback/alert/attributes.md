# Alert - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `type` | enum | `info` | type: `info`, `success`, `warning`, `error` |
| `title` | string | - | title |
| `message` | string | - | message |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `dismissible` | boolean | `false` | can be closed? |
| `closable` | boolean | `false` | can be closed? |
| `sticky` | boolean | `true` | fixed at the top? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onClose` | function | runs when closing |
| `onAction` | function | runs on the action |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `alert` |

## Action attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `actionLabel` | string | action label |
| `onActionClick` | function | runs when the action is clicked |
| `actionLabel2` | string | second action label |
| `onActionClick2` | function | runs when the second action is clicked |

## Icon attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcon` | boolean | `true` | show an icon? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
