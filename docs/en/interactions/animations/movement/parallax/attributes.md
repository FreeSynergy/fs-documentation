# Parallax - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `parallax` | boolean | `true` | enable parallax for the container |
| `ebenen` | array | - | layers, ordered from the back to the front |
| `trigger` | string | `scroll` | `scroll`, `zeiger` or `gyroskop` |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `200` | pull-along time at jumps (anchor, end) |
| `timingFunction` | string | `ease-out` | a soft run-out after the scroll stops |

## Layer attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `faktorProEbene` | array | `[0.2, 0.5, 1]` | 0 = stands still, 1 = normal speed |
| `achse` | string | `y` | `x`, `y` or `beide` |
| `maxAusschlag` | number | `0` | limit of the layer offset in px (0 = free) |
| `tiefe` | number | `0` | an extra 3D offset via perspective in px |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
