# Fingerprint - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onFingerprint` | function | - | Wird nach erfolgreichem Scan ausgeführt |
| `onFingerprintFail` | function | - | Wird bei ausbleibendem Match ausgeführt |
| `requireFingerprint` | boolean | `false` | Aktion ist per Fingerabdruck geschützt? |

## Sensor-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `sensorType` | string | `capacitive` | `capacitive`, `optical` oder `ultrasonic` |
| `sensorLocation` | string | `front` | `display`, `front`, `side-key`, `rear` |
| `scanMode` | string | `touch` | `touch` (halten) oder `swipe` (darüberziehen) |
| `scanTimeout` | number | `10000` | Zeitlimit für den Scan in ms |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hapticFeedback` | boolean | `true` | Vibration bei Erfolg/Misserfolg |
| `showScanAnimation` | boolean | `true` | Scan-Ring pulsiert während des Scans |
| `maxRetries` | number | `5` | Versuche bis zum Fallback |
| `fallbackAction` | function | - | Alternative nach Timeout (PIN, Passwort) |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `fallbackAction` | function | Pflicht-Alternative ohne Biometrie (PIN, Muster, Passwort) |
