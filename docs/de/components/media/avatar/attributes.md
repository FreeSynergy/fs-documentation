# Avatar - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `name` | string | - | Name des Benutzers (für Initials) |
| `src` | string | - | URL zum Benutzerbild |
| `size` | enum/string | `medium` | Größe: `xsmall`, `small`, `medium`, `large`, `xl`, `xxl` |
| `shape` | enum | `circular` | Form: `circular`, `square`, `pill` |
| `variant` | enum | `initials` | Inhalt: `image`, `initials`, `icon`, `placeholder` |
| `status` | enum | `offline` | Status: `online`, `offline`, `away`, `busy`, `in-meeting` |

## Interaktive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird ausgeführt beim Klick |
| `onHover` | function | Wird ausgeführt beim Hover |
| `disabled` | boolean | Avatar deaktivieren? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text (z.B. "Profil von John Doe") |
| `alt` | string | Alt-Text für Bilder |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onFocus` | function | Wird ausgeführt beim Fokus |
| `onBlur` | function | Wird ausgeführt beim Verlassen des Fokus |

## Status-Badge Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showStatus` | boolean | Status-Badge anzeigen? |
| `statusPosition` | enum | Position: `bottom-right`, `top-right`, `bottom-left`, `center` |
| `statusSize` | enum | Größe des Status-Badges: `small`, `medium`, `large` |

## Responsive Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsiveSize` | boolean | Größe basierend auf Screen-Größe anpassen |
| `hideOnMobile` | boolean | Auf Mobile verstecken |
