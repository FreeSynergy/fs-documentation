# Color Input - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | string | - | value (colour) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `placeholder` | string | `null` | placeholder text |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcon` | boolean | `true` | show an icon? |
| `icon` | string | `palette` | icon name |
| `formats` | array[] | `['hex', 'rgb', 'hsl']` | colour formats |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onOpen` | function | runs when the picker opens |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `color` |

## Picker attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showAlpha` | boolean | `false` | show the alpha channel? |
| `showPalette` | boolean | `true` | show the colour palette? |
| `showSpectrum` | boolean | `true` | show the colour spectrum? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
