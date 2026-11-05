# Highlight - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `highlight` | Name of the animation |
| `farbe` | string | `accent` | Glow colour of the background |
| `intensity` | number | `0.35` | Opacity at the maximum (0–1) |
| `modus` | string | `background` | `background`, `outline`, `text` or `border` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `900` | Duration of one glow in ms |
| `timingFunction` | string | `ease-in-out` | soft rise and decay |
| `delay` | number | `0` | Delay before the start in ms |
| `iterationCount` | number | `1` | usually once; 2 for stronger attention |
| `fillMode` | string | `none` | afterwards the original colour applies again |

## Colour attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `startFarbe` | string | `transparent` | Starting overlay |
| `endFarbe` | string | `transparent` | Ending overlay |
| `anstiegAnteil` | number | `0.25` | Share of the duration until the maximum |
| `radius` | number | `4` | Corner radius of the glowing surface in px |
| `puffer` | number | `8` | Distance of the glowing surface from the content in px |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `kontrastCheck` | boolean | `true` | Force a minimum contrast while glowing |
