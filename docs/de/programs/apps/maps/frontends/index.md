# Maps — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Maps` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Leaflet](leaflet/index.md) | [latest](leaflet/latest/description.md) | Leaflet (BSD-2-Clause) ist die leichtgewichtige JavaScript-Kartenbibliothek: Raster-Kacheln, Marker, Polygone, Layer-Wechsel, Touch-Unterstützung — der Standard, auf dem uMap und tausende Karten-Wi… |
| [MapLibre](maplibre/index.md) | [latest](maplibre/latest/description.md) | MapLibre (BSD, Abspaltung von Mapbox GL JS nach Lizenzwechsel) ist die Vektorkarten-Engine: Kacheln + Stil-JSON (GL Style Spec), WebGL-Rendering mit 3D-Kippen, eigene Stile (Maputnik), Self-hosting… |
| [OpenStreetMap](openstreetmap/index.md) | [latest](openstreetmap/latest/description.md) | OpenStreetMap (OSM) ist die weltweite kollaborative Kartenplattform: Jeder editiert die Geodaten („Wiki der Karten“). |
| [Organic Maps](organic-maps/index.md) | [latest](organic-maps/latest/description.md) | Organic Maps (GPL, Abo-freie Nonprofit-App) ist die schlanke Offline-Karten-/Navigations-App (Android/iOS/Desktop): schnell, datensparsam (keine Tracking-Werbelogik), OSM-basiert, mit eigenen Orten… |
| [OsmAnd](osmand/index.md) | [latest](osmand/latest/description.md) | OsmAnd (Apache-2.0) ist die Offline-Navigations-App auf OSM-Basis (Android/iOS): herunterladbare Kartenregionen, Routing (Auto/Rad/Fuß/ÖPNV-Routenplan offline möglich), POI-Suche, Track-Aufzeichnun… |
| [QGIS](qgis/index.md) | [latest](qgis/latest/description.md) | QGIS (GPL) ist das professionelle Desktop-GIS: Layer (Shapefile/GeoPackage/PostGIS/WMS), Analyse-Werkzeuge (Puffer, Überlagerungen, Geoprocessing), Druck-Layouts, QGIS Server (OGC-Dienste) und Pyth… |
| [uMap](umap/index.md) | [latest](umap/latest/description.md) | uMap (uMap Project, free software) ist kollaborative Karten-Diagrammung: eigene Ebenen mit Markern/Polylinien/Flächen, Popup-Inhalte (HTML), Sharing per Link, Mehrbenutzer-Edit. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/maps/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
