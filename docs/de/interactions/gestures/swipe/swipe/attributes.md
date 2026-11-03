# Swipe - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onSwipe` | function | - | Wird beim Swipe ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showDirection` | boolean | `true` | Pfeil anzeigen? |
| `showVelocity` | boolean | `false` | Geschwindigkeit anzeigen? |

## Threshold-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `swipeThreshold` | number | `50` | Min. Distanz in px |
| `maxTime` | number | `300` | Max. Zeit in ms |

## Richtungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `allowedDirections` | array[] | `[left, right, up, down]` | Erlaubte Richtungen |
| `requireDirection` | boolean | `true` | Richtung erforderlich? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `slider` |
