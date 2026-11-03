# Label - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../base.md). The `label` attribute of the base class is the visible
content here.

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `for` | string | - | `id` of the element being captioned |
| `required` | boolean | `false` | required marking with text |
| `hidden` | boolean | `false` | visually hidden, active for screen readers |
| `shortcut` | string | `null` | access key, shown underlined |

## Events

No own events are used; a click on the label affects the linked element.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `label` |
| – | – | linking via `for`/`id` or by nesting |
| – | – | required additionally with text ("required"), not only "*" |

## Inherited from

`id`, `label`, `visible`, `size`, `theme`, `state`, `aria-*` →
[base component](../base.md)
