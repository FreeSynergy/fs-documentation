# Textarea - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `autoResize` | boolean | `true` | auto-resize? |
| `placeholder` | string | `null` | placeholder text |
| `readOnly` | boolean | `false` | read-only mode? |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showLabel` | boolean | `true` | show the label? |
| `rows` | number | `3` | number of rows |
| `maxRows` | number | `10` | maximum rows |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onKeyDown` | function | runs on a key press |
| `onResize` | function | runs on resize |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `textbox` |

## Validation attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `required` | boolean | `false` | required? |
| `error` | string | - | error message |
| `minLength` | number | - | minimum length |
| `maxLength` | number | - | maximum length |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
