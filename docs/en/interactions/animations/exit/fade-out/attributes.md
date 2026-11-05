# Fade Out - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the fade-out starts |
| `onAnimateEnd` | function | - | Runs after the element is fully faded out |
| `onElementHidden` | function | - | Reports that the element was hidden |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `200` | Fade-out duration in ms |
| `timingFunction` | string | `ease-in` | exits feel more natural with acceleration |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Keeps the end state (invisible) after the end |

## Opacity attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `fromOpacity` | number | `1` | Starting opacity (1 = fully visible) |
| `toOpacity` | number | `0` | Target opacity (0 = invisible) |
| `removeOnEnd` | boolean | `false` | Remove the element from the DOM after fading out? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `aria-hidden` | string | - | Is automatically set to `true` after the end |
