# Two-Finger Long Press - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onTwoFingerLongPress` | function | - | Wird beim Zwei-Finger-Langdruck ausgeführt |
| `onTwoFingerLongPressMove` | function | - | Bewegung während des gehaltenen Drucks |
| `onTwoFingerLongPressEnd` | function | - | Finger wurden gehoben |

## Threshold-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `longPressThreshold` | number | `500` | Haltezeit in ms bis zur Erkennung |
| `pointerCount` | number | `2` | Erforderliche Fingeranzahl |
| `moveTolerance` | number | `10` | Erlaubte Bewegung in px |
| `maxTouchDelay` | number | `100` | Max. Zeitversatz beim Aufsetzen in ms |

## Auswahl-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `extendSelection` | boolean | `false` | Auswahl durch Bewegung erweitern? |
| `multiSelect` | boolean | `false` | Danach Mehrfachauswahl-Modus aktivieren? |
| `dragAfterHold` | boolean | `false` | Drag-Start nach Halten erlauben? |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hapticFeedback` | boolean | `true` | Vibration beim Erreichen des Threshold? |
| `progressRing` | boolean | `false` | Fortschrittsring bis zum Threshold anzeigen? |
| `contextMenu` | node | - | Menü, das nach dem Halten erscheint |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Ein-Finger-Long-Press oder Button als Ersatz (WCAG 2.5.1) |
| `longPressEquivalent` | boolean | `true` | Ein-Finger-Long-Press löst dieselbe Aktion aus? |
