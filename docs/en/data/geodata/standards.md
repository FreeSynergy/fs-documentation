# Geodata – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.**

## Standards in this domain

| Standard | Evidence | Role |
|----------|----------|------|
| **The GeoJSON Format, RFC 7946** | ✅ | canonical model for geometries (decision 1): `Feature`, `FeatureCollection`, `geometry` (point/line/polygon), `properties` |
| **`geo:` URI, RFC 5870** | ✅ | coordinate format in JSContact `Address.coordinates` |
| **JSContact `Address`** (RFC 9553 §2.5.1) | ✅ | postal addresses with component types (`locality`, `region`, `postcode`, `country`, …) |
| **ISO 19160 Addressing** (part 1:2015, part 4:2023) | ✅ URL verified, **content unread** ⚠️ | conceptual frame for international postal addresses |

## GeoJSON — verified frame (RFC 7946, ✅)

- `type`: `Feature` | `FeatureCollection` | geometry types `Point`, `MultiPoint`, `LineString`, `MultiLineString`, `Polygon`, `MultiPolygon`, `GeometryCollection`
- `Feature` has `geometry`, `properties`, optional `id`
- Coordinates: `[longitude, latitude]` (with altitude as a third element)

## JSContact `Address` — verified building blocks (RFC 9553, ✅)

`components[]` with `kind` (among others `street`, `locality`, `region`, `postcode`, `country`), plus `texts[]` (multilingual one-line forms) and `coordinates` as a `geo:` URI. Details: [contacts/jscontact/description.md](../contacts/jscontact/description.md).

## Open standard points

- **Read ISO 19160 and decide:** do we only use the JSContact components, or do we also carry the 19160 element names for exports? (⚠️ content unread — deliberately not reloaded on 2026-11-02)
- **DIN/ISO on address formats per country:** not researched; if needed, evidence individual country standards.
