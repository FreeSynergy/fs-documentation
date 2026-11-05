# Documents – technical explanation

Decisions: ADR 0020/0030 (original + envelope + log), ADR 0023 (code and block editor), ADR 0031.

## Storage (ADR 0034)

| Building block | Original | Envelope | Content |
|----------------|----------|----------|---------|
| text file | bytes as written/imported | `Document` (`mediaType`); Markdown: `Article` + `source` | rendered HTML derived, never stored as truth |
| page (block document) | — (born here) | `Article`, `mediaType` = block format | block tree JSON, stable block IDs |
| passage | — | named mark (ADR 0033) on a range, or a block with a name | referenced wherever it is reused |
| collection | — | `Collection` / `OrderedCollection` | item IRIs, references to other collections, `locked` state |
| shelf | — | instance boundary | own `fs-store`, own rights |
| mark (explanation, variable, …) | — | Web Annotation, one `freesynergy.net` motivation | anchor (point/range/image region) + name + type + value |

- IDs UUIDv7 (ADR 0027); sensitive marking applies (ADR 0029).
- **Muting:** a range mark with a replacement value mutes the original for its audience;
  `Undo`/`Delete` of the mark brings it back. The original is never changed.

## Log mapping (AS2)

| Action | Activity |
|--------|----------|
| create page / collection | `Create` |
| edit | `Update` (block-level diff in the payload) |
| add page/collection to a collection | `Add` (target = collection) / `Remove` |
| lock / unlock a collection | `Update` (state) |
| mark (insert, name, replace) | `Create` on the mark |
| remove mark / unmute | `Undo` / `Delete` on the mark |

## Help in every tool (ADR 0031)

- Each tool declares a **help key**; the library resolves it to an entry (own spec, gap 4).
- Opened in a window/workbench (code or block editor, read mode), not in the wiki app.

## Crates

| Need | Crate | Licence |
|------|-------|---------|
| Markdown parse/render | `markdown` (markdown-rs) 1.0 / `pulldown-cmark` 0.13 | MIT |
| syntax highlighting | `syntect` 5.3 with `fancy-regex` (pure Rust) | MIT |
| parsing for code editor | `tree-sitter` 0.27 — **excluded**: C core, does not fit Blinc / 100 % Rust (user 2026-11-05); pure-Rust option being researched | MIT |
| formatting | dprint (MIT), Biome (MIT OR Apache-2.0, crates.io outdated) | |
| export | EPUB 3.3 / GFM writers — crates to choose | |
| history | `gix` 0.90 (candidate) | MIT OR Apache-2.0 |

`comrak` is BSD-2-Clause — permissive, but outside our licence rule; not used.
