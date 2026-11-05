# fs-wiki — ideas from existing wikis, rich-text layer, Markdown extensions

Researched: 2026-11-05 · by: Claude subagent

Context: every text is a wiki entry; building blocks passage → page → collection → shelf (ADR 0034);
one marking mechanism (point = insert/variable, range = name/replace) (ADR 0033); two editing modes
(code/text = Markdown, must be complete; block mode = Notion-like); first features: templates,
links that survive moves, Markdown; wiki replaces mkdocs for our own docs; rich text = plain text +
separate span/mark layer. Nothing is copied (ADR 0013) — only ideas and functions are collected.

Legend: ✅ = verified at the URL during this research · ⚠️ = from secondary sources / prior knowledge,
URL given but the specific claim was not re-checked (re-verify before relying on it).

Versions/licences: GitHub API + raw LICENSE files + crates.io API, 2026-11-05. The GitHub API rate
limit (60/h unauthenticated) ran out mid-research; the remaining licences were read from the raw
LICENSE files.

---

## Part 1 — Products: notable functions

### Overview: licence and latest version

| Product | Licence | Latest version (date) | Source |
|---|---|---|---|
| Outline | BSL 1.1 (source-available, not OSI) | v1.12.0 (2026-10-23) | ✅ https://github.com/outline/outline/blob/main/LICENSE |
| BookStack | MIT | v26.09.2 (2026-10-20) | ✅ https://github.com/BookStackApp/BookStack |
| Docmost | AGPL-3.0 (+ separate enterprise edition) | v0.97.0 (2026-10-25) | ✅ https://github.com/docmost/docmost |
| Wiki.js | AGPL-3.0 | 3.1.0 (2026-11-05) | ✅ https://github.com/requarks/wiki/releases |
| DokuWiki | GPL-2.0 | release-2026-07-14c (2026-09-02) | ✅ https://github.com/dokuwiki/dokuwiki |
| XWiki | LGPL-2.1 | xwiki-platform 18.4.8 (2026-11-03) | ✅ https://github.com/xwiki/xwiki-platform |
| MediaWiki | GPL-2.0-or-later | not checked (rate limit), see https://www.mediawiki.org/wiki/Release_notes | ✅ licence: https://github.com/wikimedia/mediawiki/blob/master/COPYING |
| Obsidian | proprietary (free; Markdown files stay open) | not checked | ⚠️ https://obsidian.md/changelog |
| Logseq | AGPL-3.0 | 2.0.2 (2026-10-07) | ✅ https://github.com/logseq/logseq |
| AFFiNE | MIT, except `packages/backend` and `packages/common/native`, which use the AFFiNE EE licence | v0.27.4 (2026-08-18) | ✅ https://github.com/toeverything/AFFiNE/blob/canary/LICENSE |
| Anytype | Any Source Available License 1.0 (not OSI) | anytype-ts v0.57.7 (2026-11-03) | ✅ https://github.com/anyproto/anytype-ts/blob/main/LICENSE.md |
| SiYuan | AGPL-3.0 | v3.8.9 (2026-10-29) | ✅ https://github.com/siyuan-note/siyuan |
| TiddlyWiki | BSD-3-Clause | v5.4.1 (2026-07-10) | ✅ https://github.com/TiddlyWiki/TiddlyWiki5/blob/master/license |
| Notion | proprietary SaaS | n/a | — |
| Confluence | proprietary (Cloud / Data Center) | n/a | — |
| Tango (tango.ai, formerly tango.us) | proprietary SaaS + browser extension | n/a | ✅ https://www.tango.ai/ |
| Trilium (TriliumNext) | AGPL-3.0 | v0.106.1 (2026-10-23) | ✅ https://github.com/TriliumNext/Trilium |
| Dendron | Apache-2.0, **maintenance only, active development has stopped** | — (last push 2025-11) | ✅ https://github.com/dendronhq/dendron |
| Foam | MIT | vscode@0.47.1 (2026-11-04) | ✅ https://github.com/foambubble/foam |
| HedgeDoc | AGPL-3.0 | 1.12.0 (2026-08-21); 2.x in development | ✅ https://github.com/hedgedoc/hedgedoc |

### Outline
- **Templates with placeholders and preset variables** (`{datetime}`, `{author}`, …) that are filled in when a document is created. Templates can live in a collection or apply to the whole workspace. ✅ (search snippet) https://docs.getoutline.com/s/guide/doc/templates-GP6DXgRtxl
- **ID-based document URLs** (`/doc/<slug>-<urlId>`): the slug is cosmetic and the short ID resolves the document, so links survive renames and moves. ⚠️ (visible in the URL above)
- **Backlinks** panel ("Referenced by") on each document. ⚠️ https://docs.getoutline.com/s/guide
- **Import/export**: Markdown, HTML, JSON; whole-workspace import from Notion and Confluence. ⚠️ https://docs.getoutline.com/s/guide
- **Collections** with per-collection permissions; documents nested inside them. ⚠️
- Editor is ProseMirror-based ("rich-markdown-editor"), with Markdown shortcuts while typing. ⚠️

### BookStack (the hierarchy closest to ours: Shelf → Book → Chapter → Page)
- **Include tags `{{@page_id}}` and `{{@page_id#block_id}}`**: transclude a page or a single block by numeric ID. Permissions are enforced on includes, nesting is capped at 3 levels, included content is not indexed in the host page, and selecting text shows a popup that yields the include tag. ✅ https://www.bookstackapp.com/docs/user/reusing-page-content/
- **Block IDs as HTML ids `bkmrk-…`**, generated per block; they are the target of includes and deep links. ✅ (same URL)
- **Page templates**: any page can be marked as a template, and a book or chapter can set a *default template* for new pages. ⚠️ https://www.bookstackapp.com/docs/user/page-templates/
- **Page permalinks** by ID (`/link/<id>`), which do not depend on slugs. ⚠️ https://www.bookstackapp.com/docs/user/page-permalinks/
- **Revisions** with diff and restore; **entity-level permissions** that are inherited down Shelf → Book → Chapter → Page and can be overridden. ⚠️ https://www.bookstackapp.com/docs/user/roles-and-permissions/
- **Two editors**, WYSIWYG and Markdown, chosen per page. Content is stored as HTML, with the Markdown kept alongside. ⚠️ https://www.bookstackapp.com/docs/user/markdown-editor/

### Docmost
- **Synced blocks**: the same content reused across pages and kept in sync. ✅ https://docmost.com/docs/
- **Bases** (table and kanban database views with properties, filters and formulas) inside the wiki. ✅
- **Page history** with restore; space- and workspace-level permissions plus groups. ✅
- Built-in **Draw.io, Excalidraw and Mermaid** diagrams; KaTeX math; callouts and toggle blocks. ✅
- **Import/export** of pages; Confluence/Notion import is advertised. ✅ (Confluence importer partly in the EE ⚠️)

### Wiki.js
- **Multilingual namespacing**: one page path exists in several languages (`/en/foo`, `/de/foo`), and users switch language on the same page. ✅ https://docs.requarks.io/locales
- **Page history**: view, compare and restore revisions. **Page operations**: move, duplicate, delete. ✅ https://docs.js.wiki/
- **Storage modules**, e.g. a two-way Git sync of all pages as Markdown files. ⚠️ https://docs.requarks.io/storage/git
- 3.1.0 added an **importer from HedgeDoc**. ✅ https://github.com/requarks/wiki/releases
- Pages are path-addressed, so a move changes the path (no automatic rewrite of incoming links in 2.x). ⚠️

### DokuWiki (plain-text files, no database)
- **Namespace templates** `_template.txt` / `__template.txt`, with substitution variables `@ID@ @NS@ @CURNS@ @PAGE@ @FILE@ @USER@ @NAME@ @MAIL@ @DATE@`, …. ✅ (variable list read from `inc/common.php` in https://github.com/dokuwiki/dokuwiki) · doc ⚠️ https://www.dokuwiki.org/namespace_templates
- **Page locking**: an edit lock with timeout prevents two people editing the same page at once. ⚠️ https://www.dokuwiki.org/locking
- **Move plugin**: renames or moves pages and namespaces and **rewrites all links to them** (and relative links inside them). ⚠️ https://www.dokuwiki.org/plugin:move
- **ACL** per namespace or page, inherited down the tree. ⚠️ https://www.dokuwiki.org/acl
- Old revisions + diff view (side-by-side and inline). ⚠️

### XWiki
- **Rename/move with backlink update**: the rename dialog can update all pages that link to the renamed page and leave a redirect behind. ⚠️ https://www.xwiki.org/xwiki/bin/view/Documentation/UserGuide/Features/PageEditing/
- **Templates via Template Providers**, restricted to spaces, so "create page here" offers only matching templates. ⚠️ https://extensions.xwiki.org/xwiki/bin/view/Extension/Administration%20Application#HTemplates
- **Structured data (App Within Minutes)**: classes, objects and sheets turn a page into a typed record. ⚠️
- **Translations per page** (one document, several language versions). ⚠️
- Confluence migrator (import Confluence XML spaces, including macros). ⚠️ https://extensions.xwiki.org/xwiki/bin/view/Extension/Confluence%20Migrator%20Application%20Pro/

### MediaWiki
- **Templates with parameters** `{{Name|arg1|key=value}}` → `{{{1}}}` / `{{{key|default}}}`, plus **transclusion of any page**, `<noinclude>/<includeonly>/<onlyinclude>`, and **substitution** `{{subst:…}}`, which inlines the template once instead of linking it. ⚠️ https://www.mediawiki.org/wiki/Help:Templates
- **Move leaves a redirect** (optionally moves the talk page and subpages). Incoming links keep working through the redirect, and "double redirects" are reported for cleanup. ⚠️ https://www.mediawiki.org/wiki/Help:Moving_a_page
- **Special:WhatLinksHere** (backlinks, including transclusions and redirects). ⚠️
- Full history with diff between any two revisions; edit conflicts are detected on save. ⚠️
- Page protection levels (semi/full). Categories via `[[Category:X]]` in the text. ⚠️

### Obsidian (Markdown files in a folder = "vault")
- **Automatic link rewrite on rename/move**: "Automatically update internal links" (setting; prompting instead is possible). ✅ https://help.obsidian.md/links (source: https://github.com/obsidianmd/obsidian-help)
- **Block references**: append `^block-id` to a paragraph or list item and link to it with `[[Note#^block-id]]`. **Heading links** `[[Note#Heading#Sub]]`; vault-wide heading search `[[## term]]`. ✅
- **Embeds/transclusion** `![[Note]]`, `![[Note#Heading]]`, `![[Note#^id]]`. ✅ https://help.obsidian.md/obsidian-flavored-markdown
- **Callouts** `> [!type]± Title`: foldable with `+`/`-`, nestable, custom types via CSS. ✅ https://help.obsidian.md/callouts
- **Templates core plugin**: a template folder with variables `{{title}}`, `{{date:FORMAT}}`, `{{time}}`; template **properties are merged** into the note's YAML front matter. ✅ https://help.obsidian.md/plugins/templates
- **Properties** = typed YAML front matter (text, list, number, checkbox, date, tags). A property name has one type vault-wide. ✅ https://help.obsidian.md/properties

### Logseq
- **Block references** `((uuid))`: typing `((` searches blocks, and each block shows a reference counter. ✅ https://github.com/logseq/docs/blob/master/pages/Block%20Reference.md
- In file-based graphs the referenced block gets an **`id:: <uuid>` property line** in the Markdown file. ⚠️ https://docs.logseq.com/
- **Block embeds** `{{embed ((uuid))}}` and page embeds `{{embed [[page]]}}`. ⚠️
- **Templates**: a block with `template:: name`, inserted via `/template`. ⚠️
- **Queries** (simple and Datalog) embedded in pages. The new 2.x "DB version" moves from Markdown files to a database. ⚠️

### AFFiNE
- **BlockSuite** editor: every block is a Yjs-backed CRDT node, with the same doc viewable as a page or as an "edgeless" whiteboard. ⚠️ https://github.com/toeverything/blocksuite
- **Linked docs and synced/embedded docs** (an embed shows the live doc inline). ⚠️ https://docs.affine.pro/
- Markdown and Notion import, Markdown/HTML/PDF export. ⚠️

### Anytype
- **Object types + relations**: every page is an object with a type, and a type has **default templates**. ⚠️ https://doc.anytype.io/anytype-docs/basics/object-types/templates
- Local-first, E2E-encrypted sync (any-sync), and **backlinks/graph**. ⚠️ https://doc.anytype.io/
- Import from Notion and Markdown. ⚠️

### SiYuan
- **Every block has a stable ID** (timestamp + random, e.g. `20210808180117-czj9bvb`). Documents are stored as `.sy` JSON trees, and the Markdown form uses kramdown IAL `{: id="…"}`. ⚠️ https://github.com/siyuan-note/siyuan
- **Block-level reference** `((id "anchor text"))` and two-way links (backlinks + unlinked mentions). ✅ README https://github.com/siyuan-note/siyuan
- **Embed blocks driven by SQL queries** over the block table (`{{SELECT * FROM blocks WHERE …}}`). ✅ ("SQL query embed" in README)
- Templates with Go-template syntax and `.action{}` variables. ⚠️
- "Standard Markdown with assets" export. ✅

### TiddlyWiki
- **The tiddler as the atomic unit** (close to our "passage"): small named units combined by transclusion. ✅ https://tiddlywiki.com/static/Transclusion.html
- **Transclusion** `{{Title}}`, field transclusion `{{Title!!field}}`, **transclusion with a template** `{{Title||Template}}`. ✅ (same, sub-pages)
- **Procedures/macros with parameters** and **filters** (a query language over tiddlers, e.g. `[tag[Docs]sort[title]]`). ⚠️ https://tiddlywiki.com/static/Filters.html
- **Rename with relink — only partly**: the core only offers to update the `tags` and `list` fields of other tiddlers, not links in body text (the third-party "Relink" plugin does the body). ✅ (core string `Title/Relink/Prompt` in `core/language/en-GB/EditTemplate.multids`)
- Lesson for us: link rewriting must be done fully by the core.

### Notion
- **Synced blocks**: the same block lives on several pages, and an edit anywhere updates everywhere. ✅ https://www.notion.com/help/synced-blocks · design notes ✅ https://www.notion.com/blog/designing-synced-blocks
- Block-based data model: every block has a UUID, so moving pages never breaks `@`-mentions/links. ⚠️ (same blog)
- **Database templates** (per-database page templates, including recurring ones). ⚠️ https://www.notion.com/help/database-templates
- **Page history** and per-page sharing/permissions. **Markdown & CSV export** (ZIP, IDs appended to file names). ⚠️ https://www.notion.com/help/export-your-content
- Markdown shortcuts while typing in block mode. ⚠️

### Confluence
- **Templates with variables**: a variable becomes a form that is filled in when the page is created, plus **placeholder (instructional) text** that disappears on typing, plus labels. ✅ https://support.atlassian.com/confluence-cloud/docs/create-a-template/ · ✅ https://confluence.atlassian.com/docm/latest/create-a-template-966052016.html
- **Blueprints** (templates with a wizard and an index page). ⚠️
- **Include Page** and **Excerpt / Excerpt Include** macros (transclusion of a named section). ⚠️ https://confluence.atlassian.com/doc/excerpt-include-macro-148067.html
- Page IDs: links keep working after rename/move. **Page history with compare**; page restrictions (view/edit) inherited down the page tree. ⚠️
- Markdown shortcuts. Live docs and real-time co-editing. ✅ (navigation of the doc above)

### Tango (in-context help)
- **Capture**: a browser extension records clicks while you work and turns them into a **step-by-step guide with annotated screenshots** automatically. ✅ https://microsoftedge.microsoft.com/addons/detail/ifigbhjamijkipoeckabmilnagjcfhec
- **Guide Me**: turns a recorded workflow into a **live in-browser walkthrough** that highlights where to click in the real app. ✅ https://help.tango.ai/en/collections/4046693-guide-me
- **Pins / in-app support**: guidance attached to specific pages or elements of the target app. ✅ https://www.tango.ai/
- Automatic blurring of sensitive data in screenshots. ⚠️ https://www.tango.ai/features
- Idea for us: wiki passages bound to an app's route/element ID, shown as contextual help inside FreeSynergy apps. Guides are just pages with "step" passages.

### Trilium / TriliumNext
- **Note cloning**: one note appears in several places in the tree (multiple parents). This is not a copy. ⚠️ https://docs.triliumnotes.org/
- **Templates as relations** (`~template=…`): the instance inherits all template attributes, and the template's content and child structure are used for new notes. ✅ https://docs.triliumnotes.org/user-guide/advanced-usage/template
- **Inheritable attributes** (`#isInheritable`) flow down the tree. ✅ https://docs.triliumnotes.org/user-guide/advanced-usage/attributes/attribute-inheritance
- **Note revisions** (snapshots at intervals), protected (encrypted) notes, scripting. ⚠️

### Dendron / Foam (Markdown in VS Code)
- Dendron: **dot-hierarchy file names** (`a.b.c.md`), **schemas** that validate and suggest hierarchy and template, and **refactor hierarchy** that renames many notes and updates links. Note refs `![[note#heading]]`. ⚠️ https://wiki.dendron.so/ · project status ✅ maintenance only.
- Foam: **wikilinks + generated Markdown "link reference definitions"** at the end of a file, so `[[x]]` also resolves in plain CommonMark renderers. ⚠️ https://foamnotes.com/
- Foam: **note templates** with variables (`FOAM_TITLE`, `FOAM_DATE_*`, …), default and daily-note templates, and **JavaScript templates** (a template as a function). ✅ https://github.com/foambubble/foam/blob/main/docs/user/features/templates.md
- Foam: graph view and backlinks panel; rename updates links (VS Code rename provider). ⚠️

### HedgeDoc
- **Real-time collaborative Markdown** (CodeMirror + OT) with split view. ⚠️ https://docs.hedgedoc.org/
- **Per-note permissions** (freely / editable / limited / locked / protected / private). ⚠️ https://docs.hedgedoc.org/references/permissions/
- **Revisions** with diff; slide mode (reveal.js); YAML metadata (title, tags, lang…). ⚠️
- Rich Markdown extension set: `:::info` containers, mermaid, math, footnotes, TOC `[TOC]`. ⚠️ https://hedgedoc.org/features/

### Cross-cutting conclusions (Part 1)
1. **Links target IDs, not paths** (Outline, Notion, Confluence, BookStack permalinks). Path-based systems need either a rewrite pass (Obsidian, DokuWiki Move, XWiki, Dendron) or redirects (MediaWiki). Best of both: store links by ID, *render/export* them as paths, rewrite the Markdown text on move, and keep redirects for external URLs.
2. **Block-level identity** is needed for block refs and transclusion (Obsidian `^id`, Logseq `id::`, SiYuan IAL, BookStack `bkmrk-`). IDs should be stable, short, and only written into Markdown when referenced (Obsidian style), so the files stay clean.
3. **Templates** fall into three families: (a) text substitution of variables at creation time (DokuWiki, Obsidian, Foam, Outline), (b) form-driven variables (Confluence), (c) live inheritance (Trilium templates, Anytype types). Our ADR 0033 "point = variable" matches (a)/(b). A "template link" à la Trilium is optional.
4. **Transclusion must respect permissions** and cap nesting (BookStack). Searching transcluded content is a decision (BookStack: not indexed in the host).
5. Without a core-level rename/relink, links decay (TiddlyWiki).

---

## Part 2 — Rich text as "plain text + formatting layer"

### How existing systems store formatting

| System | Model | Where marks live | Boundary rule | Source |
|---|---|---|---|---|
| **Peritext** (Ink & Switch, 2021/22) | CRDT: plain-text sequence + separate list of *mark operations* anchored to character IDs (`before`/`after` an op id) | separate op log; computed per character | per mark type: bold/italic **grow** at end; link/comment **do not grow**. Conflicting values (colour) → LWW; same-type multi-instance marks (comments) may overlap | ✅ https://www.inkandswitch.com/peritext/ · repo MIT, prototype (last push 2022) ✅ https://github.com/inkandswitch/peritext |
| **Automerge** (≥2.1) | text object + **marks** (name + primitive value + range) + **block markers** inline in the text | marks separate, can overlap; blocks are inline marker objects | `expand: "before" \| "after" \| "both" \| "none"` chosen per mark | ✅ https://automerge.org/docs/reference/documents/rich-text/ · Rust crate `automerge` 0.12.0, MIT ✅ |
| **Yjs / yrs** | `Y.Text` items; formatting = `ContentFormat` items (start/end format markers) in the **same** item list as the text | inline markers ("attributes" in the Delta view) | inherits attributes of the preceding position. Deltas via `insert(pos, text, attrs)` / `format(pos, len, attrs)` | ⚠️ https://docs.yjs.dev/api/shared-types/y.text · yrs 0.28.1 MIT ✅ |
| **Loro** | `LoroText` (B-tree), Peritext-style rich text, **per-format expand config** `after`(default)/`before`/`none`/`both` | separate style anchors | configured per mark key | ✅ https://loro.dev/docs/tutorial/text · crate `loro` 1.17.1 MIT, pure Rust ✅ |
| **ProseMirror** | tree of block nodes; inline content is a *flat* run of text nodes, each with a **mark set** (not nested elements) | on text nodes | `MarkSpec.inclusive` (default true; links usually false); `excludes` decides which marks can coexist | ⚠️ https://prosemirror.net/docs/guide/#doc · https://prosemirror.net/docs/ref/#model.MarkSpec |
| **Quill Delta** | list of `{insert, attributes}` ops (flat runs); block formats as attributes on the `\n` | on runs | editor-side | ⚠️ https://quilljs.com/docs/delta · Quill 2.0.3 BSD-3 ✅ |
| **NSAttributedString / AttributedString** (Apple) | string + **attribute runs**, queried with `attributes(at:effectiveRange:)` | runs | typing attributes from the preceding character | ⚠️ https://developer.apple.com/documentation/foundation/nsattributedstring |
| **xi-rope** | rope + `Spans<T>`: "spans (in an interval tree), useful for rich text annotations", generic over T; edits transform spans through deltas | separate interval tree | caller | ✅ module doc in https://github.com/xi-editor/xi-editor/blob/master/rust/rope/src/spans.rs · crate 0.3.0 (2019, unmaintained) Apache-2.0 |
| **Zed** | `rope` crate on its **SumTree** (B+-tree with summaries); syntax highlights, diagnostics and inlays are separate layers with *anchors* (`Anchor` = insertion id + offset + bias) that survive edits | separate layers | `Bias::Left/Right` on each anchor | ⚠️ https://zed.dev/blog/zed-decoded-rope-sumtree (Zed: GPL-3/AGPL/Apache mix, check per crate) |
| **Lapce** | fork of xi-rope (`lapce-xi-rope`) + floem editor; styles as spans | separate | caller | ⚠️ https://github.com/lapce/lapce (Apache-2.0 ✅) |
| **Stand-off annotation** (TEI stand-off, W3C Web Annotation) | text untouched; annotations point into it via selectors: `TextPositionSelector` (start/end) **plus** `TextQuoteSelector` (exact + prefix/suffix) for robust re-anchoring | fully external | n/a (re-anchor on change) | ⚠️ https://www.w3.org/TR/annotation-model/#text-quote-selector |

Trend: formatting is a set of **ranges anchored to stable positions** over a plain sequence, not a
tree of formatted nodes. Block structure is either inline markers (Automerge, Quill `\n`) or a
separate block list (ProseMirror, Notion). This matches our "passage" being the block: each passage =
`text` + `marks` (+ block type/attrs).

### Rust crates

| Crate | What | Licence | Version (date) | Pure Rust | Rich-text marks? |
|---|---|---|---|---|---|
| `ropey` | UTF-8 rope (B-tree), char/line indexing | MIT OR Apache-2.0 | 1.6.1 (2025-08) | yes | no, add your own layer |
| `crop` | B-tree rope, cheap `clone` (Arc nodes) → good for snapshots/undo, byte- and line-based | MIT | 0.4.3 (2025-04) | yes | no |
| `xi-rope` | rope + `Spans<T>` interval tree + delta/transform | Apache-2.0 | 0.3.0 (2019, stale) | yes | **yes (Spans)**, but unmaintained; good to study the idea |
| `jumprope` | skip-list rope (very fast inserts) | ISC OR Apache-2.0 | 1.1.2 (2023) | yes | no |
| `cola` | op-based plain-text CRDT that sits *next to* your own buffer (you keep the `String`/rope; cola transforms offsets) | MIT | 0.5.1 | yes | no; marks would need own anchors via cola's `Anchor` ⚠️ |
| `diamond-types` | Eg-walker plain-text CRDT, very fast | ISC | 1.0.0 on crates.io (2022); repo at 2.0.0 unreleased | yes | no |
| `loro` | full CRDT suite (text, list, map, tree, movable list), **rich text with expand config**, undo manager, time travel, shallow snapshots | MIT | 1.17.1 (2026-10-22) | yes | **yes** |
| `yrs` | Rust port of Yjs; `TextRef` with formatting attributes, `OffsetKind` (bytes/UTF-16) | MIT | 0.28.1 (2026-11-04) | yes | yes (Yjs model) |
| `automerge` | Automerge core in Rust: marks + block markers | MIT | 0.12.0 (2026-09-16) | yes | yes |

All checked via crates.io API ✅ (https://crates.io/crates/<name>). The `cola` description was checked
✅ https://docs.rs/cola/latest/cola/.

### Pitfalls (with mitigations)
1. **Expansion at boundaries.** Typing at the end of bold should be bold; at the end of a link or comment it should *not* extend. At the start of a paragraph, inherit from the following character. ✅ Peritext examples 8–9. → A per-mark-type `expand` policy (`before/after/both/none`), as in Automerge ✅ and Loro ✅.
2. **Coinciding ends of different marks** (bold and link both end on the same character): Word gives "bold, not link", Docs/Pages give "neither". ✅ Peritext. → Decide by policy and document it.
3. **Overlap semantics differ by mark type.**
   - Boolean marks merge (bold ∪ bold).
   - Value marks conflict (red vs blue → deterministic LWW per character).
   - Multi-instance marks coexist (two comments, two of our ADR 0033 "names"), so they need an identity (mark id), not just a name.
   ✅ Peritext ex. 4–7.
4. **Markdown cannot express everything.** Partly overlapping bold/italic must be split into properly nested runs when serialising. Underline, colour and "name" ranges need an escape hatch (attribute syntax `[text]{.u #name}` or inline HTML). Zero-width points need a marker syntax. → The serialiser normalises; the parser must give the same mark set back (round-trip tests).
5. **Markdown in a plain-text CRDT** (storing `**` in the text) breaks on concurrent edits (half-deleted delimiters). ✅ Peritext section "Markdown in a plain text CRDT". → Keep Markdown as *a view*, not the storage, if collaboration is planned.
6. **Index units.** Byte vs char vs UTF-16 offsets (Yjs JS = UTF-16; yrs has `OffsetKind` ⚠️; ropey = chars; crop = bytes). Marks must snap to grapheme boundaries. → Fix one unit (UTF-8 byte offsets on char boundaries) in the API.
7. **Anchoring through edits.** Offsets shift on every insert/delete. Solutions: transform offsets on each edit (xi `Spans`), sticky anchors with bias (Zed), CRDT IDs (Peritext/Loro). Deleting all text of a range leaves an empty mark → policy: drop it, or keep it as a point (relevant for ADR 0033 "name" ranges).
8. **Undo.** Undoing "format" must restore the *previous* marks per run, not just remove the new mark. Undoing a delete must restore marks of the deleted text. In collaborative mode undo is *selective* (only my ops). Loro ships an `UndoManager` ✅ (loro.dev docs list "Undo/Redo"). → Store the inverse as an exact before-snapshot of the affected mark slice (cheap with Arc/B-tree, e.g. crop-style structural sharing).
9. **Links as values.** Merging concurrent edits *inside* a URL string can produce invalid URLs. Loro recommends LWW for URLs. ✅ loro.dev/docs/tutorial/text → URLs and link targets (page IDs) as atomic mark values.

### Recommended design for fs-wiki
- **Passage = { id, kind (paragraph/heading/list-item/code/callout/…), attrs, text: Rope, marks: MarkSet }.** Page = ordered tree of passages. This removes most of the block-marker complexity.
- **MarkSet** = sorted interval structure (B-tree/sum-tree of runs or interval tree) of `Mark { id, kind, value, range: start..end, expand }`. `start == end` means a **point** (ADR 0033 insert/variable) and `start < end` a **range** (ADR 0033 name/replace). Formatting (bold, link, code, …) is just more mark kinds, so there is one mechanism.
- **Mark-kind registry** with `expand` (before/after/both/none), `overlap` (merge | lww | multi), and `markdown` (how to serialise, fallback to attribute syntax).
- **Positions** go through an `Anchor { offset, bias }` API. Internally they are plain byte offsets now, and can be swapped for CRDT ids later without changing callers.
- **Crate choice:**
  - **Now (single writer, server-authoritative):** `crop` (MIT, pure Rust, cheap clones for history/undo) or `ropey` (MIT/Apache) for text, plus our *own* small MarkSet (study xi-rope `Spans` and Peritext rules, write it ourselves per ADR 0013).
  - **If real-time collaboration becomes a requirement:** **`loro`** (MIT, pure Rust, Peritext-style marks with expand config, undo manager, version DAG). Keep our MarkSet semantics aligned to Loro's expand vocabulary so a later switch is cheap. `yrs` is the alternative, but it puts formatting inline as markers.

---

## Part 3 — Markdown extensions for a wiki

| Extension | Common syntax | Specified? | Spec / reference |
|---|---|---|---|
| Base | CommonMark | **yes**, formal spec 0.31.2 | ⚠️ https://spec.commonmark.org/0.31.2/ |
| Tables, task lists, strikethrough, extended autolinks, disallowed raw HTML | GFM | **yes**, formal (GFM spec, CommonMark superset) | ⚠️ https://github.github.com/gfm/ |
| Footnotes `[^1]` | PHP Markdown Extra / GitHub / Pandoc / Obsidian ✅ | **no formal spec**. Described by PHP Markdown Extra and Pandoc; GitHub supports it, but it is not in the GFM spec text | ⚠️ https://michelf.ca/projects/php-markdown/extra/#footnotes · https://pandoc.org/MANUAL.html#footnotes |
| Callouts/admonitions | (a) GitHub alerts / Obsidian callouts `> [!NOTE]` (Obsidian: any type, `+/-` fold, custom title ✅); (b) Python-Markdown/mkdocs-material `!!! note "Title"` (**our current mkdocs docs**); (c) generic directive `:::note` (HedgeDoc, Docusaurus, remark-directive) | (a) documented by GitHub, (b) documented by Python-Markdown, (c) **CommonMark "generic directives" proposal only** | ⚠️ https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts · ⚠️ https://python-markdown.github.io/extensions/admonition/ · ⚠️ https://talk.commonmark.org/t/generic-directives-plugins-syntax/444 |
| Wiki links `[[Page]]`, `[[Page\|alias]]`, `[[Page#Heading]]`, `[[Page#^block]]`, embed `![[…]]` | Obsidian ✅, Foam, Dendron, Logseq | **no spec**. De facto Obsidian; comrak and pulldown-cmark have opt-in wikilink parsing ⚠️ | ✅ https://help.obsidian.md/links · ✅ https://help.obsidian.md/obsidian-flavored-markdown |
| Front matter | YAML `---` (Jekyll, Obsidian properties ✅), TOML `+++` (Hugo, Zola) | **no formal spec** (convention); Pandoc documents `yaml_metadata_block` | ⚠️ https://gohugo.io/content-management/front-matter/ · ⚠️ https://pandoc.org/MANUAL.html#extension-yaml_metadata_block |
| Math | `$…$`, `$$…$$`, GitHub also `` $`…`$ `` and ```` ```math ```` | **no CommonMark spec**. GitHub and Pandoc (`tex_math_dollars`) document it | ⚠️ https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions |
| Mermaid | ```` ```mermaid ```` fenced code (info string) | Uses the standard fenced code info string; the rendering is a GitHub/Docmost/HedgeDoc convention | ⚠️ https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams · ✅ Docmost has Mermaid |
| Highlights `==x==`, comments `%%x%%` | Obsidian ✅ | no spec | ✅ https://help.obsidian.md/obsidian-flavored-markdown |
| Heading IDs / attributes `{#id .class key=val}` | Pandoc `header_attributes`/`attributes`, kramdown IAL `{: #id}`, markdown-it-attrs, Djot | Pandoc manual; kramdown syntax doc; **Djot has a formal attribute syntax** | ⚠️ https://pandoc.org/MANUAL.html#extension-attributes · ⚠️ https://kramdown.gettalong.org/syntax.html#inline-attribute-lists · ⚠️ https://djot.net/ |
| Definition lists, sub/superscript | Pandoc, PHP Markdown Extra, comrak options | described, not standardised | ⚠️ |

### How tools store block IDs in Markdown
- **Obsidian:** `^block-id` appended at the end of the block (paragraph/list item; on its own line after tables and quotes). It is written only when a reference is created. ✅ https://help.obsidian.md/obsidian-flavored-markdown (the help files themselves contain e.g. `… knowledge. ^b15695`)
- **Logseq (file graphs):** child property line `id:: 6501c…-uuid` under the block; refs `((uuid))`. ✅ refs / ⚠️ `id::` https://github.com/logseq/docs/blob/master/pages/Block%20Reference.md
- **SiYuan:** canonical storage is `.sy` JSON with an ID per node. The Markdown/kramdown form uses IAL `{: id="20210808180117-czj9bvb" …}` after blocks, and refs `((id "text"))`. ⚠️ https://github.com/siyuan-note/siyuan
- **Outline:** ProseMirror JSON in Postgres; Markdown is an import/export view. Anchors come from headings, with no persistent block IDs in the Markdown. ⚠️
- **BookStack:** HTML element ids `bkmrk-<slug>`, inside stored HTML, not Markdown syntax. ✅ https://www.bookstackapp.com/docs/user/reusing-page-content/
- **Dendron:** same `^anchor` convention as Obsidian; **Notion export:** IDs only in file names (`Title 1a2b…md`). ⚠️

### Rust Markdown parsers (for our code/text mode)
- `comrak` 0.59.0 (2026-10-26), BSD-2-Clause, CommonMark + GFM, AST with source positions, plus many opt-in extensions (front matter, footnotes, alerts, math, wikilinks, description lists …) ✅ crates.io / ⚠️ extension list https://docs.rs/comrak
- `pulldown-cmark` 0.13.6 (2026-10-30), MIT, streaming pull parser with offsets; options for tables, footnotes, tasklists, strikethrough, heading attributes, metadata blocks, math, GFM alerts, wikilinks (recent) ✅ crates.io / ⚠️ options https://docs.rs/pulldown-cmark
- `markdown` (markdown-rs, wooorm) 1.0.0 (2025-04), MIT, 100 % CommonMark with mdast + MDX/GFM/math/frontmatter constructs ✅ crates.io

### Recommended Markdown extension set for fs-wiki
CommonMark 0.31 + GFM (tables, task lists, strikethrough, autolinks), footnotes, YAML front matter
(TOML accepted on import), wiki links `[[target|label]]` / `[[target#heading]]` / `[[target#^block]]`
plus embed `![[…]]`, block IDs as trailing `^id` (only when referenced), callouts `> [!type]± Title`
(GitHub/Obsidian-compatible; importer converts mkdocs `!!! type`), math `$…$`/`$$…$$`, mermaid
fenced blocks, heading/inline attributes `{#id .class}` as the escape hatch for marks Markdown lacks
(underline, colour, ADR 0033 names/variables). Links are stored as page IDs and serialised as
`[[path]]`/relative paths on export.
