# Select (Auswahlliste) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string/number/array | - | Wert |
| `onChange` | function | - | Event bei Änderung |
| `options` | array[] | - | Array von Optionen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Placeholder-Text |
| `multiple` | boolean | `false` | Mehrfachauswahl? |
| `searchable` | boolean | `false` | Suche erlauben? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `false` | Icon anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird bei Auswahl ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Option-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `value` | string/number | Wert |
| `label` | string | Label-Text |

## Auto-Complete-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array von Vorschlägen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
