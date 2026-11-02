# Single-Finger Gestures (single)

Single-finger gestures are performed with exactly one finger (or a single
pointer: mouse, pen). They are the most common gesture family and largely
replace click interactions.

## Elements

- **tap** - brief touch (selection, click)
- **double-tap** - two quick touches (zoom, open)
- **long-press** - long touch (context menu, marking)
- **swipe** - swiping in one direction (navigation, switching)
- **flick** - fast swipe with lift-off and momentum (throw-scrolling)
- **drag** - dragging while pressed (reorder, scroll, moving)
- **edge-swipe** - swipe from the screen edge (back, system bars)
- **force-press** - firm pressure with a pressure sensor (peek & pop)
- **hover** - pointer over an element without contact (tooltip, preview)
- **draw-gesture** - drawing a shape/letter (shortcut)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Trigger an element | tap |
| Open/zoom quickly | double-tap |
| More options | long-press, hover |
| Switching sideways | swipe, edge-swipe |
| Scrolling with momentum | flick |
| Moving an element | drag |
| Preview then open | force-press |
| Shortcut without a menu | draw-gesture |

## Accessibility

Single-finger gestures are the recommended **single alternative** for
multi-finger and path gestures (WCAG 2.5.1). Path-based gestures such as
draw-gesture always need an alternative from this family.

## See also

- [Gesture overview](../index.md)
- [Multi-finger gestures](../multi/) - pinching, turning, several fingers
- [Combinations](../combined/) - drag-and-drop, pull-to-refresh
