# Pinch - Attribute

## Hauptattribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `onPinch` | function | - | Wird beim Pinch ausgeführt |

## Feedback-Attribute

| Attribute | Typ | Beschreibung |
|-----------|------|--------------|
| `showZoomFactor` | boolean | `false` | Zoom-Faktor anzeigen? |
| `scaleElement` | boolean | `true` | Element skaliert? |

## Threshold-Attribute

| Attribute | Typ | Beschreibung |
|-----------|------|--------------|
| `pinchThreshold` | number | `20` | Min. Distanz in px |
| `pointerCount` | number | `2` | Mindestanzahl beteiligter Finger |
| `minScale` | number | `0.5` | Min. Zoom-Faktor |
| `maxScale` | number | `2.0` | Max. Zoom-Faktor |

## Accessibility (Barrierefreiheit)

| Attribute | Typ | Beschreibung |
|-----------|------|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `slider` |
