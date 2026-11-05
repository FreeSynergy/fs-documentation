# Pulse - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `pulse` | Name of the animation |
| `minScale` | number | `1` | size at the start of the cycle |
| `maxScale` | number | `1.06` | size at the peak |
| `minOpacity` | number | `1` | opacity in the starting state |
| `maxOpacity` | number | `0.65` | opacity at the peak |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `1200` | Duration of one cycle in ms |
| `timingFunction` | string | `ease-in-out` | even swelling and shrinking |
| `iterationCount` | number \| `infinite` | `infinite` | endless, for as long as the status is active |
| `direction` | string | `alternate` | peak and trough alternating, without a jump |
| `playState` | string | `running` | `paused` while the element is not visible |

## Cycle attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `dauerProZyklus` | number | `1200` | length of one full cycle in ms |
| `waveform` | string | `sinusoidal` | `sinusoidal`, `linear` or `triangle` |
| `haloRadius` | number | `0` | an extra radiating ring in px (0 = off) |
| `haloFarbe` | string | `accent` | colour of the ring |
| `pauseWhenHidden` | boolean | `true` | pause outside the viewport |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `maxCyclesPerView` | number | `3` | end the endless loop after n cycles |
