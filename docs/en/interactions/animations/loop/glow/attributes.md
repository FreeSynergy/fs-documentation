# Glow - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `glowColor` | string | `accent` | colour of the glow |
| `glowIntensity` | number | `1.0` | brightness of the shine (0.0–2.0) |
| `glowSpread` | number | `12` | radius of the shine in px |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `1500` | Duration of one cycle in ms |
| `timingFunction` | string | `ease-in-out` | soft swelling and shrinking |
| `iterationCount` | number \| `infinite` | `infinite` | runs for as long as the status is active |
| `direction` | string | `alternate` | the shine swells up and back down |

## Glow attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aktiv` | boolean | `false` | turn the glow on (e.g. on selection) |
| `pulsierend` | boolean | `true` | the shine breathes in the loop; `false` = a constant glow |
| `glowForm` | string | `kontur` | `kontur` follows the element shape, `rechteckig` renders faster |
| `glowEbene` | string | `hinter` | draw the shine behind or above the content |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
