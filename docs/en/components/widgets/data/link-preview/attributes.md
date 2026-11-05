# Link Preview - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `url` | string | - | link target |
| `title` | string | - | title provided by the sender |
| `description` | string | - | short text |
| `image` | blob | - | attached image, never remote |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `card` | `card`, `compact` |
| `confirmOpen` | boolean | `true` | ask before opening external targets |

## Events

| Event | Type | Description |
|---|---|---|
| `onOpen` | function | activated; the host decides how to open |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `link` |
| `aria-label` | string | "Link: title, example.org" |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
