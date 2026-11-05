# uMap - Description

## What the program does

uMap turns OSM maps into jointly maintained topic cards: a hike with huts, member locations, demonstration meeting points — layers, markers with popup text, a share link straight into the wiki.

## Advantages

- **zero GIS knowledge needed**, collaborative immediately
- **the data remains accessible as GeoJSON** (import/export/remote sources)
- self-hostable, easy to integrate in a FreeSynergy environment

## Differentiation

| System | Difference |
|--------|------------|
| **Google My Maps** | Proprietary, no export cycle; uMap is open |
| **QGIS web publishing** | Professional workflows; uMap is an end-user editor |
| **OSM directly** | Global data; uMap is private/group maps on top of OSM |

## Technical details

- **Stack**: Django (Python), PostgreSQL/PostGIS, Leaflet frontend
- **Models**: Map (JSON data blob or remote datamode), Datalayer, Pict
- **Auth**: instance login optional; map access via link/token
- **Licence**: MPL-2.0 (uMap), OSM data ODbL

## Who it suits

- Groups that collect/comment on places together → the core of the [location point model](../../../standpunkte.md)
