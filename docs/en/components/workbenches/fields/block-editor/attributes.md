# Block Editor - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `value` | object | - | block document |
| `onChange` | function | - | change event |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `edit` | `edit`, `read`, `template` |
| `blockTypes` | array | all | allowed block types |
| `showLayers` | boolean | `true` | show marks |

## Events

| Event | Type | Description |
|---|---|---|
| `onBlockAdd` | function | block inserted |
| `onBlockMove` | function | block moved |
| `onLinkFollow` | function | internal link followed |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `textbox` (multi-line) with `group` per block |
| `aria-label` | string | document name |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
