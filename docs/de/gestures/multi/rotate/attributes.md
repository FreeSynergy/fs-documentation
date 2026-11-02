# Rotate - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onRotate` | function | - | Wird beim Rotate ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showAngle` | boolean | `false` | Winkel anzeigen? |
| `rotateElement` | boolean | `true` | Element dreht sich? |

## Threshold-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `rotateThreshold` | number | `10` | Min. Winkel in Grad |
| `minAngle` | number | `-180` | Min. Winkel |
| `maxAngle` | number | `180` | Max. Winkel |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `slider` |
