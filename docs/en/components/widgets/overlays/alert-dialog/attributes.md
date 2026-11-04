# Alert Dialog - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | string | - | the question as the title |
| `message` | string | - | the effect in one sentence |
| `confirmLabel` | string | `Confirm` | verb of the confirm button |
| `cancelLabel` | string | `Cancel` | verb of the cancel button |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `destructive` | boolean | `false` | destructive variant (error colour) |
| `confirmWord` | string | `null` | word that has to be typed to confirm |
| `busy` | boolean | `false` | request running, actions locked |
| `closeOnEsc` | boolean | `true` | `Esc` = cancel |
| `closeOnOutsideClick` | boolean | `false` | a click outside does not cancel |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onConfirm` | function | confirmed |
| `onCancel` | function | cancelled or `Esc` |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `role` | string | `alertdialog` | - |
| `aria-describedby` | string | - | id of the message text |
| `initialFocus` | enum | `cancel` | button focused first |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
