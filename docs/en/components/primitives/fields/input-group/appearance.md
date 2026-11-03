# Input Group - Appearance

## Base layout

```
┌──────────┬────────────────────────────┐
│ https:// │ free-synergy.org           │   prefix on the left, value right of it
└──────────┴────────────────────────────┘

┌────────────────────────────┬─────┐
│ Search for files           │ 🔍  │   action on the right, shared outer corner
└────────────────────────────┴─────┘
```

The field and the attached parts form one surface: inner edges are shared, only
the outer corners are rounded.

## Variants

| Variant | Appearance |
|---------|------------|
| **praefix** | offset strip on the left, same height as the field |
| **suffix** | offset strip on the right |
| **aktion** | button at field height, separated by an inner edge |
| **auswahl** | prefix with an arrow, opens a small menu |

## Sizes

Connected to the size scale of the [base component](../../basics/base.md):

| Size | Height | Icon in the attached part | Font |
|------|--------|---------------------------|------|
| `small` | 28 px | 14 px | 13 px |
| `medium` | 36 px | 16 px | 14 px |
| `large` | 44 px | 20 px | 16 px |

## Colours and states

| State | Appearance |
|-------|------------|
| `default` | attached part on a neutral surface, dividing edge visible |
| `focus-within` | field border in the primary colour, attached part stays neutral |
| `filled` | value set, the action button becomes active |
| `error` | border of the whole group in the error colour |
| `disabled` | group dimmed, attached part with it |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `highlight` | attached part and field react to focus together |
| `tone` | action button one step darker on hover |
| `ring` | focus ring around the whole group for keyboard navigation |

## Responsive

```css
.input-group { display: flex; align-items: stretch; }
.input-group > * { border-radius: 0; }
.input-group > :first-child { border-top-left-radius: 6px; border-bottom-left-radius: 6px; }
.input-group > :last-child  { border-top-right-radius: 6px; border-bottom-right-radius: 6px; }

@media (max-width: 480px) {
  .input-group--aktion { flex-direction: column; }   /* action below the field */
}
```

On a narrow surface the action slips below the field; prefixes stay on the field,
because they belong to the value.
