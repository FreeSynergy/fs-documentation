# Combined Gestures (combined)

Combined gestures are made up of simple gestures, or arise from the
interplay of gesture and context (list, list + time). They are documented
in their own right because they have their own attributes and cancellation
rules.

The pointer count follows the base gestures (drag): both gestures work with
one as well as several fingers (multipoint-capable up to the device limit).

## Elements

- **pull-to-refresh** - pulling down at the top boundary of a list (refresh)
- **drag-and-drop** - grabbing, pulling, dropping onto a drop zone (moving)

## Mapping

| Situation | Gesture |
|-----------|---------|
| Reloading content | pull-to-refresh |
| Bringing an element elsewhere | drag-and-drop |
| Changing the order | drag-and-drop (with reorder animation) |

## Accessibility

Under WCAG 2.5.7 (Dragging Movements), every drag interaction needs a
single-pointer alternative ("up/down" buttons, select + paste). Always
supplement `pull-to-refresh` with an explicit refresh button.

## See also

- [Gesture overview](../index.md)
- [Drag](../swipe/drag/description.md) - base gesture of drag-and-drop
- [Reorder animation](../../animations/transition/reorder/description.md) - answer to drag-and-drop
