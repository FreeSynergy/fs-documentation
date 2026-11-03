# Mention Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Text mit Mentions) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `users` | array[] | - | Array von Benutzern |
| `placeholder` | string | `null` | Placeholder-Text |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showSelectedCount` | boolean | `false` | Ausgewählte Anzahl anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onMentionSelect` | function | Wird bei Mention-Auswahl ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Auto-Complete-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showSuggestions` | boolean | `true` | Vorschläge anzeigen? |
| `trigger` | string | `@` | Trigger-Zeichen |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
