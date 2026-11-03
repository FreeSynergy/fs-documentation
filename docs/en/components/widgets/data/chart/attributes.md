# Chart - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | array[] | - | array of data |
| `type` | string | `line` | type: `line`, `bar`, `pie`, `doughnut`, `scatter`, `radar` |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `interactive` | boolean | `true` | interactive? |

## Presentation
| Attribute | Type | Default | Description |
|---|---|---|---|
| `showLegend` | boolean | `true` | show the legend? |
| `showTooltip` | boolean | `true` | show a tooltip? |
| `showGrid` | boolean | `true` | show the grid? |

| Attribute | Type | Default | Description |
|---|---|---|---|
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `1000` | duration in ms |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onHover` | function | runs on hover |
| `onDataChange` | function | runs when the data changes |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `img` |

## Data attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `labels` | array[] | labels |
| `values` | array[] | values |
| `colors` | array[] | colours |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
