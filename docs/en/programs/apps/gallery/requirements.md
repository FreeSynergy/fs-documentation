# Gallery — Requirements

What `FreeSynergy.Gallery` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.
The bytes of photos and videos live in `fs-files`; the gallery stores **metadata objects that
reference those files** (no raw storage management here). Sharing uses shared `fs-store` objects.

Status: `implemented` · `planned` · `proposed`

**Seen in** — analysed frontends: [Im](frontends/immich/index.md) Immich ·
[Ph](frontends/photoprism/index.md) PhotoPrism · [Li](frontends/librephotos/index.md) LibrePhotos ·
[Ly](frontends/lychee/index.md) Lychee · [Pi](frontends/piwigo/index.md) Piwigo ·
[Co](frontends/coppermine/index.md) Coppermine · [Da](frontends/damselfly/index.md) Damselfly ·
[Nc](frontends/nextcloud-photos/index.md) Nextcloud Photos.
*arch.* = required by our architecture or principles, not by counting.
⚠️ = not (or not clearly) evidenced in our files (frontend or standards); to be verified first.

**Rule:** a capability is *Required* when at least four of the eight frontends show it, or when
our architecture needs it. The capability id in backticks (`<object>.<action>`) is a proposal —
a capability is an action on the object, never a menu item or a gesture.
**Exception:** face recognition and ML tagging are shown by 4–5 frontends but stay *Optional*:
they run **local only** (data must not leave the device), and faces are sensitive data
(see below).

**Sensitive data (ADR 0029):** photos can reveal faces (biometric), health, religion, place and
home. Such fields or objects must be **marked** (vocabulary: W3C DPV 2.3 `dpv:SpecialCategoryPersonalData`;
a biometric-specific DPV term is ⚠️ not checked). Marked data is never linked automatically
(no automatic `owl:sameAs`), leaves the device only with explicit approval per recipient,
is stored encrypted by default (ADR 0024) and is visibly marked in frontends.

Data references: [standards](../../../data/standards.md) ·
[geodata](../../../data/geodata/standards.md) (Exif 3.1, XMP, IPTC 2025.1, GeoJSON) ·
[models](../../../data/models.md) (File / media: `mimeType`, `checksum`, `width`/`height`, `duration`).

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Register a file as a media object that references it in `fs-files` (`media.register`) | *arch.* (bytes in `fs-files`) | AS2 `Image` / `Video` with a reference to the File record (`mimeType`, `checksum` `sha256:…`, `width`/`height`, `duration`) | proposed |
| Import media: upload, folder, URL, from other tools (`media.import`) | Im, Ph, Li, Ly, Pi, Co, Da, Nc | creates the file in `fs-files`, then `media.register`; import formats of other tools: gap | proposed |
| Scan / watch a folder and index new or changed files incrementally (`library.scan`) | Im, Ph, Li, Pi, Co, Da, Nc | triggers on `fs-files` changes; file `checksum` | proposed |
| Upload automatically from a phone or client (`media.autoUpload`) | Im, Li, Nc, Pi (Companion app) | client path onto `media.import`; resume of progress: gap | proposed |
| Read capture metadata: date, camera, GPS, description (`metadata.read`) | Im, Ph, Pi, Ly | Exif 3.1, Exif↔XMP mapping, XMP, IPTC 2025.1; the file stays the original (ADR 0030) | proposed |
| Edit metadata: date correction, description, location, in series (`metadata.edit`) | Im, Ph, Pi, Da | stored in the metadata object, original file untouched; write-back to XMP sidecar → Optional | proposed |
| Tag media manually (`tag.add`, `tag.remove`) | Im, Ph, Pi, Da | Web Annotation motif `tagging` (ADR 0033); label vocabulary: gap | proposed |
| Generate previews and thumbnails in several sizes, original unchanged (`preview.generate`) | Im, Ph, Ly, Pi, Co, Nc | derived locally, stored as files in `fs-files`; no standard for size sets: gap | proposed |
| List media on a timeline grouped by day / month / year (`media.list`) | Im, Li, Nc, Ph, Da | view parameters over Exif capture date | proposed |
| Open one item in a viewer: full size, slideshow, metadata overlay (`media.open`) | Im, Ph, Li, Ly, Pi, Nc | AS2 `Image` / `Video` + File URL | proposed |
| Play videos: seek, stream, thumbnail (`video.play`) | Im, Ph, Li, Nc, Da | AS2 `Video`; `duration`; streaming delivery from `fs-files`; transcoding → Optional | proposed |
| Search by text, date, place, folder, label, camera, media type (`media.search`) | Im, Ph, Li, Da, Nc, Ly | full text and filters over metadata fields; query model: gap | proposed |
| Create, rename, describe, delete albums (`album.create`, `album.edit`, `album.delete`) | Im, Ph, Li, Ly, Pi, Co, Da, Nc | AS2 `Collection` / `OrderedCollection` | proposed |
| Add and remove media in an album; one item in several albums (`album.add`, `album.remove`) | Im, Ph, Li, Ly, Pi, Co, Da, Nc | AS2 `Add` / `Remove` on the `Collection`; items by reference, not copy | proposed |
| Nest albums in sub-albums or folders (`album.nest`) | Ly, Pi, Co, Ph (folders), Nc (folder albums) | AS2 `Collection` with `partOf`-style link ⚠️ no tree profile: gap | proposed |
| Share an album or item by link, with password, expiry and download permission (`share.create`) | Im, Ph, Ly, Da, Nc | shared `fs-store` object (ADR 0019); link/permission model: gap | proposed |
| Share with named users or groups, with permissions (`share.grant`, `share.revoke`) | Im, Li, Nc, Pi, Co, Ly | shared `fs-store` object; roles: gap | proposed |
| Download an original or a size (`media.download`) | Im, Ly, Pi, Ph, Nc | File URL from `fs-files`; allowed by share permission | proposed |
| Rotate and crop non-destructively (`media.edit`) | Im, Ph, Li, Ly, Pi, Co, Nc | Exif `Orientation`; crop instructions: ⚠️ no XMP crop term evidenced → gap | proposed |
| Delete media; trash with a deadline (`media.delete`, `media.restore`) | Im (trash), Ph (archive), Pi (batch delete); *arch.* | AS2 `Delete` + tombstone; file removal in `fs-files` is a separate, explicit step | proposed |
| Detect duplicates (`media.duplicates`) | Im, Ph, Li, Da | exact: `checksum` `sha256:…`; perceptual hash (pHash): gap | proposed |
| Show media on a map; group by place (`place.list`, `place.assign`) | Im, Li, Ph, Nc (Maps app) | GeoJSON, AS2 `Place`, IPTC "Location Created/Shown"; map tiles: PMTiles ([geodata](../../../data/geodata/standards.md)); self-hosted tiles only | proposed |
| Mark sensitive media, fields or people (`sensitive.mark`) | *arch.* ADR 0029 | `dpv:SpecialCategoryPersonalData` (DPV 2.3); never auto-linked, encrypted by default | proposed |
| Sync across devices, work offline (`sync`) | *arch.* (ADR 0019, 0024) | `fs-store` + `fs-hub` object sync; encrypted at rest | proposed |

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Recognise and name faces, merge clusters — **local only**, off by default, sensitive (`person.detect`, `person.name`, `person.merge`) | Im, Ph, Li, Da, Nc (optional app) | no standard for face regions in our files ⚠️ (XMP/IPTC region terms not evidenced) → gap; marked per ADR 0029 | proposed |
| Link a recognised person to a contact only after explicit approval (`person.link`) | *arch.* ADR 0020/0029 | live reference into contacts (JSContact); no automatic `owl:sameAs` | proposed |
| Label objects and scenes by ML — local only (`label.suggest`) | Im, Ph, Li, Da, Nc (optional app) | suggestions become `tag.add` after approval; Web Annotation `classifying` | proposed |
| Semantic search in natural language (`media.searchSemantic`) | Im, Li, Ph (similarity), Da | embedding vectors, local model; no standard: gap | proposed |
| Find similar images (`media.similar`) | Im, Ph, Da | embedding vectors: gap | proposed |
| OCR: find text in images (`media.ocr`) | Ph, Da | extracted text as a metadata field | proposed |
| Smart / saved-search album (`album.query`) | Ly, Ph (virtual), Li (auto albums) | stored query on an AS2 `Collection` ⚠️ gap | proposed |
| Group media into stacks (bracketing, panorama) (`stack.create`) | Im | AS2 `Collection` of kind stack: gap | proposed |
| Mark favourites (`media.favourite`) | Im, Ph, Co | own keyword; Web Annotation `bookmarking` | proposed |
| Archive / hide media from the timeline (`media.archive`) | Im, Ph | visibility flag on the metadata object | proposed |
| Set status: published, pending, private; visibility per group (`media.visibility`) | Pi, Co | gap | proposed |
| Comment on media (`comment.add`) | Co, Pi | AS2 `Note` with `inReplyTo`; Web Annotation `commenting`; moderation: AS2 `Flag` | proposed |
| Rate media (`rating.set`) | Co, Pi | gap (no rating standard in our files) | proposed |
| Edit metadata in series: rename, move, label (`media.batch`) | Da, Pi, Ly, Im | same capabilities applied to a selection | proposed |
| Write metadata back as XMP sidecar (`metadata.export`) | Ph (sidecars), Im (XMP) | XMP sidecar, Exif↔XMP mapping | proposed |
| Reverse-geocode GPS to a place name — only via a self-hosted service (`place.resolve`) | Im | ⚠️ no geocoding service/standard evidenced → gap | proposed |
| Auto-albums by event (`album.suggest`) | Li | clustering by date and place: gap | proposed |
| Stories, calendar view (`media.story`) | Ph, Im | view parameters; stories: gap | proposed |
| Apply a watermark at delivery (`media.watermark`) | Co, Pi, Ph (Plus) | derived rendition; original unchanged | proposed |
| Transcode videos to common codecs (`video.transcode`) | Im | derived rendition in `fs-files` | proposed |
| Set an album cover and sort order (`album.sort`) | Ly | view parameters of `album.list` | proposed |
| Strip location from a shared copy (`share.create` option) | — (our idea, no frontend) | removes IPTC/Exif GPS in the shared rendition | proposed |
| Embed a shared album in other pages (iframe) | Da | frontend path on `share.create` | proposed |

## Not planned (deliberately)

| Feature | Seen in | Why not |
|---------|---------|---------|
| Raw storage management: quotas, buckets, folder mounts, S3 setup | Ly (quotas), Im, Ph, Da (S3) | bytes belong to `fs-files`; the gallery only references them |
| Sending images or face data to cloud ML services | — | data must not leave the device; ML is local and optional (ADR 0029) |
| Automatic linking of people across programs | Im, Ph, Li | sensitive data is never linked automatically (ADR 0029) |
| Own login, OAuth/SSO, LDAP, 2FA, API keys | Im, Ph, Li, Ly, Pi, Da, Nc | platform identity, not the gallery |
| Own REST API and webhooks as the integration path | Im, Ph, Li, Ly, Pi, Da, Nc | integration is the capability contract and `fs-hub` events (ADR 0021) ⚠️ to verify |
| Plugin/hook interfaces inside the program | Co, Pi | extension via capabilities and frontends, not code hooks |
| Gallery themes, templates, CMS bridges, RSS, sitemap | Co, Pi | presentation is a frontend concern (ADR 0021, 0038) |
| Full image editor (layers, RAW development) | — (all frontends lack it) | out of scope; only non-destructive rotate/crop |
| Paid tiers that unlock features (e.g. Plus editions) | Ph | free forever (ADR 0016) |
| Copying the originals into the gallery | Co, Pi (import copies) | files stay in `fs-files`; the gallery references |

## Notes on the sources

- ⚠️ PhotoPrism: "Plus/CE" is used for two opposite statements (AI available, and reduced in
  the Community Edition); which functions need which edition is unclear.
- ⚠️ Nextcloud Photos: "no own image database" next to virtual albums and sharing — the album
  storage is unclear. Face/ML functions come from separate apps, not the base.
- ⚠️ Lychee and Damselfly: "React interface" looks doubtful; irrelevant for the functions.
- ⚠️ Damselfly: AI pipeline (pgvector, face clustering) not clearly described as local or remote.
