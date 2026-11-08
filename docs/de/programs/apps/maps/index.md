# Kartensysteme

## Kurz gesagt

FreeSynergy Maps bringt Kartendaten auf dein Gerät und behält die Orte, die dir wichtig sind. Es beantwortet die Frage: Kann ich meine eigene Karte haben und sie trotzdem nutzen, wenn das Netz weg ist? Es lädt eine Karte Stück für Stück, nur das, was du ansiehst, und du kannst eine ganze Region zur Offline-Nutzung herunterladen.

## Was hier anders ist

- Es gibt keinen Standard-Kartenserver, und nichts wird kopiert. Du zeigst es auf eine Kartenquelle deiner Wahl, im offenen PMTiles-Format.
- Es belastet öffentliche Server nicht: Es nutzt die Kachelserver von OpenStreetMap nicht, verlangt eine eindeutige User-Agent-Kennung und stellt nur wenige Anfragen.
- Der vorgeschriebene Quellenhinweis wird in jede heruntergeladene Region geschrieben.
- Orte werden als GeoJSON gespeichert, ein offener Standard. Maps besitzt die Schnittstelle für Orte.
- Kacheln werden auf deiner Festplatte zwischengespeichert, mit einer Größenbegrenzung, die du festlegst.

## Wo es heute steht

Neueste Version: `v0.2.0`. Heute ist es der Kern, ohne Fenster. Es kann Kacheln aus einer entfernten oder lokalen PMTiles-Datei lesen und sie auf der Festplatte zwischenspeichern, mit einer harten Größengrenze und einem Verfall nach sieben Tagen. Es kann eine Region zur Offline-Nutzung herunterladen und vorher die Anzahl der Kacheln und eine Größenschätzung nennen, mit einer Kachelgrenze, Fortschrittsanzeige und einer Abbruchoption. Es hält Orte als GeoJSON (anlegen, aktualisieren, löschen, nach Name finden, alles innerhalb eines Gebiets finden) und liest und schreibt `geo:`-Links.

Noch nicht da (geplant): ein Fenster und das Zeichnen von Karten (Kachel-Dekodierung, Stile, Suche nach Adressen und Routen sind nicht begonnen), ein Server, damit andere Programme es erreichen können, und Live-Benachrichtigungen, wenn sich ein Ort ändert. Die Schnittstelle für Orte ist ein Entwurf ohne Anbindung.

## Übersicht

Dieser Bereich enthält Dokumentation für verschiedene Karten- und GIS-Systeme.

## Verfügbare Systeme

- **openstreetmap** - Kooperatives Kartenprojekt
- **mapbox** - Anpassbare Karten
- **leaflet** - Bibliothek für interaktive Karten
- **cesium** - 3D-Globus- und Kartenengine
- **qgis** - GIS-Software
- **arcgis** - Geografisches Informationssystem
- **google-maps** - Google-Maps-API
- **openlayers** - Kartenbibliothek
- **carto** - Geodaten-Plattform
- **maplibre** - Quelloffenes Kartenprojekt
- **tangram** - Echtzeit-3D-Karten
- **mapnik** - Kartenrendering-Engine
- **geoserver** - Geodaten-Server
- **postgis** - Räumliche Datenbank
- **mapbox-gl-js** - Interaktive Karten

## Was ist ein Kartensystem?

Ein Kartensystem ist eine Software zur Erstellung, Anzeige und Analyse von Karten und geografischen Daten. Kartensysteme umfassen:

- Kartenanzeige und -navigation
- Geodaten-Verwaltung
- Kartenebenen und -stile
- Geocodierung und umgekehrte Geocodierung
- Routenplanung und Navigation
- Geoanalyse

## Anwendungsbereiche

- **Navigation**: Routenplanung und Navigation
- **GIS**: Geografische Informationssysteme
- **Logistik**: Logistik und Transport
- **Umwelt**: Umweltüberwachung und -analyse
- **Stadtplanung**: Stadtplanung und -entwicklung
- **Tourismus**: Tourismus und Reisen

## Vorteile von Kartensystemen

- **Visualisierung**: Geografische Daten sichtbar machen
- **Analyse**: Geoanalyse
- **Integration**: Integration mit anderen Daten
- **Interaktivität**: Interaktive Karten
- **Mobil**: Mobile Kartenanwendungen

## Auswahlkriterien

Bei der Wahl eines Kartensystems solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen sind nötig?
- **Skalierbarkeit**: Wie viele Karten und Nutzer?
- **Bedienbarkeit**: Wie benutzerfreundlich ist es?
- **Integration**: Integration mit anderen Werkzeugen
- **Kosten**: Kostenlos oder kostenpflichtig?
- **Open Source**: Ist das System Open Source?

## Verwandte Kategorien

- [ERP](../../suites/erp/) - Enterprise Resource Planning
- [Projektmanagement](../../suites/projectmanagement/) - Projektmanagement

## Schnellstart

1. **System auswählen**: Wähle ein System anhand der Anforderungen
2. **Installation/Konto**: System installieren oder Konto anlegen
3. **Konfiguration**: System anpassen und einrichten
4. **Daten importieren**: Geodaten importieren
5. **Karten erstellen**: Erste Karten erstellen

## Weitere Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Kartensysteme.

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (7), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Leaflet](frontends/leaflet/index.md) — Leaflet (BSD-2-Clause) ist die schlanke JavaScript-Kartenbibliothek: Rasterkacheln, Marker, Polygone, Wechsel von Ebenen, Touch-Unterstützung — der Standard, auf dem uMap und Tausende Kartenwidgets aufsetzen.
- [MapLibre](frontends/maplibre/index.md) — MapLibre (BSD, ein Fork von Mapbox GL JS nach der Lizenzänderung) ist die **Vektorkarten-Engine**: Kacheln und Stil-JSON (GL Style Spec), WebGL-Rendering mit 3D-Neigung, eigene Stile (Maputnik), selbst gehos…
- [OpenStreetMap](frontends/openstreetmap/index.md) — OpenStreetMap (OSM) ist die weltweite gemeinschaftliche Kartenplattform: Jeder bearbeitet die Geodaten („das Wiki der Karten“).
- [Organic Maps](frontends/organic-maps/index.md) — Organic Maps (GPL, abonnementfreie gemeinnützige App) ist die schlanke Offline-Karten- und Navigations-App (Android/iOS/Desktop): schnell, sparsam mit Daten (keine Tracking- oder Werbelogik), OSM-basiert, mit eigenen Orten…
- [OsmAnd](frontends/osmand/index.md) — OsmAnd (Apache-2.0) ist die auf OSM basierende Offline-Navigations-App (Android/iOS): herunterladbare Kartenregionen, Routing (Auto/Rad/zu Fuß; ÖPNV-Planer offline verfügbar), POI-Suche, Streckenaufzeichnung…
- [QGIS](frontends/qgis/index.md) — QGIS (GPL) ist das professionelle Desktop-GIS: Ebenen (Shapefile/GeoPackage/PostGIS/WMS), Analysewerkzeuge (Puffer, Überlagerungen, Geoverarbeitung), Druck-Layouts, **QGIS Server** (OGC-Dienste) und Python (P…
- [uMap](frontends/umap/index.md) — uMap (uMap Project, freie Software) ist **gemeinschaftliches Kartenzeichnen**: eigene Ebenen mit Markern, Linien und Polygonen, Popup-Inhalte (HTML), Teilen per Link, gleichzeitiges Bearbeiten durch mehrere Nutzer.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
