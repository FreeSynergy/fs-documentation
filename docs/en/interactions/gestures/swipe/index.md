# Swipe Gestures (swipe)

Swipe gestures perform a **connected movement** in one direction – guiding,
with momentum, or as a drawn path. Start position and speed tell the
individual gestures apart.

All swipe gestures are multipoint-capable: any number of fingers up to the
device limit is recognised as one gesture at the centre of all pointers. The
multi-finger swipe requires two or more fingers by definition (`pointerCount`
as a setting). One exception: draw-gesture draws a single connected stroke –
further fingers create their own paths.

## Elements

- **swipe** - gliding in one direction (navigation, switching)
- **flick** - swipe with momentum and lift-off (throw-scrolling)
- **drag** - dragging while pressed (reorder, scroll)
- **edge-swipe** - swipe from the screen edge (back, system bars)
- **multi-finger-swipe** - swiping with two or more fingers (app/workspace switching)
- **draw-gesture** - drawn shape/letter (shortcuts, commands)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Change direction, page through | swipe |
| Throw a list far | flick |
| Guide an element (sort, scroll) | drag |
| Back / system bars out of the edge | edge-swipe |
| App or workspace switching | multi-finger-swipe |
| Shortcut by shape/letter | draw-gesture |

## Accessibility

Per WCAG 2.5.1 and 2.5.7 swipe gestures need single-pointer alternatives
(buttons, switches); the multi-finger swipe additionally a variant with
fewer fingers. Edge gestures (edge-swipe) must never be the only way.

## See also

- [Gesture overview](../index.md)
- [Swipe](swipe/description.md) - base gesture of the family
- [Slide animation](../../animations/entrance/slide-in/description.md) - answer to swipe gestures
