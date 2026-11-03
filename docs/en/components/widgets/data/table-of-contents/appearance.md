# Table of Contents - Appearance

## Base layout
A table of contents is an overview of chapters/sections.

```
┌─────────────────────────────────────────┐
│ 📚 Contents                             │
│                                         │
│  1. Chapter 1                           │
│  2. Chapter 2                           │
│  3. Chapter 3                           │
│    3.1. Subchapter 1                    │
│    3.2. Subchapter 2                    │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **randspalte** | narrow strip at the margin, sticky header |
| **block** | list in the text flow, slightly indented |
| **aufklappbar** | button with the list above it, the list covers the text |

## Sizes

| Size | Font size | Use |
|------|-----------|-----|
| small | 12px | inline |
| medium | 14px | standard |
| large | 16px | featured |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **Active** | primary colour | current section |
| **Inactive** | grey | inactive sections |
| **Hover** | lighter | hover state |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `color` | the colour changes |
| `border-bottom` | an underline appears |

## Responsive

- As a margin column the list is at most 240 px wide and stays put while scrolling
  (its own scroll area when it is taller than the viewport).
- Below `small` screen width the margin column is dropped; the variant `aufklappbar`
  opens above the text and closes after a selection.
- Sub-items open with `expand`/`collapse`, the active item stays marked
  even when the list itself has scrolled.

## Collapsible sections

```
┌─────────────────────────────────────────┐
│ 📚 Contents                             │
│                                         │
│ ▶ 1. Chapter 1                          │
│ ▶ 2. Chapter 2                          │
│   └─ 2.1. Subchapter 1                  │
│   └─ 2.2. Subchapter 2                  │
│ ▶ 3. Chapter 3                          │
└─────────────────────────────────────────┘
```
