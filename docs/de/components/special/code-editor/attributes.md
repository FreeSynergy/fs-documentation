# Code Editor - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Code) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `language` | string | `javascript` | Sprache |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `dark` | Theme: `dark`, `light`, `custom` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `textbox` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onBlur` | function | Wird beim Verlassen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onKeyDown` | function | Wird bei Tastendruck ausgeführt |

## Features-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showLineNumbers` | boolean | `true` | Zeilennummern anzeigen? |
| `showGutter` | boolean | `true` | Gutter anzeigen? |
| `autoCompletion` | boolean | `true` | Autovervollständigung aktivieren? |

## Editor-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `lineHeight` | number | `1.5` | Zeilenhöhe |
| `fontSize` | number | `14` | Schriftgröße |
| `tabSize` | number | `2` | Tab-Größe |
