# Context Menu - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Array der Menüeinträge |
| `onSelect` | function | - | Ereignis bei Auswahl |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `closable` | boolean | `true` | schließbar? |
| `keyboardShortcuts` | boolean | `true` | Tastenkürzel? |

## Darstellung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `position` | object | { x, y } |
| `anchorEl` | DOM element | Ankerelement |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | wird beim Öffnen ausgeführt |
| `onClose` | function | wird beim Schließen ausgeführt |
| `onItemClick` | function | wird beim Klick ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `menu` |

## Attribute der Einträge

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | eindeutige ID |
| `label` | string | Beschriftung des Menüeintrags |
| `icon` | string | Name des Symbols |
| `danger` | boolean | gefährliche Aktion? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
