# Icon - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `name` | string | - | Name des Icons (z. B. "mdi:home", "fa:search") |
| `shape` | enum | `square` | Form: `circular`, `square`, `rectangular`, `hexagonal`, `pill` |
| `color` | string | `neutral` | Farbe: `primary`, `secondary`, `success`, `warning`, `error`, `neutral`, Hex-Code |
| `interactive` | boolean | `false` | ist das Icon klickbar? |
| `hoverEffect` | enum | `none` | Hover-Effekt: `zoom`, `border`, `shadow`, `none` |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Überfahren ausgeführt |

## Darstellung
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `spin` | boolean | das Icon drehen lassen (z. B. beim Laden) |
| `pulse` | boolean | das Icon pulsieren lassen |
| `animationDuration` | number | Dauer der Animation in ms |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsiveSize` | boolean | Größe an die Bildschirmgröße anpassen |
| `hideOnMobile` | boolean | auf dem Handy ausblenden |
| `hideOnDesktop` | boolean | auf dem Desktop ausblenden |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle (z. B. `button`, `img`) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
