# Documents

**Every text is a wiki entry** (ADR 0031). Technically there are four building blocks (ADR 0034) —
whether something is a book, a web page, bookkeeping or a log does not matter; EPUB, Markdown and
HTML are **export formats only**. Stored as original + AS2 envelope + activity log (ADR 0020, 0030).

| Building block | What | AS2 envelope |
|----------------|------|--------------|
| **passage** | extractable, named part (like a block); reusable elsewhere | named mark (ADR 0033) / block type |
| **page** | one document | `Article` (not `Page`: AS2 `Page` = a web page) |
| **collection** | group of pages/collections, may reference each other (graph), lockable | `Collection` / `OrderedCollection` |
| **shelf** | independent instance (own store, own rights) | instance boundary (ADR 0019/0028) |

**Marking** (ADR 0033): one mechanism for all data — a point inserts (variable, mail merge), a range
names/replaces (own explanation instead of the muted original, reusable passage). Based on W3C Web
Annotation.

Details: [standards.md](standards.md) · [technical.md](technical.md) · [examples.md](examples.md)

## Open points

- Own specs: block document format (neutral name, to be submitted to IETF/W3C), marking vocabulary,
  collection profile, help keys
- Version history: activity log only, or gitoxide underneath (conversation pending)
- Parser/highlighter for the code editor: pure Rust, fitting Blinc (research running)
- Goal: our own documentation runs in our wiki instead of mkdocs (ADR 0031)
