# Rule Editor - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `rules` | array[] | - | list of rules (condition set, actions, enabled) |
| `sieve` | string | - | Sieve source; alternative to `rules` |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `list` | `list`, `simple` |
| `vocabulary` | object | mail | available conditions and actions |
| `allowExpert` | boolean | `false` | show raw Sieve |

## Events

| Event | Type | Description |
|---|---|---|
| `onChange` | function | rule set changed |
| `onTest` | function | test run requested |
| `onSave` | function | valid rule set confirmed |

Gestures (swipe, long-press, drag) are **not** attributes of this component: they are added
by the frontend (ADR 0037).

## Accessibility

| Attribute | Type | Description |
|---|---|---|
| `role` | string | `group` per rule, `list` for the set |
| `aria-label` | string | "Rule 2: if sender contains news@" |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Base component](../../../primitives/basics/base.md)
