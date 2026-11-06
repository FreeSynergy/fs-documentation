# Gallery — design

**Superseded in part (2026-11-06):** the gallery is no longer a program of its own. It is a workbench and frontend of [`fs-files`](../files/design.md). Albums, modes and metadata below move there; see the [overall plan](../roadmap.md).

**Status: proposal (2026-11-06).** Back to the [roadmap](../roadmap.md) · [requirements](requirements.md).

## Idea

The gallery owns the **view of photos and videos**, not their bytes. Bytes live in [`fs-files`](../files/design.md). The
gallery adds albums, timeline, places and people. A photo stays a normal file that other programs can use too.

## Data

| Piece | Standard | Notes |
|-------|----------|-------|
| Photo, video | AS2 `Image`, `Video`, referring to an `fs-files` object | |
| Embedded metadata | Exif 3.1, XMP, IPTC 2025.1 | Evidenced in [standards](../../../data/standards.md). Read only; originals stay untouched (ADR 0030) |
| Place | GeoJSON, AS2 `Place` | Shown through `fs-maps` |
| Album | AS2 `Collection` | |
| Edits | gap | Stored as instructions, not as a changed file |
| Faces | gap | Sensitive; see below |

## Derived data

Thumbnails and indexes can always be rebuilt, so they are kept apart from the data and are not synced by default.

## Faces and automatic tagging

Optional and **local only**: photos and face data never leave the device for analysis. Faces are biometric data and fall
under ADR 0029. This is off by default and explained before it is switched on.

## Patterns

| Pattern | Use |
|---------|-----|
| Repository | `MediaRepository`, `AlbumRepository` |
| Pipeline (template method) | Import: read metadata → thumbnails → index; each step can be repeated |
| Strategy | Thumbnail generation per format; optional tagging engine |
| Adapter | Metadata crates behind our own trait |
| Decorator | Thumbnail cache over the generator |

## Candidates

| Purpose | Crate (2026-11-06) |
|---------|--------------------|
| Decode and scale images | `image` 0.25 |
| Read metadata | `kamadak-exif` 0.6 or `nom-exif` 3.8 (also reads video metadata, to be checked) |
| Modern formats | `ravif` 0.13, `jxl-oxide` 0.12 |

Video posters need a decoder, which raises the same question as [streaming](../streaming/design.md#encoding).
For that reason, video posters are not in stage 1.

## Interface sketch

| Interface | Capabilities |
|-----------|--------------|
| `Gallery` (root) | `capabilities()`, hands out the others |
| `Library` | `media.import`, `media.list`, `media.search`, `media.delete` |
| `Albums` | `album.create`, `album.add`, `album.remove`, `album.nest` |
| `Metadata` | `metadata.read`, `metadata.edit` |
| `Timeline`, `Places` | Query by time and place |
| `subscribe` | Live changes |

The ids follow the [requirements](requirements.md).

## Components

Existing: `gallery`, `carousel`, `image`, `video`, `map-view`, `timeline`, `description-list`. New: workbench
`gallery-browser`, overlay `lightbox`. See [planned components](../../../components/planned.md).

## Stages

1. Import from `fs-files`, metadata, thumbnails, timeline, albums.
2. Workbench, lightbox, map view through `fs-maps`, first simple frontend.
3. Sharing, search, non-destructive edits.
4. Videos with posters, optional local face and object recognition.

## Open questions

1. **Automatic upload from the phone:** this appears in the requirements. Does it belong to the gallery or to `fs-files`?
   We propose `fs-files`, with the gallery as a view on the result.
2. **Writing metadata:** only to our objects, or also into the file? We propose our objects, with an optional export.
3. **Raw camera formats:** in scope? We propose later.
