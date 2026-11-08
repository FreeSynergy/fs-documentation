# Sidebar - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `position` | enum | `left` | Position: `left`, `right` |
| `width` | number/string | `240` | Breite in px oder einer CSS-Einheit |
| `collapsed` | boolean | `false` | Sidebar eingeklappt? |
| `collapsible` | boolean | `true` | Kann der Nutzer sie einklappen? |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onSelect` | function | läuft beim Klick |
| `onToggle` | function | läuft beim Öffnen/Schließen |

## Menü-Attribute

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `items` | array[] | Liste der Menüpunkte |
| `groups` | array[] | Liste der Menügruppen |
| `showIcons` | boolean | Icons anzeigen? |
| `showLabels` | boolean | Textbeschriftungen anzeigen? |

## Punkt-Attribute (pro Menüpunkt)

| Attribut | Typ | Pflicht | Beschreibung |
|-----------|------|----------|-------------|
| `id` | string | ja | eindeutige ID |
| `label` | string | ja | angezeigter Text |
| `icon` | string | nein | Iconname (z. B. "mdi:mail") |
| `path` | string | nein | Ziel-Pfad/Navigation |
| `badge` | string/number | nein | kleiner Badge-Text (z. B. "3") |
| `children` | array[] | nein | Untermenüs (Dropdown/Baum) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
