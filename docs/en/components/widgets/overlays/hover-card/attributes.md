# Hover Card - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `target` | string | - | id or reference to the target of the preview |
| `content` | object | - | pre-filled fields of the card |
| `placement` | enum | `top` | side of the card: `top`, `bottom`, `left`, `right` |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `openDelay` | number | `300` | delay until opening, in ms |
| `closeDelay` | number | `150` | delay until closing, in ms |
| `pressDuration` | number | `500` | long-press in ms that opens the card on touch |
| `interactive` | boolean | `true` | the card may be entered and operated |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onOpen` | function | the card appears |
| `onClose` | function | the card disappears |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `tooltip` |
| `aria-describedby` | string | id of the card the trigger points at |
| `focusable` | boolean | the card is reachable via keyboard when `interactive` |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
