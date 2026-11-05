# Cross Fade - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `elementAus` | referenz | - | the element that is faded out |
| `elementEin` | referenz | - | the element that is faded in |
| `inhalt` | any | - | the content whose change is cross-faded |

## Animation attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `duration` | number | `300` | Duration of the cross-fade in ms |
| `timingFunction` | string | `ease` | a symmetrical opacity curve |
| `delay` | number | `0` | delay the start of the new element |
| `direction` | string | `normal` | `alternate` when switching back |

## Cross Fade attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `overlap` | number | `100` | 100 = both at the same time, 0 = one after the other |
| `ebenenReihenfolge` | string | `neuOben` | which element lies on top during the transition |
| `skalaMit` | boolean | `false` | additionally zoom the new element in slightly |

## Accessibility

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `aria-label` | string | - | Descriptive text |
| `respectReducedMotion` | boolean | `true` | Reduce the animation under prefers-reduced-motion? |
