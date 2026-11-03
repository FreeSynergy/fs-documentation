# File Upload - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | file/array | - | Datei(en) |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `multiple` | boolean | `false` | Mehrere Dateien? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showProgress` | boolean | `true` | Progress anzeigen? |
| `showPreview` | boolean | `false` | Vorschau anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDrop` | function | Wird beim Drop ausgeführt |
| `onError` | function | Wird bei Fehler ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `button` |

## Validation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `accept` | string | Akzeptierte Dateitypen (z.B. `.jpg,.png`) |
| `maxSize` | number | Maximale Dateigröße in bytes |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
