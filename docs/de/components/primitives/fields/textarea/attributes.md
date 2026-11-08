# Textarea - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | string | - | Wert |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `autoResize` | boolean | `true` | automatische Größenanpassung? |
| `placeholder` | string | `null` | Platzhaltertext |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showLabel` | boolean | `true` | Label anzeigen? |
| `rows` | number | `3` | Anzahl der Zeilen |
| `maxRows` | number | `10` | maximale Zeilen |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onKeyDown` | function | wird bei einem Tastendruck ausgeführt |
| `onResize` | function | wird beim Vergrößern oder Verkleinern ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Validierungsattribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Pflichtfeld? |
| `error` | string | - | Fehlermeldung |
| `minLength` | number | - | minimale Länge |
| `maxLength` | number | - | maximale Länge |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
