# Unfold - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `unfold` | Name of the animation |
| `foldOrigin` | string | `top` | Fold edge: `top`, `bottom`, `left`, `right` |
| `startAngle` | number | `-90` | Starting angle in degrees (90 = edgewise) |
| `endAngle` | number | `0` | Target angle in degrees (lying flat) |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `450` | Duration in ms |
| `timingFunction` | string | `ease-out` | sweeping start, soft end |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `both` | the folded start state also before the start |
| `onAnimateEnd` | function | - | Runs after the element is fully unfolded |

## Folding attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `perspective` | number | `800` | Camera distance in px (smaller = stronger 3D effect) |
| `segments` | number | `1` | Number of folds (several segments = wavelike) |
| `segmentStagger` | number | `60` | Offset of the segments in ms |
| `backfaceVisible` | boolean | `false` | Is the back side visible during the swing? |
| `shadow` | string | `auto` | Moving shadow while unfolding |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `fallbackAnimation` | string | `expand` | Substitute without the 3D rotation |
