# Tick Draw - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `tick-draw` | Name of the animation |
| `onDrawStart` | function | - | Runs when the drawing begins |
| `onDrawEnd` | function | - | Runs once the tick is complete |
| `behalten` | boolean | `true` | keep the tick visible after the animation |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `400` | Duration of the drawing in ms |
| `timingFunction` | string | `ease-out` | start quickly, run out calmly |
| `delay` | number | `150` | run-up for the circle or background |
| `fillMode` | string | `forwards` | keep the finished tick |

## Drawing attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `strokeLength` | number | `auto` | prepared path length (auto: measured from the icon) |
| `strokeWidth` | number | `2.5` | stroke thickness in px |
| `strokeFarbe` | string | `erfolg` | colour of the stroke, follows the status-colour system |
| `strichEnde` | string | `round` | `round`, `square` or `butt` |
| `hintergrund` | string | `kreis` | `none`, `kreis` or `flaeche` |
| `hintergrundDauer` | number | `200` | duration of the circle or surface appearing in ms |
| `nachziehen` | number | `0` | a short overshoot at the end of the stroke in px |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | `Done` | text for screen readers – never only the sign |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `instant` | the tick appears without the drawing movement |
