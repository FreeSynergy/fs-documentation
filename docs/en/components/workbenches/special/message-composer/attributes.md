# Message Composer - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `draft` | object | - | draft with recipients, subject, text, attachments |
| `onSend` | function | - | send requested |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `chat` | `chat`, `mail`, `reply` |
| `editor` | enum | `simple` | `simple` (default), `extended` ⚠️ |
| `encryptionRequired` | boolean | `true` | messages are sent encrypted only (ADR 0018) |

## Events

| Event | Type | Description |
|---|---|---|
| `onChange` | function | draft changed (autosave) |
| `onSend` | function | send requested |
| `onAttach` | function | attachment added |
| `onMention` | function | mention inserted |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `form` |
| `aria-label` | string | "Write message" |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
