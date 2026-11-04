# Code Editor - Appearance

## Base layout
A code editor is an editor for source code.

```
┌─────────────────────────────────────────┐
│ 1  const greeting = "Hello";            │
│ 2  console.log(greeting);               │
│ 3                                       │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **voll** | line numbers on the left, suggestion list at the cursor |
| **nur-lesen** | no cursor, copy button top right |
| **vergleich** | two halves, changed lines marked in red and green |

## Sizes

| Size | Height | Use |
|------|--------|-------------|
| Small | 200px | inline |
| Medium | 400px | standard |
| Large | 600px | featured |
| Full | 100% | full width |

## Colours and states

| State | Colour | Description |
|--------------|--------|----------------------|
| **Background** | dark | dark theme |
| **Text** | light | text colour |
| **Keyword** | purple | keywords |
| **String** | orange | strings |
| **Comment** | grey | comments |

## Hover and focus effects

| Effect | Description |
|-------------|-----------------------------|
| `line-number` | highlights the line number |
| `cursor` | changes the cursor |

## Responsive

- The editor fills the width; code does not wrap but scrolls horizontally (`swipe`).
- Below `small` screen width the suggestion list is placed over the keyboard, the line
  number block becomes narrower.
- The comparison variant puts the two halves below each other instead of side by side; the
  height stays limited per half.

## Features

| Feature | Description |
|---------------------|---------------------------|
| **Syntax Highlighting** | coloured highlighting |
| **Line Numbers** | line numbers |
| **Auto-completion** | autocompletion |
| **Error Detection** | error detection |
| **Multiple Cursors** | multiple cursors |

## Themes

| Theme | Description |
|-------|-------------|
| **Dark** | dark theme |
| **Light** | light theme |
| **Custom** | custom |
