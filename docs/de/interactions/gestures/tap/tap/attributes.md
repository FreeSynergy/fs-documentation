# Tap - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onTap` | function | - | Wird beim Tap ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `rippleEffect` | boolean | `true` | Ripple-Effekt anzeigen? |
| `scaleEffect` | boolean | `false` | Scale-Effekt anzeigen? |
| `colorEffect` | boolean | `false` | Farbe ändern? |

## Threshold-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `tapThreshold` | number | `250` | Zeitlimit für Tap in ms |
| `moveThreshold` | number | `10` | Max. Bewegung in px |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `button` |
