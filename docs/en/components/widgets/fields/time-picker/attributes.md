# Time Picker - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | time | `null` | selected time of day |
| `step` | number | `15` | grid in minutes |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|---------|---------|-------------|
| `min` | time | `00:00` | earliest time |
| `max` | time | `23:59` | latest time |
| `hour12` | boolean | `false` | 12-hour display |
| `blocked` | array[] | `[]` | times that cannot be selected |
| `freeInput` | boolean | `true` | allow typing, correct onto the grid |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onChange` | function | time of day changed |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `listbox`, entries `option` |
| `aria-selected` | boolean | selected time |
| `label` | string | mandatory, e.g. "Start" |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
