# uMap - API Dokumentation

## Übersicht

uMap ist datenoffen: Karten-Daten liegen als **GeoJSON** vor (Export-Link, Remote-Quellen). Die Django-Instanz hat JSON-Endpunkte für Maps/Datalayers (kurzlebig über Versionen — für Skin-Integration primär Export/Import + Remote-GeoJSON nutzen).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Export GeoJSON/GPX/KML (`/export/` im Karten-Menü) | Daten rausziehen | offiziell |
| Remote-Data (URL-Ebene) | Daten rein (Live-GeoJSON) | offiziell |
| Interne REST-artige Endpunkte (`/map/{id}/`, `/datalayer/…`) | UI-intern | instanzabhängig (nicht stabil) |
| Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Authentifizierung

- öffentliche Karten: keine
- Bearbeiten per **Edit-Token-Link** (Geheimnis im Link) oder Instanz-Login (selbst gehostet)

## Muster: Datenkreislauf für Skins

```
FreeSynergy-Datenbank → GeoJSON end Point (eigener Dienst)
      → uMap-Ebene „Remote Data“ (automatisch neu geladen)
      → manuelle Ergänzungen der Gruppe → Export → zurückspielen
```

GeoJSON-Schema (praktisch):

```json
{ "type": "FeatureCollection", "features": [
  { "type": "Feature",
    "geometry": { "type": "Point", "coordinates": [9.058, 48.530] },
    "properties": { "_title": "Treffpunkt Hbf",
      "_description": "Brunnenseite", "_iconClass": "tintred" } } ] }
```

(`_title`/`_description`/`_iconClass` = uMap-Konventionen.)

## Einbettung

iframe aus „Teilen“: `https://uMap.example.org/map/{id}#/{zoom}/{lat}/{lng}` — Deep-Links auf Marker per `marker-{id}`-Hash.

## Rate Limits

Instanzbetreiber-seitig (OSM-Kacheln über Proxy empfohlen).

## Skin-Hinweis

Standpunkte-Skins schreiben GeoJSON und nutzen uMap als **View-Layer**; Rechte-Logik bleibt in FreeSynergy ([standpunkte.md](../../standpunkte.md)).
