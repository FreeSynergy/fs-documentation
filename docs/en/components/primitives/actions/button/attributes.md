# Button - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `secondary` | here with a fixed value range: `primary`, `secondary`, `outline`, `ghost`, `danger`, `link` |
| `type` | enum | `button` | form role: `button`, `submit`, `reset` |
| `loading` | boolean | `false` | loading state, blocks repeated triggering |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `fullWidth` | boolean | `false` | full width of the parent box |
| `preventDoubleClick` | boolean | `true` | ignore a second trigger within 300 ms |
| `group` | string | `null` | group id when the button belongs to a `button-group` |

## Events

Only the inherited events are used: `onClick`, `onFocus`, `onBlur`.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-label` | string | required when `iconOnly = true` |
| `aria-busy` | boolean | set as long as `loading = true` |
| `role` | string | `button` |

## Icon

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `icon` | string | `null` | icon name (see [icon](../../media/icon/)) |
| `iconPosition` | enum | `left` | `left`, `right`, `none` |
| `iconOnly` | boolean | `false` | square button without text; requires `aria-label` |

## Inherited from

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[base component](../../basics/base.md)
