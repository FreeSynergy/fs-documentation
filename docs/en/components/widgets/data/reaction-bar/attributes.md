# Reaction Bar - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `reactions` | array[] | - | list of `{emoji, count, own}` |
| `messageId` | string | - | message the reactions belong to |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `inline` | `inline`, `compact` |
| `maxVisible` | number | `8` | chips before the overflow chip |
| `canReact` | boolean | `true` | write permission |

## Events

| Event | Type | Description |
|---|---|---|
| `onToggle` | function | own reaction toggled (emoji) |
| `onAdd` | function | "+" activated, open the picker |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `group` |
| `aria-pressed` | boolean | on each chip: own reaction active |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
