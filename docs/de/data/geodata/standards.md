# Geodaten – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.**

## Stand 2026-11-05 (jüngste Standards, ADR 0026)

Beleg: `temp/research/geodata-projects-profile-login.md` (2026-11-05).

| Standard | Beleg | Rolle |
|----------|-------|-------|
| GeoJSON RFC 7946 | ✅ weiter aktuell | gespeicherte Geometrie |
| **OGC JSON-FG 1.0** (2026-05-21) | ✅ | GeoJSON-Obermenge (CRS, Zeit, Körper) — nutzen, wo GeoJSON nicht reicht |
| OGC API – Features Teile 1/2 1.0.1, Teil 3 (Filter), Teil 5 (Schemata) final; Teil 4 (CRUD) Entwurf | ✅ | unsere Geodaten-API |
| **GeoParquet 2.0.0** (2026-11-05), PMTiles v3, CityJSON 2.0.2, FlatGeobuf v3 (OGC-Status ⚠️) | ✅ | Massenexport, Kacheln, 3D |
| `geo:`-URI RFC 5870 | ✅ | JSContact `Address.coordinates` |
| ISO 19160 Teile 1–4 | ✅ | nur Teil 1 (UML) ist öffentlich (ISO/TC 211 GitHub); **die Element-Codes von Teil 4 sind hinter einer Paywall** → wir nutzen die JSContact-Adresskomponenten (offen) und führen **keine** 19160-4-Namen |
| **Bild-Metadaten:** Exif 3.1 (CIPA DC-008-2026), Exif↔XMP-Mapping CIPA DC-010-2026, XMP ISO 16684-1:2019, IPTC Photo Metadata 2025.1 ("Location Created/Shown") | ✅ | Metadaten **im** Bild — die Datei ist das Original (ADR 0030; Galerie-Idee, Protokoll §22) |

## Standards in dieser Domäne

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **The GeoJSON Format, RFC 7946** | ✅ | kanonisches Modell für Geometrien (Beschluss 1): `Feature`, `FeatureCollection`, `geometry` (Punkt/Linie/Polygon), `properties` |
| **`geo:`-URI, RFC 5870** | ✅ | Koordinatenformat in JSContact `Address.coordinates` |
| **JSContact `Address`** (RFC 9553 §2.5.1) | ✅ | Postadressen mit Komponententypen (`locality`, `region`, `postcode`, `country`, …) |
| **ISO 19160 Addressing** (Teil 1:2015, Teil 4:2023) | ✅ URL geprüft, **Inhalt ungelesen** ⚠️ | konzeptioneller Rahmen für internationale Postadressen |

## GeoJSON — geprüfter Rahmen (RFC 7946, ✅)

- `type`: `Feature` | `FeatureCollection` | Geometrietypen `Point`, `MultiPoint`, `LineString`, `MultiLineString`, `Polygon`, `MultiPolygon`, `GeometryCollection`
- `Feature` hat `geometry`, `properties`, optional `id`
- Koordinaten: `[longitude, latitude]` (bei Höhen drittes Element)

## JSContact-`Address` — geprüfte Bausteine (RFC 9553, ✅)

`components[]` mit `kind` (u. a. `street`, `locality`, `region`, `postcode`, `country`), dazu `texts[]` (mehrsprachige Einzeiler-Formen) und `coordinates` als `geo:`-URI. Details: [people/jscontact/description.md](../people/jscontact/description.md).

## Offene Standard-Punkte

- **ISO 19160 lesen und entscheiden:** nutzen wir nur die JSContact-Komponenten, oder führen wir die 19160-Elementnamen für Exporte mit? (⚠️ Inhalt ungelesen — bewusst nicht nachgeladen am 2026-11-02)
- **DIN/ISO zu Adressformaten pro Land:** nicht recherchiert; bei Bedarf einzelne Länder-Normen belegen.
