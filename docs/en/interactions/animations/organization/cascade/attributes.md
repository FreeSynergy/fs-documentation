# Cascade - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `cascade` | boolean | `false` | time-offset starts along a direction |
| `richtung` | string | `top-left` | `top-left`, `top-right`, `bottom`, `center-out`, `in-center` |
| `kinder` | selector | `alle` | which child elements are cascaded |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `delay` | number | `0` | base waiting time of the whole group |
| `iterationCount` | number \| `infinite` | `1` | repeats the whole group |
| `direction` | string | `normal` | `reverse` begins at the other end of the direction |

## Timing attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `stepBase` | number | `50` | distance of the first two starts in ms (standard: `staggerStep`) |
| `stepGrowth` | number | `0` | change of the distance per element (negative = becoming faster) |
| `stepLimit` | number | `200` | upper bound of the calculated distance in ms |
| `achse` | string | `auto` | `auto`, `x`, `y` or `diagonal` – along which coordinate the sorting happens |
| `wellenLaenge` | number | `0` | child elements that start simultaneously (0 = each one alone) |
| `beimAusgangUmkehren` | boolean | `true` | the exit runs in the opposite direction |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `instant` | `instant` (all at the same time) or `short-fade` |
