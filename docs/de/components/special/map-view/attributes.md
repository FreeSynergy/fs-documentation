# Map View - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `center` | object | - | Mittelpunkt {lat, lng} |
| `zoom` | number | - | Zoom-Level |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `mapType` | enum | `roadmap` | Typ: `roadmap`, `satellite`, `hybrid`, `terrain` |
| `interactive` | boolean | `true` | Interaktiv? |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onDragEnd` | function | Wird beim Ziehen beendet ausgeführt |
| `onZoomChange` | function | Wird bei Zoom-Änderung ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `region` |

## Marker-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `markers` | array[] | Array von Markern |
| `onClickMarker` | function | Wird beim Klick auf Marker ausgeführt |

## Features-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showControls` | boolean | `true` | Steuerungselemente anzeigen? |
| `showMarker` | boolean | `true` | Marker anzeigen? |
| `showTraffic` | boolean | `false` | Verkehr anzeigen? |

## API-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `apiKey` | string | API-Schlüssel (Google Maps) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
