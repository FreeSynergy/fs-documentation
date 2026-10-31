# Icon - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `name` | string | - | Icon-Name (z.B. "mdi:home", "fa:search") |
| `size` | enum/string | `medium` | Größe: `small`, `medium`, `large`, `xl`, `xxl` |
| `shape` | enum | `square` | Form: `circular`, `square`, `rectangular`, `hexagonal`, `pill` |
| `color` | string | `neutral` | Farbe: `primary`, `secondary`, `success`, `warning`, `error`, `neutral`, hex-code |
| `interactive` | boolean | `false` | Ist das Icon klickbar? |
| `hoverEffect` | enum | `none` | Hover-Effekt: `zoom`, `border`, `shadow`, `none` |

## Interaktive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird ausgeführt beim Klick |
| `onHover` | function | Wird ausgeführt beim Hover |
| `disabled` | boolean | Icon deaktivieren? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text für Screenreader |
| `role` | string | ARIA-Rolle (z.B. `button`, `img`) |
| `tabIndex` | number | Tab-Order für Tastatur-Navigation |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onFocus` | function | Wird ausgeführt beim Fokus |
| `onBlur` | function | Wird ausgeführt beim Verlassen des Fokus |

## Animation-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `spin` | boolean | Icon rotieren lassen (z.B. für Loading) |
| `pulse` | boolean | Icon pulsieren lassen |
| `animationDuration` | number | Dauer der Animation in ms |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsiveSize` | boolean | Größe basierend auf Screen-Größe anpassen |
| `hideOnMobile` | boolean | Auf Mobile verstecken |
| `hideOnDesktop` | boolean | Auf Desktop verstecken |
