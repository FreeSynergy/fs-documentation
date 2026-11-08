# List View - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Array mit Eintrags-Objekten |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | enum | `simple` | Stil: `simple`, `with-icons`, `with-avatars`, `with-badges`, `with-actions` |
| `interactive` | boolean | `false` | interaktiv? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |
| `showAvatars` | boolean | `false` | Avatare anzeigen? |
| `showBadges` | boolean | `false` | Badges anzeigen? |
| `showActions` | boolean | `false` | Aktionen anzeigen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onHover` | function | wird beim Hover ausgeführt |
| `onActionClick` | function | wird beim Klick auf eine Aktion ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `list` |

## Eintrags-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `label` | string | Beschriftungstext |
| `icon` | string | Name des Icons |
| `avatar` | string | URL des Avatars |
| `badge` | string/number | Badge-Text |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
