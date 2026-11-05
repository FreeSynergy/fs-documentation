# Slide In - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the in-motion starts |
| `onAnimateEnd` | function | - | Runs when the final position is reached |
| `onSlideProgress` | function | - | Reports the progress of the movement (0–1) |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `300` | Duration of the in-motion in ms |
| `timingFunction` | string | `ease-out` | braking in the final phase, feels tangible |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `backwards` | The element stays outside the view before the start |

## Direction attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `direction` | string | `left` | `left`, `right`, `up` (from below), `down` (from above) |
| `distance` | number \| string | `100%` | Starting offset in px or percent of the element size |
| `combineFade` | boolean | `true` | Combine the in-motion with a fade in opacity? |
| `edge` | string | `viewport` | Reference frame of the outside position: `viewport` or the parent element |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `fade` – with reduced motion only fade in |
