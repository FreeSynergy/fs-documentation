# Whiteboard — Requirements

What `FreeSynergy.Whiteboard` (repo `fs-whiteboard`) must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.
One program covers free-form boards: sketches, diagrams, sticky notes and workshops.

Status: `implemented` · `planned` · `proposed`

**Seen in** — analysed frontends: [Dr](frontends/drawio/index.md) draw.io ·
[Ex](frontends/excalidraw/index.md) Excalidraw · [Mi](frontends/miro/index.md) Miro ·
[Mu](frontends/mural/index.md) Mural · [Op](frontends/openboard/index.md) OpenBoard ·
[Td](frontends/tldraw/index.md) tldraw.
*arch.* = required by our architecture or principles, not by counting.
⚠️ = not (or not clearly) in our frontend files; known from the products, to be verified there first.
The Mi, Mu and Op feature files are short (a few lines each): a missing entry there is weak evidence of absence.

**Rule:** a capability is *Required* when at least three of the six frontends show it, or when
our architecture needs it. The capability id in backticks (`<object>.<action>`) is a proposal
for the capability list — a capability is an action on the object, never a menu item or a gesture
(ADR 0037: gestures, shortcuts and tool keys belong to the frontend).

**Board model:** `data/standards.md` records that **no standard exists** for whiteboard shapes,
layers and z-order; InkML is only an old W3C contribution with no successor (weak evidence).
So the board model is a **gap → own spec candidate**. Proven building blocks: W3C Web Annotation
(`SvgSelector`) for comments anchored on a region; `mimeType` values in [models](../../../data/models.md).

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Create, open, rename and delete a board (`board.create`, `board.open`, `board.delete`) | Dr, Ex, Mi, Mu, Op, Td | board model: gap → own spec; the board is a resource with a stable id | proposed |
| Hold several pages or frames in one board (`page.add`, `page.remove`, `frame.add`) | Dr, Op, Td (pages); Dr, Ex, Mi, Mu, Td (frames) | gap → own spec (page = ordered child of board; frame = bounded area) | proposed |
| Add basic shapes — rectangle, ellipse, diamond, line (`shape.add`) | Dr, Ex, Mi, Mu, Op, Td | gap → own spec; geometry as `x`, `y`, `width`, `height`, `angle` | proposed |
| Add and edit text, free or bound to a shape as a label (`text.add`, `text.edit`) | Dr, Ex, Mu, Op, Td; Mi ⚠️ | gap → own spec; plain text, no markup assumed | proposed |
| Draw freehand strokes and erase them (`stroke.draw`, `stroke.erase`) | Ex, Op, Td (draw, erase); Mu (freehand) | stroke = point list; pressure/tilt: see Optional; InkML only weak evidence → gap | proposed |
| Connect shapes with lines or arrows that follow when a shape moves (`connector.add`, `connector.edit`) | Dr, Ex, Mu, Td; Mi (diagram sets) | gap → own spec; `source`/`target` references to element ids | proposed |
| Add sticky notes (`note.add`) | Mi, Mu, Td | gap → own spec; note = text shape with colour | proposed |
| Insert images (`image.add`) | Dr, Ex, Mi, Mu, Op, Td | AS2 `Image` / `mediaType` (`image/png`, `image/svg+xml` ⚠️ not evidenced in `data/`) | proposed |
| Select, move, resize, rotate, copy and delete elements (`element.select`, `element.move`, `element.delete`) | Dr, Ex, Td; Mi, Mu, Op ⚠️ (implied, not stated) | gap → own spec | proposed |
| Style an element: colour, fill, line width and style, opacity, font (`element.style`) | Dr, Ex, Td; Mi, Op (colours) | gap → own spec; style as typed properties, not a free string ⚠️ (Dr uses a style string) | proposed |
| Group elements and nest them in containers (`element.group`, `element.ungroup`) | Dr, Ex, Td; Mi (grouping), Op (stacks) | gap → own spec; `parent` reference as in Dr (`parent`), Ex (`groupIds`), Td (`parentId`) | proposed |
| Order elements front to back; lock an element (`element.reorder`, `element.lock`) | Td (layers, locking); Ex (ordered array); *arch.* (stable z-order in the model) | gap → own spec (z-order must be queryable, see standards.md) | proposed |
| Move around a large canvas — pan and zoom (`canvas.navigate`) | Ex, Td; Mi, Mu (infinite canvas); Dr | view state per user, not part of the board content ⚠️ | proposed |
| Align, distribute and snap to a grid or guides (`element.align`) | Dr, Td; Ex (grid) | gap → own spec | proposed |
| Reuse shape collections — libraries of shapes (`library.load`, `library.add`) | Dr, Ex, Op, Td (SDK); Mi (diagram sets) | library = board fragment; gap → own spec; shared via Git repositories (ADR 0036 ⚠️ check scope) | proposed |
| Export a board or a selection as an image (`board.export` to PNG, SVG) | Dr, Ex, Td, Mu (PNG); Mi ⚠️ | PNG ⚠️ and SVG ⚠️ — no entry in `data/`, to be evidenced; SVG preferred because it stays vector | proposed |
| Export as PDF, one page per page/frame (`board.export` to PDF) | Dr, Mu, Op; Mi (PDF) | PDF ⚠️ — only `application/pdf` as `mimeType` in `data/models.md` | proposed |
| Save and load the board in an own open file format; keep the original on import (`board.save`, `board.import`) | Dr, Ex, Td, Op (.obz); *arch.* (open data, ADR 0014) | own spec (JSON) ⚠️; foreign formats (`.drawio`, `.excalidraw`, `.tldraw`) are imports | proposed |
| Save automatically and work offline, sync later (`sync`) | Td (IndexedDB), Ex (localStorage), Op (offline-first), Dr (auto-save); *arch.* | `fs-store` + `fs-hub`, object-level sync (ADR 0019); encrypted at rest (ADR 0024) | proposed |
| Edit together in real time (`board.sync`) | Dr, Ex, Mi, Td; Mu ⚠️ | element/record-level deltas; CRDT or versioned store ⚠️ not decided; conflict rule needed; transport via `fs-hub` (ADR 0019) | proposed |
| Show who is present: cursor, name, selection (`presence.show`) | Ex, Mi, Td; Mu ⚠️ | ephemeral, never stored in the board; no standard checked | proposed |
| Follow another participant's view (`presence.follow`) | Ex, Mi (presenter/follow), Td | view state of the followed actor; ephemeral | proposed |
| Share a board by link with view or edit role (`board.share`) | Ex (view/edit link), Mu (guest links, roles), Td, Mi; Dr (rights from storage) | roles via platform identity and permissions, not own login; AS2 `Invite`/`Join` ⚠️ | proposed |
| Show a board read-only, also embedded in other programs (`board.view`, `board.embed`) | Ex (view mode), Td (readonly), Dr (embed), Mi ⚠️ | read-only view of the same model; embed via program contract (ADR 0017) | proposed |
| Undo and redo (`history.undo`, `history.redo`) | Ex (session undo); Dr, Mi, Mu, Op, Td ⚠️ (implied) | session-local operation log | proposed |

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Stylus input with pressure and tilt (`stroke.draw` with pressure) | Ex (tablet, touch pen), Td (pressure look), Op (pen, multitouch) | upstream contribution, entered in `todo/upstream.md`; InkML weak evidence → gap; gestures stay in the frontend (ADR 0037) | proposed |
| Pointer that leaves no marks (`presence.point`) | Ex, Td (laser) | ephemeral presence event | proposed |
| Comment on a place in the board (`comment.add`) | Mi (comment mode); Dr, Ex, Td: explicitly none | W3C Web Annotation with `SvgSelector` / region target (`data/documents/standards.md`) | proposed |
| Version history: list, compare, restore (`board.history`, `board.restore`) | Dr (versions from storage) | object history in `fs-store` ⚠️ | proposed |
| Templates and own start boards (`template.apply`, `template.save`) | Mi, Mu (thousands); Td (own start snapshots) | template = board without data; sharing via Git repositories (ADR 0036 ⚠️) | proposed |
| Facilitation: timer, voting, sections, step-by-step sequences (`session.timer`, `vote.cast`, `sequence.run`) | Mi, Mu; Op (timer, alarm); Td (community overlays) | gap → own spec; vote = one `Like`-style activity per actor ⚠️ | proposed |
| Present a board full screen or step through frames (`board.present`) | Op (full screen), Mi (presenter mode), Mu (sequences) | order of frames in the board model | proposed |
| Tables as a board element (`table.add`) | Mi, Mu | gap → own spec | proposed |
| Auto-layout for mind maps and organisation charts (`board.layout`) | Mi | gap | proposed |
| Convert text into diagram elements: Mermaid, CSV/XML tables (`board.import`) | Ex (Mermaid), Dr (CSV/XML) | Mermaid text ⚠️ not evidenced in `data/` | proposed |
| Import PDFs as frames / view PDFs on a page (`document.embed`) | Mi (PDF to frames), Op (PDF viewer) | `application/pdf`; link to the documents program (ADR 0020) | proposed |
| Attach own data fields to an element for evaluation (`element.annotate`) | Dr (Edit Data) | key/value on element; fits the `data/fields.md` idea ⚠️ | proposed |
| Search shapes in libraries and elements on the board (`library.search`, `element.search`) | Dr (shape search) | full text over labels | proposed |
| Recognise and complete rough shapes (`shape.recognise`) | Op (auto-completion) | local algorithm; no standard | proposed |
| Embed web pages, live content and other programs' objects in a board (`embed.add`) | Ex (`embeddable`), Td (`embed`, bookmark), Op (browser tool) | live reference into the other program (ADR 0020); remote content off by default ⚠️ | proposed |
| Classroom aids: ruler, protractor/geometry square, screen recording (`tool.measure`, `capture.record`) | Op | frontend/plug-in; no standard | proposed |
| Hand-drawn look as a render style (`element.style` roughness) | Ex | render property only; stored as number | proposed |
| Integrity of the sync log and who changed what (`board.audit`) | Mu (activity log, Enterprise) | log mapping as in messages technical.md ⚠️ | proposed |
| Extend the program: custom shapes, tools, bindings (`plugin.install`) | Dr (JS plugins, `.shape`), Td (SDK), Ex (libraries only), Mi (App Kit) | extension model of the platform (not decided) | proposed |
| API and webhooks on board changes (`board.subscribe`) | Mi (REST, webhooks); Dr, Ex, Mu, Op, Td: none | AS2 activities on the board resource ⚠️ | proposed |
| End-to-end encrypted rooms (`board.encrypt`) | Ex (key in URL fragment); Dr, Td: none | key handling via platform; encryption at rest ADR 0024; scheme not decided | proposed |
| Reuse images and objects from a media library, collections (`library.media`) | Op (library, stacks) | link to the media/file programs ⚠️ | proposed |

## Not planned (deliberately)

| Feature | Seen in | Why not |
|---------|---------|---------|
| Plan-limited boards, guest limits, paid tiers | Mi, Mu (free: 3 boards) | free forever, no poverty discrimination (ADR 0016) |
| Cloud-only operation, no self-hosting, no offline | Mi, Mu | local-first, self-hosted, offline (ADR 0019) |
| AI image cut-out and other plan-gated AI tools | Mi | not a core function; no tracking third-party calls |
| Vendor-locked integrations (Atlassian, Teams, Slack, Zapier apps) | Dr, Mi, Mu | other FreeSynergy programs share standard data instead (ADR 0017) |
| Own login, SSO/SCIM administration | Mu, Mi | platform identity (Kanidm), not the whiteboard |
| Permissions only via the storage provider; plaintext on a provider cloud | Dr | roles come from platform identity; content encrypted at rest (ADR 0024) |
| Task/kanban boards and project planning inside the board | Mi (apps) | separate program (projects), borrowed by live reference (ADR 0017, 0020) |
