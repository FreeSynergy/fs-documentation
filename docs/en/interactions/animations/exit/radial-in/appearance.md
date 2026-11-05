# Radial In - Appearance

## Base layout

The anchor core stays standing as the gathering point. Each point leaves its
ring position and travels back along its angle ray to the anchor centre,
shrinking and fading as it goes. The rings dissolve from the outside inward.

## Visual progress

```
┌──────────────────────────────────────────────────────────────┐
│   0 ms           50 ms            110 ms           160 ms    │
│                                                              │
│  ◆ ○ ◆         ◆   ●   ◆       ◆  ◆ ●          core only ●  │
│  all rings     ring 2 nearly    only ring 1    s = 0, α = 0  │
│  stand         gone, α → 0      at half        core fades    │
│                                radius, s → 0   out last      │
└──────────────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | all points at once, a short linear pull movement (160 ms) |
| **Rings in sequence** | the outermost ring first, `ringStep` passed inward |
| **Branch only** | if the pointer leaves a point, only that point's sub-ring travels back |
| **Fan** | at a corner or edge: the points step back into the corner |
| **Pull** | points accelerate towards the anchor (`ease-in`), looks "sucked in" |

## Duration

- Typical: 120–200 ms
- Default value: 160 ms
- Points among themselves: 8–15 ms offset (`staggerStep`)
- Rings among themselves: 40–60 ms offset (`ringStep`), order `outside-in`

## See also

- [Animations overview](../../index.md)
- [Radial Out](../../entrance/radial-out/description.md)
- [Radial Menu](../../../../components/widgets/navigation/radial-menu/description.md)
