# Scale In - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `scale-in` | Name of the animation |
| `startScale` | number | `0` | Starting size as a factor (0 = invisible) |
| `endScale` | number | `1` | Target size as a factor |
| `transformOrigin` | string | `center` | Growth point: `center`, `top`, `bottom right` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `200` | Duration in ms |
| `timingFunction` | string | `ease-out` | entrances usually `ease-out` |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `backwards` | Show the start state (0 %) already during the delay |
| `onAnimateEnd` | function | - | Runs once the final size is reached |

## Axis attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `axis` | string | `both` | `both`, `x` or `y` |
| `scaleX` | number | `1` | Additional factor for the width |
| `scaleY` | number | `1` | Additional factor for the height |
| `keepSpace` | boolean | `true` | Reserve the layout space during the animation |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `announceOnEnd` | boolean | `false` | Only announce the content after the animation ends |
