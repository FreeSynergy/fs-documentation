# Select - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | string/number/array | - | Wert |
| `onChange` | function | - | Ereignis bei Änderung |
| `options` | array[] | - | Array mit Optionen |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Platzhaltertext |
| `multiple` | boolean | `false` | Mehrfachauswahl? |
| `searchable` | boolean | `false` | Suche erlauben? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `false` | Icon anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | wird bei Auswahl ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Attribute der Option

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `value` | string/number | Wert |
| `label` | string | Beschriftung |

## Attribute für Auto-complete

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array mit Vorschlägen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
