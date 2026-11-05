# Bounce Out - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onAnimateStart` | function | - | Runs when the farewell starts |
| `onAnticipation` | function | - | Runs on the anticipation (compression) |
| `onAnimateEnd` | function | - | Runs once the element has fully disappeared |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `400` | Total duration of anticipation and exit jump in ms |
| `timingFunction` | string | `ease-in` | accelerating take-off |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | The invisible end state is kept |

## Anticipation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `anticipation` | number | `8` | Pull-back against the exit direction in % of the element size |
| `squash` | number | `0.9` | Compression of the scale before the take-off (1 = none) |
| `exitDirection` | string | `up` | Direction of the exit jump: `up`, `down`, `left`, `right` |
| `endScale` | number | `0.2` | Scale at the moment of disappearing (0 = fully shrunk) |
| `removeOnEnd` | boolean | `true` | Remove the element from the DOM after it disappears? |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | - | `instant` – hide right away without the spring |
