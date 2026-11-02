# Rotate - Attribute

## Hauptattribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `onRotate` | function | - | Wird beim Rotate ausgeführt |

## Feedback-Attribute

| Attribute | Typ | Beschreibung |
|-----------|------|--------------|
| `showAngle` | boolean | `false` | Winkel anzeigen? |
| `rotateElement` | boolean | `true` | Element dreht sich? |

## Threshold-Attribute

| Attribute | Typ | Beschreibung |
|-----------|------|--------------|
| `rotateThreshold` | number | `10` | Min. Winkel in Grad |
| `pointerCount` | number | `2` | Mindestanzahl beteiligter Finger |
| `minAngle` | number | `-180` | Min. Winkel |
| `maxAngle` | number | `180` | Max. Winkel |

## Accessibility (Barrierefreiheit)

| Attribute | Typ | Beschreibung |
|-----------|------|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `slider` |
