# Link - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `href` | string | - | target address (required) |
| `external` | boolean | `false` | new tab window, sets `rel="noopener"` |
| `download` | boolean \| string | `false` | download instead of navigation, optionally a file name |

## Presentation

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `standard` | `standard`, `muted`, `icon`, `unterstrichen` |
| `underline` | enum | `hover` | `hover`, `always`, `never` |
| `icon` | string | `null` | icon name |
| `iconPosition` | enum | `right` | `left`, `right` |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onNavigate` | function | before the jump; can cancel it |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `link` |
| `aria-current` | string | `page`/`location` when the target is the current one |
| `aria-label` | string | additional text with an icon ("opens a new window") |

## Inherited from

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `state`,
`tabIndex`, `onFocus`, `onBlur`, `gesture`, `aria-*` →
[base component](../base.md)
