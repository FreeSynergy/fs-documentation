# List (Aufzählung) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Item-Objekten |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `simple` | Stil: `simple`, `with-icons`, `with-avatars`, `with-badges`, `with-actions` |
| `interactive` | boolean | `false` | Interaktiv? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showAvatars` | boolean | `false` | Avatare anzeigen? |
| `showBadges` | boolean | `false` | Badges anzeigen? |
| `showActions` | boolean | `false` | Actions anzeigen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | Wird beim Hover ausgeführt |
| `onActionClick` | function | Wird bei Action-Klick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `list` |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `label` | string | Label-Text |
| `icon` | string | Icon-Name |
| `avatar` | string | Avatar-URL |
| `badge` | string/number | Badge-Text |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
