# Lift - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `lift` | Name of the animation |
| `onLiftStart` | function | - | Runs when the element is raised |
| `onLiftEnd` | function | - | Runs after the reset |
| `ausloeser` | string | `hover` | `hover`, `focus` or `hover-focus` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `160` | Duration of the raising in ms |
| `timingFunction` | string | `ease-out` | rise gently, land softly |
| `delay` | number | `0` | no delay – a reaction to the pointer |
| `fillMode` | string | `forwards` | the raised state stays during the hover |

## Shadow attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `liftOffsetY` | number | `-2` | Shift upwards in px (negative = higher) |
| `shadowSpread` | number | `8` | Shadow reach in the raised state in px |
| `shadowBlur` | number | `16` | Softening of the shadow in px |
| `shadowOpacity` | number | `0.18` | Opacity of the shadow (0–1) |
| `surfaceDelta` | number | `0.03` | Lightening of the surface in the raised state |
| `nurSchatten` | boolean | `false` | without movement, only the shadow changes |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `nurSchatten` | `nurSchatten` or `rand` (outline instead of height) |
