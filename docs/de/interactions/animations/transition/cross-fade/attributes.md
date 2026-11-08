# Cross Fade - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `elementAus` | referenz | - | das Element, das ausgeblendet wird |
| `elementEin` | referenz | - | das Element, das eingeblendet wird |
| `inhalt` | any | - | der Inhalt, dessen Wechsel überblendet wird |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `300` | Dauer der Überblendung in ms |
| `timingFunction` | string | `ease` | eine symmetrische Deckkraft-Kurve |
| `delay` | number | `0` | verzögert den Start des neuen Elements |
| `direction` | string | `normal` | `alternate` beim Zurückwechseln |

## Cross-Fade-Attribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `overlap` | number | `100` | 100 = beide gleichzeitig, 0 = nacheinander |
| `ebenenReihenfolge` | string | `neuOben` | welches Element während des Übergangs oben liegt |
| `skalaMit` | boolean | `false` | das neue Element zusätzlich leicht vergrößern |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
