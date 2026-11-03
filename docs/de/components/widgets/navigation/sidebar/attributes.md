# Sidebar - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `position` | enum | `left` | Position: `left`, `right` |
| `width` | number/string | `240` | Breite in px oder CSS-Einheit |
| `collapsed` | boolean | `false` | Sidebar eingeklappt? |
| `collapsible` | boolean | `true` | Kann der User einklappen? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird ausgeführt beim Klick |
| `onToggle` | function | Wird beim Öffnen/Schließen ausgeführt |

## Menü-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `items` | array[] | Array von Menüpunkten |
| `groups` | array[] | Array von Menügruppen |
| `showIcons` | boolean | Icons anzeigen? |
| `showLabels` | boolean | Text labels anzeigen? |

## Item-Attribute (pro Menüpunkt)

| Attribut | Typ | Erforderlich | Beschreibung |
|----------|-----|--------------|--------------|
| `id` | string | yes | Eindeutige ID |
| `label` | string | yes | Anzeigetext |
| `icon` | string | no | Icon-Name (z.B. "mdi:mail") |
| `path` | string | no | Ziel-Pfad/Navigation |
| `badge` | string/number | no | Kleiner Badge-Text (z.B. "3") |
| `children` | array[] | no | Sub-Menüs (Dropdown/Tree) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
