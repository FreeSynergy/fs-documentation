# Bounce In - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the in-motion starts |
| `onBounce` | function | - | Runs on each overshoot |
| `onAnimateEnd` | function | - | Runs after the final settling |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `500` | Total duration including the spring-back in ms |
| `timingFunction` | string | `cubic-bezier(.34,1.56,.64,1)` | spring curve with overshoot |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Keeps the final position after settling |

## Amplitude attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `overshoot` | number | `12` | Overshoot past the final position in % |
| `bounceCount` | number | `2` | Number of spring-backs |
| `startScale` | number | `0.5` | Starting scale (0 = pops out of nothing) |
| `dropHeight` | number | `0` | Drop height from above in px (greater than 0 for the drop variant) |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `fade` – only fade in instead of the spring motion |
