# Radial Menu

| Field | Value |
|-------|-------|
| **Category** | `navigation` |
| **Inherits from** | `base`, `menu` |
| **Variants** | `ring`, `sektoren`, `facher`, `launcher`, `kontext` |
| **States** | `open`, `expanded`, `dimmed`, `pinned` |
| **Gestures** | `tap`, `long-press`, `drag`, `rotate` |
| **Animations** | `radial-out`, `radial-in`, `stagger`, `lift`, `morph` |
| **Related** | `menu`, `context-menu`, `floating-action-button`, `toolbar`, `command` |
| **Role** | `menu` |
| **State** | documented |

!!! info "Standardisation"
    The action fan of the [floating-action-button](../../../primitives/actions/floating-action-button/)
    (`expanded`) and the circular right-click menu are variants of **one**
    component: `radial-menu` with `variant: facher` or `variant: kontext`. The FAB
    remains the *one* main action of the view; it merely anchors the circular menu
    (`anchor: "fab"`).

## Description

A radial menu (circular menu) arranges menu items around a centre point. The anchor
sits in the middle, the items lie on a ring. If an item has sub-items, they appear in
the **next ring** around the first one: two levels become two rings, three levels
become three. The anchor point itself is usually inactive and only serves as a starting point.

Selection happens by **direction** towards the item, not by distance. The pointer therefore
only has to travel briefly in the right direction — the item remains hittable even when it
lies further away. Repetition leads to muscle memory: experienced users pick the item
without looking at the menu.

The anchor is freely choosable: corner, edge midpoint, screen centre, free coordinates, the
position of another element, or the pointer itself. The same element therefore works just as
well in the top right as in the middle of the surface; at an edge the full circle is
automatically clamped into a fan.

!!! note "Origin"
    Radial menus are nothing new: the first documented case is PIXIE (1969), the first
    measured comparison with linear menus (1988) showed around 15 % shorter selection time
    with fewer errors. The best-known form is the **Pie Menu** with pie segments around an
    empty centre (inactive core, direction selection); the **Marking Menu** is the related
    gesture without a visible menu. `sektoren` is the pie form, `ring` the form common today
    with individual item surfaces.

## Purpose

- recurring actions in a fixed place, driven from muscle memory
- actions at the pointer (right-click, long-press) as the round variant of the context menu
- quick access in surface-based programs: [whiteboard](../../../workbenches/special/whiteboard/),
  [map-view](../../special/map-view/), editors
- corner and edge menus that grow on hover and push their sub-items outwards
- launcher in the screen centre on touch, kiosk and large-screen surfaces
- menu navigation on controllers and stylus (direction instead of aiming precision)

## Variants

| Variant | Description |
|---------|-------------|
| **ring** | item surfaces on a ring around the anchor — default, 3–8 items |
| **sektoren** | pie segments around an empty centre (pie menu): selected by angular range, very large hit areas |
| **facher** | ring segment instead of a full circle (half or quarter circle) emerging from a corner or edge, also as a speed dial |
| **launcher** | free-standing circle, usually in the screen centre, with sub-items in further rings |
| **kontext** | appears at the pointer position (right-click, long-press) |

## Features

- **A ring per level** — a point's sub-items appear in the next ring (`levels`, at most three)
- **Free anchor** — nine edge and corner positions, screen centre, free coordinates, `anchor` pointing at another element, or the pointer position
- **Edge clamping** — `clamp` turns the full circle into a quarter or half fan at a corner or edge; the whole ring stays visible
- **Hover** — the item grows, moves a little outwards and casts a shadow; its sub-items fan out outwards in a stagger
- **Travel tolerance** — `closeDelay` lets the pointer travel between the rings without the menu closing
- **Shapes** — circle, polygon with 3–12 corners, squircle, wedge, flower (see [Shapes and corners](./appearance.md#shapes-and-corners))
- **Direction selection** — in `sektoren` an item counts as hit as soon as the pointer is inside its angular range
- **Keyboard** — arrow keys move around the ring, `Enter` goes one level in, `Esc` goes back; 4- and 8-item rings sit on the arrow keys
- **Pinnable** — a click keeps the menu open (`pinned`), otherwise it closes when the area is left
- **Ring emphasis** — `dimInactive` dims every ring except the active one

## Distinction

- **Do not confuse with** [menu](../menu/): the linear menu follows reading order and suits
  long and dynamic lists; the circular menu follows **directions** and relies on a small,
  always identical number of items.
- **Do not confuse with** [context-menu](../../overlays/context-menu/): both appear at the
  pointer and carry the same actions — the context menu as a list, the circular menu in a
  circle. Both have the role `menu`.
- **Do not confuse with** [floating-action-button](../../../primitives/actions/floating-action-button/):
  the FAB carries the *one* main action, the circular menu several equal ones. The FAB's fan
  is the variant `facher`.
- **Do not confuse with** [toolbar](../toolbar/): the toolbar is permanently visible, the
  circular menu appears on demand (hover, tap, right-click) and disappears again.
- **Do not confuse with** [command](../command/): the command palette searches among many
  commands; the circular menu shows a fixed, learned selection without search.

## Best Practices

- 3–12 items per ring; above 8 items prefer sectors or a second ring.
- At most three rings: each ring enlarges both the area and the pointer path.
- Keep directions identical across the whole program (e.g. up = New, right = Share) — the
  entire advantage rests on this; a reordered layout costs users their speed.
- `hoverDelay` 80–150 ms, `closeDelay` 150–250 ms — without tolerance the menu closes as
  soon as the pointer travels to the sub-item.
- On touch: **press – drag – release** instead of hover; hover menus need `trigger: tap` there.
- No circular menu for long, dynamic or unfamiliar lists — use linear menus or
  [command](../command/) for those.
- Labels only in the active segment or as a [tooltip](../../overlays/tooltip/);
  a full circle with permanent labels becomes unreadable.
- With `prefers-reduced-motion`: `radial-out` → `fade-in`, switch off growth and co-rotation.

## See also

- [navigation – overview](../index.md)
- [Menu](../menu/) — parent class
- [Context Menu](../../overlays/context-menu/) — the same items, linear
- [Floating Action Button](../../../primitives/actions/floating-action-button/) — anchor for `facher`
- [radial-out](../../../../interactions/animations/entrance/radial-out/) and [radial-in](../../../../interactions/animations/exit/radial-in/)
- [Base component](../../../primitives/basics/base.md)
