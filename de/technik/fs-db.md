# fs-db

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-db` ist die Datenbank-Abstraktion für FreeSynergy — eine reine Library, kein Daemon.
Sie definiert den `DbEngine`-Trait. Konkrete Implementierungen leben in separaten Adapter-Repos
(`fs-db-engine-sqlite`, `fs-db-engine-postgres`).

Consumer-Code kennt nur `dyn DbEngine` — nie die konkrete Engine.

---

## Architektur

```
DbEngine-Trait   ← Strategy Pattern (austauschbare Implementierungen)
      ↑
fs-db-engine-sqlite    ← konkrete Impl (SQLite / SeaORM)
fs-db-engine-postgres  ← konkrete Impl (PostgreSQL / SeaORM)
```

Kein direktes SeaORM oder sqlx außerhalb von Adapter-Repos.

---

## DbEngine-Trait

| Methode     | Beschreibung                                                 |
|-------------|--------------------------------------------------------------|
| `open`      | Verbindungspool öffnen (aus `DbConfig`)                     |
| `migrate`   | Alle ausstehenden Schema-Migrationen anwenden               |
| `execute`   | SQL ausführen (SELECT + DML), JSON-Parameter                |
| `health`    | Verbindung prüfen → `DbHealth` (latency, connected, backend)|
| `close`     | Verbindungspool sauber schließen                            |

---

## Typen

| Typ         | Beschreibung                                              |
|-------------|-----------------------------------------------------------|
| `DbConfig`  | URL + `max_connections`; Hilfsmethoden `sqlite(path)`    |
| `DbRow`     | Eine Zeile: `columns: Vec<String>`, `values: Vec<Value>` |
| `DbRows`    | Ergebnis-Set: `rows` + `rows_affected`                   |
| `DbHealth`  | `connected`, `latency_ms`, `backend`                     |

---

## Weitere Traits

| Trait              | Datei              | Zweck                                      |
|--------------------|--------------------|--------------------------------------------|
| `CrudRepo`         | `repository.rs`    | Generisches Repository Pattern (CRUD)      |
| `WriteBuffer`      | `write_buffer.rs`  | Buffered Writes + Flush                    |
| `MigrationRunner`  | `migration.rs`     | Abstraktion für Migration-Ausführung       |
| `ConnectionManager`| `manager.rs`       | Pool-Management                            |

---

## Verwendung (Consumer)

```rust
use fs_db::engine::{DbConfig, DbEngine};

async fn run(engine: &impl DbEngine) {
    engine.migrate().await.unwrap();
    let rows = engine.execute("SELECT 1 AS n", vec![]).await.unwrap();
    println!("{} row(s)", rows.rows.len());
}
```

Die konkrete Engine wird per Dependency Injection übergeben — nie direkt instanziiert.

---

## Engines als Artifacts

```
Standard: fs-db-engine-sqlite (Capability "db.engine.sqlite")
Optional: fs-db-engine-postgres (Capability "db.engine.postgres")
```

Programme fragen `fs-registry` nach einer Capability `db.engine.*` — welche Engine
installiert ist, entscheidet das System, nicht der Code.

---

## Repo

- Lokal: `/home/kal/Server/fs-db/`
- GitHub: `git@github.com:FreeSynergy/fs-db.git`

---

Weiter: [fs-db-engine-sqlite](fs-db-engine-sqlite.md) | [fs-db-engine-postgres](fs-db-engine-postgres.md) | [← Index](../INDEX.md)
