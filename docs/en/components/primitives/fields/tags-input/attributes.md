# Tags Input - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `tags` | array[] | - | array of tags |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `maxTags` | number | - | maximum number |
| `placeholder` | string | `null` | placeholder text |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showRemove` | boolean | `true` | show the remove button? |
| `separator` | string | `,` | separator for several tags |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onTagAdd` | function | runs when adding |
| `onTagRemove` | function | runs when removing |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `combobox` |

## Tag attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | string | unique ID |
| `label` | string | label text |
| `value` | string | value |

## Auto-complete attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showSuggestions` | boolean | `false` | show suggestions? |
| `suggestions` | array[] | - | array of suggestions |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
