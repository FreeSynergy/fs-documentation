# Rotate - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the turn starts |
| `onRotate` | function | - | Runs continuously on every change of angle |
| `onAnimateEnd` | function | - | Runs when the target angle is reached |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `300` | Duration of the turn in ms |
| `timingFunction` | string | `ease-in-out` | a natural start and stop of the turn |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | the target angle stays as the new state |

## Angle attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `angle` | number | `180` | target angle in degrees (negative = counter-clockwise) |
| `transformOrigin` | string | `center` | pivot point: `center`, `top left`, `50% 100%` … |
| `rotationDirection` | string | `shortest` | `cw`, `ccw` or `shortest` (the shortest direction of turn) |
| `stateAngle` | boolean | `true` | remember the end angle as a lasting state (e.g. opened/closed)? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `instant` – change the angle without turning |
