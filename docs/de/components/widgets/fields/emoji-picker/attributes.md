# Emoji Picker - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Emoji) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Placeholder-Text |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showSearch` | boolean | `true` | Suche anzeigen? |
| `showRecent` | boolean | `true` | Letzte Emojis anzeigen? |
| `showCategories` | boolean | `true` | Kategorien anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onSelect` | function | Wird bei Auswahl ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `button` |

## Categories-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `categories` | array[] | - | Array von Kategorien |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
