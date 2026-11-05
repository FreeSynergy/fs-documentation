# Progress - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `wert` | number | `0` | Current progress |
| `wertMin` | number | `0` | Lower bound |
| `wertMax` | number | `100` | Upper bound |
| `indikator` | string | `balken` | `balken`, `ring`, `segmente` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `300` | softly taking over new values in ms |
| `timingFunction` | string | `ease-out` | the filling grows while running out |
| `iterationCount` | number \| `infinite` | `1` | `infinite` only for an indeterminate display |

## Progress attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `unbestimmt` | boolean | `false` | a running display without a known value |
| `farbe` | string | `accent` | fill colour, optionally `success` from 100 % |
| `beschriftung` | string | `auto` | percentage value, own text or `keine` |
| `dicke` | number | `8` | bar thickness or ring width in px |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
