# Turso / libSQL — sync, features, and fit for `fs-store`

Researched: 2026-11-05 · by: Claude subagent · status: ⚠️ unless marked ✅

Legend: ✅ = checked against the linked primary source on 2026-11-05 · ⚠️ = inference, secondary source, or not fully verified.

---

## 1. Turso vs. libSQL, licences, versions, ownership

| | **Turso Database** (repo `tursodatabase/turso`) | **libSQL** (repo `tursodatabase/libsql`) |
|---|---|---|
| What | SQLite-compatible engine **rewritten from scratch in Rust** (earlier codename "Limbo"). Now also has an experimental Postgres frontend. | **Fork of SQLite (C)**, plus Rust crates around it (embedded replicas, `sqld`/`libsql-server`). |
| Licence (SPDX) | `MIT` ✅ [LICENSE.md](https://github.com/tursodatabase/turso/blob/main/LICENSE.md), crate metadata `MIT` ✅ [crates.io API](https://crates.io/api/v1/crates/turso) | `MIT` (repo LICENSE.md, "Copyright 2023 the sqld authors") ✅ [LICENSE.md](https://github.com/tursodatabase/libsql/blob/main/LICENSE.md); crate `libsql` `MIT` ✅ [crates.io API](https://crates.io/api/v1/crates/libsql). The SQLite C code itself is public domain. |
| Status | README: "runs in production today at multiple organizations", but **not yet 1.0**; several features explicitly *experimental* ✅ [README FAQ](https://github.com/tursodatabase/turso). The libSQL README still calls Turso "currently in beta" ✅ [libsql README](https://github.com/tursodatabase/libsql). | "actively maintained, but new features are being developed in Turso" — i.e. maintenance mode. ✅ [libsql README](https://github.com/tursodatabase/libsql) |
| Latest version | Stable **v0.8.3 (2026-10-12)**; pre-release **v0.9.0-pre.2 (2026-10-28)** ✅ [releases](https://github.com/tursodatabase/turso/releases); crate `turso` max stable 0.8.3, newest 0.9.0-pre.2 ✅ [crates.io](https://crates.io/crates/turso) | crate `libsql` **0.10.0 (2026-10-13)** ✅ [crates.io](https://crates.io/crates/libsql); last tagged `libsql-server` GitHub release **v0.24.32 (2025-02-14)** ✅ [releases](https://github.com/tursodatabase/libsql/releases) (Cargo.toml on main says 0.24.33) |
| Vendor's direction | "Rewriting SQLite in Rust ... replaces libSQL as our intended direction." ✅ [README FAQ](https://github.com/tursodatabase/turso) | "If you're starting a new project, you probably want to look into Turso." ✅ [libsql README](https://github.com/tursodatabase/libsql) |

**Ownership — the user is right:** ✅ Supabase announced on **2026-10-02** that it is **acquiring Turso** (with a $150M funding round led by GIC).
- Turso blog: "Turso ... is being acquired by Supabase." Glauber Costa becomes Supabase "Head of Agentic Services"; co-founder Pekka Enberg and the team join. "Open source stays open. Turso Database remains open source and actively developed." ✅ [turso.tech/blog/turso-is-joining-supabase](https://turso.tech/blog/turso-is-joining-supabase)
- Supabase blog: "Supabase will continue building around Postgres, while Turso will continue its work on SQLite." ✅ [supabase.com/blog/supabase-is-acquiring-turso](https://supabase.com/blog/supabase-is-acquiring-turso)
- Company history (⚠️ background knowledge): Turso was formerly ChiselStrike Inc. (founders Glauber Costa, Pekka Enberg); libSQL fork 2022; rename to Turso 2023; Limbo (Rust rewrite) started 2024 and was renamed "Turso Database" in 2025.
- Wording "is being acquired / agreed to buy" — whether closing has completed was not verified ⚠️.

**Implication:** MIT licence protects us against a licence change of existing code, but the roadmap is now driven by a Postgres company focused on "a database per AI agent" in the cloud. Local/self-hosted sync is not their business priority ⚠️ (inference).

---

## 2. Turso Sync (push/pull, offline writes)

Two generations:

1. **libSQL Embedded Replicas** (old): local *read* replica of a Turso Cloud DB; physical page/frame replication; writes go to the primary; "offline writes" (`offline: true`, Rust `Builder::new_synced_database`) were a public beta in March 2025, "not yet recommended for production ... data loss is possible", conflict *detection* only ✅ [Offline Sync Public Beta blog, 2025-03-31](https://turso.tech/blog/turso-offline-sync-public-beta).
2. **Turso Sync** (new, built on the Rust Turso Database engine, recommended now) ✅ [local-first guide, 2026-07-27](https://turso.tech/blog/building-local-first-apps-the-complete-guide-to-offline-first-database-sync):
   - **Push**: local changes are collected from the local **CDC table** and sent as **logical row-level mutations / batched SQL**; the remote applies them atomically ✅ [docs: sync/usage](https://docs.turso.tech/sync/usage), ✅ [agent-skills sync.md](https://github.com/tursodatabase/agent-skills/blob/main/skills/turso-db/references/sync.md).
   - **Pull**: client sends its revision; server returns **physical WAL frames/pages** since then; the local copy "eventually becomes byte-for-byte identical to the remote" ✅ (same sources). Local un-pushed changes are rebased via a "revert database/WAL".
   - **No automatic background sync** — the app must call `push()`/`pull()` itself; `checkpoint()` and `stats()` exist ✅ [agent-skills sync.md].
   - Offline start: `bootstrap_if_empty(false)` lets the app start with no network ✅ [docs: sync/usage].
   - **A synced file MUST only be opened via the sync SDK** — opening it with the CLI, a non-sync SDK or sqlite3 can "corrupt the sync state permanently" ✅ [agent-skills sync.md]. (Relevant: fs-hub could not just open a program's synced file.)

**One local DB ↔ exactly one remote DB.** ✅ Each sync connection is configured with exactly one `path` + one `remote_url` ✅ [docs: sync/usage]. "The remote Turso database is always the source of truth, and all sync flows through it"; peer-to-peer is not supported ✅ [local-first guide].

**Two programs (a.db, b.db) pointing at the same remote URL** → both are replicas of **the same** database. Because pull is physical-page based and converges to a byte-identical copy, both files get **all tables** of the remote (unless partial sync, see below). ⚠️ (direct consequence of the documented design, not a sentence in the docs.) **There is no mechanism to merge several independent databases into one remote**; that would have to be done at the application level (e.g. distinct table names per program in one shared DB — which defeats isolation — or our own object-level sync). Turso's own docs recommend "control which data goes into which database (e.g., per user or per tenant), and then transfer the entire database" ✅ [Offline Sync beta blog].

**Partial sync:** ✅ experimental; it is *lazy page loading*, not a table/row filter. Strategies: `prefix` (first N bytes) or `query` (pages touched by a SQL query), plus `segmentSize`/`prefetch`; "remaining pages are fetched on demand" ✅ [agent-skills sync.md]; Rust: `with_partial_sync_opts_experimental(PartialSyncOpts { bootstrap_strategy: Prefix{..} })` ✅ [bindings/rust/src/sync.rs](https://github.com/tursodatabase/turso/blob/main/bindings/rust/src/sync.rs). → **No selective replication of "only these tables/rows".**

**Conflict resolution:** ✅ default **"last push wins"** at row level ("regardless of when the local commit happened") ✅ [docs: sync/usage], [local-first guide]. A `transform` hook can rewrite each mutation (gets `before`/`after`) before push — documented for **JavaScript** ✅. **The Rust `sync::Builder` has no transform hook** (no `transform` in `bindings/rust/src/sync.rs` on main) ✅ [sync.rs]. No built-in CRDTs ✅.

---

## 3. Local sync server / self-hosting

- ✅ **`tursodb --sync-server <ADDR>`** exists (flag help: "Start sync server instead of interactive shell and listen at given address (e.g. 0.0.0.0:8080)"). **No default port** — the address is mandatory; `8080` is only the example. New flag `--sync-dir PATH` serves every DB under a directory as `/db/{name}` (max 256 open, default) ✅ [cli/app.rs](https://github.com/tursodatabase/turso/blob/main/cli/app.rs). Turso's guide: "You can try sync locally without a Turso Cloud account ... `npx turso@latest --sync-server 0.0.0.0:8080`" ✅ [local-first guide].
- Implementation spec ✅ [cli/sync_server.mdx](https://github.com/tursodatabase/turso/blob/main/cli/sync_server.mdx) (the server is LLM-generated from this prompt): "simple implementation", processes **one request at a time**, HTTP/1.1 non-chunked, page size 4096 only, checkpoint disabled, endpoints `POST /v2/pipeline` (Hrana SQL-over-HTTP) and `POST /pull-updates` (protobuf). No auth/TLS mentioned ⚠️. → **Clearly a dev/test server**; there is no explicit "production" statement either way ⚠️. The *protocol* is documented as an "open protocol", so a production-grade self-hosted sync server could in principle be written ⚠️.
- **Production self-hosting today:** the only server product is **`sqld` / `libsql-server`** (MIT ✅), but it belongs to the libSQL generation (embedded replicas, Hrana) and its last GitHub release is Feb 2025 ✅. The Turso Cloud backend (diskless, WAL-on-S3) is offered as **BYOC** ("on your own through BYOC") ✅ [Turso joining Supabase blog] — that is a commercial offering, not an open-source self-host ⚠️. `turso dev` starts a local libSQL server (port 8080 in docs) ✅ [docs: local-development](https://docs.turso.tech/local-development).

---

## 4. Engine features

| Feature | Status | Source |
|---|---|---|
| **Multi-process access to one file** | **Experimental**: `--experimental-multiprocess-wal` / Rust `experimental_multiprocess_wal(true)`, `.tshm` sidecar, 64-bit Unix (+ Windows with IOCP VFS), "not production ready". Manual "Limitations" still lists "No multi-process access". Mixed SQLite+Turso multi-process is explicitly unsupported. | ✅ [manual.md](https://github.com/tursodatabase/turso/blob/main/docs/manual.md), ✅ [COMPAT.md](https://github.com/tursodatabase/turso/blob/main/COMPAT.md), ✅ README |
| **MVCC / `BEGIN CONCURRENT`** | `PRAGMA journal_mode = mvcc`; snapshot isolation, row-level write-write conflict → `SQLITE_BUSY`; Hekaton-style in-memory index. Manual: "not production ready". Limitations (no index on WITHOUT ROWID, TRUNCATE checkpoint blocks). | ✅ manual.md |
| **Encryption at rest** | Experimental (`--experimental-encryption`, Rust `experimental_encryption(true)` + `with_encryption(EncryptionOpts)`). Page-level AEAD: AES-GCM-128/256, AEGIS-128L/256 (+X2/X4); key never stored, per-connection; WAL encrypted too; no KDF/passphrase yet; rekey = rewrite. "not production ready". **The sync engine does NOT support local encryption** (comment in `bindings/rust/src/sync.rs`: "Local at-rest `encryption` is intentionally omitted because the sync engine does not support local encryption"); only *remote* (cloud) encryption via `with_remote_encryption`. | ✅ manual.md, ✅ sync.rs |
| libSQL encryption | `libsql` crate has an `encryption` feature (SQLCipher-based) | ✅ crate features on crates.io; details ⚠️ |
| **Vector search** | Vector types (dense/sparse/quantized/binary), distance functions, **exact search** supported; ANN **vector indexing still on roadmap** (libSQL has DiskANN-style index). Compatible with libSQL vector functions. | ✅ README, ✅ COMPAT.md |
| Full-text search | Experimental, tantivy-based, default crate feature `fts` | ✅ README, crates.io |
| **CDC** | "Early Preview". `PRAGMA capture_data_changes_conn('<off|id|before|after|full>[,table]')` — **per connection**; writes to a regular table (default `turso_cdc`) with `change_id` (strictly increasing PK), `change_time` (not monotonic), `change_type` (1 insert / 0 update / -1 delete / 2 COMMIT), `table_name`, `id` (rowid), `before`/`after`/`updates` BLOBs, `change_txn_id`. DDL captured as `sqlite_schema` rows. Caveats: records visible before commit; WITHOUT ROWID not supported; full mode triples write I/O; decoding old records after schema change needs own schema versioning. CDC is what Turso Sync's push uses internally. | ✅ manual.md "CDC (Early Preview)" |
| Triggers / views / savepoints | Supported per COMPAT.md (manual's limitation list is outdated) | ✅ COMPAT.md |

---

## 5. Rust crates

- **`turso`** (MIT ✅) — async API (`Builder::new_local(path).build().await`, `conn.query/execute/prepare`), tokio; feature **`sync`** enables `turso::sync::Builder::new_remote(path).with_remote_url(..).with_auth_token(..).bootstrap_if_empty(..).build()` with `push()/pull()/checkpoint()/stats()` ✅ [crates.io](https://crates.io/crates/turso), ✅ sync.rs. Experimental flags exposed as builder methods (`experimental_encryption`, `experimental_multiprocess_wal`, `experimental_materialized_views`, ...). Pre-1.0, ~140 versions since 2025-07, frequent API churn ⚠️. **docs.rs failed to build 0.8.3** (last successful docs build 0.8.0-pre.12) ✅ [docs.rs](https://docs.rs/turso/latest/turso/). Feature `pure-rust-crypto` exists ✅.
- **`libsql`** (MIT ✅) 0.10.0 — mature but maintenance-mode; features `core`, `replication`, `remote`, `sync`, `encryption`, `hrana` ✅ [crates.io](https://crates.io/crates/libsql). Links SQLite C code (not 100 % Rust) ⚠️.
- Recommendation for a "100 % Rust" project: **`turso`** (pure Rust engine) behind our own `fs-store` trait; pin exact versions; keep a SQLite-file-format escape hatch (Turso guarantees "You should always be able to go back to SQLite" ✅ COMPAT.md).

---

## Assessment for FreeSynergy

1. **Object-level sync via our own activity log is the right call** (⚠️ reasoning, based on ✅ facts above):
   - Turso Sync = 1 local file ↔ 1 remote DB, full-DB replication, no table/row filtering, no merge of independent DBs, hub-and-spoke only, LPW by default, no transform hook in Rust. That does not match "N programs each with their own DB → one hub aggregating standardised objects".
   - Turso Sync requires a sync server (Cloud, BYOC, or the dev-only `--sync-server`); no production-grade open self-hosted sync server for the new engine exists.
   - Synced files can't be opened by anything else (corruption risk) and **can't be encrypted locally** — conflicts with our "programs may store data encrypted" requirement.
   - Our own log is backend-independent (keeps `fs-store` swappable) and carries semantic objects (AS2 + JSContact/JSCalendar) instead of rowids/pages.
2. **Can Turso CDC feed the activity log?** Partially. It is a good *change trigger / outbox* (monotonic `change_id`, transaction grouping, before/after images), but: Early Preview, per-connection opt-in (a forgotten PRAGMA = silent gaps), rowid-based (not object IDs), binary record blobs that need schema-aware decoding, extra write amplification. Safer design: `fs-store` writes the activity-log entry **explicitly in the same transaction** as the object change (transactional outbox); CDC can optionally be used later as a consistency check or to detect writes that bypassed `fs-store`.
3. Multi-process: since each program owns its DB and the hub has its own DB, we avoid relying on experimental multi-process WAL; programs should hand objects to fs-hub via IPC, not let the hub open their files.
4. Encryption: usable only for non-synced local DBs and still experimental; plan `fs-store` so encryption is a backend capability flag, and keep a fallback (e.g. app-level envelope encryption of object payloads) until Turso's encryption leaves experimental.
