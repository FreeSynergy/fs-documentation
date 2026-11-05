# Radial Out - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `radial-out` | Name of the animation |
| `onAnimateStart` | function | - | Runs at the start |
| `onAnimateEnd` | function | - | Runs after the last point |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `220` | Duration per ring in ms |
| `timingFunction` | string | `cubic-bezier(.2,.8,.3,1)` | brisk start, soft landing |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Keep the end state (ring position) |

## Radial attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `origin` | string | `anchor` | Starting point: anchor centre (`center`, `fab`, pointer …) |
| `fromRadius` | number | `0` | Starting distance from the anchor (0 = core centre) |
| `fromScale` | number | `0` | Starting size of the points |
| `toScale` | number | `1` | Final size |
| `overshoot` | number | `1` | Factor past the ring position (1 = none) |
| `staggerStep` | number | `18` | Offset between points in ms |
| `ringStep` | number | `80` | Offset between rings in ms |
| `order` | string | `angle` | Order: `angle`, `inside-out`, `random` |
| `fadePoints` | boolean | `true` | Additionally fade the points in? |
| `mirrorOf` | string | `radial-in` | Name of the opposite animation |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `fade-in` | `instant` (visible right away) or `fade-in` |
