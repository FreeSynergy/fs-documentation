# MapLibre - Description

## What the program does

MapLibre renders maps as vector stacks: the browser draws streets/buildings/labels from tiles in your own style — scalable, animatable, 3D-capable. It emerged from the Mapbox GL community as a free branch (fork) after their licence change.

## Advantages

- **free styling latitude** (Maputnik, your own tiles, PMTiles files)
- **performance** with large data volumes (WebGL)
- API compatible enough with Mapbox GL, migration is easy

## Differentiation

| System | Difference |
|--------|------------|
| **Leaflet** | Raster + DOM, simple; MapLibre = WebGL/style engine |
| **Mapbox GL** | A service + mandatory token; MapLibre is neutral/self-hosted |
| **Cesium** | Globe/era 3D; MapLibre stays with Web Mercator maps |

## Technical details

- **API**: `maplibregl.Map({style: url|json})`, the layer/source API, `queryRenderedFeatures`
- **Tiles**: pbf + style.json; alternatives PMTiles (single file)
- **Licence**: BSD-3

## Who it suits

- Map apps with their own style/performance; FreeSynergy skins for interactive location point maps with 3D/clusters
