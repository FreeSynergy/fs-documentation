# Tap Gestures (tap)

Tap gestures are short touches **without a traveled path**: what decides is
contact, time or pressure – not a movement.

The four base gestures are multipoint-capable: they work with any number of
fingers up to the device limit (recognised at the centre of all pointers).
The multi-finger variants require two or more fingers by definition – their
count is a setting (`pointerCount`), not a separate gesture type.

## Elements

- **tap** - brief touch (selection, click)
- **double-tap** - two quick touches (zoom, open)
- **long-press** - long touch (context menu, marking)
- **force-press** - pressure via pressure sensor (peek & pop)
- **multi-finger-tap** - tapping with two or more fingers (secondary action)
- **multi-finger-long-press** - long press with two or more fingers (secondary menu, multiselect)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Select element / trigger button | tap |
| Open or zoom by double tap | double-tap |
| Context menu | long-press (or force-press where available) |
| Secondary action without a right mouse button | multi-finger-tap |
| Multiselect / secondary menu with holding | multi-finger-long-press |

## Accessibility

The four base gestures are single-pointer-friendly; per WCAG 2.5.1 the
multi-finger variants need a single-finger alternative (long press or
button). Force press is unavailable without a pressure sensor – always
provide a long-press fallback.

## See also

- [Gesture overview](../index.md)
- [Swipe](../swipe/swipe/description.md) - swiping instead of tapping
- [Press animation](../../animations/feedback/press/description.md) - answer to pressure
