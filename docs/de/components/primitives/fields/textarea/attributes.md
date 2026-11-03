# Textarea (Mehrzeiliges Textfeld) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `autoResize` | boolean | `true` | Auto-Resize? |
| `placeholder` | string | `null` | Placeholder-Text |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showLabel` | boolean | `true` | Label anzeigen? |
| `rows` | number | `3` | Anzahl Zeilen |
| `maxRows` | number | `10` | Maximale Zeilen |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onKeyDown` | function | Wird bei Tastendruck ausgeführt |
| `onResize` | function | Wird beim Resize ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Validation-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Erforderlich? |
| `error` | string | - | Fehlermeldung |
| `minLength` | number | - | Minimale Länge |
| `maxLength` | number | - | Maximale Länge |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
