# Avatar - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `name` | string | - | Name des Nutzers (für die Initialen) |
| `src` | string | - | URL des Nutzerbildes |
| `shape` | enum | `circular` | Form: `circular`, `square`, `pill` |
| `variant` | enum | `initials` | Inhalt: `image`, `initials`, `icon`, `placeholder` |
| `status` | enum | `offline` | Status: `online`, `offline`, `away`, `busy`, `in-meeting` |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Hover ausgeführt |

## Darstellung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsiveSize` | boolean | Größe an die Bildschirmgröße anpassen |
| `hideOnMobile` | boolean | auf dem Smartphone ausblenden |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `alt` | string | Alternativtext für Bilder |

## Attribute des Status-Badges

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showStatus` | boolean | Status-Badge anzeigen? |
| `statusPosition` | enum | Position: `bottom-right`, `top-right`, `bottom-left`, `center` |
| `statusSize` | enum | Größe des Status-Badges: `small`, `medium`, `large` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
