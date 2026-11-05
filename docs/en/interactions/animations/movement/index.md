# Movement

Movement animations hang on scrolling or on the position in the document, not on
a single action. They change the speed of layers relative to one another.

## Elements

- **parallax** - layers move at differing speeds

## Differentiation

Parallax is tied to the scroll progress and repeatable; a one-time displacement
of an element belongs in [entrance](../entrance/) or
[transition](../transition/).

## Mandatory rules

- at most two layers with a clear difference in speed
- switch it off entirely under `prefers-reduced-motion` – movement in the field of
  view is for many users the strongest trigger of discomfort
- never combine it with text blocks whose reading flow would tip as a result

## See also

- [Animations overview](../index.md)
- [Stagger](../organization/stagger/description.md) - a temporal rather than spatial staggering
- [Accessibility](../index.md#accessibility)
