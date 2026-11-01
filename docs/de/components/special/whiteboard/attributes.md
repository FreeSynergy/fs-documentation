# Whiteboard - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `toolbar` | array[] | - | Array von Toolbar-Buttons |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `interactive` | boolean | `true` | Interaktiv? |
| `grid` | boolean | `true` | Raster anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDraw` | function | Wird beim Zeichnen ausgeführt |
| `onClear` | function | Wird beim Löschen ausgeführt |
| `onExport` | function | Wird beim Exportieren ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Features-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `undoRedo` | boolean | `true` | Rückgängig/Wiederherstellen? |
| `collaborative` | boolean | `false` | Kollaborativ? |

## Export-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `exportFormats` | array[] | `['png', 'jpg', 'pdf']` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
