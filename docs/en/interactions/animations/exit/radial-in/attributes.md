# Radial In - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `radial-in` | Name of the animation |
| `onAnimateStart` | function | - | Runs at the start |
| `onAnimateEnd` | function | - | Runs before the menu is taken out of the layout |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `160` | Duration per ring in ms |
| `timingFunction` | string | `ease-in` | points accelerate towards the anchor (a pull) |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Keep the shrinking until removal |

## Radial attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `origin` | string | `anchor` | Gathering point: anchor centre (`center`, `fab`, pointer …) |
| `toRadius` | number | `0` | Target distance from the anchor (0 = core centre) |
| `fromScale` | number | `1` | Starting size of the points |
| `toScale` | number | `0` | Final size |
| `staggerStep` | number | `10` | Offset between points in ms |
| `ringStep` | number | `50` | Offset between rings in ms |
| `order` | string | `outside-in` | Order: `outside-in`, `angle`, `all` |
| `fadePoints` | boolean | `true` | Additionally fade the points out? |
| `keepAnchorLast` | boolean | `true` | Does the anchor core disappear last? |
| `mirrorOf` | string | `radial-out` | Name of the opposite animation |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `fade-out` | `instant` (hidden right away) or `fade-out` |
