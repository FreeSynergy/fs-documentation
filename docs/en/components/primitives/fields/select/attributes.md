# Select - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string/number/array | - | value |
| `onChange` | function | - | event on change |
| `options` | array[] | - | array of options |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `placeholder` | string | `null` | placeholder text |
| `multiple` | boolean | `false` | multiple choice? |
| `searchable` | boolean | `false` | allow search? |

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

## Option attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | string/number | value |
| `label` | string | label text |

## Auto-complete attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | show suggestions? |
| `suggestions` | array[] | - | array of suggestions |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
