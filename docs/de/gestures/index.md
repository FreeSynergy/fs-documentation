# Touch-Gesten

Touch-Gesten sind Interaktionsmethoden für Touchscreen-Geräte.

## Gesten

| Geste | Beschreibung | Verwendung |
|-------|-------------|------------|
| **Tap** | Kurze Berührung | Button-Klick, Item-Auswahl |
| **Double Tap** | Zwei schnelle Berührungen | Zoom, Öffnen |
| **Long Press** | Lange Berührung | Kontextmenü, Markierung |
| **Swipe** | Wischen in eine Richtung | Navigation, Switchen |
| **Drag** | Ziehen | Reorder, Scroll |
| **Pinch** | Zwei Finger zusammenziehen | Zoom out |
| **Spread** | Zwei Finger auseinanderziehen | Zoom in |
| **Rotate** | Zwei Finger drehen | Rotieren |
| **Shake** | Schnelles Hin- und Herbewegen | Undo, Fehler-Feedback, Neu mischen |

## Gesten-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onTap` | function | Wird beim Tap ausgeführt |
| `onDoubleTap` | function | Wird beim Double Tap ausgeführt |
| `onLongPress` | function | Wird beim Long Press ausgeführt |
| `onSwipe` | function | Wird beim Swipe ausgeführt |
| `onDragStart` | function | Wird beim Drag-Start ausgeführt |
| `onDragEnd` | function | Wird beim Drag-Ende ausgeführt |
| `onPinch` | function | Wird beim Pinch ausgeführt |
| `onSpread` | function | Wird beim Spread ausgeführt |
| `onRotate` | function | Wird beim Rotate ausgeführt |
| `onShake` | function | Wird beim Shake ausgeführt |

## Konfiguration

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `tapThreshold` | number | Zeitlimit für Tap in ms |
| `longPressThreshold` | number | Zeitlimit für Long Press in ms |
| `swipeThreshold` | number | Minimaler Abstand für Swipe |
| `shakeThreshold` | number | Minimale Beschleunigung/Bewegung für Shake |
| `minShakes` | number | Minimale Anzahl Richtungswechsel für Shake |
| `enabled` | boolean | Gesten aktivieren? |

## Siehe auch

- [Tap](tap/description.md)
- [Double Tap](double-tap/description.md)
- [Long Press](long-press/description.md)
- [Swipe](swipe/description.md)
- [Drag](drag/description.md)
- [Pinch](pinch/description.md)
- [Spread](spread/description.md)
- [Rotate](rotate/description.md)
- [Shake](shake/description.md)
- [Animationen](../animations/)
