# Skeleton - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `ladezustand` | string | `geladen` | `laden` shows/hides the skeleton |
| `struktur` | string | `zeilen` | `zeilen`, `liste`, `karte`, `tabelle` |
| `zeilen` | number | `3` | Number of placeholder rows |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `1500` | Duration of one shimmer cycle in ms |
| `timingFunction` | string | `linear` | a shimmer travelling at a constant pace |
| `iterationCount` | number \| `infinite` | `infinite` | runs until the content arrives |

## Skeleton attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `blockFormen` | array | `balken` | a mix of `balken`, `kreis`, `block` per row |
| `zeilenBreiten` | array | `auto` | percentage widths, e.g. `100 %, 60 %` |
| `rowHeight` | number | `16` | height of one placeholder row in px |
| `zeilenAbstand` | number | `10` | distance between the rows in px |
| `schimmerFarbe` | string | `hell` | colour of the travelling shimmer |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
