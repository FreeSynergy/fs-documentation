# Loop

Loop animations run repeatedly until a state ends. They need a long duration
(800–2000 ms per cycle) and pause as soon as the element is not visible.

## Elements

- **spin** - a lasting rotation (loader, activity)
- **pulse** - a cyclic swelling and shrinking (attention)
- **heartbeat** - a double pulse in the rhythm of a heart rate
- **glow** - a glow around the contour (selection, live status)

## Differentiation

Lasting loading states with a structure are in [loading](../loading/), movements
of layers are in [movement](../movement/).

## Mandatory rules

- always bind `iterationCount: infinite` to a state (progress, connection)
- pause outside the viewport (`playState: paused`)
- never two loop animations in the same field of view at the same time

## See also

- [Animations overview](../index.md)
- [Loading](../loading/)
- [Feedback](../feedback/) - a one-time response instead of continuous running
