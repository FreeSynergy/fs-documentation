# Language Switcher - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `languages` | array[] | - | Array von Sprachen |
| `currentLanguage` | string | - | Aktuelle Sprache |
| `onChange` | function | - | Event bei Sprachwechsel |

## Sprach-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `code` | string | Sprachcode (z.B. 'de', 'en') |
| `label` | string | Anzeigename |
| `flag` | string | Flaggen-Emoji |

## Varianten-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `dropdown`, `buttons`, `icons` |
| `showCurrentLanguage` | boolean | `true` | Aktuelle Sprache anzeigen? |
| `showFlags` | boolean | `true` | Flaggen anzeigen? |

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
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |

## Features-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `autoDetect` | boolean | `false` | Automatische Erkennung? |
| `persist` | boolean | `true` | Einstellung speichern? |
| `reload` | boolean | `false` | Seite neu laden? |
