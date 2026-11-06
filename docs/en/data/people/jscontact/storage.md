# JSContact – storage

According to decision 4 in [standards.md](../../standards.md) the **evidenced standard model is the source of truth**: contacts are stored field by field as a JSContact object (RFC 9553) — not in an intermediate table of our own from which the model is merely projected. All other formats (vCard, jCard, Cap'n Proto, JSON-LD/AS2) are derived projections.

## Basic rules

| Point | Rule | Evidence/decision |
|-------|------|-------------------|
| Canonical form | one card = one JSContact object, exact JSON fields | decisions 1, 4 |
| `uid` | stays identical across all projections and exports | RFC 9553 §2.3 |
| Internal ID | UUIDv7 (RFC 9562, time-sortable) | decision 3 |
| External handle | absolute IRI `https://<instance>/contacts/<uuid>` | decision 3 (AS2 Core §4.1) |
| Partial change | JSON Patch (RFC 6902) or `PatchObject` from RFC 9553; paths like `emails/work/value` | [api.md](../../api.md) |
| Own fields | only as vendor properties `<domain>:<name>` (RFC 9553 §1.8.1, ✅) — never through renamed or repurposed standard fields | decision 5 |

## Storage form

- The card is persisted as a whole (JSON column or document) so that the standard structure survives without field shredding
- Indexable extractions (`uid`, name components, organisation name, `directories`) may exist as derived columns/indexes — they are projections, not the source
- Revisions: the standard defines no revision model; FreeSynergy records changes in the **activity log** (ADR 0020), the export remains a single valid card

## Exchange paths (derived projections)

| Direction | Format | Mechanism |
|-----------|--------|-----------|
| Export/import file | vCard 4.0 (RFC 6350) | bridge via RFC 9554, lossless for the evidenced properties |
| Export/import JSON-vCard | jCard (RFC 7095) | conversion vCard ↔ JSON |
| Sync with clients | CardDAV (RFC 6352) | card ↔ vCard resource per contact folder (`directories`) |
| Envelope outwards | AS2/ActivityPub (`Create`/`Update`/`Delete`) | card as the domain payload in the object; `to`/`cc` control disclosure, not access (decision 2) |
| internally | Cap'n Proto (ADR 0021) | generated from the standard model (decision 4) |

## Open points (to be settled standards-conformingly, not invented)

- `lifecycle` as vendor property `freesynergy.net:lifecycle` (mechanism ✅, ADR 0028)
- Define revision/deletion states (`status`) in interplay with CardDAV sync
- `media` objects: data URI inline or moved to object storage with a URL — both are RFC 9553 conforming, document the decision

## See also

- [description.md](description.md) – what JSContact is
- [people/index.md](../index.md) – contacts domain
- [standards.md](../../standards.md) – decisions 1–5
- [mappings.md](../../mappings.md) – mapping onto legacy fields and target systems
- [api.md](../../api.md) – patch and error format
