# Search Field (Suchfeld mit Filter) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Suchbegriff) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Placeholder-Text |
| `showClear` | boolean | `true` | Clear-Button anzeigen? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `search` | Icon-Name |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSubmit` | function | Wird bei Submit ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `search` |

## Auto-Complete-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `false` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array von Vorschlägen |

## Filter-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `showFilters` | boolean | `false` | Filter anzeigen? |
| `filters` | array[] | - | Array von Filtern |
| `onFilterChange` | function | - | Wird bei Filteränderung ausgeführt |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
