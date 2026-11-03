# Range Calendar - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `from` | date | `null` | start of the period |
| `to` | date | `null` | end of the period |
| `presets` | array[] | `[7, 30, quarter]` | preset ranges |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|---------|---------|-------------|
| `months` | number | `2` | visible months |
| `minRange` | number | `1` | shortest length in days |
| `maxRange` | number | `365` | longest length in days |
| `min` | date | `null` | earliest day |
| `max` | date | `null` | latest day |
| `showCount` | boolean | `true` | show the number of days |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onChange` | function | period changed |
| `onPreset` | function | a preset range was chosen |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `dialog` with `grid` |
| `aria-selected` | boolean | days inside the period |
| `label` | string | mandatory, e.g. "Period" |

## Inherited from

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
