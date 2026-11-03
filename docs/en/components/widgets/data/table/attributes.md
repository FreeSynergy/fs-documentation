# Table - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `columns` | array[] | - | array of columns |
| `data` | array[] | - | array of data |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `variant` | enum | `data` | style: `simple`, `data`, `tree`, `inline-edit` |
| `interactive` | boolean | `false` | interactive? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onRowClick` | function | runs on clicking a row |
| `onSortChange` | function | runs when the sorting changes |
| `onFilterChange` | function | runs when the filter changes |
| `onRowDoubleClick` | function | runs on a double click |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `table` |

## Column attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `key` | string | column key |
| `title` | string | column title |
| `dataIndex` | string | data field |
| `sortable` | boolean | sortable? |
| `filterable` | boolean | filterable? |

## Features attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showHeader` | boolean | `true` | show the header? |
| `showPagination` | boolean | `false` | show pagination? |
| `showBorder` | boolean | `true` | show the border? |
| `showStriped` | boolean | `false` | striped? |
| `showHover` | boolean | `true` | hover effect? |

## Pagination attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `pagination` | object | pagination configuration |
| `total` | number | total number |
| `pageSize` | number | elements per page |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
