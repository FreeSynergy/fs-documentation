# OpenStreetMap - API Dokumentation

## Übersicht

OSM hat eine ganze API-Familie: **OSM API 0.6** (Karte lesen/schreiben, Changesets), **Overpass** (Leseabfragen), **Nominatim** (Suche/Geocoding), Diff-/Planet-Downloads. Authentifizierung nur für Schreibzugriff (OAuth2/OpenID).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| OSM API `api.openstreetmap.org/api/0.6/…` | elements, changesets, notes, GPS traces | offiziell |
| Overpass QL (`overpass-api.de/api/interpreter`) | geofilterte Objekt-Abfragen (JSON/XML) | Community-Standard |
| Nominatim (`nominatim.openstreetmap.org`) | search/reverse | offiziell (Usage-Policy!) |
| Mapillary/Notizen | Bild-/Hinweis-APIs | offiziell (Notes) |
| GraphQL | — | ❌ |

## Authentifizierung

- Lesen: ohne Login (Rate-Limits respektieren!)
- Schreiben: OAuth2 (OSM-Login) → `PUT /api/0.6/changeset/create` als User

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/0.6/map?bbox=l,s,r,t` | Rohdaten im Ausschnitt (OsmXML) |
| `GET` | `/api/0.6/node/{id}` | Element |
| `PUT` | `/api/0.6/changeset/create` | Changeset öffnen |
| `PUT/POST` | `/api/0.6/node/create` | Element anlegen (im Changeset) |
| `GET` | `/api/0.6/notes?bbox=…` | Fehler-Notizen lesen |
| `POST` | `/api/0.6/node/{id}/comment` | Notiz kommentieren |
| `POST` | `overpass…/api/interpreter` | Overpass-Query |
| `GET` | `nominatim…/search?q=…&format=jsonv2` | Suche |

## Beispiel

Overpass: alle Bäckereien in Tübingen:

```
[out:json][timeout:25];
area["name"="Tübingen"]["admin_level"="8"]->.a;
(node["shop"="bakery"](area.a););
out body;
```

Nominatim:

```http
GET /search?q=Bahnhof+Tübingen&format=jsonv2&limit=3 HTTP/1.1
User-Agent: fs-skin-demo/1.0
```

Response: `[{ "place_id":…, "lat":48.530, "lon":9.058,
"display_name":"Tübingen Hbf, …", "type":"railway" }]`

## Rate Limits

OSM-API: moderate Limits (Write-Bursts begrenzt); **Overpass/Nominatim laufen öffentlich mit fairen Limits** → für Skin-Produktion: eigene Instanz oder Dienstleister.

## SDKs und Client-Bibliotheken

- Python `osmapi`, `overpy`/`requests-overpass`; JS `osm`-Tools
- Osmosis/osmium für Datenverarbeitung, `pyosmium`

## Skin-Hinweis

Overpass-Abfragen = Datenquelle für [Standpunkte](../../standpunkte.md)-Skins; Attribution („© OpenStreetMap contributors“) in jeder Skin-Ausgabe Pflicht (ODbL).
