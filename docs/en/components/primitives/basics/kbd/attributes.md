# Kbd - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `shortcut` | string | - | key or combination, e.g. `Ctrl+S` |
| `keys` | array[] | - | individual key caps of a combination (instead of `key`) |
| `separator` | string | `+` | character between the key caps |
| `active` | boolean | `false` | currently pressed? |

## Events

No events are used; listening to keys belongs to the application.

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| – | – | make the whole element readable (`aria-label="Ctrl plus S"`) |
| – | – | name modifiers in full words, symbols only in addition |

## Inherited from

`id`, `visible`, `size`, `theme`, `rounded`, `state`, `aria-*` →
[base component](../base.md)
