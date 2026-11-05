# Typing - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aktiv` | boolean | `false` | show/hide the indicator |
| `punktzahl` | number | `3` | Number of dots or bars |
| `wellenform` | string | `welle` | `welle`, `blinken`, `huepfen` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `1200` | Duration of one cycle in ms |
| `timingFunction` | string | `ease-in-out` | soft lifting and lowering |
| `iterationCount` | number \| `infinite` | `infinite` | runs for as long as `aktiv` holds |
| `delay` | number | `0` | delay the start after the typing event |

## Typing attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `dotSize` | number | `6` | diameter of one dot in px |
| `punktAbstand` | number | `8` | distance between the dots in px |
| `farbe` | string | `muted` | dot colour, matching the chat theme |
| `sprechblase` | boolean | `true` | show the dots in a bubble above the input field |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
