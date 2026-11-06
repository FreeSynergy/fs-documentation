# Coding rules (all FreeSynergy repos) — ADR 0043

Read before writing or changing any code. Applies to Opus, Sonnet and humans alike.

## 1. Program against interfaces
- Every capability is first a **trait** (or a Cap'n Proto interface between programs, ADR 0021).
  Callers depend on the trait, never on a concrete type. Concrete types live behind it.
- Standards first: the interface follows the data standard (ADR 0014), not the other way round.
- Public API = traits + small data types. Implementations are `pub(crate)` unless there is a reason.

## 2. Design patterns — always, and named
Rust has no classes, but the patterns map cleanly. Use the pattern, and **say which one** in the
module doc (`//! Pattern: Repository over Store (strategy for the backend)`).

| Pattern | Rust form | Typical use here |
|---------|-----------|------------------|
| Strategy | trait + `dyn Trait` / generic `T: Trait` | storage backends, tile sources, highlighters, key providers |
| Repository | trait with CRUD/query over a `Store` | contacts, calendar, wiki pages |
| Adapter | struct wrapping a foreign type, implementing our trait | vCard/ICS/Markdown import, Blinc behind our components, Turso behind `Store` |
| Facade | one small type that hides a subsystem | `fs-hub-client`, program cores' entry points |
| Builder | `XBuilder` with `build() -> Result<X>` | complex construction (queries, compiler commands, envelopes) |
| Command | enum of operations + `apply`/`invert` | undo/redo, activity log |
| Observer | `tokio::sync::broadcast`/`watch`, listener traits | subscriptions, change streams |
| State | enum states + transition fns, or typestate generics | invitations, drafts, connections, delivery state |
| Template method | trait with provided default methods | shared flows (import → validate → store) |
| Decorator | wrapper implementing the same trait | `CachedSource` over `TileSource`, logging, metrics |
| Newtype | `struct ObjectId(Uuid)` | ids, units, validated values |
| Iterator | `impl Iterator` | paging, expansion (recurrences), tokenising |
| RAII / Guard | `Drop` | transactions, subscriptions, locks |
| Registry | map of kind → behaviour | mark kinds, representation register (ADR 0023) |
| Factory | fn/trait creating trait objects from config | choose backend/source at runtime |

No pattern for its own sake: pick the one that makes the code reusable and testable, and write why.

## 3. Small files, many of them
- **One concept per file.** Guideline: **≤ 200 lines**, hard limit **300** (tests included —
  split tests by feature into `tests/<feature>.rs`). Generated code is exempt.
- Folders mirror concepts: `src/store/mod.rs` (trait) + `src/store/turso/{schema,query,undo,…}.rs`.
- `mod.rs`/`lib.rs` only declare modules and re-export; no logic there.

## 4. Reuse before writing
- Look first: existing FreeSynergy crate? existing permissive crate (ADR 0015)? Only then write.
- Shared code moves into a shared crate instead of being copied between repos.

## 5. Refactoring is part of the work
- Every change leaves the code at least as clean as before. When a file passes the limit or a
  second implementation of an idea appears → refactor now, not later.
- Refactoring commits are separate from feature commits (`refactor: …`), tests stay green.

## 6. Documentation — for people and for the next agent
- `//!` module doc on every module: purpose, **pattern used**, how it fits.
- `///` on every public item (`#![deny(missing_docs)]` in libraries).
- `DESIGN.md` per repo: architecture, **pattern map** (which pattern where, why), decisions, a
  **State** section kept current at every commit.
- Examples in `examples/` for every public entry point.

## 7. Quality gates (before every commit)
`cargo fmt --check` (**ohne** `--all` — `--all` prüft auch Pfad-Abhängigkeiten anderer Repos) · `cargo clippy --all-targets -- -D warnings` (with `clippy::pedantic` as warn) ·
`cargo test` · `scripts/check_rust_rules.py` (file length, module docs, pattern line) ·
Rust hygiene (ADR 0041).
