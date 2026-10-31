# Table (Tabelle) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `columns` | array[] | - | Array von Spalten |
| `data` | array[] | - | Array von Daten |

## Column-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `key` | string | Spalten-Schlüssel |
| `title` | string | Spalten-Titel |
| `dataIndex` | string | Daten-Feld |
| `sortable` | boolean | Sortierbar? |
| `filterable` | boolean | Filterbar? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `data` | Stil: `simple`, `data`, `tree`, `inline-edit` |
| `interactive` | boolean | `false` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |

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
| `role` | string | ARIA-Rolle: `table` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onRowClick` | function | Wird beim Zeilen-Klick ausgeführt |
| `onSortChange` | function | Wird bei Sortieränderung ausgeführt |
| `onFilterChange` | function | Wird bei Filteränderung ausgeführt |
| `onRowDoubleClick` | function | Wird beim Doppelklick ausgeführt |

## Features-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
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
