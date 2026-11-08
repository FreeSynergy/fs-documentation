# Map View - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `center` | object | - | Mittelpunkt {lat, lng} |
| `zoom` | number | - | Zoomstufe |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `mapType` | enum | `roadmap` | Typ: `roadmap`, `satellite`, `hybrid`, `terrain` |
| `interactive` | boolean | `true` | interaktiv? |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onDragEnd` | function | läuft, wenn das Verschieben endet |
| `onZoomChange` | function | läuft, wenn sich die Zoomstufe ändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | ARIA-Rolle: `region` |

## Marker-Attribute

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `markers` | array[] | Liste der Marker |
| `onClickMarker` | function | läuft, wenn ein Marker angeklickt wird |

## Funktions-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showControls` | boolean | `true` | Bedienelemente anzeigen? |
| `showMarker` | boolean | `true` | Marker anzeigen? |
| `showTraffic` | boolean | `false` | Verkehr anzeigen? |

## API-Attribute

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `apiKey` | string | API-Schlüssel (Google Maps) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../../primitives/basics/base.md)
