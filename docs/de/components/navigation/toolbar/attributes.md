# Toolbar - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `buttons` | array[] | - | Array von Button-Objekten |
| `variant` | enum | `default` | Stil: `default`, `floating`, `sidebar` |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |
| `tabs` | array[] | - | Array von Tab-Objekten |
| `activeTab` | string | - | Aktiver Tab |
| `onChange` | function | - | Event bei Tab-Wechsel |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showLabels` | boolean | `true` | Labels anzeigen? |
| `showIcons` | boolean | `true` | Icons anzeigen? |
| `collapsed` | boolean | `false` | Eingeklappt? |
| `autoHide` | boolean | `true` | Automatisch ausblenden? |
| `target` | DOM element | - | Ziel-Element |
| `offset` | object | - | { x, y } Offset zur Position |
| `groups` | array[] | - | Array von Group-Objekten |
| `commands` | array[] | - | Array von Command-Objekten |
| `minimized` | boolean | `false` | Minimiert? |
| `collapsible` | boolean | `true` | Ein-/Ausklappbar? |
| `size` | enum | `standard` | Größe: `compact`, `standard`, `large` |

## Events
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onButtonClick` | function | Wird beim Button-Klick ausgeführt |
| `onExpand` | function | Wird beim Erweitern ausgeführt |
| `onCollapse` | function | Wird beim Einklappen ausgeführt |
| `onVisibilityChange` | function | Wird bei Sichtbarkeitsänderung ausgeführt |
| `onSelect` | function | Wird beim Selektieren ausgeführt |
| `onMinimize` | function | Wird beim Minimieren ausgeführt |

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `keyboardShortcuts` | boolean | `true` | Keyboard-Shortcuts aktivieren? |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `toolbar` |

## Button-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `id` | string | Eindeutige ID |
| `icon` | string | Icon-Name |
| `label` | string | Button-Label |
| `variant` | enum | `primary`, `secondary`, `danger` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
