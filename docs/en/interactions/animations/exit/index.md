# Exit

Exit animations make an element disappear and its space become free. They may
last noticeably shorter than the matching entrance.

## Elements

- **fade-out** - gradually blend out (opacity 1 → 0)
- **slide-out** - glide out to the outside
- **zoom-out** - scale from full size to null
- **scale-out** - shrink from 100 % to 0 %
- **bounce-out** - spring before it disappears
- **pop-out** - briefly anticipate and fold away (chips, badges)
- **collapse** - reduce height or width to 0 (accordion closing)
- **radial-in** - points travel back to the anchor (closing a circular menu)

## Families

Each entry has its counterpart in [entrance](../entrance/): `fade-out` ↔
`fade-in`, `slide-out` ↔ `slide-in`, `zoom-out` ↔ `zoom-in`, `scale-out` ↔
`scale-in`, `bounce-out` ↔ `bounce-in`, `pop-out` ↔ `pop-in`, `collapse` ↔
`expand`, `radial-in` ↔ `radial-out`.

## Note on layout

The element is only taken out of the layout after `onAnimateEnd`. Removing it
before that tears the rest of the surface abruptly open – which reads as
stronger than any exit animation.

## See also

- [Animations overview](../index.md)
- [Entrance](../entrance/)
- [Accordion](../../../components/widgets/containers/accordion/description.md), [Toast](../../../components/primitives/feedback/toast/description.md)
- [Radial Menu](../../../components/widgets/navigation/radial-menu/description.md) - uses `radial-in` when closing
