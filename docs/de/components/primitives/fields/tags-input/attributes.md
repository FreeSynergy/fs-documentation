# Tags Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `tags` | array[] | - | Array von Tags |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `maxTags` | number | - | Maximale Anzahl |
| `placeholder` | string | `null` | Placeholder-Text |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showRemove` | boolean | `true` | Remove-Button anzeigen? |
| `separator` | string | `,` | Separator für mehrere Tags |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onTagAdd` | function | Wird beim Hinzufügen ausgeführt |
| `onTagRemove` | function | Wird beim Entfernen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Tag-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `label` | string | Label-Text |
| `value` | string | Wert |

## Auto-Complete-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `false` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array von Vorschlägen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
