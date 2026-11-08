# File Upload - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | file/array | - | Datei(en) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `multiple` | boolean | `false` | mehrere Dateien? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showProgress` | boolean | `true` | Fortschritt anzeigen? |
| `showPreview` | boolean | `false` | Vorschau anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDrop` | function | wird beim Ablegen ausgeführt |
| `onError` | function | wird bei einem Fehler ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `button` |

## Validierungsattribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `accept` | string | erlaubte Dateitypen (z. B. `.jpg,.png`) |
| `maxSize` | number | maximale Dateigröße in Bytes |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
