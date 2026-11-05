# Geodata – technical explanation

## Storage perspective

- **Table `location`** for standalone places (map features): one row per GeoJSON `Feature`; canonical payload = feature JSON (decision 4). Extracted columns: `id` (ULID), `geometry_type`, `bbox` (index), `created_at`, `updated_at`.
- **Addresses are not a table of their own** as long as they belong to a card: they stay in the card's JSON in [contacts/](../contacts/index.md) (`addresses` map with components). This domain only defines the **component names and validation**.

## Keys and links

- Externally: `https://<instance>/geodata/<ulid>` (decision 3). An appointment in [events/](../events/index.md) references this IRI via JSCalendar `locations`/`locationId`.
- Coordinates in maps: `Address.coordinates` requires a `geo:` URI (RFC 5870, ✅), e.g. `geo:52.5200,13.4050`.

## Flow

1. Create/change a feature: `Create`/`Update` (AS2 envelope) with a GeoJSON payload.
2. Map clients query filters via BBox/radius (API pattern in [api.md](../api.md)); the answer is a `FeatureCollection`.
3. Address entry in every app produces **components**, not a free-text line; the presentation (one line, country-specific) is a render rule, not storage.

## Projections

| Target | Projection |
|--------|------------|
| [events/](../events/index.md) | JSCalendar `locations` (text + reference) |
| [contacts/](../contacts/index.md) | `Address` components + `geo:` URI |
| Map renderers | tiles (MVT) — generated from the geometries, not stored |
| ISO-OA exports | components in ISO 19160 names, if we carry them (open) |

## Open technical points

- Do we carry ISO 19160 **element names** in addition to the JSContact components? (decision open, the content of ISO 19160 is still unread — ⚠️)
- Topology between features (building ⊂ plot) is not standardised — needs our own decision, not started yet.
