# Three-Finger Swipe - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onThreeFingerSwipe` | function | - | Wird beim Drei-Finger-Wisch ausgeführt |
| `onThreeFingerSwipeStart` | function | - | Drei Finger berühren, Bewegung beginnt |
| `onThreeFingerSwipeEnd` | function | - | Finger gehoben, Richtung steht fest |

## Erkennungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `pointerCount` | number | `3` | Erforderliche Fingeranzahl |
| `syncWindow` | number | `150` | Gemeinsames Down-Fenster in ms |
| `swipeThreshold` | number | `80` | Min. Distanz in px |
| `direction` | string | `left`\|`right`\|`up`\|`down`\|`any` | Erlaubte Richtung |
| `maxDuration` | number | `800` | Max. Dauer der Geste in ms |

## System-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `systemGesture` | boolean | `true` | Geste gehört zur Systemnavigation? |
| `reservedByOS` | boolean | readonly | `true` wenn das OS die Geste global fängt |
| `action` | string | `task-switch` \| `workspace` \| `back` | Aktion der Geste |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `previewCards` | boolean | `true` | Vorschau-Karten der Ziele zeigen? |
| `hapticFeedback` | boolean | `false` | Vibration beim Auslösen? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Button/Geste mit weniger Fingern als Ersatz |
| `twoFingerFallback` | boolean | `false` | Zwei-Finger-Variante zulassen? |
| `voiceOverMapping` | string | - | VoiceOver-Entsprechung, falls vorhanden |
