# Description List - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | pairs of `label` and `value` |
| `columns` | number | `2` | columns of the list |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|---------|---------|-------------|
| `variant` | enum | `zweispaltig` | `zweispaltig`, `gestapelt`, `inline` |
| `showEmpty` | boolean | `false` | show empty values as a placeholder |
| `dividers` | boolean | `false` | divider lines between rows |
| `copyable` | boolean | `false` | make the value copyable per row |
| `groups` | array[] | `null` | subheadings for long lists |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onCopy` | function | the value was copied |
| `onValueClick` | function | the value is a reference and was triggered |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `list`, rows with `listitem` |
| `label` | string | heading of the list, e.g. "Details" |
| `aria-label` | string | needed for the copy icon |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
