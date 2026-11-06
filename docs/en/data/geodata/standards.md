# Geodata – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.**


## State 2026-11-05 (newest standards, ADR 0026)

Evidence: `temp/research/geodata-projects-profile-login.md` (2026-11-05).

| Standard | Evidence | Role |
|----------|----------|------|
| GeoJSON RFC 7946 | ✅ still current | stored geometry |
| **OGC JSON-FG 1.0** (2026-05-21) | ✅ | GeoJSON superset (CRS, time, solids) — use where GeoJSON is not enough |
| OGC API – Features Parts 1/2 1.0.1, Part 3 (filter), Part 5 (schemas) final; Part 4 (CRUD) draft | ✅ | our geodata API |
| **GeoParquet 2.0.0** (2026-11-05), PMTiles v3, CityJSON 2.0.2, FlatGeobuf v3 (OGC status ⚠️) | ✅ | bulk export, tiles, 3D |
| `geo:` URI RFC 5870 | ✅ | JSContact `Address.coordinates` |
| ISO 19160 parts 1–4 | ✅ | only part 1 UML is public (ISO/TC 211 GitHub); **part 4 element codes are paywalled** → we use JSContact address components (open) and do **not** carry 19160-4 names |
| **Image metadata:** Exif 3.1 (CIPA DC-008-2026), Exif↔XMP mapping CIPA DC-010-2026, XMP ISO 16684-1:2019, IPTC Photo Metadata 2025.1 ("Location Created/Shown") | ✅ | metadata **inside** image files — the file is the original (ADR 0030; gallery idea, protocol §22) |

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

`components[]` with `kind` (among others `street`, `locality`, `region`, `postcode`, `country`), plus `texts[]` (multilingual one-line forms) and `coordinates` as a `geo:` URI. Details: [people/jscontact/description.md](../people/jscontact/description.md).

## Open standard points

- **Read ISO 19160 and decide:** do we only use the JSContact components, or do we also carry the 19160 element names for exports? (⚠️ content unread — deliberately not reloaded on 2026-11-02)
- **DIN/ISO on address formats per country:** not researched; if needed, evidence individual country standards.
