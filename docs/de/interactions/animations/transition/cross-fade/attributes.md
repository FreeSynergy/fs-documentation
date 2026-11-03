# Cross Fade - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `elementAus` | referenz | - | Element, das ausgeblendet wird |
| `elementEin` | referenz | - | Element, das eingeblendet wird |
| `inhalt` | any | - | Inhalt, bei dessen Wechsel überblendet wird |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `300` | Dauer des Überblendens in ms |
| `timingFunction` | string | `ease` | symmetrischer Deckkraftverlauf |
| `delay` | number | `0` | Start des neuen Elements verzögern |
| `direction` | string | `normal` | `alternate` beim Zurückwechseln |

## Cross-Fade-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `overlap` | number | `100` | 100 = beide gleichzeitig, 0 = nacheinander |
| `ebenenReihenfolge` | string | `neuOben` | welches Element während des Übergangs oben liegt |
| `skalaMit` | boolean | `false` | neues Element zusätzlich leicht hereinzoomen |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
