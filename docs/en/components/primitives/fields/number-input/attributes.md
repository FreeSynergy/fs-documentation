# Number Input - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | number | - | value |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `min` | number | - | minimum value |
| `max` | number | - | maximum value |
| `step` | number | `1` | step size |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showStepButtons` | boolean | `true` | show the step buttons? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onKeyDown` | function | runs on a key press |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `spinbutton` |

## Validation attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `required` | boolean | `false` | required? |
| `error` | string | - | error message |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
