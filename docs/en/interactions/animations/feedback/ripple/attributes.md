# Ripple - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `ripple` | Name of the animation |
| `wellenUrsprung` | string | `click` | `click` (point of contact) or `center` |
| `farbe` | string | `onSurface 0.2` | Fill colour of the wave with opacity |
| `radius` | string \| number | `auto` | Target radius; `auto` = reach the whole surface |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `450` | Spread duration of one wave in ms |
| `timingFunction` | string | `ease-out` | the wave slows down as it grows |
| `delay` | number | `0` | Delay before the start in ms |
| `iterationCount` | number | `1` | One wave per interaction |
| `fillMode` | string | `none` | the wave disappears completely |

## Wave attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `startRadius` | number | `0` | Starting radius in px |
| `spreadDuration` | number | `450` | Time until the target radius is reached |
| `fadeAnteil` | number | `0.6` | Share of the duration in which the wave fades out |
| `containInElement` | boolean | `true` | Clip the wave at the element contour |
| `maxWellen` | number | `3` | Simultaneous waves, the oldest one is replaced |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `focusRipple` | boolean | `true` | Trigger the wave on keyboard focus as well |
