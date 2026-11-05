# Blinc health check & pure-Rust parser/highlighter stack

Researched: 2026-11-05 · by: Claude subagent

Legend: ✅ = verified against a primary source (URL or local file named) · ⚠️ = secondary source, inference, or opinion.
Local research clone: `.research-blinc/` = shallow clone of `https://github.com/project-blinc/Blinc` at the 0.6.0 cut
(1 commit visible locally, `2026-11-03 darmie docs: cut the 0.6.0 changelog sections`). Metrics fetched on 2026-11-05
from the GitHub REST API (`api.github.com/repos/<repo>`, `/contributors`, `/releases`, `/commits?since=…`,
`/search/issues`) and the crates.io API (`crates.io/api/v1/crates/<name>`).

---

## Part A — Blinc health

### A.1 Facts

| Metric | Value | Source |
|---|---|---|
| Repo | `github.com/project-blinc/Blinc`, created 2022-04-10, last push 2026-11-04 | ✅ https://api.github.com/repos/project-blinc/Blinc |
| Licence | Apache-2.0 only (not dual MIT) | ✅ `.research-blinc/LICENSE`, `Cargo.toml` `[workspace.package] license` |
| Stars / forks / watchers | 561 / 16 / 12 | ✅ GitHub API (repo) |
| Total commits | 2 633 | ✅ GitHub API (`/commits` pagination, last page = 2633) |
| Contributors | 6 listed; **darmie (Damilare Akinlaja) = 2 610 of 2 633 commits (99.1 %)**, next: 14, 4, 3 | ✅ https://api.github.com/repos/project-blinc/Blinc/contributors |
| Last 100 commits (since 2026-05-05) | 100 % darmie | ✅ GitHub API `/commits?since=2026-05-05` |
| Commits per month (default branch) | May 660 · Jun 135 · Jul 226 · Aug 130 · **Sep 7** · Oct 296 | ✅ GitHub API `/commits?since&until` |
| Releases (GitHub) | v0.1.0 2025-12-20 · v0.1.1 2026-01-14 · v0.4.0 2026-04-05 · **v0.6.0 2026-11-04** | ✅ https://api.github.com/repos/project-blinc/Blinc/releases |
| Changelog versions (blinc_app) | 0.1.12 (2025-01-19) … 0.1.13–0.1.15 (Feb–Mar 2026), 0.4.0 (2026-04-05), 0.5.0 (2026-04-10), 0.6.0 (2026-11-03) | ✅ `.research-blinc/crates/blinc_app/CHANGELOG.md` |
| Cadence | irregular: 0.5 → 0.6 took ~7 months; minor versions carry breaking changes (0.5→0.6 migration guide exists) | ✅ CHANGELOG + `docs/book/src/migration/0.5-to-0.6.md` |
| Issues | 1 open / 24 closed | ✅ GitHub search API |
| PRs | 0 open / 32 closed, 24 merged (12 merged PRs by non-darmie authors) | ✅ GitHub search API |
| Maintainer response | Issues #28–#64 (May–Aug 2026) closed within 0–5 days (e.g. #28 "High CPU on Ubuntu": 48 comments, closed in 5 days). Only open issue #63 (WASM lazy loading, 2026-07-26) has 0 comments after ~100 days | ✅ https://api.github.com/repos/project-blinc/Blinc/issues?state=all |
| Funding | `.github/FUNDING.yml`: GitHub Sponsors `darmie`, Patreon `dami476` — individual donations only, no org/company backing found | ✅ local file; ⚠️ absence of other funding not provable |
| Roadmap | `Cargo.toml` refers to "ROADMAP §3" but **no ROADMAP file is in the repo**; README marks hot-reload `blinc dev` as "on the roadmap" | ✅ local clone (grep) |
| Docs | mdBook "Blinc Book" (getting started, mobile, web, core concepts, migration, 45+ gallery pages), docs.rs, `Skills.md` for AI agents, live WebGPU gallery | ✅ `docs/book/src/SUMMARY.md`, README |
| crates.io | first publish 2026-01-14; all-time downloads: blinc_core 3 275, blinc_layout 1 592, blinc_app 988, blinc_cn 347 (90-day: 1 128 / 492 / 314 / 77) | ✅ https://crates.io/api/v1/crates/blinc_core (etc.) |
| Dependants (crates.io) | only **one** non-Blinc crate (`kyu-visualizer`) | ✅ `/reverse_dependencies` for blinc_core, blinc_app, blinc_layout |
| Platforms | macOS/Windows/Linux/Android/iOS "Stable", Web (WASM/WebGPU) "Preview", HarmonyOS "in progress"; Fuchsia archived | ✅ README, `extensions/` |
| Accessibility | **No AccessKit dependency**; web a11y "Pending"; blinc_cn "screen reader support (planned)" | ✅ grep Cargo.toml; `docs/web.md:189`; `docs/book/src/cn/overview.md:119` |
| Pinned deps | `wgpu = "=26.0.1"`, `wgpu-hal = "=26.0.5"` (deliberate, documented driver regressions) | ✅ `Cargo.toml` |
| Author-owned git deps | `zyntax_embed` and `krio-*` via git rev from `github.com/darmie/*`, used only by the unpublished DSL crates (`blinc_dsl_core` has `publish = false`) | ✅ `crates/blinc_dsl_core/Cargo.toml`, `crates/blinc_cn_dsl/Cargo.toml` |
| Sibling crates in other repos | `blinc_canvas_kit`, `blinc_portal_ui`, `blinc_node_editor`, `blinc_game_kit` live in separate repos, pinned by git | ✅ README "Running the examples" |

### A.2 Text, editor and highlighting inside Blinc 0.6.0

| Item | Finding | Source |
|---|---|---|
| Text shaping | own `blinc_text`: `ttf-parser` + **`rustybuzz` 0.20** + `fontdb` + `swash` + `unicode-bidi`/`unicode-linebreak`. **Not** cosmic-text, **not** parley | ✅ `crates/blinc_text/Cargo.toml` |
| rustybuzz status | upstream README: "not developed further, unmaintained, and archived … switch to HarfRust" → Blinc must migrate to `harfrust` eventually | ✅ https://crates.io/api/v1/crates/rustybuzz/0.20.1/readme |
| Layout | Taffy 0.14 (flexbox) | ✅ `Cargo.toml` |
| `code(...)` / `code_editor(&state)` | Exists (`widgets/code/mod.rs`, 3 170 lines + search 446). Read-only and editable modes; undo/redo, auto-indent, word jumps, smart Home, clipboard, line numbers, folding (`detect_fold_regions`), search/replace, current-line highlight | ✅ `crates/blinc_layout/src/widgets/code/mod.rs` |
| Buffer model | `lines: Vec<String>` (no rope) | ✅ same file, `code_editor_state` |
| Highlighting | `syntax.rs`: trait `SyntaxHighlighter` with ordered regex `TokenRule`s (crate `regex`); built-ins `RustHighlighter`, `JsonHighlighter`, `LuaHighlighter`, `PlainHighlighter`; `TokenHit` callbacks for "intellisense" | ✅ `crates/blinc_layout/src/syntax.rs` |
| Highlighting limitation | the editable editor calls `highlighter.highlight(line)` **per line** and caches per line → no state across lines (block comments, multi-line strings, Markdown fences break). The `highlight()` default method can be overridden, but only with single-line input | ✅ `widgets/code/mod.rs` ~l. 1236–1250 |
| Rich text | `rich_text` element + `rich_text_editor` widget (≈7 000 lines: blocks, formatting, toolbar, Markdown import via **pulldown-cmark 0.10**) and a `markdown` widget | ✅ `widgets/rich_text_editor/markdown.rs`, `crates/blinc_layout/Cargo.toml` |
| Plain text | `text_input`, `text_area`, `input_otp`, `number_input`, `blinc_cn` textarea | ✅ `widgets/` |
| IME | desktop: `Ime::Commit` delivered as char events; **`Ime::Preedit` ignored** (`// TODO: render pre-edit text`); web: IME "out of scope" | ✅ `extensions/blinc_platform_desktop/src/event_loop.rs:552–580`; `docs/book/src/web/overview.md:5` |

### A.3 Comparison (same metrics, 2026-11-05)

| | Blinc | Dioxus + Blitz | Makepad | Xilem / Masonry |
|---|---|---|---|---|
| Licence | Apache-2.0 | MIT OR Apache-2.0 (crates) ✅ | MIT (repo), MIT OR Apache-2.0 (crates) ✅ | Apache-2.0 ✅ |
| Stars | 561 | dioxus 39 620 / blitz 4 346 ✅ | 7 239 ✅ | 5 593 ✅ |
| Top committer share (contributors page 1) | 99.1 % (1 person) | blitz: nicoburns 1 979 / 2 203 ≈ 90 %; dioxus: top-2 = 79 % of 6 823 ✅ | "Admin" 1 730 / 2 422 ≈ 71 %, +kevinaboos 263 ✅ | top 439 / 1 483 ≈ 30 %, 97 contributors ✅ |
| Commits/month May–Oct 2026 | 660/135/226/130/7/296 | blitz 84/47/144/144/101/178 ✅ | 39/50/183/295/147/70 ✅ | 27/1/6/10/1/8 ✅ (⚠️ activity may sit in other Linebender repos – parley 0.12 released 2026-10-09) |
| Latest release | 0.6.0, 2026-11-04 | dioxus 0.7.10 (stable) / 0.8.0-alpha.3 2026-10-16; blitz-dom 0.2.4 2026-10-16, blitz tag v0.3.0-beta.4 ✅ | makepad-widgets 1.0.0 (2025-05-13) on crates.io; git tag `release-2026-11-05` ✅ | xilem/masonry 0.4.0, 2025-10-29 ✅ |
| crates.io downloads | blinc_core 3 275 | dioxus 3.5 M, blitz-dom 319 k ✅ | makepad-widgets 20 k ✅ | masonry 24 k, xilem 12 k ✅ |
| Open issues (API count incl. PRs) | 1 | blitz 377, dioxus 898 ✅ | 44 ✅ | 157 ✅ |
| Funding / backing | individual sponsors/Patreon | Dioxus team joined **Cognition** on 2026-09-10; Cognition says it continues supporting Dioxus, Blitz, Taffy, Subsecond and "increasing investment in Dioxus-Native and Blitz" ✅ https://dioxuslabs.com/blog/joining-cognition/ , https://cognition.com/blog/welcoming-dioxus ; earlier $3.5 M VC (YC, Khosla) ⚠️ (beri.net secondary) | company-driven (Makepad), ⚠️ funding not verified | Linebender community, Google Fonts sponsoring text/rendering work ⚠️ |
| Accessibility | none | AccessKit (`blitz-shell` deps) ✅ | none found in `makepad-widgets` deps ✅ | AccessKit (`masonry` deps) ✅ |
| Text stack | own (rustybuzz) | parley ✅ | own | parley ✅ |
| Code editor | regex `code_editor` | none built-in ⚠️ | `makepad-code-editor` 1.0.0 crate ✅ | parley `PlainEditor` only ⚠️ |
| Mobile | Android/iOS "Stable" | Dioxus mobile (webview); Blitz native mobile ⚠️ | Android/iOS ✅ (README claims) ⚠️ | Android experimental ⚠️ |

### A.4 Risks (facts → consequence)

1. **Bus factor 1** (99 % single-author commits, all of the last 100). If darmie stops, there is no second maintainer with history. ✅ fact / ⚠️ consequence.
2. **Tiny adoption**: ~3 k downloads, one external dependant → nobody else would pick it up; bugs are found by us. ✅ / ⚠️
3. **Bursty cadence & breaking minors** (Sep 2026: 7 commits; 0.5→0.6 rewrote the builder API). ✅
4. **Ageing foundations**: `rustybuzz` archived; `wgpu` pinned at 26 while upstream moves on; pulldown-cmark 0.10 vs 0.13.6 current. Each is a migration someone must do. ✅
5. **Gaps relevant to us**: no accessibility (AccessKit), IME pre-edit not rendered (CJK input poor), code editor line-local highlighting and `Vec<String>` buffer. ✅
6. **Licence**: Apache-2.0 only — compatible with our MIT OR Apache-2.0 distribution (we can ship under Apache-2.0 terms); a fork would stay Apache-2.0. ✅ (licence text) / ⚠️ (legal reading)
7. **Positive facts**: very fast issue turnaround (days), extensive docs + migration guide, broad platform coverage incl. mobile and WebGPU, release 0.6.0 one day ago, active Discord, author open to extension requests (ADR 0009). ✅

### A.5 Mitigations (opinion ⚠️)

- **Our component layer is the abstraction**: Components (the 84) expose FreeSynergy types (props, events, signals) and never leak `blinc_*` types into program code. A port to Dioxus-Native/Blitz or Xilem then means re-implementing the component layer, not the programs.
- **Keep app logic, state, parsing, text buffer, highlighting outside Blinc** (pure crates: buffer = ropey/crop, highlighting = syntect, Markdown = pulldown-cmark). Blinc only paints styled spans. This is also what the code editor needs anyway (see Part B).
- **Pin + vendor**: pin Blinc by version, keep a fork ready (Apache-2.0 allows it); budget for occasional own patches (rustybuzz→harfrust, IME pre-edit, AccessKit).
- **Upstream contributions** (IME pre-edit, multi-line highlighter state, a11y) both fill our gaps and raise the bus factor; track whether PRs from non-darmie authors keep being merged (12 so far ✅).
- **Tripwires for re-evaluation**: no commit for 3 months; an issue of ours unanswered > 30 days; no AccessKit plan by our first public release; Blitz reaching a stable 0.3 with Cognition backing.

---

## Part B — pure-Rust parsing / highlighting / text stack (no C)

### B.1 Highlighters and parsers

| Option | What | Pure Rust? | Licence | Maintenance | Source |
|---|---|---|---|---|---|
| **syntect** 5.3.0 | Sublime/TextMate grammars, stateful line-by-line parser (`ParseState` carries across lines), themes | **Yes with `default-fancy` feature** (`regex-fancy` → fancy-regex); default feature `default-onig` uses Oniguruma (C) | MIT | 38 M dl, updated 2025-09, repo pushed 2026-10-31, 139 open issues | ✅ https://crates.io/api/v1/crates/syntect/5.3.0 (features map), GitHub API |
| fancy-regex 0.20.0 | backtracking regex (look-around, backrefs) over `regex-automata` | Yes | MIT | released 2026-10-24 | ✅ crates.io deps: bit-set, regex-automata, regex-syntax |
| **two-face** 0.5.2 | extra syntaxes/themes from `bat` for syntect | Yes (deps: syntect, serde) — use its fancy feature | MIT OR Apache-2.0 | 2026-08, 15 M dl; repo on Codeberg | ✅ crates.io |
| giallo 0.6.0 | VSCode/Shiki TextMate grammars (220+), VSCode-identical output | 0.6.0 depends on fancy-regex, no onig (README on GitHub still mentions an onig fork → stale) | **EUPL-1.2** (weak copyleft – conflicts with our MIT/Apache-only policy) | very active (Zola) | ✅ crates.io deps & licence; ⚠️ README/version mismatch |
| synoptic 2.2.9 | small regex highlighter for TUI editors | Yes (regex) | MIT | dormant since 2024-11, 36 ★ | ✅ crates.io, GitHub |
| inkjet 0.11.1 | highlighter bundle | **No** – tree-sitter + tree-sitter-highlight (C) | MIT OR Apache-2.0 | **repo archived** | ✅ crates.io deps, GitHub API `archived=true` |
| arborium 2.18.2 | 100+ tree-sitter grammars packaged | **No** – `arborium-tree-sitter` and every `arborium-<lang>` have `cc` build-dependency | MIT OR Apache-2.0 | active | ✅ crates.io dependency lists |
| tree-sitter 0.27.1 | incremental GLR parsing | **No** – `cc` build-dep (C runtime); grammars are generated `parser.c` | MIT | very active | ✅ crates.io deps |
| **tree-sitter-c2rust** 0.25.2 | fork with the *runtime* auto-translated to (unsafe, non-idiomatic) Rust, drop-in API | Runtime yes (no `cc` dep), **but every grammar is still C** `parser.c` compiled with `cc` → fails "no C code". Little-endian only. Last release 2025-02, 59 ★, 1 maintainer | MIT | ✅ https://github.com/shadaj/tree-sitter-c2rust README; crates.io deps |
| rust-sitter 0.4.5 / adze | define tree-sitter grammars in Rust macros | generator still emits tree-sitter C tables; depends on `tree-sitter`/`tree-sitter-c2rust` | MIT | ⚠️ no full C-freedom verified | ✅ crates.io deps |
| Zed / Helix / Lapce | editors | all use tree-sitter (C): Zed via `tree-sitter`, Helix via `tree-house` (MPL-2.0), Lapce via tree-sitter + `lapce-xi-rope` | — | — | ✅ crates.io (`tree-house`), ⚠️ Zed/Lapce from known architecture |
| Lezer port | — | **no Rust port on crates.io** (search "lezer" finds none) | — | — | ✅ crates.io search |
| **rowan** 0.17.0 | rust-analyzer's lossless red/green syntax tree (no parser; you bring lexer+parser) | Yes | MIT OR Apache-2.0 | 24 M dl, 2026-10 | ✅ crates.io, GitHub |
| cstree 0.14.0 | rowan fork, thread-safe, interning | Yes | MIT OR Apache-2.0 | 2026-04 | ✅ crates.io |
| ra_ap_syntax 0.0.360 | full Rust parser from rust-analyzer | Yes | MIT OR Apache-2.0 | weekly, API unstable (0.0.x) | ✅ crates.io |
| logos 0.16.1 | fast derive lexer | Yes | MIT OR Apache-2.0 | 98 M dl | ✅ crates.io |
| lelwel 0.10.4 | LL(1) parser generator producing lossless CSTs, resilient | Yes | MIT OR Apache-2.0 | 2026-04 | ✅ crates.io |
| Biome parsers (`biome_js_parser`, `biome_css_parser`, `biome_json_parser`) | lossless JS/TS/CSS/JSON parsers on Biome's rowan fork | Yes | MIT OR Apache-2.0 | **last crates.io release 2024-03 / 2024-12** – Biome no longer publishes them; must git-depend on a moving monorepo | ✅ crates.io dates; ⚠️ reason |
| **pulldown-cmark** 0.13.6 | CommonMark + GFM pull parser; `into_offset_iter()` gives byte ranges per event | Yes | MIT | 198 M dl, 2026-10-30; Blinc already uses it (0.10) | ✅ crates.io; ⚠️ offset API from docs.rs knowledge |
| markdown (markdown-rs) 1.0.0 | 100 % CommonMark/GFM/MDX, mdast with `position` on every node | Yes (deps: unicode-id) | MIT | **repo last push 2025-04-23**, 99 open issues | ✅ crates.io, GitHub API |
| comrak 0.59.0 | CommonMark/GFM AST with `sourcepos` | Yes | BSD-2-Clause | very active | ✅ crates.io |

### B.2 Text buffer and text layout

| Crate | Role | Pure Rust | Licence | Maintenance | Source |
|---|---|---|---|---|---|
| **ropey** 1.6.1 | rope, char/line indexing, used by Helix | Yes | MIT OR Apache-2.0 (repo says MIT) | 14.5 M dl, 2025-08; repo pushed 2026-09, 4 open issues | ✅ crates.io, GitHub |
| crop 0.4.3 | B-tree rope, UTF-8 byte indexing, used by nomad | Yes | MIT | 2025-04 | ✅ crates.io (⚠️ GitHub repo moved; API returned 404) |
| lapce-xi-rope 0.4.0 | xi-editor rope fork | Yes | Apache-2.0 | 2025-12 | ✅ crates.io |
| cosmic-text 0.19.0 | shaping (now `harfrust`), layout, `Editor`, optional syntect `SyntaxEditor`, vi mode | Yes | MIT OR Apache-2.0 | 11.7 M dl, 2026-04 | ✅ crates.io deps |
| parley 0.12.0 | Linebender rich-text layout + `PlainEditor`, used by Blitz and Masonry | Yes | Apache-2.0 OR MIT | 2026-10-09, 6 crates.io owners | ✅ crates.io; owners ⚠️ (beri.net) |
| harfrust 0.15.0 | official HarfBuzz Rust port, successor of rustybuzz | Yes | MIT | 2026-10-22 | ✅ crates.io |

### B.3 How it fits Blinc (⚠️ opinion, based on the ✅ code facts in A.2)

- Blinc already owns text shaping and rendering; adding cosmic-text or parley as a second layout engine would duplicate fonts/shaping. Use them only as *references*, not inside the Blinc tree.
- Blinc's `code_editor` highlighter API is line-local, so a stateful highlighter (syntect) cannot be plugged in correctly through `SyntaxHighlighter` as-is. Two paths: (a) upstream PR adding a stateful/whole-buffer highlight hook (`highlight_lines(&[String]) -> Vec<StyledLine>` with state checkpoints), or (b) our own workbench editor component built from Blinc primitives (canvas/rich_text + text_selection) on top of ropey, emitting `StyledText` spans.

### B.4 Recommended pure-Rust stack (⚠️ opinion)

1. **Buffer**: `ropey` (mature, Helix-proven; switch to `crop` only if byte-offset-first API matters more).
2. **Highlighting (all languages)**: `syntect` with `default-features = false, features = ["default-fancy"]` + `two-face` (fancy feature) for the bat grammar/theme set. Keep `ParseState`/`HighlightState` checkpoints every N lines for incremental re-highlighting after edits. Map scopes to FreeSynergy theme tokens (not syntect themes) so CSS theming stays in Blinc.
3. **Structure (folding, outline, diagnostics) where needed**: `logos` + `rowan` (or `lelwel`) for our own formats (TOML/manifest, FS DSLs); `ra_ap_syntax` only if a Rust-specific workbench is required.
4. **Markdown**: `pulldown-cmark` 0.13 with `into_offset_iter()` for source mapping (actively maintained, already in Blinc); `markdown` (markdown-rs) only if an mdast with positions is essential — accept its slowed maintenance.
5. **Avoid**: anything tree-sitter (C runtime and/or C grammars: tree-sitter, tree-sitter-c2rust grammars, arborium, inkjet[archived], tree-house); syntect's default `onig` feature (C); giallo (EUPL-1.2); Biome crates (unpublished since 2024).
