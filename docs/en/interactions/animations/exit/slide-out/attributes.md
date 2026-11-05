# Slide Out - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the out-motion starts |
| `onAnimateEnd` | function | - | Runs when the view has been fully left |
| `onSlideProgress` | function | - | Reports the progress of the movement (0–1) |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Duration of the out-motion in ms |
| `timingFunction` | string | `ease-in` | an accelerating exit looks deliberate |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | The element stays outside the view after the end |

## Direction attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `direction` | string | `right` | `left`, `right`, `up` (upwards), `down` (downwards) |
| `distance` | number \| string | `100%` | Distance travelled until outside, in px or percent |
| `combineFade` | boolean | `false` | Combine the out-motion with a fade out of the opacity? |
| `removeOnEnd` | boolean | `false` | Remove the element from the DOM after it glides out? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `instant` – with reduced motion hide right away |
