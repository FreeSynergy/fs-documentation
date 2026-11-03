# Table of Contents

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `randspalte`, `block`, `aufklappbar` |
| **States** | `aktiv` |
| **Gestures** | `tap` |
| **Animations** | `expand`, `collapse`, `highlight` |
| **Related** | `tree-view`, `sidebar`, `breadcrumb`, `tabs` |
| **Status** | documented |

## Description
A table of contents is an overview of chapters/sections.

## Purpose

- Documentation
- Books
- Websites
- Chapter overview

## Variants

| Variant | Description |
|---------|-------------|
| **randspalte** | beside the text, stays put while scrolling |
| **block** | at the start of the text as a list |
| **aufklappbar** | collapsed button, the list expands above it |

## Features

- Scroll spy (marks the current section)
- Click to scroll (jumps to a section)
- Collapsible sections (collapse/expand)

## Distinction

- **Do not confuse with** [tree-view](../tree-view/): the contents list shows the headings **of one**
  text with jump targets, the tree view shows arbitrary data hierarchies.
- **Do not confuse with** [sidebar](../../navigation/sidebar/): the sidebar changes the
  view, this contents list stays in the same view and scrolls within it.
- **Do not confuse with** [breadcrumb](../../navigation/breadcrumb/): the breadcrumb shows where you
  are; the contents list shows what there is.
- **Do not confuse with** [tabs](../../navigation/tabs/): tabs swap content, here everything stays
  on one surface.

## Best Practices

- Only headings from the second level on, at most three levels deep.
- Mark the heading currently in view (scroll spy) and update the URL with the anchor.
- Scroll smoothly when jumping, but make the "jump to section" target clearly visible.
- On narrow screens switch to `aufklappbar`, do not take up half the height.
- Only take over the numbering if the text shows it visibly too.

## Layout

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

## See also

- [data – overview](../index.md)
- [Tree View](../tree-view/) — data hierarchy
- [Sidebar](../../navigation/sidebar/) — changing the view
- [Base component](../../../primitives/basics/base.md)
