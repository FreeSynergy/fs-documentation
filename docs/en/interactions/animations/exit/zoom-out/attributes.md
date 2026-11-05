# Zoom Out - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the shrinking starts |
| `onAnimateEnd` | function | - | Runs once the element has fully disappeared |
| `onElementHidden` | function | - | Reports that the element was hidden |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `200` | Duration of the hide in ms |
| `timingFunction` | string | `ease-in` | accelerating shrinking looks deliberate |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | The invisible end state is kept |

## Scaling attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `startScale` | number | `1` | Starting scale (full size) |
| `endScale` | number | `0` | Target scale (0 = fully shrunk) |
| `opacitySync` | boolean | `true` | Fade the opacity out in sync with the scaling? |
| `removeOnEnd` | boolean | `false` | Remove the element from the DOM after it shrinks? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `instant` – hide right away without scaling |
