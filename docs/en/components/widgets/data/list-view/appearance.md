# List View - Appearance

## Base layout
Vertical list: one entry per row, full width of the container.

```
┌─────────────────────────────────────────┐
│ Element 1                               │
│ Element 2                               │
│ Element 3                               │
│ Element 4                               │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einfach** | text only, optional grey second line |
| **icon** | symbol on the left before the text |
| **avatar** | image on the left, text next to it on the right |
| **badge** | status or counter at the end of the row |
| **aktion** | buttons at the end of the row, visible on hover |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | inline |
| medium | 300px | standard |
| large | 400px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Default** | light | standard |
| **Hover** | lighter | hover state |
| **Active** | primary colour | active state |
| **Disabled** | grey | disabled |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `background` | the background changes |
| `border` | the border lights up |

## Responsive

- The list is always full width; the number of columns does not depend on the size, but
  the split within a row does: on narrow screens the right part slides below the text.
- Secondary actions become reachable on touch devices by swiping (`swipe`), not through
  small buttons.
- Lists that load more show a `skeleton` placeholder at the end, new entries slide in with
  `stagger`.

## With icons

```
┌─────────────────────────────────────────┐
│ 📁 File 1                               │
│ 📁 File 2                               │
│ 📁 File 3                               │
└─────────────────────────────────────────┘
```
