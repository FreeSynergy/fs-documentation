# Pagination - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `currentPage` | number | 1 | Aktuelle Seite |
| `totalItems` | number | - | Gesamtanzahl |
| `itemsPerPage` | number | 10 | Elemente pro Seite |
| `onChange` | function | - | Event bei Seitenwechsel |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showTotal` | boolean | `false` | Gesamtanzahl anzeigen? |
| `showPageSizes` | boolean | `false` | Page-Size-Selector anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPageChange` | function | Wird bei Seitenwechsel ausgeführt |
| `onPageSizeChange` | function | Wird bei Page-Size-Änderung ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `navigation` |

## Navigation-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showFirstLast` | boolean | `false` | First/Last-Buttons anzeigen? |
| `showEllipsis` | boolean | `true` | Ellipsis anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
