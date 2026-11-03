# Flick - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onFlick` | function | - | Executed on Flick |
| `onFlickStart` | function | - | Executed at the start of the Flick |
| `onFlickEnd` | function | - | Executed after the run-out has ended |
| `onDecelerate` | function | - | Executed per frame during the run-out |

## Velocity Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `velocityThreshold` | number | `1000` | Min. velocity in px/s at release |
| `maxFlickTime` | number | `300` | Max. touch duration in ms |
| `decelerationRate` | number | `0.998` | Decrease of velocity per frame |
| `maxFlingDuration` | number | `1500` | Max. run-out time in ms |

## Direction Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `axis` | string | `x` \| `y` \| `xy` | Axis of the Flick |
| `momentum` | boolean | `true` | Keep running after the release? |
| `overscroll` | boolean | `false` | Allow over-scroll at the end of the list? |
| `snapToItem` | boolean | `false` | Snap to the nearest element after rolling out? |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `rubberBand` | boolean | `true` | Rubber-band effect at the boundaries? |
| `hapticFeedback` | boolean | `false` | Vibration at the snap point? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `alternativeAction` | function | - | Equivalent jump (button, keyboard) |
| `instantScroll` | boolean | `false` | Scroll without run-out on `prefers-reduced-motion`? |
| `aria-label` | string | - | Descriptive text of the area |
