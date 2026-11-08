# Emoji Picker - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | string | - | Wert (Emoji) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Platzhaltertext |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showSearch` | boolean | `true` | Suche anzeigen? |
| `showRecent` | boolean | `true` | zuletzt verwendete Emojis anzeigen? |
| `showCategories` | boolean | `true` | Kategorien anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | wird beim Öffnen ausgeführt |
| `onClose` | function | wird beim Schließen ausgeführt |
| `onSelect` | function | wird bei Auswahl ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `button` |

## Attribute der Kategorien

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `categories` | array[] | - | Array von Kategorien |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
