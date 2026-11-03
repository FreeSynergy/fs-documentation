# Button Group - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | the buttons or segments of the group |
| `value` | string \| array | `null` | currently chosen value (for `segment`) |
| `selectionMode` | enum | `single` | `single`, `multiple` (only for `segment`) |
| `attached` | boolean | `true` | elements sit against each other with no gap |

## Presentation

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `variant` | enum | `verbund` | `verbund`, `segment`, `split` |
| `orientation` | enum | `horizontal` | `horizontal`, `vertical` |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onSelect` | function | selection changed (only for `segment`) |
| `onAction` | function | action of an element triggered |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `group`; for `segment` additionally `radiogroup` or `tablist` |
| `aria-label` | string | group label when there is no visible title |
| `aria-pressed` | boolean | state of a `verbund` element |
| `aria-checked` | boolean | state of a segment |

## Inherited from

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[base component](../../basics/base.md)
