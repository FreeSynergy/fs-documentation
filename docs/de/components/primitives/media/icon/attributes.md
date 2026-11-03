# Icon - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `name` | string | - | Icon-Name (z.B. "mdi:home", "fa:search") |
| `shape` | enum | `square` | Form: `circular`, `square`, `rectangular`, `hexagonal`, `pill` |
| `color` | string | `neutral` | Farbe: `primary`, `secondary`, `success`, `warning`, `error`, `neutral`, hex-code |
| `interactive` | boolean | `false` | Ist das Icon klickbar? |
| `hoverEffect` | enum | `none` | Hover-Effekt: `zoom`, `border`, `shadow`, `none` |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird ausgeführt beim Hover |

## Darstellung
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `spin` | boolean | Icon rotieren lassen (z.B. für Loading) |
| `pulse` | boolean | Icon pulsieren lassen |
| `animationDuration` | number | Dauer der Animation in ms |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsiveSize` | boolean | Größe basierend auf Screen-Größe anpassen |
| `hideOnMobile` | boolean | Auf Mobile verstecken |
| `hideOnDesktop` | boolean | Auf Desktop verstecken |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle (z.B. `button`, `img`) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
