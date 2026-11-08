# Tags Input - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `tags` | array[] | - | Array mit Tags |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `maxTags` | number | - | maximale Anzahl |
| `placeholder` | string | `null` | Platzhaltertext |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showRemove` | boolean | `true` | Entfernen-Knopf anzeigen? |
| `separator` | string | `,` | Trennzeichen für mehrere Tags |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onTagAdd` | function | wird beim Hinzufügen ausgeführt |
| `onTagRemove` | function | wird beim Entfernen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Tag-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `label` | string | Beschriftungstext |
| `value` | string | Wert |

## Attribute für Auto-complete

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `false` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array mit Vorschlägen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
