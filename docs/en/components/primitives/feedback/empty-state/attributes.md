# Empty State - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | string | - | one sentence on why the surface is empty |
| `description` | string | `null` | additional information in a second sentence |
| `icon` | string | `null` | icon name (see [icon](../../media/icon/)) |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `leer` | `leer`, `kein-treffer`, `fehler` |
| `actionLabel` | string | `null` | text of the main action |
| `actionHref` | string | `null` | target of the main action, if it is a link |
| `hint` | string | `null` | short text for a shortcut or help |
| `query` | string | `null` | search term, shown in `kein-treffer` |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onAction` | function | main action triggered |
| `onReset` | function | filter reset |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `role` | string | `status` | - |
| `aria-live` | enum | `polite` | so that changes are announced |
| `icon` | string | - | purely decorative, no `aria-label` needed |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[base component](../../basics/base.md)
