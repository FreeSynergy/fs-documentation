# Shake - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `shake` | Name of the animation |
| `amplitude` | number | `8` | Deflection in px from the position of rest |
| `cycles` | number | `3` | Number of back and forth within one run |
| `achse` | string | `x` | `x` (horizontal), `y` (vertical), `rotate` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `400` | Total duration in ms |
| `timingFunction` | string | `ease-in-out` | soft reversal at the turning points |
| `delay` | number | `0` | Delay before the start in ms |
| `iterationCount` | number | `1` | the feedback runs once, not endlessly |
| `fillMode` | string | `none` | the element always ends in the position of rest |

## Amplitude attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `decay` | boolean | `true` | the deflection decays per cycle |
| `decayFactor` | number | `0.7` | ratio between successive amplitudes |
| `waveform` | string | `sinusoidal` | `sinusoidal` or `linear` (jerky) |
| `richtung` | string | `beide` | `beide`, `links zuerst`, `rechts zuerst` |
| `interruptible` | boolean | `true` | a new shake replaces the running one |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `announceError` | boolean | `true` | also report the error as text/ARIA |
