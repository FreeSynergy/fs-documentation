# Reorder - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `reorder` | Name of the animation |
| `fromIndex` | number | - | position before the change |
| `toIndex` | number | - | position after the change |
| `onReorderStart` | function | - | Runs when the movement begins |
| `onReorderEnd` | function | - | Runs after the element clicks into place |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `320` | Duration of the movement in ms |
| `timingFunction` | string | `ease-in-out` | start softly, click in precisely |
| `delay` | number | `0` | Delay before the start in ms |
| `fillMode` | string | `forwards` | keep the new position after the end |

## Position attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `messung` | string | `flip` | `flip` (measure before/after) or `transform` (only displace) |
| `achse` | string | `auto` | `auto`, `y`, `x` – axis of movement, usually the direction of the list |
| `nurSichtbare` | boolean | `true` | elements outside the viewport jump without animation |
| `maxElemente` | number | `40` | upper bound of simultaneously animated elements |
| `einrasten` | number | `0` | a slight overshoot and spring back at the target in px |
| `andereZurueckhaltend` | number | `0.8` | neighbouring elements travel in `duration` × factor |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `aria-live` | string | `polite` | announce the new position ("entry 3 of 12") |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `instant` | swap the positions without movement |
