# Pagination - Attributes

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `currentPage` | number | 1 | current page |
| `totalItems` | number | - | total count |
| `itemsPerPage` | number | 10 | items per page |
| `onChange` | function | - | event on page change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showTotal` | boolean | `false` | show the total count? |
| `showPageSizes` | boolean | `false` | show the page-size selector? |

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
| `showFirstLast` | boolean | `false` | show first/last buttons? |
| `showEllipsis` | boolean | `true` | show an ellipsis? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
