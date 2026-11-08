# Floating Action Button – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `icon` | string | - | Icon-Name |
| `label` | string | - | Beschriftung des Buttons (für den erweiterten FAB) |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `position` | enum | `bottom-right` | Position |
| `showBadge` | boolean | `false` | Badge anzeigen? |
| `badgeValue` | string/number | - | Wert des Badges |

## Darstellung
| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `size` | enum | `standard` | Größe: `standard`, `mini`, `extended` |
| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `animate` | boolean | `true` | Animationen aktivieren? |
| `rippleEffect` | boolean | `true` | Welleneffekt? |

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `responsive` | boolean | `true` | responsives Layout? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onHover` | function | läuft beim Hover |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle: `button` |

## Varianten-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `color` | enum | `primary` | Farbe: `primary`, `secondary`, `danger` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
