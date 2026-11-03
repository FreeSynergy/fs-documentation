# Wave - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onWave` | function | - | Wird beim Winken ausgeführt |
| `onWaveApproach` | function | - | Hand nähert sich dem Sensor |
| `onWavePattern` | function | - | Erkanntes Muster (`open`, `fist`, `swipe`) |

## Sensor-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `detectionRange` | number | `60` | Erkennungsreichweite in cm |
| `minDisplacement` | number | `20` | Min. Handbewegung in cm |
| `maxWaveTime` | number | `2000` | Zeitfenster für die Bewegung in ms |
| `cooldown` | number | `3000` | Pause nach Erkennung in ms |

## Berechtigung-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `requiresMotionPermission` | boolean | readonly | Sensorberechtigung nötig? |
| `userEnabled` | boolean | `false` | Standardmäßig aus – Nutzer muss aktivieren |
| `privacyIndicator` | boolean | `true` | Anzeige, solange Sensor aktiv ist? |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `countdownUI` | boolean | `true` | Countdown vor Annahme anzeigen? |
| `hapticFeedback` | boolean | `true` | Vibration bei Erkennung? |
| `soundFeedback` | boolean | `true` | Akustische Bestätigung? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Buttons am Anruf-/Steuerungsdialog (WCAG 2.5.4) |
| `enabled` | boolean | `false` | Geste abschaltbar, Standard aus |
