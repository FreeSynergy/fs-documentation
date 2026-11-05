# Organization

Organization animations do not move anything themselves. They distribute start
times across several child elements and thereby decide in which order other
animations appear.

## Elements

- **stagger** - child elements start offset from one another (a fixed offset per index)
- **cascade** - an offset start along a direction, with a growing or shrinking step

## Combination

The actual movement comes from another category:

| Combination | Effect |
|-------------|--------|
| [Fade In](../entrance/fade-in/description.md) + Stagger | the list builds itself up softly |
| [Expand](../entrance/expand/description.md) + Cascade | the menu cascades down from the bar |
| [Pop Out](../exit/pop-out/description.md) + Cascade | the surface empties as a wave |
| [Scale In](../entrance/scale-in/description.md) + Stagger | the grid fills up in sequence |

## See also

- [Animations overview](../index.md)
- [Entrance](../entrance/), [Exit](../exit/)
- [grid-view](../../../components/widgets/data/grid-view/description.md) - build a grid up in stages
