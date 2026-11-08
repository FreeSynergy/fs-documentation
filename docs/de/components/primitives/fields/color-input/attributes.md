# Farbfeld – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `value` | string | - | Wert (Farbe) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `placeholder` | string | `null` | Platzhaltertext |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `palette` | Icon-Name |
| `formats` | array[] | `['hex', 'rgb', 'hsl']` | Farbformate |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onOpen` | function | läuft, wenn sich der Farbwähler öffnet |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle: `color` |

## Attribute des Farbwählers

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showAlpha` | boolean | `false` | Alpha-Kanal anzeigen? |
| `showPalette` | boolean | `true` | Farbpalette anzeigen? |
| `showSpectrum` | boolean | `true` | Farbspektrum anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base.md)
