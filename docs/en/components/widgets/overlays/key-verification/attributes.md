# Key Verification - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `subject` | object | - | person or device being verified |
| `fingerprint` | string | - | fingerprint or credential digest |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `fingerprint` | `fingerprint`, `qr`, `device-list` |
| `open` | boolean | `false` | visibility (overlay) |

## Events

| Event | Type | Description |
|---|---|---|
| `onConfirm` | function | person confirms a match |
| `onReject` | function | person reports a mismatch |
| `onClose` | function | dialog closed |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `dialog` |
| `aria-describedby` | string | explanation of what confirming means |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
