# OpenStreetMap - API documentation

## Overview

OSM has a whole API family: the **OSM API 0.6** (read/write map, changesets), **Overpass** (read queries), **Nominatim** (search/geocoding), diff/planet downloads. Authentication only for write access (OAuth2/OpenID).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| OSM API `api.openstreetmap.org/api/0.6/…` | Elements, changesets, notes, GPS traces | official |
| Overpass QL (`overpass-api.de/api/interpreter`) | Geo-filtered object queries (JSON/XML) | Community standard |
| Nominatim (`nominatim.openstreetmap.org`) | Search/reverse | official (usage policy!) |
| Mapillary/notes | Image/notice APIs | official (notes) |
| GraphQL | — | ❌ |

## Authentication

- Reading: without login (respect the rate limits!)
- Writing: OAuth2 (OSM login) → `PUT /api/0.6/changeset/create` as a user

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/0.6/map?bbox=l,s,r,t` | Raw data in the extent (OsmXML) |
| `GET` | `/api/0.6/node/{id}` | Element |
| `PUT` | `/api/0.6/changeset/create` | Open a changeset |
| `PUT/POST` | `/api/0.6/node/create` | Create an element (within a changeset) |
| `GET` | `/api/0.6/notes?bbox=…` | Read error notes |
| `POST` | `/api/0.6/node/{id}/comment` | Comment a note |
| `POST` | `overpass…/api/interpreter` | Overpass query |
| `GET` | `nominatim…/search?q=…&format=jsonv2` | Search |

## Example

Overpass: all bakeries in Tübingen:

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

## Rate limits

OSM API: moderate limits (write bursts limited); **Overpass/Nominatim run publicly with fair limits** → for skin production: your own instance or a provider.

## SDKs and client libraries

- Python `osmapi`, `overpy`/`requests-overpass`; JS `osm` tools
- Osmosis/osmium for data processing, `pyosmium`

## Skin note

Overpass queries = the data source for the [location point (Standpunkte)](../../../standpunkte.md) skins; attribution ("© OpenStreetMap contributors") is mandatory in every skin output (ODbL).
