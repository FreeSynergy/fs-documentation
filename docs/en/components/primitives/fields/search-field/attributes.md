# Search Field - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value (search term) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `placeholder` | string | `null` | placeholder text |
| `showClear` | boolean | `true` | show the clear button? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcon` | boolean | `true` | show an icon? |
| `icon` | string | `search` | icon name |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onSubmit` | function | runs on submit |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `search` |

## Auto-complete attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showSuggestions` | boolean | `false` | show suggestions? |
| `suggestions` | array[] | - | array of suggestions |

## Filter attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `showFilters` | boolean | `false` | show the filters? |
| `filters` | array[] | - | array of filters |
| `onFilterChange` | function | - | runs when a filter changes |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
