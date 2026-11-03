# Map View

| Field | Value |
|-------|-------|
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `standort`, `sammlung`, `route` |
| **States** | `wartend`, `ortung` |
| **Gestures** | `tap`, `drag`, `pinch`, `double-tap`, `long-press` |
| **Animations** | `fade-in`, `zoom-in` |
| **Related** | `embed`, `list-view`, `icon`, `hover-card` |
| **Status** | documented |

## Description
A map view shows interactive maps (Google Maps, Leaflet, OpenStreetMap).

## Purpose

- Showing a location
- Map view
- Geo data

## Variants

| Variant | Description |
|---------|-------------|
| **standort** | one place with an address, usually inside a form |
| **sammlung** | many markers with a selection, often as a list as well |
| **route** | lines and areas (paths, regions) instead of single points |

## Features

- Markers
- Polyline
- Polygon
- Zoom & pan
- Search
- Geolocation

## Distinction

- **Do not confuse with** [embed](../../../workbenches/special/embed/): a foreign map application is
  embedded, this component draws the map itself (OpenStreetMap, Leaflet).
- The matching place list is a [list-view](../../data/list-view/), the marker an
  [icon](../../../primitives/media/icon/) — both separate components.
- A map without a geo reference (floor plan, site plan) is an [image](../../../primitives/media/image/).

## Best Practices

- Keep the map service configurable instead of hard-wired (data protection, costs).
- Always offer a non-cartographic alternative: the address as text, the place as a list.
- Label the markers; colour alone carries no information.
- Set the initial view and zoom level, nobody wants to see the whole world.
- Locate only after consent; without locating, allow manual entry.

## See also

- [special – overview](../index.md)
- [Embed](../../../workbenches/special/embed/) — foreign map services
- [List View](../../data/list-view/) — place list
- [Base component](../../../primitives/basics/base.md)
