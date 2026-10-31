# Map View - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `center` | object | - | Mittelpunkt {lat, lng} |
| `zoom` | number | - | Zoom-Level |
| `onChange` | function | - | Event bei Änderung |

## Marker-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `markers` | array[] | Array von Markern |
| `onClickMarker` | function | Wird beim Klick auf Marker ausgeführt |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `mapType` | enum | `roadmap` | Typ: `roadmap`, `satellite`, `hybrid`, `terrain` |
| `interactive` | boolean | `true` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |

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
| `role` | string | ARIA-Rolle: `region` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onClick` | function | Wird beim Klick auf Karte ausgeführt |
| `onDragEnd` | function | Wird beim Ziehen beendet ausgeführt |
| `onZoomChange` | function | Wird bei Zoom-Änderung ausgeführt |

## Features-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showControls` | boolean | `true` | Steuerungselemente anzeigen? |
| `showMarker` | boolean | `true` | Marker anzeigen? |
| `showTraffic` | boolean | `false` | Verkehr anzeigen? |

## API-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `apiKey` | string | API-Schlüssel (Google Maps) |
