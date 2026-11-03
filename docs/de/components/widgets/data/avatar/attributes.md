# Avatar - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `name` | string | - | Name des Benutzers (für Initials) |
| `src` | string | - | URL zum Benutzerbild |
| `shape` | enum | `circular` | Form: `circular`, `square`, `pill` |
| `variant` | enum | `initials` | Inhalt: `image`, `initials`, `icon`, `placeholder` |
| `status` | enum | `offline` | Status: `online`, `offline`, `away`, `busy`, `in-meeting` |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird ausgeführt beim Hover |

## Darstellung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsiveSize` | boolean | Größe basierend auf Screen-Größe anpassen |
| `hideOnMobile` | boolean | Auf Mobile verstecken |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `alt` | string | Alt-Text für Bilder |

## Status-Badge Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showStatus` | boolean | Status-Badge anzeigen? |
| `statusPosition` | enum | Position: `bottom-right`, `top-right`, `bottom-left`, `center` |
| `statusSize` | enum | Größe des Status-Badges: `small`, `medium`, `large` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
