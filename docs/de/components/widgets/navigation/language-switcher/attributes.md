# Language Switcher - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `languages` | array[] | - | Array der Sprachen |
| `currentLanguage` | string | - | aktuelle Sprache |
| `onChange` | function | - | Ereignis beim Sprachwechsel |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | wird beim Öffnen ausgeführt |
| `onClose` | function | wird beim Schließen ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `combobox` |

## Sprachattribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `code` | string | Sprachcode (z. B. 'de', 'en') |
| `label` | string | Anzeigename |
| `flag` | string | Flaggen-Emoji |

## Variantenattribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showCurrentLanguage` | boolean | `true` | aktuelle Sprache anzeigen? |
| `showFlags` | boolean | `true` | Flaggen anzeigen? |

## Funktionsattribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `autoDetect` | boolean | `false` | automatische Erkennung? |
| `persist` | boolean | `true` | Einstellung speichern? |
| `reload` | boolean | `false` | Seite neu laden? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
