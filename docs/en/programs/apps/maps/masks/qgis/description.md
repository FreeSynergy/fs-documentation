# QGIS - Description

## What the program does

QGIS is the workshop for geodata: prepare data, analyse it, tell it cartographically, publish it as an OGC service. Everywhere location points must be **checked, buffered, aggregated**, the path leads through QGIS.

## Advantages

- **a complete GIS** under GPL, cross-platform
- Processing = automatability (models, PyQGIS, batch)
- Server in the project: publish WMS directly from the desktop

## Differentiation

| System | Difference |
|--------|------------|
| **ArcGIS Pro** | Commercial, enterprise-intertwined; QGIS is open/community |
| **uMap/Leaflet** | End-user maps; QGIS is the analysis workshop |
| **GRASS GIS** | An analysis machine; QGIS = GUI + GRASS connection |

## Technical details

- **Stack**: C++/Qt, Python (PyQGIS), the GDAL/GEOS/PROJ libraries
- **Formats**: GeoPackage (the standard!), PostGIS as the server basis
- **Deploy**: Desktop installers, Docker for QGIS Server, OGC via FCGI/MapServer competition
- **Licence**: GPL

## Who it suits

- Map groups with an analytical claim + operating their own map services ([standpunkte.md](../../standpunkte.md))
