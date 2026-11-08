# Combobox – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `value` | string | - | Wert |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `options` | array[] | - | Array mit Optionen |
| `placeholder` | string | `null` | Platzhaltertext |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `false` | Icon anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onSelect` | function | läuft bei der Auswahl |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Attribute der Autovervollständigung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array mit Vorschlägen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
