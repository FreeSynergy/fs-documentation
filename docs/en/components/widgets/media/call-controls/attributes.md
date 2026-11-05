# Call Controls - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `session` | object | - | call session (state, devices) |
| `controls` | array | all | which controls are shown |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `bar` | `bar`, `compact` |
| `muted` | boolean | `false` | microphone muted |
| `cameraOn` | boolean | `true` | camera on |

## Events

| Event | Type | Description |
|---|---|---|
| `onToggleMic` | function | microphone toggled |
| `onToggleCamera` | function | camera toggled |
| `onShareScreen` | function | screen sharing started/stopped |
| `onHangUp` | function | call ended |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `toolbar` |
| `aria-pressed` | boolean | on toggles |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
