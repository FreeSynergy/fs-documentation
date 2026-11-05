# HTML View - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `html` | string | - | foreign HTML source |
| `baseParts` | array | - | `cid:` parts that may be shown |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `sanitised` | `sanitised`, `remote-allowed` |
| `allowRemote` | boolean | `false` | load remote content |

## Events

| Event | Type | Description |
|---|---|---|
| `onLinkClick` | function | link activated; the host decides |
| `onAllowRemote` | function | remote content allowed |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `document` |
| `aria-label` | string | "Message content" |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
