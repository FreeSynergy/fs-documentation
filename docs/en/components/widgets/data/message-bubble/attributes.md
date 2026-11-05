# Message Bubble - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `message` | object | - | message object (Note + extensions) |
| `sender` | object | from message | actor shown as name and avatar |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `incoming` | `incoming`, `own`, `compact` |
| `showSender` | boolean | `true` | show name and avatar |
| `selectable` | boolean | `false` | selection mode (multi-select) |

## Events

| Event | Type | Description |
|---|---|---|
| `onReply` | function | reply requested |
| `onReact` | function | reaction toggled (from [reaction-bar](../reaction-bar/)) |
| `onOpenAttachment` | function | attachment opened |
| `onJumpTo` | function | jump to the replied-to message |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `article` |
| `aria-label` | string | "Anna, 10:42, delivered: message text …" |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
