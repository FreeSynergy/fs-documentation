# Flip - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the turn starts |
| `onContentSwap` | function | - | Runs at the 90° turning angle (change of side) |
| `onAnimateEnd` | function | - | Runs after the back side has come to rest |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `450` | Duration of the turn in ms |
| `timingFunction` | string | `ease-in-out` | a gentle start and a gentle stop |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | the back side stays standing after the turn |

## Axis and perspective attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `axis` | string | `y` | axis of rotation: `y` = turn left/right, `x` = tilt up/down |
| `angle` | number | `180` | turning angle in degrees (the standard for changing sides) |
| `perspective` | number | `1000` | perspective in px; `0` = a flat 2D turn without 3D |
| `backfaceVisibility` | string | `hidden` | only show the back side from 90° (`hidden`) or turn it along (`visible`) |
| `flipState` | string | `front` | the current side: `front` or `back` |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `swap` – swap the contents without turning |
