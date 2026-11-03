# Sidebar - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `position` | enum | `left` | Position: `left`, `right` |
| `width` | number/string | `240` | Breite in px oder CSS-Einheit |
| `collapsed` | boolean | `false` | Sidebar eingeklappt? |
| `collapsible` | boolean | `true` | Kann der User einklappen? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSelect` | function | Wird ausgeführt beim Klick |
| `onToggle` | function | Wird beim Öffnen/Schließen ausgeführt |

## Menü-Attribute

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `items` | array[] | Array von Menüpunkten |
| `groups` | array[] | Array von Menügruppen |
| `showIcons` | boolean | show icons? |
| `showLabels` | boolean | Text labels anzeigen? |

## Item-Attribute (pro Menüpunkt)

| Attribute | Type | Erforderlich | Description |
| ---------- | ----- | -------------- | -------------- |
| `id` | string | yes | Eindeutige ID |
| `label` | string | yes | Anzeigetext |
| `icon` | string | no | Icon-Name (z.B. "mdi:mail") |
| `path` | string | no | Ziel-Pfad/Navigation |
| `badge` | string/number | no | Kleiner Badge-Text (z.B. "3") |
| `children` | array[] | no | Sub-Menüs (Dropdown/Tree) |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
