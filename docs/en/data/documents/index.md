# Documents

**Every text is a wiki entry** (ADR 0031): pages → books → libraries; one shared library used by all
programs (help, tool helpers, guides), shown where you are; own explanations beside the original,
which is muted, never deleted. Stored as original + AS2 envelope + activity log (ADR 0020, 0030).

## Standards in this domain (details: [standards.md](standards.md))

| Part | Content / standard | AS2 envelope |
|------|--------------------|--------------|
| text file (`.md`, `.js`, …) | original bytes; Markdown = CommonMark 0.31.2 / GFM, `text/markdown; variant=GFM` | `Document`, or `Article` with `source` for Markdown |
| block document | **own spec** "FS Block Document" (no open standard exists) | `Article` |
| page | — | `Article` (not `Page`: AS2 `Page` = a web page) |
| book, chapter | schema.org `Book`/`Chapter`, `hasPart`/`isPartOf` | `OrderedCollection` |
| library, shelf | schema.org `Collection` | `Collection` |
| own explanation, muting | W3C Web Annotation + 2 own motivations | `Note`/`Article` as annotation body |
| export | EPUB 3.3 (books), GFM (blocks) | — |

## Open points

- Own specs: block document format, the two annotation motivations, library profile, help keys
- Version history: activity log only, or gitoxide underneath (conversation pending)
- Collaborative editing (CRDT: Automerge vs. yrs) only if needed

## See also

- [ADR 0031](https://github.com/FreeSynergy/fs-documentation/blob/main/conventions/decisions/0031-texte-wiki-bibliothek.md)
- [Wiki frontends](../../programs/apps/wiki/frontends/index.md)
