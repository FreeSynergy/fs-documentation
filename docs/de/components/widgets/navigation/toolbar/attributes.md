# Toolbar - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `buttons` | array[] | - | Liste der Schaltflächen-Objekte |
| `variant` | enum | `default` | Stil: `default`, `floating`, `sidebar` |
| `position` | enum | `top` | Position: `top`, `bottom`, `left`, `right` |
| `tabs` | array[] | - | Liste der Reiter-Objekte |
| `activeTab` | string | - | aktiver Reiter |
| `onChange` | function | - | Ereignis beim Reiterwechsel |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showLabels` | boolean | `true` | Beschriftungen anzeigen? |
| `showIcons` | boolean | `true` | Icons anzeigen? |
| `collapsed` | boolean | `false` | eingeklappt? |
| `autoHide` | boolean | `true` | automatisch ausblenden? |
| `target` | DOM-Element | - | Zielelement |
| `offset` | object | - | { x, y }-Versatz zur Position |
| `groups` | array[] | - | Liste der Gruppen-Objekte |
| `commands` | array[] | - | Liste der Befehls-Objekte |
| `minimized` | boolean | `false` | minimiert? |
| `collapsible` | boolean | `true` | einklappbar? |
| `size` | enum | `standard` | Größe: `compact`, `standard`, `large` |

## Ereignisse
| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onButtonClick` | function | läuft beim Klick auf eine Schaltfläche |
| `onExpand` | function | läuft beim Ausklappen |
| `onCollapse` | function | läuft beim Einklappen |
| `onVisibilityChange` | function | läuft, wenn sich die Sichtbarkeit ändert |
| `onSelect` | function | läuft bei Auswahl |
| `onMinimize` | function | läuft beim Minimieren |

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `keyboardShortcuts` | boolean | `true` | Tastenkürzel aktivieren? |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle: `toolbar` |

## Schaltflächen-Attribute

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `id` | string | eindeutige ID |
| `icon` | string | Iconname |
| `label` | string | Beschriftung der Schaltfläche |
| `variant` | enum | `primary`, `secondary`, `danger` |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
