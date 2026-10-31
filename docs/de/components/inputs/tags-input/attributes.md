# Tags Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `tags` | array[] | - | Array von Tags |
| `onChange` | function | - | Event bei Änderung |

## Tag-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `label` | string | Label-Text |
| `value` | string | Wert |
| `disabled` | boolean | Deaktiviert? |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `maxTags` | number | - | Maximale Anzahl |
| `disabled` | boolean | `false` | Deaktiviert? |
| `placeholder` | string | `null` | Placeholder-Text |

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
| `role` | string | ARIA-Rolle: `combobox` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onTagAdd` | function | Wird beim Hinzufügen ausgeführt |
| `onTagRemove` | function | Wird beim Entfernen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |

## Auto-Complete-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showSuggestions` | boolean | `false` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array von Vorschlägen |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showRemove` | boolean | `true` | Remove-Button anzeigen? |
| `separator` | string | `,` | Separator für mehrere Tags |
