# File Upload - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | file/array | - | Datei(en) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `file-picker` | Stil: `file-picker`, `drag-drop`, `image-preview` |
| `multiple` | boolean | `false` | Mehrere Dateien? |
| `disabled` | boolean | `false` | Deaktiviert? |

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
| `role` | string | ARIA-Rolle: `button` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDrop` | function | Wird beim Drop ausgeführt |
| `onError` | function | Wird bei Fehler ausgeführt |

## Validation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `accept` | string | Akzeptierte Dateitypen (z.B. `.jpg,.png`) |
| `maxSize` | number | Maximale Dateigröße in bytes |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showProgress` | boolean | `true` | Progress anzeigen? |
| `showPreview` | boolean | `false` | Vorschau anzeigen? |
