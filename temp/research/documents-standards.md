# Documents (Wiki) – Standards and Crates

Researched: 2026-11-05 · by: Claude subagent

Context: ADR 0031 says every text is a wiki entry. The structure is pages → books (shelves / books / chapters / pages) → libraries. One shared library holds help texts, tool helpers and guides. Users can write their own explanation or add a screenshot next to an existing text; the original is then "muted", never deleted. There are two editors: a code editor for text files and a block editor. Storage = original + AS2 envelope + content standard + append-only activity log. Rust only. Licence MIT OR Apache-2.0.

Legend: ✅ checked on a primary source · ⚠️ inferred, from memory, or not final

---

## 1. ActivityStreams 2.0 / ActivityPub

AS2 Vocabulary is a W3C Recommendation from 23 May 2017. https://www.w3.org/TR/activitystreams-vocabulary/ ✅
The W3C **Social Web WG** has been re-chartered to maintain AS2 and ActivityPub ("Chartered until 31 January 2028"). https://www.w3.org/groups/wg/social/ ✅ Any AS2 revision is maintenance work; no new document types are expected (⚠️).

| Term | Definition (quote) | Use for | |
|---|---|---|---|
| `Article` | "Represents any kind of multi-paragraph written work." | wiki page (main type) | ✅ |
| `Document` | "Represents a document of any kind." | file-backed text (.md, .js), PDF | ✅ |
| `Page` | "Represents a Web Page." (Extends: Document) | not for wiki pages; this means an HTML web page | ✅ |
| `Note` | "a short written work typically less than a single paragraph" | short help snippets, tooltips | ✅ |
| `Collection` | "represents ordered or unordered sets of Object or Link instances" | library, shelf | ✅ |
| `OrderedCollection` | "members … are assumed to always be strictly ordered" | book, chapter (order matters) | ✅ |
| `attachment` | "Identifies a resource attached or related to an object that potentially requires special handling." | screenshots, images | ✅ |
| `content` | "By default, the value of content is HTML. The mediaType property can be used … to indicate a different content type." | rendered HTML | ✅ |
| `mediaType` | "When used on an Object, identifies the MIME media type of the value of the content property." | `text/markdown`, own block media type | ✅ |
| `context` | "a means of grouping objects and activities that share a common originating context" | "belongs to program X / tool Y" for in-context help | ✅ |

All URLs above: https://www.w3.org/TR/activitystreams-vocabulary/

**ActivityPub `source`** (§3.3):
> "The source property is intended to convey some sort of source from which the content markup was derived … In general, clients do the conversion from source to content"
The official example is `"source": {"content": "I *really* like strawberries!", "mediaType": "text/markdown"}`.
https://www.w3.org/TR/activitypub/#source-property ✅
→ This fits the "original + rendered" split exactly. `source` holds the original (Markdown or the block JSON). `content` holds the rendered HTML.

**FEPs** (index https://fep.swf.pub/, licence CC0):
- **FEP-b2b8 "Long-form Text"**, DRAFT, received 2024-11-07, by Evan Prodromou. It uses `Article`. > "This FEP does not provide guidance for book-length or longer text." https://codeberg.org/fediverse/fep/src/branch/main/fep/b2b8/fep-b2b8.md ✅
- **FEP-bad1 "Object history collection"**, DRAFT. It defines a property for an object's Create/Update/Delete history and maps to our activity log. ✅
- **FEP-1985** "Signaling how an OrderedCollection is ordered", DRAFT. Useful for chapter order. ✅
- **FEP-7888** "Demystifying the context property" and **FEP-2931** "Representing context with a Collection", both DRAFT. ✅
- **FEP-1311** "Media Attachments", DRAFT. **FEP-c118** "Content licensing support", DRAFT. **FEP-4f05** "Soft Deletion", DRAFT. ✅ (titles and status from the index)
- I found **no FEP for books, chapters or libraries**. ⚠️ (I searched the index; the mirror listing ends 2025-06, so a later FEP may exist.)

## 2. W3C Web Annotation

- Data Model, Vocabulary and Protocol are all **W3C Recommendations from 23 February 2017**. https://www.w3.org/TR/annotation-model/ ✅
- **Motivations**, the exact list of 13 values: `assessing`, `bookmarking`, `classifying`, `commenting`, `describing`, `editing`, `highlighting`, `identifying`, `linking`, `moderating`, `questioning`, `replying`, `tagging`. https://www.w3.org/TR/annotation-model/#motivation-and-purpose ✅
- `editing` > "The motivation for when the user intends to request a change or edit to the Target resource. For example an Annotation that requests a typo to be corrected." ✅
- `describing` > "…intends to describe the Target, as opposed to (for example) a comment about it." ✅
- **"Replace / mute the target and show my text instead"** cannot be expressed with the standard terms. `editing` only *requests* a change. Rendering behaviour is out of scope (⚠️ my interpretation). The spec does allow extensions:
  > "New Motivations MUST be instances of oa:Motivation … The skos:broader relationship SHOULD be asserted between the new Motivation and at least one existing Motivation"
  https://www.w3.org/TR/annotation-vocab/ (Appendix C) ✅
  → Define for example `fs:supplementing` (skos:broader `oa:describing`) and `fs:superseding` (skos:broader `oa:editing`). Under these, the client mutes the target and shows the body.
- **Selectors** (§4.2): Fragment, CSS, XPath, **TextQuoteSelector**, **TextPositionSelector**, DataPositionSelector, **SvgSelector** (use it for a region of a screenshot), **RangeSelector**, and refinement through `refinedBy`. States: TimeState and HttpRequestState. `styleClass` / CssStylesheet are available for "muted" styling hints. ✅
- **Body**: an external resource (IRI, e.g. our own Article or Image), or **TextualBody** > "A class assigned to the Body for embedding textual resources within the Annotation." It has `value`, `format`, `language` and `purpose`. Multiple bodies and Choice / Composite / List are possible. ✅
- **Newer W3C work**: **EPUB Annotations 1.0** is a W3C Working Draft of 15 October 2026 (FPWD was February 2026) from the Publishing Maintenance WG. > "defines a profile of the Web Annotation Data Model … by specifying a subset of the terms, and adding terms" https://www.w3.org/TR/epub-anno-10/ ✅ There is also an **EPUB Annotations Vocabulary 1.0** FPWD (Feb 2026). ✅ Apart from these, nothing new on the core Web Annotation specs (⚠️).

## 3. Block-structured rich text: is there an open standard?

**Result: there is no IETF / W3C / ISO / OASIS standard for a block document tree.** ⚠️ This is a negative finding; I found no candidate on any of those bodies. All existing formats are vendor or project formats:

| Format | Owner / governance | Licence | Status | |
|---|---|---|---|---|
| ProseMirror doc JSON | Marijn Haverbeke; repo moved to code.haverbeke.berlin | MIT | stable, but defined by the schema (no fixed node set) | ✅ licence, ⚠️ "no fixed set" |
| Portable Text | Sanity.io | MIT | spec "v0.0.1 – WORKING DRAFT"; "rich text as an array of blocks, themselves arrays of children spans" https://github.com/portabletext/portabletext | ✅ |
| Editor.js output | CodeX team | Apache-2.0 | `{time, blocks:[{id,type,data}], version}`; no formal spec | ✅ licence, ⚠️ shape |
| Lexical JSON | Meta (repo now `meta/lexical`) | MIT | serialized EditorState, implementation-defined | ✅ |
| BlockSuite (AFFiNE) | toeverything | **MPL-2.0** | Yjs-based, implementation-defined | ✅ |
| Notion block objects | Notion Inc. | proprietary API | not open | ⚠️ |
| Block Protocol | HASH | MIT / Apache-2.0 (WordPress plugin AGPL) | about embeddable block *components*, not a document format; activity is low | ✅ licence, ⚠️ activity |
| Peritext | Ink & Switch | MIT | research algorithm (2021/22); last push 2022 | ✅ |
| Automerge rich text | Automerge | MIT | marks plus block markers in a text CRDT (since 2.2) | ⚠️ |
| Yjs Y.XmlFragment / Y.Text | Kevin Jahns | MIT | CRDT types, no document schema | ✅ licence |

**Markdown family:**
- **CommonMark 0.31.2 (2024-01-28)** is the latest; spec licence CC BY-SA 4.0. https://spec.commonmark.org/ ✅ It is still 0.x, not 1.0.
- **GFM spec 0.29-gfm (2019-04-06)**. https://github.github.com/gfm/ ✅ (unchanged for years)
- **RFC 7763** registers `text/markdown`. It is Informational: > "This document is not an Internet Standards Track specification". **RFC 7764** (March 2016, Informational) covers Markdown variants and the `variant` parameter (e.g. `text/markdown; variant=CommonMark`). https://www.rfc-editor.org/rfc/rfc7763 ✅
- **Djot** (John MacFarlane, MIT) fixes CommonMark's parse complexity and adds attributes and generic containers. It has no version-1 spec. https://github.com/jgm/djot ✅
- → There is **no "standardised Markdown"**. The best standardised option is `text/markdown; variant=GFM` (or CommonMark) per RFC 7763/7764.

## 4. Books / libraries

- **EPUB 3.3**: W3C Recommendation, **25 May 2023** (republished 2024-10, 2025-01, 2025-03, 2026-01). https://www.w3.org/standards/history/epub-33/ ✅
- **EPUB 3.4**: Candidate Recommendation Snapshot 21 July 2026; latest CR Draft 2 November 2026. https://www.w3.org/standards/history/epub-34/ ✅ It is the newest, but not a REC yet.
- **Publication Manifest**: W3C Recommendation, 10 November 2020 (with Audiobooks). https://www.w3.org/TR/pub-manifest/ ✅ It is little used outside audiobooks (⚠️).
- **schema.org**:
  - `Book` ("A book.")
  - `Chapter` ("One of the sections into which a book is divided.")
  - `Collection` ("A collection of items, e.g. creative works or products.")
  - `CreativeWorkSeries` ("usually organized into some order")
  - `hasPart` / `isPartOf` (inverse)

  All ✅, https://schema.org/
- **Dublin Core** `dcterms:hasPart`: > "A related resource that is included either physically or logically in the described resource." Its inverse is `isPartOf`. https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ ✅
- **Best fit (opinion):** library and shelf → `schema:Collection` + AS2 `Collection`. Book → `schema:Book` + AS2 `OrderedCollection`. Chapter → `schema:Chapter` + `OrderedCollection`. Page → AS2 `Article`. Use `hasPart`/`isPartOf` (schema.org, which mirrors dcterms) for the links, and AS2 `partOf`/`orderedItems` for order. Use EPUB 3.3/3.4 as the **export** format for a book, not as the storage model.

## 5. Version history / collaboration

- **CRDTs**: there is no IETF/W3C standard. ⚠️ (Negative finding; the Automerge binary format is documented by the project only.)
- `automerge` 0.12.0 (2026-09-16), **MIT**. https://crates.io/crates/automerge ✅
- `yrs` (Rust port of Yjs) 0.28.1 (2026-11-04), **MIT**, still 0.x. https://crates.io/crates/yrs ✅
- Peritext: see §3 (research algorithm, MIT).
- **gitoxide** `gix` 0.90.0 (2026-10-22), **MIT OR Apache-2.0**, pure Rust and still 0.x. https://crates.io/crates/gix ✅ *Note only, to evaluate later.* Read, clone and fetch are mature, but write paths such as push and merge are still partial (⚠️).

## 6. In-context help standards

- **OASIS DITA**: DITA 1.3 is the current OASIS Standard. DITA 2.0 has a cover page at dita-lang.org that "replaces or supersedes … DITA Version 1.3", but its citation links still point to `wd01`, so its final status is **not confirmed**. https://dita-lang.org/2.0/dita/resources/oasis-cover ⚠️ DITA is topic-based XML with maps; its map/topic split is a good conceptual model, but the format is too heavy to adopt.
- I found **no standard for "contextual help IDs"** (DITA has `resourceid` for this; ⚠️ from memory). JSON Schema `title`/`description` covers per-field help only.
- → Use own stable help keys (e.g. `help:<program>/<tool>/<topic>`) and attach them through AS2 `context` or a `fs:helpFor` property.

## 7. Rust crates (crates.io API, 2026-11-05)

| Crate | Version | Licence | Note | |
|---|---|---|---|---|
| `comrak` | 0.59.0 | **BSD-2-Clause** | CommonMark + GFM, AST round-trip back to Markdown. Permissive, but not MIT/Apache | ✅ |
| `pulldown-cmark` | 0.13.6 | MIT | pull parser; CommonMark + GFM extensions; no AST | ✅ |
| `markdown` (markdown-rs) | 1.0.0 | MIT | CommonMark + GFM + MDX, mdast AST | ✅ |
| `jotdown` | 0.10.0 | MIT | Djot | ✅ |
| `tree-sitter` | 0.27.1 | MIT | **C core** compiled through cc. Grammar crates have their own (mostly MIT) licences | ✅ / ⚠️ grammars |
| `syntect` | 5.3.0 | MIT | Sublime grammars. Default regex engine is onig (**C**); the `fancy-regex` feature is pure Rust | ✅ / ⚠️ feature |
| `dprint-core` | 0.75.2 | MIT | formatter framework (plugins are Wasm) | ✅ |
| biome (repo) | — | MIT OR Apache-2.0 | JS/TS/JSON/CSS formatter. Its crates.io crates are stale (biome_formatter 0.5.7, 2024), so use it via git or the CLI | ✅ / ⚠️ |
| `automerge` / `yrs` / `gix` | see §5 | | | ✅ |

---

## Recommendation (opinion)

**(a) Text files (code editor):** store the original bytes unchanged. In the AS2 envelope use `Document` with `mediaType` = the real type (`text/markdown; variant=GFM`, `text/javascript` …). For Markdown wiki pages use `Article` with `source{content, mediaType:"text/markdown; variant=GFM"}` and a rendered `content` (HTML). Use the `markdown` (markdown-rs, MIT) parser for the Markdown AST, since it is 1.0 and has an mdast tree. Alternatively use `pulldown-cmark`. Avoid making `comrak` a core dependency because of BSD-2. Use tree-sitter for highlighting and structure, accepting the C core (note this in the ADR as an exception to "100 % Rust"). Djot is worth watching but is not the default.

**(b) Block documents:** **there is no standard → own spec candidate "FS Block Document" (JSON).** Model it on Portable Text and ProseMirror: a tree of blocks with stable `id`, `type`, `attrs` and `children`, plus inline spans with marks. Give it its own media type (e.g. `application/vnd.freesynergy.blocks+json`) and use it in `source.mediaType`. Define a lossless mapping to GFM for export. Block IDs make annotation targets stable (FragmentSelector `#block=<id>` + TextQuoteSelector).

**(c) Book / library structure:**
- Library and shelf: AS2 `Collection`.
- Book and chapter: AS2 `OrderedCollection` (order through `orderedItems`).
- Page: AS2 `Article`.
- Add `schema:Book` / `schema:Chapter` / `schema:Collection` as extra types in JSON-LD.
- Use `partOf` / `hasPart` for the links.
- Export to EPUB 3.3 (3.4 once it is a REC).

**(d) "Own explanation beside the original, original muted":** use a Web Annotation (`type: Annotation`). `target` = the page or block plus a selector; use SvgSelector for screenshot regions. `body` = the user's own `Article` / `Image` (by IRI), or a TextualBody. `motivation` = own extensions `fs:supplementing` (skos:broader oa:describing) or `fs:superseding` (skos:broader oa:editing); the latter tells the client to mute the target. The original stays untouched. Map to the log as follows:
- `Create{Annotation}` mutes the original.
- `Undo` or `Delete` of the annotation un-mutes it.
- Per-user choice can be `Ignore` or a preference.

Every change to pages and books goes into the append-only log as AS2 `Create` / `Update` / `Add` / `Remove` / `Move`, exposed like FEP-bad1. Follow EPUB Annotations 1.0 as a profile reference.

**Gaps → own spec candidates:**
1. Block document format and media type (main gap).
2. Motivation extensions `fs:supplementing` / `fs:superseding` and the "muted" rendering semantics.
3. Library / shelf / book / chapter profile on AS2 Collections (no FEP covers books).
4. Contextual help key scheme (`fs:helpFor`).
5. Later: version storage (gix vs. log-only) and, if collaborative editing is needed, a choice between Automerge (MIT) and yrs (MIT).
