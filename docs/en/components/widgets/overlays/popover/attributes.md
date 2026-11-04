# Popover - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `content` | slot | - | content of the popover (actions, text, form) |
| `open` | boolean | `false` | open? (controlled) |
| `variant` | enum | `inhalt` | `inhalt`, `aktionen`, `formular` |

## Behaviour
| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `trigger` | enum | `click` | `click`, `hover`, `focus` |
| `placement` | enum | `bottom` | `top`, `right`, `bottom`, `left`, `auto` |
| `dismiss` | enum | `beides` | `click-outside`, `escape`, `beides`, `none` |
| `arrow` | boolean | `true` | arrow pointing at the trigger |
| `offset` | number | `8` | distance to the trigger in px |

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `autoFocus` | boolean | `true` | put focus into the popover when opening |
| `returnFocus` | boolean | `true` | return focus to the trigger when closing |
| `closeOnAction` | boolean | `false` | close after an action inside the popover |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onOpen` | function | the popover was opened |
| `onClose` | function | the popover was closed |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `dialog` for `variant="formular"`, otherwise `presentation` |
| – | – | the trigger gets `aria-expanded` and `aria-controls` |
| – | – | the popover gets a label (`aria-label` or a heading) |

## Inherited from

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
