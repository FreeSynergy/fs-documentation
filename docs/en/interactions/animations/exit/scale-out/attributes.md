# Scale Out - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `scale-out` | Name of the animation |
| `startScale` | number | `1` | Starting size as a factor |
| `endScale` | number | `0` | Target size as a factor (0 = disappears) |
| `transformOrigin` | string | `center` | Shrink point; often `top right` at the trigger |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `180` | Duration in ms (exits often shorter than entrances) |
| `timingFunction` | string | `ease-in` | exits usually `ease-in` |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | Hold the end state (0 %) until removal |
| `iterationCount` | number | `1` | exits run exactly once |

## Axis attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `axis` | string | `both` | `both`, `x` or `y` |
| `scaleX` | number | `1` | Additional factor for the width |
| `scaleY` | number | `1` | Additional factor for the height |
| `removeAfter` | boolean | `true` | Remove the element from the layout after the end |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `removeImmediately` | boolean | `false` | Remove the element right away without animation |
