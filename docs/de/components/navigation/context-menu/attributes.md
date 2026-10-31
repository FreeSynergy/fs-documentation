# Context Menu - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Menüpunkten |
| `onSelect` | function | - | Event bei Auswahl |

## Item-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `label` | string | Menüpunkt-Label |
| `icon` | string | Icon-Name |
| `danger` | boolean | Gefährliche Aktion? |
| `onClick` | function | Klick-Event |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `disabled` | boolean | `false` | Gesamtes Menu deaktivieren? |
| `closable` | boolean | `true` | Schließbar? |
| `keyboardShortcuts` | boolean | `true` | Keyboard-Shortcuts? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `menu` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onItemClick` | function | Wird beim Klick ausgeführt |

## Positionierung

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `position` | object | { x, y } |
| `anchorEl` | DOM element | Anchor-Element |
