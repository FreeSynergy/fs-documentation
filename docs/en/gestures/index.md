# Touch Gestures

Touch gestures are interaction methods for touchscreen devices.

## Gestures

| Gesture | Description | Usage |
|---------|-------------|-------|
| **Tap** | Brief touch | Button click, item selection |
| **Double Tap** | Two quick touches | Zoom, open |
| **Long Press** | Long touch | Context menu, marking |
| **Swipe** | Swiping in one direction | Navigation, switching |
| **Drag** | Dragging | Reorder, scroll |
| **Pinch** | Pulling two fingers together | Zoom out |
| **Spread** | Moving two fingers apart | Zoom in |
| **Rotate** | Turning two fingers | Rotation |
| **Shake** | Quick back-and-forth movement | Undo, error feedback, reshuffle |

## Gesture Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `onTap` | function | Executed on Tap |
| `onDoubleTap` | function | Executed on Double Tap |
| `onLongPress` | function | Executed on Long Press |
| `onSwipe` | function | Executed on Swipe |
| `onDragStart` | function | Executed on drag start |
| `onDragEnd` | function | Executed on drag end |
| `onPinch` | function | Executed on Pinch |
| `onSpread` | function | Executed on Spread |
| `onRotate` | function | Executed on Rotate |
| `onShake` | function | Executed on Shake |

## Configuration

| Attribute | Type | Description |
|-----------|------|-------------|
| `tapThreshold` | number | Time limit for Tap in ms |
| `longPressThreshold` | number | Time limit for Long Press in ms |
| `swipeThreshold` | number | Minimum distance for Swipe |
| `shakeThreshold` | number | Minimum acceleration/movement for Shake |
| `minShakes` | number | Minimum number of direction changes for Shake |
| `enabled` | boolean | Enable gestures? |

## See also

- [Shake](shake/description.md)
- [Animations](../animations/index.md)
