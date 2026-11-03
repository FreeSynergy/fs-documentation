# Rating - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | number | - | value (rating) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `readonly` | boolean | `false` | display only? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `max` | number | `5` | maximum rating |
| `showCount` | boolean | `false` | show the count? |
| `count` | number | - | number of ratings |
| `decimal` | boolean | `false` | decimal places? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `rating` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
