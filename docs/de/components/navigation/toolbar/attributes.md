# Toolbar - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `buttons` | array[] | - | Array von Button-Objekten |
| `variant` | enum | `default` | Stil: `default`, `floating`, `sidebar` |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |

## Button-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `icon` | string | Icon-Name |
| `label` | string | Button-Label |
| `variant` | enum | `primary`, `secondary`, `danger` |
| `onClick` | function | Klick-Event |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showLabels` | boolean | `true` | Labels anzeigen? |
| `showIcons` | boolean | `true` | Icons anzeigen? |
| `collapsed` | boolean | `false` | Eingeklappt? |
| `disabled` | boolean | `false` | Gesamte Toolbar deaktivieren? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark`, `light` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `toolbar` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onButtonClick` | function | Wird beim Button-Klick ausgeführt |
| `onExpand` | function | Wird beim Erweitern ausgeführt |
| `onCollapse` | function | Wird beim Einklappen ausgeführt |

## Keyboard-Shortcuts

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `keyboardShortcuts` | boolean | `true` | Keyboard-Shortcuts aktivieren? |
