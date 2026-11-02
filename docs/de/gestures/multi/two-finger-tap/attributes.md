# Two-Finger Tap - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onTwoFingerTap` | function | - | Wird beim Zwei-Finger-Tap ausgeführt |

## Erkennungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `pointerCount` | number | `2` | Anzahl erforderlicher Finger |
| `maxTouchDelay` | number | `100` | Max. Zeitversatz zwischen dem Aufsetzen beider Finger in ms |
| `tapThreshold` | number | `300` | Max. Berührungsdauer in ms |
| `moveTolerance` | number | `10` | Erlaubte Bewegung in px |
| `minFingerDistance` | number | `20` | Mindestabstand der Finger in px |

## Kontext-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `action` | string | `secondary` | Aktionstyp (`secondary`, `zoom`, `custom`) |
| `contextMenu` | node | - | Menü, das bei `secondary` geöffnet wird |
| `enabled` | boolean | `true` | Geste aktiv? |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hapticFeedback` | boolean | `false` | Vibration bei Sekundäraktion? |
| `ripple` | boolean | `true` | Ripple an beiden Berührungspunkten? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Kontextmenü-Button / Long Press als Ersatz |
| `longPressEquivalent` | boolean | `true` | Reagiert Long Press auf dieselbe Aktion? |
| `aria-label` | string | - | Beschreibung der Sekundäraktion |
