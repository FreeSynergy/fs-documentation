# Radial Menu - Appearance

## Base layout

An item sits on the circle around the anchor, not in a row. The anchor core is usually
inactive; it is the starting point of all directions.

```
                        ○
                   ○         ○
              ○                 ○
          ○        ◆       ◆        ○
        ○                              ○
       ○            ◆   ●   ◆          ○      ●  anchor (centre, inactive)
        ○                              ○      ◆ items in ring 1
          ○        ◆       ◆        ○          ○ items in ring 2
              ○                 ○
                   ○         ○
                        ○
```

Geometry instead of a ruler: items are placed by **angle** and **radius**.

| Size | Meaning |
|------|---------|
| `radius` | distance anchor centre → item centre (ring 1) |
| `ringGap` | distance between two rings |
| `itemSize` | diameter of an item |
| angle step | `sweepAngle / items` — with 6 items and a full circle 60° |
| `startAngle` | alignment of the first item (0° = up) |
| `coneAngle` | angular range in which a sub-item ring appears |

## Variants

### ring (default)

```
        ◆          ◆              items lie on a circle,
            \      |              each item is its own
             \     |              hittable surface
        ◆ ──  ●  ── ◆
                    |
        ◆          ◆
```

### sektoren (pie menu)

```
   ╲   │   ╱        segments fill the ring, the centre stays
    ╲  │  ╱         empty. A segment is hit via its
  ─────●───────     angular range — not via the item centre.
    ╱  │  ╲         That is why even small pointer
   ╱   │   ╲        movements work reliably.
```

### facher (speed dial at a corner or edge)

```
   ┌───┬──────────────          anchor top right, ring clamped
   │ ●  ╲         │             inwards as a quarter or half
   │  ◆   ╲   ○   │             fan
   │   ◆    ╲     │
   └──────────────┘
```

### launcher (centred, several rings)

```
        ○   ○   ○             ring 2 = sub-items of the active
      ○  ◆  ●  ◆  ○           item. Only the active branch
        ○   ◆   ○             opens the next ring.
```

### kontext (at the pointer position)

```
   right-click ──►  ● at the pointer position,
                    rings grow outwards from there
```

## Sizes

| Size | Anchor Ø | Item Ø | Radius R1 | Radius R2 | Use |
|------|----------|--------|-----------|-----------|-----|
| `small` | 28 px | 32 px | 56 px | 96 px | dense surfaces, map, whiteboard |
| `medium` | 36 px | 40 px | 72 px | 124 px | standard on desktop |
| `large` | 44 px | 48 px | 88 px | 148 px | touch, kiosk, controller |

`large` matches the minimum hit area from the [base component](../../../primitives/basics/base.md).
On touch surfaces `small` is unsuitable because the items in the ring touch each other.

## Colours and states

| State | Appearance | Description |
|-------|------------|-------------|
| **default** | primary tone, saturated | item in an open ring |
| **hover** | lighter, slightly larger | pointer stands on the item |
| **active** | accent colour, filled core | item selected or its branch opened |
| **focus** | 2 px ring outline outside | item reached via keyboard |
| **dimmed** | saturated → 40 % opacity | item does not belong to the active branch |
| **pinned** | subtle shadow glow | menu stays open after a click |
| **disabled** | greyed out, no outline | item not selectable |
| **loading** | [spinner](../../../primitives/feedback/spinner/) in the item | target is still loading |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `grow` | item grows to 110 % (`scaleOnHover`) |
| `shift` | item moves 4–8 px radially outwards (`shiftOnHover`) |
| `lift` | shadow grows, item lifts off the ring |
| `glow` | glow around the outline of the active item |
| `morph` | shape of the active item changes smoothly (circle → hexagon) |
| `ring-rotate` | the whole ring rotates a little so the active item points up |
| `label-reveal` | the label only appears on the activated item |
| `sector-lift` | in `sektoren`: the segment pops out of the ring as a wedge |

## Responsive

| Breakpoint | Behaviour |
|------------|-----------|
| desktop | open on hover (`trigger: hover`), sub-items in the next ring |
| tablet | open by tap, sub-items after a second tap |
| mobile (< 600 px) | one ring, `large`, selection by press–drag–release |
| narrow edge | `clamp`: the full circle becomes a quarter or half fan |
| `prefers-reduced-motion` | `radial-out` → `fade-in`, no growth, no co-rotation |
| very large surfaces (whiteboard, map) | up to three rings, `launcher` freely positionable |

## Shapes and corners

Shape and number of corners carry information — they are not just decoration.

| Shape (`shape`) | Corners | Description | Use |
|-----------------|---------|-------------|-----|
| `kreis` | – | smooth circular surface | standard in all rings |
| `quadrat` | 4 | polygon with `cornerRadius = 0` | angular surfaces, grid look |
| `abgerundet` | 4 | polygon with softly rounded corners | bridge between angular and round |
| `squircle` | 4 | superellipse: smoothly rounded throughout | icon look, touch surfaces |
| `dreieck` | 3 | with `rotation` so one corner points outwards | indicates the direction of the item |
| `fuenfeck` | 5 | pentagon | marking of a special item |
| `sechseck` | 6 | tessellatable, neighbours fit flush | several menus side by side, honeycombs |
| `achteck` | 8 | polygon with eight corners | distinguishing without looking like a circle |
| `vieleck` | `sides` = 3–12 | regular polygon with adjustable corner count | corner count shows the number of items in the ring |
| `keil` | 2 corners + arc | pie segment (`sektoren`) | direction selection, large hit area |
| `bluete` | n waves | wavy edge, one wave per neighbouring item | the edge counts the items in the ring |
| `stern` | 2n points | points face the neighbours | only the active item of a ring |

Rules for the corner count:

- `sides` grows from 3 (triangle) through 4, 5, 6, 8 up to 12. From about 8 corners **and**
  `cornerRadius > 0` the shape reads as a circle — so for a distinguishable silhouette either
  keep at most 6 corners or keep sharp corners.
- `cornerRadius` controls the rounding independently of that: `0` = sharp corner, half the
  side length = strongly rounded, beyond that the shape grows towards a circle. A square with
  half its side length as radius is a circle — the rounding is a continuum, not a switch.
- Grasp the corner count as information: 3 corners = "direction", 6 corners = "group",
  `sides = items` = "this many items the ring has". Otherwise the shape stays neutral.
- Only the **active** item changes its shape (`morph`), the others stay constant —
  otherwise the whole ring flickers.
- `rotation` turns the shape so that a corner, point or wave faces outwards towards the ring.
- The anchor core (`●`) always keeps the basic shape; if it changes shape, the menu itself
  reads as an action.

## Rings and levels

| Level | Ring | Radius | Content |
|-------|------|--------|---------|
| 1 | ring 1 | `radius` | main items of the menu |
| 2 | ring 2 | `radius + itemSize + ringGap` | sub-items of the active item |
| 3 | ring 3 | `radius + 2 · (itemSize + ringGap)` | sub-sub-items |

- Only the active branch opens the next ring; the other items stay in the previous ring.
- The items of a new ring appear in the **angular range** of their parent item
  (`coneAngle`), not spread over the whole circle.
- An item may not lie deeper than the anchor is far from the edge — then `clamp` kicks in
  and the ring becomes a fan.
- Siblings of the active item become `dimmed`, but their angular range stays hittable
  (direct switch without a detour via the anchor).

## See also

- [Radial Menu – description](./description.md)
- [Attributes](./attributes.md)
- [Usage](./usage.md)
- [radial-out](../../../../interactions/animations/entrance/radial-out/) and [radial-in](../../../../interactions/animations/exit/radial-in/)
