# Touch Gestures

Touch gestures are interaction methods for touchscreen devices (and related
pointers: mouse, pen, motion sensors). Gestures are **inputs** – the visual
answer to them is an [animation](../animations/index.md).

Gestures are grouped into four families (mirroring the animation categories).

## Families

| Family | Principle | Gestures |
|--------|-----------|----------|
| `single` (single-pointer) | From one pointer, mostly replaces clicks – all multipoint-capable | 10 |
| `multi` (multi-pointer) | Two+ pointers (never one), the count is a setting, transforms content | 6 |
| `device` | Movement of the device itself (sensors, no pointers) | 4 |
| `combined` | Composite gestures with their own logic | 2 |

## Pointer Count: Single-Point and Multipoint

A touch sensor reports every simultaneous contact; depending on the device,
five to ten fingers are detected at once. From this follow the rules for all
gestures:

- **Single-point gestures are multipoint-capable.** Tap, double tap, long
  press, swipe, flick, drag, edge swipe and force press work with any number
  of fingers up to the device limit – recognised on the primary pointer or on
  the centre of all pointers. “Single” is the minimum, not the maximum.
- **Multipoint always covers every finger count.** A gesture carries no limit
  of its own; the ceiling is always the device limit.
- **Multi gestures cannot run single-point.** Pinch, spread and rotate
  require two pointers by necessity (distance and angle only exist from two
  on), and the multi-finger variants do by definition.
- **Two exceptions without multipoint:** `draw-gesture` (one path is one
  connected stroke – further fingers create their own, separate paths) and
  `hover` (no contact; a hovering multi-finger pointer does not exist).
- **Device gestures know no pointer count:** shake, tilt, flip and wave run
  on sensors, touches play no role.

| Family / Gesture | Single-Point | Multipoint | Basis |
|------------------|--------------|------------|-------|
| single (all but draw-gesture, hover) | ✓ | ✓ up to device limit | primary pointer / pointer centre |
| single: draw-gesture | ✓ | ✗ | one path = one stroke |
| single: hover | ✓ | ✗ | only one hovering pointer |
| multi (all) | ✗ | ✓ up to device limit | at least two pointers needed |
| device (all) | not applicable | not applicable | sensors instead of pointers |
| combined | ✓ | ✓ | follows its base gestures (drag) |

## All Gestures

| Gesture | Family | Description | Usage |
|---------|--------|-------------|-------|
| **Tap** | single | Brief touch | Button click, item selection |
| **Double Tap** | single | Two quick touches | Zoom, open |
| **Long Press** | single | Long touch | Context menu, marking |
| **Swipe** | single | Swiping in one direction | Navigation, switching |
| **Flick** | single | Fast swipe with lift-off momentum | Throw-scrolling |
| **Drag** | single | Dragging while pressed | Reorder, scroll |
| **Edge Swipe** | single | Swipe from the screen edge | Back, system bars |
| **Force Press** | single | Pressure via pressure sensor | Peek & pop, context |
| **Hover** | single | Pointer over element without contact | Tooltip, preview |
| **Draw Gesture** | single | Drawing a shape/letter | Shortcuts, commands |
| **Pinch** | multi | Pulling pointers together (from two) | Zoom out |
| **Spread** | multi | Moving pointers apart (from two) | Zoom in |
| **Rotate** | multi | Turning pointers (from two) | Rotation |
| **Multi-Finger Tap** | multi | Tapping with several fingers | Secondary action |
| **Multi-Finger Long Press** | multi | Long press with several fingers | Secondary menu, multiselect |
| **Multi-Finger Swipe** | multi | Swiping with several fingers | App/workspace switching |
| **Shake** | device | Quick back-and-forth movement | Undo, error feedback, reshuffle |
| **Tilt** | device | Tilting the device | Steering, parallax |
| **Flip** | device | Turning the device over | Mute, do not disturb |
| **Wave** | device | Waving a hand over a sensor | Answer calls, air gestures |
| **Pull to Refresh** | combined | Pulling at the list top edge | Refresh |
| **Drag and Drop** | combined | Grab, move, drop | Move, combine |

## Gesture Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `onTap` | function | Executed on Tap |
| `onDoubleTap` | function | Executed on Double Tap |
| `onLongPress` | function | Executed on Long Press |
| `onSwipe` | function | Executed on Swipe |
| `onFlick` | function | Executed on Flick |
| `onDragStart` | function | Executed on drag start |
| `onDragEnd` | function | Executed on drag end |
| `onEdgeSwipe` | function | Executed on Edge Swipe |
| `onForcePress` | function | Executed on Force Press |
| `onHoverStart` / `onHoverEnd` | function | Hover starts/ends |
| `onDrawGesture` | function | Executed after a recognized shape |
| `onPinch` | function | Executed on Pinch |
| `onSpread` | function | Executed on Spread |
| `onRotate` | function | Executed on Rotate |
| `onMultiFingerTap` | function | Executed on Multi-Finger Tap |
| `onMultiFingerLongPress` | function | Executed on Multi-Finger Long Press |
| `onMultiFingerSwipe` | function | Executed on Multi-Finger Swipe |
| `onShake` | function | Executed on Shake |
| `onTilt` | function | Executed on tilt |
| `onFlip` | function | Executed on Flip |
| `onWave` | function | Executed on Wave |
| `onRefresh` | function | Executed on Pull to Refresh |
| `onDrop` | function | Executed on drop (Drag and Drop) |

## Configuration

| Attribute | Type | Description |
|-----------|------|-------------|
| `tapThreshold` | number | Time limit for Tap in ms |
| `longPressThreshold` | number | Time limit for Long Press in ms |
| `swipeThreshold` | number | Minimum distance for Swipe |
| `velocityThreshold` | number | Minimum velocity for Flick in px/s |
| `edgeSize` | number | Width of the edge zone for Edge Swipe in px |
| `pointerCount` | number | Minimum pointer count for the gesture (single: 1, multi: 2 or 3 …) – limited above by the device |
| `shakeThreshold` | number | Minimum acceleration/movement for Shake |
| `minShakes` | number | Minimum number of direction changes for Shake |
| `deadZone` | number | Degree tolerance for Tilt |
| `matchThreshold` | number | Shape similarity for Draw Gesture (0–1) |
| `enabled` | boolean | Enable gestures? |

## Standards and Accessibility

| Rule | Meaning |
|------|---------|
| WCAG 2.5.1 Pointer Gestures | Multi-point and path gestures need a single-pointer alternative |
| WCAG 2.5.2 Pointer Cancellation | Execute the action on release, not on press |
| WCAG 2.5.4 Motion Actuation | Sensor gestures (shake, tilt, flip, wave) need a UI alternative |
| WCAG 2.5.7 Dragging Movements | Drag needs a single-pointer alternative |
| `touch-action` (CSS) | Control browser-native gestures (pan, pinch-zoom) |

## See also

- Families: [single](single/) · [multi](multi/) · [device](device/) · [combined](combined/)
- [Animations](../animations/index.md) — Shake, Wiggle as feedback to gestures
