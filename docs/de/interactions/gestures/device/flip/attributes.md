# Flip - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onFlip` | function | - | Wird beim Umdrehen ausgeführt |
| `onFlipBack` | function | - | Gerät wurde zurückgedreht |
| `onFlipStart` | function | - | Drehbewegung beginnt |

## Sensor-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `flipAngle` | number | `150` | Ab welchem Winkel (Grad) gilt die Lage als umgedreht? |
| `holdTime` | number | `1000` | Min. Zeit in umgedrehter Lage in ms |
| `maxFlipTime` | number | `2000` | Max. Dauer des Umdrehens in ms |
| `requireProximity` | boolean | `false` | Näherungssensor zusätzlich prüfen? |

## Aktions-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `action` | string | `mute` \| `dnd` \| `custom` | Aktion beim Flip |
| `autoRevert` | boolean | `true` | Aktion endet beim Zurückdrehen? |
| `onlyWhileRinging` | boolean | `false` | Nur bei eingehendem Anruf aktiv? |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hapticFeedback` | boolean | `true` | Vibration bei Aktivierung? |
| `soundFeedback` | boolean | `false` | Bestätigungston? |
| `confirmationToast` | boolean | `true` | „Nicht stören aktiv“-Meldung? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Schalter/Button als gleichwertiger Weg (WCAG 2.5.4) |
| `enabled` | boolean | `true` | Geste abschaltbar? |
