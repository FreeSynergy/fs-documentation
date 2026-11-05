# Message List - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `messages` | array[] | - | messages of the context (or a data source with paging) |
| `context` | string | - | conversation id |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `chat` | `chat`, `thread`, `mail` |
| `anchor` | enum | `bottom` | `bottom`, `top` |
| `showSeparators` | boolean | `true` | day and unread separators |
| `showTyping` | boolean | `true` | typing indicator ⚠️ |

## Events

| Event | Type | Description |
|---|---|---|
| `onLoadOlder` | function | top reached, more history needed |
| `onVisible` | function | message became visible (used for read receipts) |
| `onSelect` | function | message selected (multi-select mode) |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `log` (new entries announced politely) ⚠️ or `feed` |
| `aria-label` | string | conversation name |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
