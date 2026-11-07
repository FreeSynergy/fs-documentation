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
| Value object | small immutable type, compared by value, valid on construction | dates, addresses, rules, plans |
| Specification | pure predicate over a value, combinable | the "encrypted only" gate, validation rules |
| Null object | a type that implements the trait and does nothing, on purpose | no-op listener, empty source |
| Composite | a tree of the same trait | nested layouts, nested filters |
| Memento | an opaque snapshot to restore or read from | undo, consistent reads |
| Visitor | one function per variant, kept outside the data | walking a document or schema |
| Interpreter | evaluate a small language over its tree | recurrence rules, queries |
| Capability object | a type only one place can hand out; holding it is the right | the port of a guard, a local enrolment |

No pattern for its own sake: pick the one that makes the code reusable and testable, and write why.

**Name only what is really there (2026-11-07).** A module head names a pattern from this table, plus how it is used here. A name that is not
in the table is reported to the strategy session, not invented. A file of constants is not a Registry, because nothing is looked up by
kind: it says `Constants`. A test file names what it tests; it has no pattern of its own. A type split over several files says so: `Adapter, part of MatrixProvider`. The check before a tag compares the name with the code.

**A small file without behaviour may say so (project owner, 2026-11-07):** `Pattern: none`, for error lists, plain data, constants, a single pure function or a small set of them for one concept, and a thin binary. A
made-up name is worse than an honest "none". Anything with behaviour still names a pattern and sits behind an interface. "Behaviour" here means state or side effects: a function that only computes its result from its arguments has none. A fixed sequence that reads, writes or calls out names its pattern (usually Facade or Template method), except the thin binary. If nothing fits, report it.

## 2a. Text a person reads (ADR 0057)
Translation itself comes later (ADR 0053), but text must be translatable from now on.
- No sentence a person reads inline in code. It goes in the program's `words.rs` or a component's `labels.rs`.
- A whole sentence with named placeholders, never joined from pieces: word order differs between languages. New text does not use positional `{}`.
- Code never decides by comparing text. It decides by a type, an id or a problem type.
- Numbers, dates and plurals are not formatted by hand when a reader sees them, as far as the code can avoid it.
- Log lines and developer errors stay English and are not translated.

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

## 8. Dependencies between our repos
- Always **git dependencies with a tag**, never local paths:
  `fs-store = { git = "https://github.com/FreeSynergy/fs-store", tag = "v0.2.0" }`.
- A change in a shared repo → new tag → dependents bump the tag in the same step.
- Working across repos on one machine: override temporarily with
  `cargo test --config 'patch."https://github.com/FreeSynergy/fs-store".fs-store.path="../fs-store/crates/fs-store"'`
  — never commit such paths (a fresh clone must build; check with a clone into `/tmp`).

