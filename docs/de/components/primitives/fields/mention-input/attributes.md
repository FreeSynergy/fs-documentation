# Mention Input - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | string | - | Wert (Text mit Erwähnungen) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `users` | array[] | - | Liste der Benutzer |
| `placeholder` | string | `null` | Platzhaltertext |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `showSelectedCount` | boolean | `false` | Anzahl der Auswahl anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onMentionSelect` | function | wird bei der Auswahl einer Erwähnung ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Attribute der Autovervollständigung

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `showSuggestions` | boolean | `true` | Vorschläge anzeigen? |
| `trigger` | string | `@` | Auslösezeichen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
