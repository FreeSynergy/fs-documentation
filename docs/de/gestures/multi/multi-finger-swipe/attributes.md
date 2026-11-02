# Multi-Finger Swipe - Attribute

## Hauptattribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `onMultiFingerSwipe` | function | - | Wird beim Multi-Finger-Swipe ausgeführt |
| `onMultiFingerSwipeStart` | function | - | Finger berühren, Bewegung beginnt |
| `onMultiFingerSwipeEnd` | function | - | Finger gehoben, Richtung steht fest |

## Erkennungs-Attribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `pointerCount` | number | `3` | Erforderliche Fingeranzahl (ab 2) |
| `syncWindow` | number | `150` | Gemeinsames Down-Fenster in ms |
| `swipeThreshold` | number | `80` | Min. Distanz in px |
| `direction` | string | `left`\|`right`\|`up`\|`down`\|`any` | Erlaubte Richtung |
| `maxDuration` | number | `800` | Max. Dauer der Geste in ms |

## System-Attribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `systemGesture` | boolean | `true` | Geste gehört zur Systemnavigation? |
| `reservedByOS` | boolean | readonly | `true` wenn das OS die Geste global fängt |
| `action` | string | `task-switch` \| `workspace` \| `back` | Aktion der Geste |

## Feedback-Attribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `previewCards` | boolean | `true` | Vorschau-Karten der Ziele zeigen? |
| `hapticFeedback` | boolean | `false` | Vibration beim Auslösen? |

## Accessibility (Barrierefreiheit)

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `alternativeAction` | function | - | Button/Geste mit weniger Fingern als Ersatz |
| `reducedPointerFallback` | boolean | `false` | Variante mit weniger Fingern zulassen? |
| `voiceOverMapping` | string | - | VoiceOver-Entsprechung, falls vorhanden |
