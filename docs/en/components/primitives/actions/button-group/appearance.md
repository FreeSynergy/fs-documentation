# Button Group - Appearance

## Base layout

Verbund (two buttons share one edge):

```
┌────────────┬────────────┐
│    Save    │   Cancel   │
└────────────┴────────────┘
```

Segmented control (exactly one segment active):

```
┌──────────┬──────────┬──────────┐
│  List    │  Grid    │ Timeline │
└──────────┴──────────┴──────────┘
   active = coloured surface
```

Split button:

```
┌──────────────────┬─────┐
│  Save            │  ▾  │
└──────────────────┴─────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **verbund** | inner sides have no rounding, only the outside is rounded |
| **segment** | one shared frame, segment dividers as thin lines |
| **split** | like `verbund`, the last element is clearly narrower (arrow only) |

## Sizes

The size table of [Button](../button/) applies to every group element;
elements of different sizes must not sit in the same group.

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | like a single button, inner sides shared |
| `hover` | tone one step darker, as for a button |
| `active` (segment selected) | coloured surface, text in the primary colour |
| `focus` | ring around the whole element, not around the group |
| `disabled` | 40 % opacity of the element |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `tone` | surface tone changes as it does for a single button |
| `ring` | focus ring on the element; the group border stays unchanged |
| `indicator` | selection shown by the surface, not by colour alone |

## Responsive

- Groups that are too wide are stacked vertically on narrow screens.
- Labels must not wrap; when space is tight, switch to icons.
