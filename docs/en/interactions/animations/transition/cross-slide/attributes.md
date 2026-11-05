# Cross Slide - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `cross-slide` | Name of the animation |
| `altesElement` | node | - | the element that leaves the surface |
| `neuesElement` | node | - | the element that comes in |
| `onTransitionEnd` | function | - | Runs after the swap is complete |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `280` | Duration of the swap in ms |
| `timingFunction` | string | `ease-in-out` | both elements move symmetrically |
| `delay` | number | `0` | Delay before the start in ms |
| `iterationCount` | number \| `infinite` | `1` | a one-time swap |

## Direction attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `richtung` | string | `left` | `left`, `right`, `up`, `down` |
| `distanz` | string | `100%` | distance travelled, usually the full width; also possible in px |
| `anteilUeberlappung` | number | `1` | 1 = both move at the same time, 0 = one after the other |
| `deckkraftAmRand` | number | `1` | optional fading at the edges while sliding |
| `abgeschnitten` | boolean | `true` | elements outside the surface are not visible |
| `nurNeues` | boolean | `false` | instead the old element disappears via a fade out |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `aria-live` | string | `polite` | announce the change of content |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
| `reducedMotionFallback` | string | `cross-fade` | cross-fade instead of sliding as a substitute |
