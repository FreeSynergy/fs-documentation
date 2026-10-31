# Mention Input - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Text mit Mentions) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `users` | array[] | - | Array von Benutzern |
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
| `onBlur` | function | Wird beim Verlassen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onMentionSelect` | function | Wird bei Mention-Auswahl ausgeführt |

## Auto-Complete-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showSuggestions` | boolean | `true` | Vorschläge anzeigen? |
| `trigger` | string | `@` | Trigger-Zeichen |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showSelectedCount` | boolean | `false` | Ausgewählte Anzahl anzeigen? |
