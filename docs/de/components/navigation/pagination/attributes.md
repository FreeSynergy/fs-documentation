# Pagination - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `currentPage` | number | 1 | Aktuelle Seite |
| `totalItems` | number | - | Gesamtanzahl |
| `itemsPerPage` | number | 10 | Elemente pro Seite |
| `onChange` | function | - | Event bei Seitenwechsel |

## Varianten-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `numeric` | Stil: `numeric`, `previous-next`, `load-more`, `infinite-scroll` |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `disabled` | boolean | `false` | Gesamte Pagination deaktivieren? |
| `showTotal` | boolean | `false` | Gesamtanzahl anzeigen? |
| `showPageSizes` | boolean | `false` | Page-Size-Selector anzeigen? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `navigation` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPageChange` | function | Wird bei Seitenwechsel ausgeführt |
| `onPageSizeChange` | function | Wird bei Page-Size-Änderung ausgeführt |

## Navigation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showFirstLast` | boolean | `false` | First/Last-Buttons anzeigen? |
| `showEllipsis` | boolean | `true` | Ellipsis anzeigen? |
