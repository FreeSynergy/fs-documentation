# Transition

Transition animations change an existing state without creating or removing
elements. Both states belong to the same surface; the animation makes the change
traceable.

## Elements

- **flip** - turn by 180° (front and back side)
- **rotate** - turn around its own axis
- **morph** - softly move a shape into another shape
- **cross-fade** - two elements cross-fade into each other
- **cross-slide** - two elements push each other out of view
- **reorder** - list elements softly swap their places (FLIP)

## Choice

| Change | Animation |
|--------|-----------|
| same element, new shape | morph |
| different element, no directional reference | cross-fade |
| different element, with an order | cross-slide |
| two sides of one object | flip |
| the order changes | reorder |
| the angle changes | rotate (persistently as [Spin](../loop/spin/description.md)) |

## See also

- [Animations overview](../index.md)
- [Entrance](../entrance/), [Exit](../exit/)
- [Tabs](../../../components/widgets/navigation/tabs/description.md), [Accordion](../../../components/widgets/containers/accordion/description.md)
