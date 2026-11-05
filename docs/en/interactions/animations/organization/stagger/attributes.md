# Stagger - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `stagger` | boolean | `false` | time-offset starts for child elements |
| `reihenfolge` | string | `index` | `index`, `umgekehrt` or `zufall` |
| `kinder` | selector | `alle` | which child elements are staggered |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `delay` | number | `0` | base waiting time of the whole group |
| `iterationCount` | number \| `infinite` | `1` | repeats the whole group |
| `direction` | string | `normal` | `reverse` staggers starting from the last child |

## Stagger attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `offsetProElement` | number | `50` | time distance of the starts in ms (standard: `staggerStep`) |
| `gruppenLimit` | number | `0` | max. child elements starting simultaneously (0 = unlimited) |
| `beimAusgangUmkehren` | boolean | `true` | the exit begins at the last child |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
