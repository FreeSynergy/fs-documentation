# Geodata

Places, coordinates and postal addresses. Resolves our criticism of the "Western-Europeanisation" of address fields (`mappings.md`): JSContact `Address` components + ISO 19160.

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **GeoJSON, RFC 7946** | ✅ | canonical model for geometries (features in `map-view`) |
| **`geo:` URI, RFC 5870** | ✅ | coordinates in JSContact `Address.coordinates` |
| **JSContact `Address`** (RFC 9553 §2.5.1) | ✅ | postal addresses with component types (`locality`, `region`, `postcode`, …) |
| **ISO 19160 Addressing** (part 1:2015, part 4:2023) | ✅ URL verified, content unread | conceptual frame for international postal addresses |

## Open points

- Read the ISO 19160 content and decide whether we only use the JSContact components or also carry the 19160 element names
- Tile formats (PBF/MVT) are map technology, not a data standard — outside this domain

## See also

- [standards.md → Places, files](../standards.md)
- [people/jscontact](../people/jscontact/description.md) (addresses belong to the card)
