# Dots - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `dots` | Name of the animation |
| `anzahl` | number | `3` | Number of dots |
| `onAnimateStart` | function | - | Runs at the start |
| `onAnimateEnd` | function | - | Runs when it stops |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `1400` | Duration of one cycle in ms |
| `timingFunction` | string | `ease-in-out` | soft swelling and fading |
| `delay` | number | `150` | display delay, to avoid flickering |
| `iterationCount` | number \| `infinite` | `infinite` | runs until loading ends |
| `playState` | string | `running` | `paused` hides the dots without clearing the state |

## Dot attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `dotSize` | number | `6` | Dot diameter in px |
| `dotSpacing` | number | `6` | Distance between the dots in px |
| `offsetProPunkt` | number | `160` | time offset of the dots within one cycle in ms |
| `hub` | number | `4` | lift height when rising in px |
| `modus` | string | `bounce` | `bounce`, `fade` or `scale` |
| `farbe` | string | `sekundaer` | dot colour, follows the theme |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | `Loading` | description for screen readers |
| `aria-live` | string | `polite` | region that announces the loading state |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `static` | the dots stand still instead of pulsing |
