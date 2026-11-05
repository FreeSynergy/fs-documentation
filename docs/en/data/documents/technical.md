# Documents – technical explanation

Decisions: ADR 0020/0030 (original + envelope + log), ADR 0023 (code and block editor), ADR 0031.

## Storage

| Object | Original | Envelope | Content |
|--------|----------|----------|---------|
| text file | bytes as written/imported | `Document` (`mediaType`), Markdown: `Article` + `source` | rendered HTML derived, never stored as truth |
| block document | — (born here) | `Article`, `mediaType` = FS Block Document | block tree JSON, stable block IDs |
| book / chapter | — | `OrderedCollection` + schema `Book`/`Chapter` | ordered item IRIs |
| library / shelf | — | `Collection` + schema `Collection` | item IRIs |
| own explanation | — | Web Annotation (`motivation` `fs:supplementing`/`fs:superseding`), body = `Note`/`Article`, `attachment` for screenshots | target = selector on the original |

- IDs UUIDv7 (ADR 0027); sensitive marking applies (ADR 0029).
- **Muting:** creating an `fs:superseding` annotation mutes the targeted original for that audience;
  `Undo`/`Delete` of the annotation brings it back. The original is never changed.

## Log mapping (AS2)

| Action | Activity |
|--------|----------|
| create page / book / library | `Create` |
| edit | `Update` (block-level diff in the payload) |
| add page to book, book to library | `Add` (target = collection) / `Remove` |
| own explanation, mute | `Create` on the annotation |
| unmute | `Undo` / `Delete` on the annotation |

## Help in every tool (ADR 0031)

- Each tool declares a **help key**; the library resolves it to an entry (own spec, gap 4).
- Opened in a window/workbench (code or block editor, read mode), not in the wiki app.

## Crates

| Need | Crate | Licence |
|------|-------|---------|
| Markdown parse/render | `markdown` (markdown-rs) 1.0 / `pulldown-cmark` 0.13 | MIT |
| syntax highlighting | `syntect` 5.3 with `fancy-regex` (pure Rust) | MIT |
| parsing for code editor | `tree-sitter` 0.27 | MIT, **C core** ⚠️ (100 % Rust rule, ADR 0015) |
| formatting | dprint (MIT), Biome (MIT OR Apache-2.0, crates.io outdated) | |
| book export | EPUB 3.3 writer — crate to choose | |
| history | `gix` 0.90 (candidate) | MIT OR Apache-2.0 |

`comrak` is BSD-2-Clause — permissive, but outside our licence rule; not used.
