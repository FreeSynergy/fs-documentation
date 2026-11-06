# Geodata – description

**What this domain is:** places as **geometries and features** (maps, points, ways) and the **component model of postal addresses**. Canonical model: **GeoJSON** (RFC 7946, ✅) for geometries; **JSContact `Address`** (RFC 9553 §2.5.1, ✅) for postal addresses; conceptual frame **ISO 19160** (✅ URL verified, content unread).

**What it covers:**

- Features for map views (`map-view`): point, line, polygon as GeoJSON
- Coordinates given as a `geo:` URI (RFC 5870, ✅)
- International postal addresses **without Western-Europeanisation**: addresses consist of named components (`locality`, `region`, `postcode`, `country`, …), not fixed fields like "street + house number"
- Linking features to other domains (appointment `locations`, map markers on contacts)

**Differentiation from other domains:**

| Topic | Where it lives | Why |
|-------|----------------|-----|
| Postal address **of a person/organisation** | [people/](../people/index.md) (JSContact `Address`) | the address is part of the card; this domain only supplies the address **model** |
| Place **at an appointment** | [events/](../events/index.md) (JSCalendar `locations`) | the appointment references a place but does not own it |
| Tile formats (PBF/MVT) | outside (map technology) | presentation format, not a data standard |

**Why this is a domain of its own:** the address component model and the geometries are needed across domains (contacts, events, projects, marketplace). Copying one "address" field per module violates rule no. 1 (one field, one owner).
