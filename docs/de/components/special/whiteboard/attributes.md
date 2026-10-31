# Whiteboard - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `toolbar` | array[] | - | Array von Toolbar-Buttons |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `interactive` | boolean | `true` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |
| `grid` | boolean | `true` | Raster anzeigen? |

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
| `onDraw` | function | Wird beim Zeichnen ausgeführt |
| `onClear` | function | Wird beim Löschen ausgeführt |
| `onExport` | function | Wird beim Exportieren ausgeführt |

## Features-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `undoRedo` | boolean | `true` | Rückgängig/Wiederherstellen? |
| `collaborative` | boolean | `false` | Kollaborativ? |

## Export-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `exportFormats` | array[] | `['png', 'jpg', 'pdf']` |
