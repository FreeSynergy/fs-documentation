# Pinch - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onPinch` | function | - | Wird beim Pinch ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showZoomFactor` | boolean | `false` | Zoom-Faktor anzeigen? |
| `scaleElement` | boolean | `true` | Element skaliert? |

## Threshold-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `pinchThreshold` | number | `20` | Min. Distanz in px |
| `minScale` | number | `0.5` | Min. Zoom-Faktor |
| `maxScale` | number | `2.0` | Max. Zoom-Faktor |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `slider` |
