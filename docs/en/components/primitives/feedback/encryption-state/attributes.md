# Encryption State - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `kind` | enum | - | `mls`, `openpgp`, `megolm`, `transport-only`, `none`, `unknown` |
| `guideId` | string | derived from `kind` | library page the click opens ⚠️ ids open |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `icon` | `icon`, `icon-text`, `warning` |
| `showTooltip` | boolean | `true` | show the explanation on hover/focus |

## Events

| Event | Type | Description |
|---|---|---|
| `onActivate` | function | click or Enter; default opens the guide |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `aria-label` | string | required, e.g. "End-to-end encrypted with MLS. Open guide" |
| `role` | string | `link` (it navigates) |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../basics/base.md)
