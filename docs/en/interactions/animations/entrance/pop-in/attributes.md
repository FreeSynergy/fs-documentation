# Pop In - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `pop-in` | Name of the animation |
| `onAnimateStart` | function | - | Runs at the start |
| `onAnimateEnd` | function | - | Runs after the element lands |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `250` | Duration in ms |
| `timingFunction` | string | `cubic-bezier(.34,1.56,.64,1)` | fast rise, soft landing |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Keep the end state (full size) |

## Size attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `fromScale` | number | `0.8` | Starting size |
| `toScale` | number | `1` | Target size |
| `overshoot` | number | `1.06` | Factor the element shoots past |
| `bounces` | number | `1` | Number of after-oscillations following the overshoot |
| `origin` | string | `center` | Reference point: `center`, `top`, `bottom-left` … |
| `fromOpacity` | number | `0` | Starting opacity (0 = fully transparent) |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `short-fade` | `instant` (visible right away) or `short-fade` |
