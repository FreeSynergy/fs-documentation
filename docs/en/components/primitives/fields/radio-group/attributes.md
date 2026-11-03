# Radio Group - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `options` | array[] | - | array of option objects |
| `value` | string/number | - | current value |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `default` | style: `default`, `toggle` |
| `name` | string | - | name for the form |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showIcons` | boolean | `false` | show icons? |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `radiogroup` |

## Option attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `value` | string/number | value |
| `label` | string | label text |
| `icon` | string | icon name |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [base component](../../basics/base.md)
