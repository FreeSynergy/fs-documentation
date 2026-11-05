# Morph - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `startForm` | string | - | SVG path or shape of the starting state |
| `endForm` | string | - | SVG path or shape of the target state |
| `zustand` | string | `start` | `start`/`ende` switches the shape |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `400` | Duration of the shape change in ms |
| `timingFunction` | string | `ease-in-out` | soft starting and ending phase |
| `delay` | number | `0` | delayed start in ms |
| `direction` | string | `normal` | `reverse` morphs back |

## Shape attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `randRadiusStart` | number | `0` | corner radius of the starting shape in px |
| `randRadiusEnd` | number | `0` | corner radius of the target shape in px |
| `punktabgleich` | string | `auto` | assign the support points of both paths (`auto`, `manuell`) |
| `colorTransition` | boolean | `true` | transition fill and border colour softly |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
