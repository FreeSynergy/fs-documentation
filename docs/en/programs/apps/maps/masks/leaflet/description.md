# Leaflet - Description

## What the program does

Leaflet puts "a map in a div": tiles, markers, GeoJSON — in ~40 KB of JS, runnable everywhere (oldest smartphones included). It is a library, not a service: map hosting and data come from elsewhere (OSM tiles are the classic).

## Advantages

- **minimal, stable, BSD** — the API has held for years
- **GeoJSON-first** = a perfect partner for the uMap/QGIS data cycles
- huge plugin/tutorial landscape

## Differentiation

| System | Difference |
|--------|------------|
| **MapLibre GL** | Vector tiles, 3D/pitch, styling; Leaflet = raster + SVG pragmatism |
| **OpenLayers** | Full GIS build-out (projections, WebGIS standards); Leaflet deliberately narrow |
| **Google Maps JS** | Proprietary + costs; Leaflet is free |

## Technical details

- **API**: `L.map('id')`, `L.tileLayer(url,{attribution})`, `L.geoJSON(data)`
- **Licence**: BSD-2-Clause
- **Age**: since 2011 (CloudMade → community), 1.x maintained stably

## Who it suits

- Wiki/CMS embeds, location point (Standpunkte) dashboards, prototypes ([standpunkte.md](../../standpunkte.md))
