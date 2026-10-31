# Dashboard - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `widgets` | array[] | - | Array von Widgets |

## Widget-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `type` | string | Widget-Typ |
| `title` | string | Titel |
| `content` | string/node | Inhalt |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `dragAndDrop` | boolean | `true` | Drag & Drop aktivieren? |
| `responsive` | boolean | `true` | Responsives Layout? |
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
| `role` | string | ARIA-Rolle: `region` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onWidgetMove` | function | Wird beim Verschieben ausgeführt |
| `onWidgetResize` | function | Wird beim Resizen ausgeführt |
| `onWidgetRemove` | function | Wird beim Entfernen ausgeführt |

## Layout-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `columns` | number | `3` | Anzahl Spalten |
| `gap` | number | `16` | Abstand zwischen Widgets |
