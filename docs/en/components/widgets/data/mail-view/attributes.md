# Mail View - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `mail` | object | - | JMAP `Email` object with body parts |
| `source` | blob | - | original MIME, optional |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `full` | `full`, `compact`, `source` |
| `allowRemote` | boolean | `false` | load remote content for this mail |
| `showHeaders` | enum | `basic` | `basic`, `all` |

## Events

| Event | Type | Description |
|---|---|---|
| `onOpenAttachment` | function | attachment opened/saved |
| `onAddressClick` | function | address selected (reply, add contact) |
| `onAllowRemote` | function | remote content allowed by the person |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `article` |
| `aria-label` | string | "Mail from Anna: subject" |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
