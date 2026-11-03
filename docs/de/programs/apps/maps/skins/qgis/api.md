# QGIS - API Dokumentation

## Übersicht

QGIS öffnet drei Türen: **PyQGIS** (Python-Konsole/Plugins im Desktop), **QGIS Server** (OGC-Dienste aus dem Projekt) und die **Datenformate** (GeoPackage/PostGIS — der eigentliche Austausch). 

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| PyQGIS (`qgis.core`, `qgis.gui`, `qgis.utils`) | everything inside QGIS | offiziell |
| Processing-API | Algorithmen skriptbar (`processing.run`) | offiziell |
| QGIS Server OGC: WMS/WFS(2.0)/WCS/WMTS | Karten-/Feature-Dienste | offiziell |
| Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## PyQGIS (Beispiel)

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

- Deployment: FCGI/Apache, Docker (`qgis/qgis-server`), oder **PGF/Plugin-Stacks**
- Zugriffschutz: Service-Capabilities einschränken, OGC-Access-Controls im Projekt

## GeoPackage als Skin-Boden

- eine Datei = viele Layer + Trigger/Metadaten; ideal für Git-ferne Gruppenverteilung (QGIS ↔ Server ↔ QField)

## Rate Limits

Server-seitig (FCGI-Prozesse); OGC-Parameter `maxfeatures`.

## Skin-Hinweis

Standpunkte-Herkunft oft QGIS (Prüfen/Puffern) → Publish via WFS-JSON → Leaflet/MapLibre-View; Chain in [standpunkte.md](../../standpunkte.md).
