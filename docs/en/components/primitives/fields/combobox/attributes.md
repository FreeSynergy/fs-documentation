# Combobox - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `options` | array[] | - | array of options |
| `placeholder` | string | `null` | placeholder text |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcon` | boolean | `false` | show an icon? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onSelect` | function | runs on selection |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `combobox` |

## Auto-complete attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | show suggestions? |
| `suggestions` | array[] | - | array of suggestions |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
