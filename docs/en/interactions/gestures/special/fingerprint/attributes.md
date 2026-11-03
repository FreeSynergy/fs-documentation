# Fingerprint - Attributes

## Main Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `onFingerprint` | function | - | Executed after a successful scan |
| `onFingerprintFail` | function | - | Executed when no match is found |
| `requireFingerprint` | boolean | `false` | Action protected by fingerprint? |

## Sensor Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `sensorType` | string | `capacitive` | `capacitive`, `optical`, or `ultrasonic` |
| `sensorLocation` | string | `front` | `display`, `front`, `side-key`, `rear` |
| `scanMode` | string | `touch` | `touch` (hold) or `swipe` (slide across) |
| `scanTimeout` | number | `10000` | Time limit for the scan in ms |

## Feedback Attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `hapticFeedback` | boolean | `true` | Vibration on success/failure |
| `showScanAnimation` | boolean | `true` | Scan ring pulses during the scan |
| `maxRetries` | number | `5` | Attempts before the fallback |
| `fallbackAction` | function | - | Alternative after timeout (PIN, password) |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `fallbackAction` | function | Mandatory alternative without biometrics (PIN, pattern, password) |
