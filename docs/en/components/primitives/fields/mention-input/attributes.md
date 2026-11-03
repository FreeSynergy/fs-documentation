# Mention Input - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value (text with mentions) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `users` | array[] | - | array of users |
| `placeholder` | string | `null` | placeholder text |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showSelectedCount` | boolean | `false` | show the number selected? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onMentionSelect` | function | runs on mention selection |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `combobox` |

## Auto-complete attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | show suggestions? |
| `trigger` | string | `@` | trigger character |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
