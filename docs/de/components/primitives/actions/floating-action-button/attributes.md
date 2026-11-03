# Floating Action Button - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `icon` | string | - | Icon-Name |
| `label` | string | - | Button-Label (für Extended FAB) |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `position` | enum | `bottom-right` | Position |
| `showBadge` | boolean | `false` | Badge anzeigen? |
| `badgeValue` | string/number | - | Badge-Wert |

## Darstellung
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `size` | enum | `standard` | Größe: `standard`, `mini`, `extended` |
| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `rippleEffect` | boolean | `true` | Ripple-Effekt? |

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | Responsives Layout? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `button` |

## Varianten-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `color` | enum | `primary` | Farbe: `primary`, `secondary`, `danger` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
