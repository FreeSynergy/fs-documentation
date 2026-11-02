# Multi-Finger Tap - Attribute

## Hauptattribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `onMultiFingerTap` | function | - | Wird beim Multi-Finger-Tap ausgeführt |

## Erkennungs-Attribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `pointerCount` | number | `2` | Anzahl erforderlicher Finger (2, 3, 4, 5 …) |
| `maxTouchDelay` | number | `100` | Max. Zeitversatz zwischen dem Aufsetzen aller Finger in ms |
| `tapThreshold` | number | `300` | Max. Berührungsdauer in ms |
| `moveTolerance` | number | `10` | Erlaubte Bewegung in px |
| `minFingerDistance` | number | `20` | Mindestabstand der Finger in px |

## Kontext-Attribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `action` | string | `secondary` | Aktionstyp (`secondary`, `zoom`, `custom`) |
| `contextMenu` | node | - | Menü, das bei `secondary` geöffnet wird |
| `enabled` | boolean | `true` | Geste aktiv? |

## Feedback-Attribute

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `hapticFeedback` | boolean | `false` | Vibration bei Sekundäraktion? |
| `ripple` | boolean | `true` | Ripple an jedem Berührungspunkt? |

## Accessibility (Barrierefreiheit)

| Attribute | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `alternativeAction` | function | - | Kontextmenü-Button / Long Press als Ersatz |
| `longPressEquivalent` | boolean | `true` | Reagiert Long Press auf dieselbe Aktion? |
| `aria-label` | string | - | Beschreibung der Sekundäraktion |
