# Combobox - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `options` | array[] | - | Array von Optionen |
| `placeholder` | string | `null` | Placeholder-Text |

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

## Auto-Complete-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array von Vorschlägen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
