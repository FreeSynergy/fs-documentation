# Flick - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onFlick` | function | - | Wird beim Flick ausgeführt |
| `onFlickStart` | function | - | Wird beim Start des Flick ausgeführt |
| `onFlickEnd` | function | - | Wird nach Ende des Nachlaufens ausgeführt |
| `onDecelerate` | function | - | Wird pro Frame während des Nachlaufens ausgeführt |

## Velocity-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `velocityThreshold` | number | `1000` | Min. Geschwindigkeit in px/s beim Loslassen |
| `maxFlickTime` | number | `300` | Max. Berührungsdauer in ms |
| `decelerationRate` | number | `0.998` | Abnahme der Geschwindigkeit pro Frame |
| `maxFlingDuration` | number | `1500` | Max. Nachlaufzeit in ms |

## Richtungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `axis` | string | `x` \| `y` \| `xy` | Achse des Flick |
| `momentum` | boolean | `true` | Nachlaufen nach dem Loslassen? |
| `overscroll` | boolean | `false` | Over-Scroll am Listenende erlauben? |
| `snapToItem` | boolean | `false` | Nach dem Auslaufen am nächsten Element einrasten? |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `rubberBand` | boolean | `true` | Gummiband-Effekt an Grenzen? |
| `hapticFeedback` | boolean | `false` | Vibration am Einrastpunkt? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Equivalenter Sprung (Button, Tastatur) |
| `instantScroll` | boolean | `false` | Bei `prefers-reduced-motion` ohne Nachlaufen scrollen? |
| `aria-label` | string | - | Beschreibender Text des Bereichs |
