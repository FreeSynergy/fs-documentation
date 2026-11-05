# Rubber Band - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `rubberBand` | boolean | `true` | rubber-band resistance enabled |
| `achse` | string | `vertikal` | `vertikal`, `horizontal` or `beide` |
| `widerstand` | number | `0.35` | follow factor: 1 = follows 1:1, smaller = tougher |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `400` | springing back after release in ms |
| `timingFunction` | string | `spring` | springy return into the edge position |

## Rubber Band attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `maxAuszug` | number | `120` | maximum pull-out past the edge in px |
| `randEinzug` | number | `0` | free distance before the resistance sets in (px) |
| `trigger` | string | `scroll` | `scroll`, `drag` or `beides` |
| `seite` | string | `beide` | `beide`, `anfang`, `ende` of the list |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
