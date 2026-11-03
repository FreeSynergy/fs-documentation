# Radial Menu - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `items` | array[] | - | array of menu items; sub-items in the `children` field |
| `activeItem` | string/number | - | active item — its sub-items appear in the next ring |
| `onChange` | function | - | event on selection |
| `isOpen` | boolean | `false` | is it open? |
| `onToggle` | function | - | event on opening/closing |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `ring` | form: `ring`, `sektoren`, `facher`, `launcher`, `kontext` |
| `anchor` | string | `center` | anchor: `center`, `top`, `right`, `bottom`, `left`, `top-right` …, coordinates `{x, y}`, CSS selector, `pointer` or `fab` |
| `levels` | number | `2` | number of rings (levels), at most 3 |
| `trigger` | enum | `hover` | trigger: `hover`, `tap`, `long-press`, `right-click` |
| `hoverDelay` | number | `100` | ms before hover opens |
| `closeDelay` | number | `200` | travel tolerance in ms; the menu only closes afterwards |
| `clamp` | boolean | `true` | clamp a full circle at an edge into a quarter/half fan? |
| `pinnable` | boolean | `true` | a click keeps the menu open (`pinned`) |
| `dimInactive` | boolean | `false` | dim all rings except the active one? |
| `keyboardNavigation` | boolean | `true` | arrow keys, `Enter`, `Esc`? |
| `animate` | boolean | `true` | enable animations? |
| `animationDuration` | number | `220` | duration in ms (see [radial-out](../../../../interactions/animations/entrance/radial-out/)) |

## Geometry

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `radius` | number | `72` | radius of ring 1 (anchor centre → item centre) |
| `ringGap` | number | `12` | distance between two rings |
| `itemSize` | number | `40` | diameter of an item |
| `startAngle` | number | `0` | alignment of the first item (0° = up) |
| `sweepAngle` | number | `360` | angular range of the ring (`clamp` reduces it) |
| `coneAngle` | number | `90` | angular range in which the sub-item ring appears |

## Presentation

| Attribute | Type | Default | Description |
|---|---|---|---|
| `size` | enum | `medium` | `small`, `medium`, `large` |
| `shape` | enum | `kreis` | shape of the items: `kreis`, `quadrat`, `abgerundet`, `squircle`, `dreieck`, `fuenfeck`, `sechseck`, `achteck`, `vieleck`, `keil`, `bluete`, `stern` |
| `sides` | number | `6` | corner count for `vieleck` (3–12) |
| `cornerRadius` | number | `0` | corner rounding: `0` = sharp, half the side length = close to a circle |
| `rotation` | number | `0` | turns the shape so a corner/point faces outwards |
| `showLabels` | boolean | `false` | label permanently visible; otherwise only on the active item (`label-reveal`) |
| `color` | enum | `default` | colour: `default`, `light`, `primary` |

## Hover effects

| Attribute | Type | Default | Description |
|---|---|---|---|
| `grow` | boolean | `true` | item grows to 110 % |
| `shift` | number | `6` | item moves radially outwards (px) |
| `lift` | boolean | `true` | shadow grows, item lifts |
| `glow` | boolean | `false` | glow around the active item |
| `morphShape` | boolean | `false` | shape of the active item changes smoothly |
| `ringRotate` | boolean | `false` | ring rotates until the active item is at the top |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onSelect` | function | runs when an item is selected |
| `onOpen` | function | runs on opening |
| `onClose` | function | runs on closing |
| `onLevelChange` | function | runs when the active ring changes |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `menu` |
| `aria-expanded` | boolean | is the menu open? |
| `aria-haspopup` | boolean | item has sub-items |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
