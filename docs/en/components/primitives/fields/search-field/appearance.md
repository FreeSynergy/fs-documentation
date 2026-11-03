# Search Field - Appearance

## Base layout
A search field is a search box with filter options.

```
┌─────────────────────────────────────────┐
│ 🔍 Search…                              │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **simple** | simple search |
| **filter** | with filters |
| **auto-complete** | with suggestions |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 150px | inline |
| medium | 250px | standard |
| large | 350px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **default** | light | standard |
| **primary** | primary colour | primary |
| **active** | dark | active state |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `border` | the border lights up |
| `shadow` | shadow becomes stronger |

## Responsive

- In toolbars the field can be collapsed; clicking the search symbol expands it to the
  full bar width (`expand`).
- Below `small` screen width the field is set full width above the list, the filters
  slip behind an expand button.
- Suggestion list at most eight rows, after that it scrolls; matches are `highlight`ed.

## Clear button

```
┌─────────────────────────────────────────┐
│ 🔍 Search…                     [✕]      │
└─────────────────────────────────────────┘
```

## Filter overlay

```
┌─────────────────────────────────────────┐
│ 🔍 Search…                              │
├─────────────────────────────────────────┤
│  [Filter 1] [Filter 2] [Filter 3]       │
│  [Reset]                                │
└─────────────────────────────────────────┘
```
