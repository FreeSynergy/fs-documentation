# Accordion

| Field | Value |
|-------|-------|
| **Category** | `containers` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `mehrere`, `einzel`, `deaktiviert` |
| **States** | `geöffnet`, `geschlossen` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `expand`, `collapse` |
| **Related** | `tabs`, `panel`, `tree-view`, `table-of-contents`, `card` |
| **Status** | documented |

## Description
An accordion is a stack of headers that can collapse and expand content.

## Purpose

- Saving space by collapsing and expanding
- FAQ sections
- Settings groups
- Categories with sub-items

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | stack of headers, one open after the other |
| **mehrere** | several areas open at the same time |
| **einzel** | only one header, no stack |
| **deaktiviert** | header visible, but not switchable |

!!! info "Classification"
    A single collapsible element without grouping (called `collapsible` in libraries) is
    the `einzel` variant of this accordion: `items` with one entry and
    `multiple = false`.

## Features

- Expand/collapse
- Animation (collapse/expand animation)
- Keyboard navigation
- Accessibility

## Distinction

- **Do not confuse with** [tabs](../../navigation/tabs/): tabs always show only one content,
  the accordion can show several at the same time.
- **Do not confuse with** [panel](../panel/): a panel stands on its own, the accordion headers
  belong to one shared group.
- **Do not confuse with** [tree-view](../../data/tree-view/): here content is collapsed and
  expanded, there a data hierarchy is paged through.
- **Do not confuse with** [table-of-contents](../../data/table-of-contents/): the table of contents
  jumps to content, it does not hide it.

## Best Practices

- The most important area is open at the start, the rest closed.
- The whole header row is the button, the arrow is only the indicator.
- Keyboard: `Enter`/`space` toggles, arrow keys jump between the headers;
  `aria-expanded` describes the state.
- At most about eight headers; above that a navigation is better than collapsing.
- Do not collapse long content that people need for comparing.

## Behaviour

| Behaviour | Description |
|-----------|-------------|
| **single expand** | only one open |
| **multiple expand** | several open |
| **accordion group** | groups of accordion items |

## See also

- [containers – overview](../index.md)
- [Panel](../panel/) — an area on its own
- [Tabs](../../navigation/tabs/) — always only one content
- [Base component](../../../primitives/basics/base.md)
