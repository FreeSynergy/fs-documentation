# Search Field - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | string | - | Wert (Suchbegriff) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Platzhaltertext |
| `showClear` | boolean | `true` | Clear-Knopf anzeigen? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `search` | Name des Icons |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSubmit` | function | wird beim Absenden ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `search` |

## Attribute für Auto-complete

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `false` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array mit Vorschlägen |

## Filter-Attribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `showFilters` | boolean | `false` | Filter anzeigen? |
| `filters` | array[] | - | Array mit Filtern |
| `onFilterChange` | function | - | wird ausgeführt, wenn sich ein Filter ändert |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
