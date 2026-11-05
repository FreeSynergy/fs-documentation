# Documents – standards

> Evidence: `temp/research/documents-standards.md` (2026-11-05). Policy: newest viable standard (ADR 0026).

## Envelope (ActivityStreams 2.0, ✅)

| Term | Definition (short) | Use |
|------|--------------------|-----|
| `Article` | "any kind of multi-paragraph written work" | page, block document |
| `Document` | a document of any kind | text file |
| `Page` | "a Web Page" | **not** used for wiki pages |
| `Collection` / `OrderedCollection` | unordered / ordered set of items | library, shelf / book, chapter |
| `attachment` | attached objects | screenshots, images |
| `content` + `mediaType`; ActivityPub `source` | rendered content; original source (e.g. Markdown) | original + rendered (ADR 0030) |
| FEP-b2b8 long-form text | draft, excludes book length | watch |
| FEP-bad1 object history | draft | close to our activity log |

## Text and blocks

| Standard | Evidence | Role |
|----------|----------|------|
| CommonMark 0.31.2 (2024-01-28), GFM 0.29-gfm | ✅ | Markdown dialect; Markdown itself is not standardised (RFC 7763/7764 Informational: media type `text/markdown; variant=…`) |
| Block document tree | ❌ **no open standard** (checked: ProseMirror, Portable Text, Editor.js, Lexical, BlockSuite, Notion, Block Protocol — all project/vendor formats) | **own spec** "FS Block Document": stable block IDs, typed blocks (each a data type with a representation, ADR 0023), lossless export to GFM; learn from Portable Text/ProseMirror (ideas, not code — ADR 0013) |

## Books and libraries

| Standard | Evidence | Role |
|----------|----------|------|
| schema.org `Book`, `Chapter`, `Collection`, `hasPart`/`isPartOf` (= Dublin Core) | ✅ | structure vocabulary |
| EPUB 3.3 (W3C Rec 2023-05-25); EPUB 3.4 CR (draft 2026-11-02) | ✅ | book export |
| Publication Manifest (W3C Rec 2020-11-10) | ✅ | manifest for exported books |
| DITA 1.3 (OASIS) | ✅ (2.0 status ⚠️) | reference for topic-based help; not adopted |
| contextual help IDs | ❌ no standard | own spec: help keys |

## Annotations — own explanation beside, original muted

| Standard | Evidence | Role |
|----------|----------|------|
| W3C Web Annotation Data Model / Vocabulary / Protocol (Rec 2017-02-23) | ✅ | anchor own explanations, comments, tags on text and screenshot regions (`TextQuoteSelector`, `TextPositionSelector`, `SvgSelector`, …) |
| 13 motivations (`assessing`, `bookmarking`, `classifying`, `commenting`, `describing`, `editing`, `highlighting`, `identifying`, `linking`, `moderating`, `questioning`, `replying`, `tagging`) | ✅ | `editing` only *requests* a change; **nothing means "mute the original"** |
| own motivations allowed via `skos:broader` | ✅ | `fs:supplementing` (broader `describing`) and `fs:superseding` (broader `editing`, client mutes the original) — vocabulary under `freesynergy.net` (ADR 0028) |
| EPUB Annotations 1.0 (W3C WD 2026-10-15) | ✅ | profile of Web Annotation for books — follow |

## Versioning and collaboration

| Item | Evidence | Note |
|------|----------|------|
| CRDT standard | ❌ none | Automerge (`automerge` 0.12, MIT) / `yrs` 0.28 (MIT) only if live co-editing is needed |
| gitoxide (`gix` 0.90, MIT OR Apache-2.0, pure Rust, 0.x) | ✅ | candidate for file history (conversation pending) |

## Gaps → own specification candidates

1. **FS Block Document** format (main gap)
2. motivations `fs:supplementing` / `fs:superseding` + how "muted" is displayed
3. library/shelf/book/chapter profile on AS2 collections
4. help keys (tool → library entry)
