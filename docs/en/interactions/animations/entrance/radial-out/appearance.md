# Radial Out - Appearance

## Base layout

The anchor core stays put. Each point begins at `scale 0` in the anchor centre
and travels along its angle ray to its ring position. The movement is radial:
the shortest way to a point is at the same time the direction that gets
selected.

## Visual progress

```
┌──────────────────────────────────────────────────────────────┐
│   0 ms           70 ms            150 ms           220 ms    │
│                                                              │
│     ●          ◆   ●   ◆       ◆  ◆ ● ◆  ◆      ◆ ○ ◆       │
│  only core    points at 30 %   ring 1 nearly    ring 1 set,  │
│  s = 0        radius, s = 0.4  done, α = 1      ring 2 steps │
│  α = 0        α = 0.5                           out of it    │
└──────────────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | points staggered clockwise, one ring (220 ms) |
| **Rings in sequence** | ring 2 starts `ringStep` after the last point of ring 1 |
| **Fan** | at a corner or edge: only the unclamped angular range fills up |
| **Gentle** | without overshoot, `ease-out` – for dense menus |
| **With overshoot** | points shoot 4 % past the ring position and spring back |

## Duration

- Typical: 180–260 ms per ring
- Default value: 220 ms
- Points among themselves: 12–25 ms offset (`staggerStep`)
- Rings among themselves: 60–90 ms offset (`ringStep`)

## See also

- [Animations overview](../../index.md)
- [Radial In](../../exit/radial-in/description.md)
- [Radial Menu](../../../../components/widgets/navigation/radial-menu/description.md)
- [Stagger](../../organization/stagger/description.md)
