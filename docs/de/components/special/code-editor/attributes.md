# Code Editor - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Code) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `language` | string | `javascript` | Sprache |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onKeyDown` | function | Wird bei Tastendruck ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Features-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showLineNumbers` | boolean | `true` | Zeilennummern anzeigen? |
| `showGutter` | boolean | `true` | Gutter anzeigen? |
| `autoCompletion` | boolean | `true` | Autovervollständigung aktivieren? |

## Editor-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `lineHeight` | number | `1.5` | Zeilenhöhe |
| `fontSize` | number | `14` | Schriftgröße |
| `tabSize` | number | `2` | Tab-Größe |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
