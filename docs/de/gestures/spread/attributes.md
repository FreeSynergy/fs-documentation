# Spread - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onSpread` | function | - | Wird beim Spread ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showZoomFactor` | boolean | `false` | Zoom-Faktor anzeigen? |
| `scaleElement` | boolean | `true` | Element skaliert? |

## Threshold-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `spreadThreshold` | number | `20` | Min. Distanz in px |
| `minScale` | number | `0.5` | Min. Zoom-Faktor |
| `maxScale` | number | `2.0` | Max. Zoom-Faktor |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `slider` |
