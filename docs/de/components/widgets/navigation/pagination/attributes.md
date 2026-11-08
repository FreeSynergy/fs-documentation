# Pagination - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `currentPage` | number | 1 | aktuelle Seite |
| `totalItems` | number | - | Gesamtzahl |
| `itemsPerPage` | number | 10 | Einträge pro Seite |
| `onChange` | function | - | Ereignis bei Seitenwechsel |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `showTotal` | boolean | `false` | Gesamtzahl anzeigen? |
| `showPageSizes` | boolean | `false` | Auswahl der Seitengröße anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onPageChange` | function | wird bei einem Seitenwechsel ausgeführt |
| `onPageSizeChange` | function | wird ausgeführt, wenn sich die Seitengröße ändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `navigation` |

## Navigationsattribute

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `showFirstLast` | boolean | `false` | Schaltflächen für erste/letzte Seite? |
| `showEllipsis` | boolean | `true` | Auslassungszeichen anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
