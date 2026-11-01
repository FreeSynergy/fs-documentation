# Language Switcher - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `languages` | array[] | - | Array von Sprachen |
| `currentLanguage` | string | - | Aktuelle Sprache |
| `onChange` | function | - | Event bei Sprachwechsel |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Sprach-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `code` | string | Sprachcode (z.B. 'de', 'en') |
| `label` | string | Anzeigename |
| `flag` | string | Flaggen-Emoji |

## Varianten-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showCurrentLanguage` | boolean | `true` | Aktuelle Sprache anzeigen? |
| `showFlags` | boolean | `true` | Flaggen anzeigen? |

## Features-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `autoDetect` | boolean | `false` | Automatische Erkennung? |
| `persist` | boolean | `true` | Einstellung speichern? |
| `reload` | boolean | `false` | Seite neu laden? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
