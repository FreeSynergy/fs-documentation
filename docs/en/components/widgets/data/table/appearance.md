# Table - Appearance

## Base layout
A table is a tabular display with rows and columns.

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Age │ Action                 │
├─────────────────────────────────────────┤
│ 1  │ John │ 25  │ [Edit] [Delete]        │
│ 2  │ Jane │ 30  │ [Edit] [Delete]        │
│ 3  │ Bob  │ 28  │ [Edit] [Delete]        │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einfach** | header row, rows, no controls |
| **daten** | sort symbols in the header, page numbers below |
| **baum** | one indent per level, collapse triangle on the left |
| **inline-bearbeitung** | the active cell shows a field with a border, the rest stays calm |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 400px | inline |
| medium | 600px | standard |
| large | 800px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Header** | light | header row |
| **Row** | white/alternating | rows |
| **Hover** | lighter | hover state |
| **Active** | primary colour | active row |
| **Disabled** | grey | disabled row |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `background` | the background changes |
| `border` | the border lights up |

## Responsive

- The table fills the width; if there is not enough, it scrolls horizontally (`swipe`) and
  the first column stays put.
- Below `small` screen width the actions per row move behind a menu, and the
  header row stays visible while scrolling vertically.
- Column widths adjust by `drag`; row heights only grow when text wraps, otherwise they
  stay on one line (at least 44 px).

## Sorting

```
┌─────────────────────────────────────────┐
│ ID ▼ │ Name ▲ │ Age │ Action             │
├─────────────────────────────────────────┤
│ 1  │ John │ 25  │ [Edit] [Delete]        │
│ 2  │ Jane │ 30  │ [Edit] [Delete]        │
│ 3  │ Bob  │ 28  │ [Edit] [Delete]        │
└─────────────────────────────────────────┘
```
