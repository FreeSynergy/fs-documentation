# Slider - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | number | - | value |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `min` | number | `0` | minimum value |
| `max` | number | `100` | maximum value |
| `step` | number | `1` | step size |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showLabels` | boolean | `false` | show labels? |
| `showValue` | boolean | `true` | show the value? |
| `vertical` | boolean | `false` | vertical? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onChangeEnd` | function | runs at the end of a change |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `slider` |

## Range attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `range` | boolean | `false` | range selection? |
| `minRange` | number | - | minimum range size |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
