# Table - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `columns` | array[] | - | Array mit Spalten |
| `data` | array[] | - | Array mit Daten |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | enum | `data` | Stil: `simple`, `data`, `tree`, `inline-edit` |
| `interactive` | boolean | `false` | interaktiv? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onRowClick` | function | wird beim Klick auf eine Zeile ausgeführt |
| `onSortChange` | function | wird ausgeführt, wenn sich die Sortierung ändert |
| `onFilterChange` | function | wird ausgeführt, wenn sich der Filter ändert |
| `onRowDoubleClick` | function | wird bei einem Doppelklick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `table` |

## Spalten-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `key` | string | Spaltenschlüssel |
| `title` | string | Spaltentitel |
| `dataIndex` | string | Datenfeld |
| `sortable` | boolean | sortierbar? |
| `filterable` | boolean | filterbar? |

## Funktions-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showHeader` | boolean | `true` | Kopfzeile anzeigen? |
| `showPagination` | boolean | `false` | Paginierung anzeigen? |
| `showBorder` | boolean | `true` | Rahmen anzeigen? |
| `showStriped` | boolean | `false` | gestreift? |
| `showHover` | boolean | `true` | Hover-Effekt? |

## Paginierungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `pagination` | object | Konfiguration der Paginierung |
| `total` | number | Gesamtanzahl |
| `pageSize` | number | Elemente pro Seite |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
