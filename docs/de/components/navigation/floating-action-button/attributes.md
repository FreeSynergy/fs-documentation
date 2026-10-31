# Floating Action Button - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `icon` | string | - | Icon-Name |
| `label` | string | - | Button-Label (für Extended FAB) |
| `onClick` | function | - | Klick-Event |

## Varianten-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `standard` | Stil: `standard`, `mini`, `extended` |
| `color` | enum | `primary` | Farbe: `primary`, `secondary`, `danger` |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `position` | enum | `bottom-right` | Position |
| `disabled` | boolean | `false` | Deaktiviert? |
| `showBadge` | boolean | `false` | Badge anzeigen? |
| `badgeValue` | string/number | - | Badge-Wert |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `standard` | Größe: `standard`, `mini`, `extended` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `button` |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `rippleEffect` | boolean | `true` | Ripple-Effekt? |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | `true` | Responsives Layout? |
