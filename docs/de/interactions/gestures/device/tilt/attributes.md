# Tilt - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onTilt` | function | - | Wird bei Neigungsänderung ausgeführt |
| `onTiltStart` | function | - | Deadzone wurde verlassen |
| `onTiltEnd` | function | - | Gerät wieder in Ruhelage |

## Sensor-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `axes` | string | `beta` \| `gamma` \| `both` | Auswertete Achsen |
| `deadZone` | number | `3` | Grad bis Bewegung zählt |
| `maxAngle` | number | `45` | Winkel, der auf 100% Eingang gemappt wird |
| `smoothing` | number | `0.2` | Glättung 0–1 gegen Wackeln |
| `sampleRate` | number | `60` | Sensorereignisse pro Sekunde |

## Steuerungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `mode` | string | `absolute` \| `relative` | Ruhelage = Ursprung oder Drift erlaubt? |
| `inverted` | boolean | `false` | Richtung umkehren |
| `parallaxDepth` | number | `0` | Parallax-Tiefe in px (Hintergrundversatz) |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `levelIndicator` | boolean | `false` | Wasserwaagen-Indikator anzeigen? |
| `hapticFeedback` | boolean | `false` | Vibration an Anschlägen? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Buttons/Slider als Ersatz (WCAG 2.5.4) |
| `disableTilt` | boolean | `false` | Sensorsteuerung komplett abschaltbar? |
| `respectReducedMotion` | boolean | `true` | Parallax bei reduzierter Bewegung deaktivieren? |
