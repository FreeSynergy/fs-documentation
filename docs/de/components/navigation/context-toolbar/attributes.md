# Context Toolbar - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `buttons` | array[] | - | Array von Button-Objekten |
| `visible` | boolean | `false` | Sichtbar? |

## Button-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `icon` | string | Icon-Name |
| `label` | string | Button-Label |
| `variant` | enum | `primary`, `danger` |
| `onClick` | function | Klick-Event |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `position` | enum | `top` | Position: `top`, `bottom` |
| `showLabels` | boolean | `true` | Labels anzeigen? |
| `autoHide` | boolean | `true` | Automatisch ausblenden? |

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
| `role` | string | ARIA-Rolle: `toolbar` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onButtonClick` | function | Wird beim Button-Klick ausgeführt |
| `onVisibilityChange` | function | Wird bei Sichtbarkeitsänderung ausgeführt |

## Positionierung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `target` | DOM element | Ziel-Element |
| `offset` | object | { x, y } | Offset zur Position |
