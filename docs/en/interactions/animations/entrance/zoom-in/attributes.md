# Zoom In - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the enlargement starts |
| `onAnimateEnd` | function | - | Runs when the full size is reached |
| `onScaleChange` | function | - | Reports the current scale during the animation |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Duration of the reveal in ms |
| `timingFunction` | string | `ease-out` | brakes cleanly down to the full size |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | The full size is kept after the end |

## Scaling attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `startScale` | number | `0.5` | Starting scale (must be smaller than 1) |
| `endScale` | number | `1` | Target scale in X and Y |
| `opacitySync` | boolean | `true` | Raise opacity in sync with the scaling? |
| `transformOrigin` | string | `center` | Origin of the scaling (e.g. `center`, `top left`) |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `fade` – only fade in instead of scaling |
