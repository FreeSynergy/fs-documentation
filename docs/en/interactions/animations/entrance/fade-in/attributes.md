# Fade In - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the fade-in starts |
| `onAnimateEnd` | function | - | Runs after the element is fully visible |
| `onVisibilityChange` | function | - | Reports the visibility change (hidden → visible) |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Fade-in duration in ms |
| `timingFunction` | string | `ease-out` | Soft start, calm landing |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Keeps the end state (fully visible) after the end |

## Opacity attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `fromOpacity` | number | `0` | Starting opacity (0 = fully transparent) |
| `toOpacity` | number | `1` | Target opacity (1 = fully visible) |
| `blur` | number | `0` | Blur in px at the start, decays as the element fades in |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `instant` (visible right away) or `short-fade` |
