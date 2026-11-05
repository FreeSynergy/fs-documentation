# QGIS - API documentation

## Overview

QGIS opens three doors: **PyQGIS** (Python console/plugins in the desktop), **QGIS Server** (OGC services from the project) and the **data formats** (GeoPackage/PostGIS — the actual exchange).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| PyQGIS (`qgis.core`, `qgis.gui`, `qgis.utils`) | everything inside QGIS | official |
| Processing API | Scriptable algorithms (`processing.run`) | official |
| QGIS Server OGC: WMS/WFS(2.0)/WCS/WMTS | Map/feature services | official |
| Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## PyQGIS (example)

```python
from qgis.core import QgsProject, QgsVectorLayer
proj = QgsProject.instance()
std = QgsVectorLayer("/daten/standpunkte.gpkg|layername=punkte", "Standpunkte", "ogr")
proj.addMapLayer(std)
feat_iter = std.getFeatures()  # Attributzugriff, Geometrien (QgsGeometry)
```

Processing:

```python
processing.run("native:buffer",
  {"INPUT": std, "DISTANCE": 300, "OUTPUT": "/tmp/nahversorger.geojson"})
```

## QGIS Server (OGC)

```
GET /qgisserver?service=WMS&version=1.3.0&request=GetMap
    &map=/srv/projekte/standpunkte.qgs&layers=punkte
    &bbox=9.04,48.52,9.08,48.54&width=800&height=600&crs=EPSG:4326
GET …service=WFS…&request=GetFeature&typeName=punkte&outputFormat=application/json
```

- Deployment: FCGI/Apache, Docker (`qgis/qgis-server`), or **PGF/plugin stacks**
- Access protection: restrict the service capabilities, OGC access controls in the project

## GeoPackage as the skin foundation

- One file = many layers + triggers/metadata; ideal for group distribution outside git (QGIS ↔ server ↔ QField)

## Rate limits

Server-side (FCGI processes); the OGC parameter `maxfeatures`.

## Skin note

Location points often originate in QGIS (checking/buffering) → publish via WFS-JSON → Leaflet/MapLibre view; the chain is in [standpunkte.md](../../../standpunkte.md).
