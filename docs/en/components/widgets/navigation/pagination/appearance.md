# Pagination - Appearance

## Base layout

Pagination is a navigation for large lists that splits data into pages.

## Variants

### Numeric

```
┌─────────────────────────────────────────┐
│ [◀] 1 2 3 4 5 [▶]                       │
└─────────────────────────────────────────┘
```

### Previous/Next

```
┌─────────────────────────────────────────┐
│ [◀ Zurück] [Weiter ▶]                   │
└─────────────────────────────────────────┘
```

### Load More

```
┌─────────────────────────────────────────┐
│ [Mehr laden]                            │
└─────────────────────────────────────────┘
```

### Infinite Scroll

```
┌─────────────────────────────────────────┐
│ (Automatisch nachladen beim Scrollen)   │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Font size | Use |
| ------- | ------------- | ------------ |
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Active** | primary colour | current page |
| **Inactive** | grey | inactive pages |
| **Hover** | lighter | hover state |
| **Disabled** | grey | disabled buttons |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `background` | the page number gets a filled area |
| `ring` | focus ring during keyboard navigation |
| `underline` | underline on the active entry |
| `none` | disabled arrows without feedback |

## Responsive

| Breakpoint | Behaviour |
| ------------ | ----------- |
| Desktop (>768px) | full pagination visible |
| Tablet (480-768px) | compact |
| Mobile (<480px) | Previous/Next oder Load More |

## Features

- **Total Items**: total number of items
- **Current Page**: current page
- **Items per Page**: items per page
- **Jump to Page**: jump straight to a page
- **Page Size Selector**: Anzahl pro Seite ändern
