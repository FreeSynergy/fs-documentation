# Message Status - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `status` | enum | - | `sending`, `sent`, `delivered`, `read`, `failed` |
| `at` | datetime | - | time of the state change, shown in the tooltip |
| `reason` | string | - | error reason for `failed` ⚠️ text source open |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `icon` | `icon`, `icon-text` |
| `showTooltip` | boolean | `true` | show the tooltip on hover/focus |

## Events

| Event | Type | Description |
|---|---|---|
| – | - | no events; display only |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `aria-label` | string | required, e.g. "Delivered" (never only the glyph) |
| `role` | string | `img` or `status`; `aria-live=polite` only for the newest message |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../basics/base.md)
