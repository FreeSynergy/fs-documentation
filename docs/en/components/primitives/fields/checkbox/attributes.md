# Checkbox - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `checked` | boolean | `false` | selected? |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `default` | style: `default`, `toggle` |
| `indeterminate` | boolean | `false` | partly selected? |
| `label` | string | - | label text |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcon` | boolean | `false` | show an icon? |
| `labelPosition` | enum | `right` | label position: `left`, `right` |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `checkbox` |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
