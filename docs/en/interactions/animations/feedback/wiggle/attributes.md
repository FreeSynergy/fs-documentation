# Wiggle - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `wiggle` | Name of the animation |
| `amplitude` | number | `2` | Deflection in degrees (with `achse: rotate`) |
| `achse` | string | `rotate` | `rotate`, `x` or `y` |
| `pivot` | string | `center` | Pivot point of the rocking movement |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `600` | Duration of one cycle in ms |
| `timingFunction` | string | `ease-in-out` | soft reversal at the turning points |
| `iterationCount` | number \| `infinite` | `infinite` | endless, as long as the mode is active |
| `direction` | string | `alternate` | back and forth without a jump back |
| `playState` | string | `running` | `paused` while the element is invisible |

## Amplitude attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `offsetX` | number | `0` | additional displacement in px |
| `offsetY` | number | `0` | additional displacement in px |
| `phaseOffset` | number | `0` | phase offset per element in ms (groups) |
| `decay` | boolean | `false` | let the movement weaken over time |
| `stopOnExit` | boolean | `true` | on leaving the mode, straight into the position of rest |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `stateInsteadOfMotion` | boolean | `true` | also mark the mode with an outline/icon |
