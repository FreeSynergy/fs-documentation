# Input Group - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../basics/base.md). The built-in field brings its own attributes
([text-input](../text-input/)).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `field` | component | - | the field in the group (`text-input`, `number-input`, …) |
| `prefix` | string | `""` | prefix on the left (unit, sign, protocol) |
| `suffix` | string | `""` | suffix on the right (unit, status) |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `action` | string | `""` | label of the attached button; empty = no action |
| `prefixOptions` | array | - | options for the prefix as a selection (e.g. country code) |
| `attach` | boolean | `true` | join the surfaces (`false` = with a gap) |
| `actionOnEnter` | boolean | `true` | `Enter` in the field triggers the action |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onAction` | function | attached button used |
| `onPrefixChange` | function | prefix selection changed |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `group`; the field keeps its own role |
| `aria-label` | string | for the group when prefix and caption belong together |
| `aria-hidden` | boolean | prefix text when it already stands in the field's `aria-label` |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `variant`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[base component](../../basics/base.md)
