# Drag - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onDragStart` | function | - | Wird beim Drag-Start ausgeführt |
| `onDragMove` | function | - | Wird beim Drag-Move ausgeführt |
| `onDragEnd` | function | - | Wird beim Drag-Ende ausgeführt |

## Feedback-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `ghostElement` | boolean | `true` | Ghost-Element anzeigen? |
| `scaleElement` | boolean | `false` | Element vergrößern? |
| `showShadow` | boolean | `true` | Schatten anzeigen? |

## Threshold-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `dragThreshold` | number | `10` | Min. Distanz in px |
| `constrain` | boolean | `false` | Begrenzen? |

## Container-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `container` | string | `parent` | Container-Selector |
| `snap` | boolean | `false` | Snap zu Grid? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `slider` |
