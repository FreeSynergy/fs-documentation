# Pop Out - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `pop-out` | Name of the animation |
| `mirrorOf` | string | `pop-in` | Name of the opposite animation |
| `onAnimateStart` | function | - | Runs at the start |
| `onAnimateEnd` | function | - | Runs after the element disappears |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `200` | Duration in ms |
| `timingFunction` | string | `cubic-bezier(.36,0,.66,-.56)` | a short anticipation, then accelerated outward |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | keep the invisible end state |

## Size attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `fromScale` | number | `1` | Starting size |
| `toScale` | number | `0` | Target size |
| `anticipation` | number | `1.04` | Anticipation before shrinking |
| `origin` | string | `center` | Reference point: `center`, `top`, `bottom-left` … |
| `toOpacity` | number | `0` | Target opacity |
| `removeAfterEnd` | boolean | `true` | Take the element out of the layout after the end |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `instant` | `instant` (remove right away) or `short-fade` |
