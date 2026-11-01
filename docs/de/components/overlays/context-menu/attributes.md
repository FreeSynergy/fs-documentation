# Context Menu - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Menüpunkten |
| `onSelect` | function | - | Event bei Auswahl |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `closable` | boolean | `true` | Schließbar? |
| `keyboardShortcuts` | boolean | `true` | Keyboard-Shortcuts? |

## Darstellung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `position` | object | { x, y } |
| `anchorEl` | DOM element | Anchor-Element |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onItemClick` | function | Wird beim Klick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `menu` |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `label` | string | Menüpunkt-Label |
| `icon` | string | Icon-Name |
| `danger` | boolean | Gefährliche Aktion? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
