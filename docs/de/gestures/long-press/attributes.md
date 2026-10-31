# Long Press - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onLongPress` | function | - | Wird beim Long Press ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `rippleEffect` | boolean | `true` | Ripple-Effekt anzeigen? |
| `hapticFeedback` | boolean | `false` | Haptisches Feedback? |
| `scaleEffect` | boolean | `false` | Scale-Effekt anzeigen? |

## Threshold-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `longPressThreshold` | number | `500` | Zeitlimit für Long Press in ms |
| `moveThreshold` | number | `10` | Max. Bewegung in px |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `button` |
