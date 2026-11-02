# Geodaten – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.**

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

`components[]` mit `kind` (u. a. `street`, `locality`, `region`, `postcode`, `country`), dazu `texts[]` (mehrsprachige Einzeiler-Formen) und `coordinates` als `geo:`-URI. Details: [contacts/jscontact/beschreibung.md](../contacts/jscontact/beschreibung.md).

## Offene Standard-Punkte

- **ISO 19160 lesen und entscheiden:** nutzen wir nur die JSContact-Komponenten, oder führen wir die 19160-Elementnamen für Exporte mit? (⚠️ Inhalt ungelesen — bewusst nicht nachgeladen am 2026-11-02)
- **DIN/ISO zu Adressformaten pro Land:** nicht recherchiert; bei Bedarf einzelne Länder-Normen belegen.
