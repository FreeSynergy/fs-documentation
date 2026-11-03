# Map View - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `center` | object | - | centre point {lat, lng} |
| `zoom` | number | - | zoom level |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `mapType` | enum | `roadmap` | type: `roadmap`, `satellite`, `hybrid`, `terrain` |
| `interactive` | boolean | `true` | interactive? |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onDragEnd` | function | runs when dragging ends |
| `onZoomChange` | function | runs when the zoom changes |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `region` |

## Marker attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `markers` | array[] | array of markers |
| `onClickMarker` | function | runs when a marker is clicked |

## Features attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showControls` | boolean | `true` | show controls? |
| `showMarker` | boolean | `true` | show markers? |
| `showTraffic` | boolean | `false` | show traffic? |

## API attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `apiKey` | string | API key (Google Maps) |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
