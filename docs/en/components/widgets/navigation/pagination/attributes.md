# Pagination - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `currentPage` | number | 1 | Aktuelle Seite |
| `totalItems` | number | - | Gesamtanzahl |
| `itemsPerPage` | number | 10 | Elemente pro Seite |
| `onChange` | function | - | event on page change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showTotal` | boolean | `false` | Gesamtanzahl anzeigen? |
| `showPageSizes` | boolean | `false` | Page-Size-Selector anzeigen? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onPageChange` | function | runs on a page change |
| `onPageSizeChange` | function | runs when the page size changes |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `navigation` |

## Navigation attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showFirstLast` | boolean | `false` | First/Last-Buttons anzeigen? |
| `showEllipsis` | boolean | `true` | Ellipsis anzeigen? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
