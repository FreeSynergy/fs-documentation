# Shake - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onShake` | function | - | Wird beim Shake ausgeführt |
| `onShakeStart` | function | - | Wird beim Start des Shake ausgeführt |
| `onShakeEnd` | function | - | Wird beim Ende des Shake ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `shakeAnimation` | boolean | `true` | Shake-/Wiggle-Feedback am Element zeigen? |
| `confirmBeforeAction` | boolean | `true` | Aktion vor Ausführung bestätigen lassen? |
| `hapticFeedback` | boolean | `true` | Vibration bei Erkennung? |
| `soundFeedback` | boolean | `false` | Ton bei Erkennung? |

## Threshold-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `shakeThreshold` | number | `15` | Min. Beschleunigung (m/s²) bzw. Bewegung in px |
| `minShakes` | number | `2` | Min. Anzahl Richtungswechsel |
| `maxTime` | number | `1000` | Zeitfenster für Shake in ms |
| `cooldown` | number | `1000` | Pause nach Shake in ms (Doppelauslösung verhindern) |

## Richtungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `axis` | string | `x` \| `y` \| `xy` | Achse der Bewegung |
| `requireAxis` | boolean | `true` | Achse erforderlich? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `role` | string | - | ARIA-Rolle: `application` |
| `alternativeAction` | function | - | Gleichwertige Aktion per Button/Tastatur |
| `respectReducedMotion` | boolean | `true` | Bei `prefers-reduced-motion` Feedback deaktivieren? |
