# MapLibre Dokumentation

> Kategorie: [maps](../../index.md)

## Übersicht

MapLibre (BSD, Abspaltung von Mapbox GL JS nach Lizenzwechsel) ist die **Vektorkarten-Engine**: Kacheln + Stil-JSON (GL Style Spec), WebGL-Rendering mit 3D-Kippen, eigene Stile (Maputnik), Self-hosting der Kacheln (Tilemaker/Martin). Der moderne Standard für freie Karten-Apps (OsmAnd-Karten, Organic-Kacheln, viele Web-Maps).

## Bemerkenswerte Ideen

_Zu tun: Was kann dieses Programm, das andere nicht können? Warum ist es hier dokumentiert (ADR 0013)?_

## Dokumentierte Versionen

<!-- gen:versions (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Abgrenzung zu Leaflet, Mapbox, Cesium |
| [features.md](latest/features.md) | Vektorkacheln, Stil-Spec, 3D, Was MapLibre NICHT kann |
| [layout.md](latest/layout.md) | Canvas-Schichten, Stil-Layer, Control-Overlay |
| [menus.md](latest/menus.md) | UI-Controls (Navigation/Geolocate/Scale), Stil-Editing (Maputnik) |
| [shortcuts.md](latest/shortcuts.md) | Interaktionen (Maus/Touch, Keyboard eingeschränkt) |
| [api.md](latest/api.md) | JS-API (`maplibregl.Map`), Style-Spec, Kachel-Server-Wege |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->
