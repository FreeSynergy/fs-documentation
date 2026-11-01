# Table (Tabelle) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `columns` | array[] | - | Array von Spalten |
| `data` | array[] | - | Array von Daten |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `data` | Stil: `simple`, `data`, `tree`, `inline-edit` |
| `interactive` | boolean | `false` | Interaktiv? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onRowClick` | function | Wird beim Zeilen-Klick ausgeführt |
| `onSortChange` | function | Wird bei Sortieränderung ausgeführt |
| `onFilterChange` | function | Wird bei Filteränderung ausgeführt |
| `onRowDoubleClick` | function | Wird beim Doppelklick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `table` |

## Column-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `key` | string | Spalten-Schlüssel |
| `title` | string | Spalten-Titel |
| `dataIndex` | string | Daten-Feld |
| `sortable` | boolean | Sortierbar? |
| `filterable` | boolean | Filterbar? |

## Features-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showHeader` | boolean | `true` | Header anzeigen? |
| `showPagination` | boolean | `false` | Pagination anzeigen? |
| `showBorder` | boolean | `true` | Rand anzeigen? |
| `showStriped` | boolean | `false` | Gestreift? |
| `showHover` | boolean | `true` | Hover-Effekt? |

## Pagination-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `pagination` | object | Pagination-Konfiguration |
| `total` | number | Gesamtanzahl |
| `pageSize` | number | Elemente pro Seite |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
