# Entrance

Entrance animations make an element appear. Almost every one of them has a
counterpart in [exit](../exit/): the same family, only the opposite direction.

## Elements

- **fade-in** - gradually blend in (opacity 0 → 1)
- **slide-in** - glide in from outside
- **zoom-in** - scale from small to full size
- **scale-in** - grow from 0 % to 100 %
- **bounce-in** - spring as it arrives
- **pop-in** - fade in with a short overshoot (chips, badges, avatars)
- **expand** - grow height or width from 0 to the content
- **unfold** - open out like a sheet
- **radial-out** - points grow radially out of an anchor (circular menu)

## Families

`fade-in`, `slide-in`, `zoom-in`, `scale-in`, `bounce-in` and `radial-out` are
the entrance sides of the families `fade`, `slide`, `zoom`, `scale`, `bounce`
and `radial`. Shared attributes such as `duration`, `timingFunction` and
`fillMode` are documented in the [overview](../index.md).

## See also

- [Animations overview](../index.md)
- [Exit](../exit/)
- [Organization](../organization/) - staggered start of several entrances
- [Toast](../../../components/primitives/feedback/toast/description.md), [Modal](../../../components/widgets/overlays/modal/description.md)
- [Radial Menu](../../../components/widgets/navigation/radial-menu/description.md) - uses `radial-out` when opening
