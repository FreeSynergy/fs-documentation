# Pagination

| Field | Value |
| ------ | ------ |
| **Category** | `navigation` |
| **Inherits from** | `base` |
| **Variants** | `zahlen`, `vor-zurueck`, `nachladen`, `endlos` |
| **States** | `aktiv` |
| **Gestures** | `tap`, `swipe` |
| **Animations** | `fade-in`, `progress` |
| **Related** | `repeater`, `list-view`, `table`, `scroll-area`, `tabs` |
| **State** | documented |

## Description
Pagination splits a long list into portions and offers switching between them.

## Purpose

- Presenting large amounts of data clearly
- Improving performance (only loading visible data)
- Increasing usability

## Variants

| Variant | Description |
| ---------- | -------------- |
| **zahlen** | page numbers with the current page and `…` |
| **vor-zurueck** | only previous and next page |
| **nachladen** | appended portion on a button press |
| **endlos** | the portion loads automatically when the end of the list is reached |

## Features

- Total Items (Gesamtanzahl)
- Current Page (aktuelle Seite)
- Items per Page (Elemente pro Seite)
- Jump to Page (direkt zu Seite springen)
- Page Size Selector (Anzahl pro Seite ändern)

## Distinction

- **Do not confuse with** [tabs](../tabs/): tabs switch the content, here it stays the same list
  in portions.
- **Do not confuse with** [scroll-area](../../containers/scroll-area/): the scroll area is the
  frame, pagination decides what gets loaded into it.
- In [repeater](../../data/repeater/) this component is already included — do not build it twice.

## Best Practices

- At least 25 items per page, otherwise paging is slower than scrolling.
- Show the total count and the current range ("41–80 of 312").
- Scroll to the top after changing the page, otherwise the new page starts half visible.
- Use `endlos` only where no specific item is being searched for; targeted jumping needs numbers.
- Operable with the arrow keys, current page with `aria-current`.

## See also

- [navigation – overview](../index.md)
- [Repeater](../../data/repeater/) — list including pagination
- [Scroll Area](../../containers/scroll-area/) — endless scroll area
- [Base component](../../../primitives/basics/base.md)
