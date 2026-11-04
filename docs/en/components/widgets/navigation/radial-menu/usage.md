# Radial Menu - Usage

## Corner menu with hover (top right)

The classic: items sit in the corner, grow on hover and push their sub-items inwards into
the surface (`clamp` turns the full circle into a fan).

```jsx
<RadialMenu
  anchor="top-right"
  variant="facher"
  trigger="hover"
  items={[
    { id: 'new', icon: 'plus', label: 'New' },
    { id: 'share', icon: 'share', label: 'Share',
      children: [
        { id: 'link', icon: 'link', label: 'Copy link' },
        { id: 'mail', icon: 'mail', label: 'E-mail' }
      ] },
    { id: 'settings', icon: 'cog', label: 'Settings' }
  ]}
  onSelect={(id) => run(id)}
/>
```

## Free anchor in the middle of the surface

Set the anchor to free coordinates or to another element — the menu appears where the user
works (whiteboard, map, editor).

```jsx
<RadialMenu
  variant="launcher"
  anchor={{ x: cursor.x, y: cursor.y }}
  size="large"
  items={palette}
/>

<RadialMenu anchor="#avatar-42" items={personActions} />
```

## Sub-items in the next ring

Hovering an item opens its `children` in the second ring; with three levels
`levels={3}` corresponds to three rings.

```jsx
<RadialMenu
  anchor="center"
  levels={3}
  activeItem={hoveredItem}      // children appear in the next ring
  dimInactive
  items={[
    { id: 'document', icon: 'file', children: [
        { id: 'rename', icon: 'pencil' },
        { id: 'versions', icon: 'history', children: [
            { id: 'v1', label: 'v1' },
            { id: 'v2', label: 'v2' }
        ] }
    ] }
  ]}
/>
```

## Sectors instead of items (pie menu)

Large hit areas, selection purely by direction — good on touch and controllers.

```jsx
<RadialMenu
  variant="sektoren"
  trigger="long-press"
  items={toolModes}
/>
```

## Context menu at the pointer

A right-click opens the same menu at the pointer position — the round variant of the
[context-menu](../../overlays/context-menu/).

```jsx
<RadialMenu variant="kontext" items={contextActions} />
```

## Speed dial on the floating action button

The FAB anchors the circular menu (`anchor: "fab"`), the fan clamps towards the screen centre.

```jsx
<FloatingActionButton icon="plus" />
<RadialMenu
  anchor="fab"
  variant="facher"
  trigger="tap"
  items={quickAccess}
/>
```

## Keyboard control

```jsx
<RadialMenu keyboardNavigation items={items} />
// arrow keys: around the ring · Enter: one level in · Esc: back or close
```

## Examples

### Example 1: corner menu, three states

```
closed             hover                sub-item active
    ●          ╲      ◆             ╲    ◆ ○
 (item in       ╲    (grows,      ╲   (ring 2 fans
  corner)       ╲    moves out)   ╲   out of ◆)
```

### Example 2: launcher with two rings

```
        ○  ○  ○
      ○  ◆  ●  ◆  ○        ● anchor · ◆ ring 1 · ○ ring 2 (children
        ○  ◆  ○              of the active ◆, visible inside coneAngle)
```

### Example 3: speed dial bottom right

```
                      ┌──────────────┐
                      │        ○   ◆ │   anchor = corner bottom right,
                      │      ○   ◆   │   ring clamped inwards as a
                      │    ○   ◆  ●  │   half fan
                      └──────────────┘
```

## See also

- [Radial Menu – description](./description.md)
- [Attributes](./attributes.md)
- [radial-out](../../../../interactions/animations/entrance/radial-out/) and [radial-in](../../../../interactions/animations/exit/radial-in/)
- [Floating Action Button](../../../primitives/actions/floating-action-button/)
