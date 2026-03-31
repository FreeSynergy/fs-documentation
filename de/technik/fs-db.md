# fs-db

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-db` ist die Datenbank-Abstraktion für FreeSynergy — eine reine Library, kein Daemon.
Sie definiert den `DbEngine`-Trait sowie das `Repository<T>`-Pattern mit type-sicherem
`Filter<T>`-Builder. Konkrete Implementierungen leben in separaten Adapter-Repos
(`fs-db-engine-sqlite`, `fs-db-engine-postgres`).

**Consumer-Code kennt weder die konkrete Engine noch schreibt er SQL.**
Alle Datenbankoperationen laufen über `Repository<T>` + `Filter<T>` — die Engine
übersetzt intern in SQL, BSON oder was die jeweilige Datenbank braucht.

---

## Grundregel: Kein SQL im Consumer-Code

```
Falsch:  engine.execute("SELECT * FROM users WHERE email = $1", vec![email]).await
Richtig: repo.find(Filter::eq(User::email, email)).await
```

SQL-Strings sind ausschließlich in Adapter-Repos erlaubt (`fs-db-engine-sqlite`,
`fs-db-engine-postgres`). Programme, Apps und Services sehen nie einen SQL-String.

---

## Architektur

```
Programme / Services
      │ benutzen nur
      ▼
Repository<T>-Trait   ← Repository Pattern (CRUD + Filter)
Filter<T>             ← Type-safe Query Builder (kein SQL-String)
      │ delegiert an
      ▼
DbEngine-Trait        ← Strategy Pattern (austauschbare Implementierungen)
      │ implementiert von
      ▼
fs-db-engine-sqlite   ← SQLite via SeaORM (default)
fs-db-engine-postgres ← PostgreSQL via SeaORM
(zukünftig: MongoDB, MariaDB, …)
```

Kein direktes SeaORM oder sqlx außerhalb von Adapter-Repos.

---

## Repository\<T\>-Trait

Das Repository ist die einzige Schnittstelle die Programme kennen:

| Methode | Beschreibung |
|---|---|
| `find_by_id(id)` | Ein Objekt per ID laden |
| `find_all()` | Alle Objekte unfiltriert laden |
| `find(filter)` | Objekte mit `Filter<T>` suchen |
| `save(record)` | Objekt speichern (INSERT wenn kein PK, sonst UPDATE) |
| `delete(id)` | Objekt per ID löschen → `true` wenn gelöscht |
| `count(filter)` | Anzahl matchender Objekte |
| `exists(filter)` | Prüfen ob mindestens ein Objekt matcht |

`EngineRepository<E>` implementiert den Trait für jede `DbEngine`-Impl.

Alle Methoden sind `async` und liefern `Result<_, FsError>`.

---

## Filter\<T\> — Type-safe Query Builder

Kein SQL-String, kein direktes SQL im Consumer-Code. Felder werden als String-Namen übergeben,
der Typ `T` bindet den Filter an den richtigen `Repository<T>`:

```rust
// Einfacher Filter
let filter = Filter::<User>::eq("email", "alice@example.com");

// Kombinierter Filter
let filter = Filter::<User>::eq("active", true)
    .and(Filter::gt("created_at", since_timestamp))
    .order_by("name", Order::Ascending)
    .limit(50);

// Repository benutzen
let users = repo.find(filter).await?;
```

Verfügbare Filter-Operatoren:

| Operator | Beschreibung |
|---|---|
| `eq(field, value)` | Gleichheit |
| `ne(field, value)` | Ungleichheit |
| `gt(field, value)` | Größer als |
| `lt(field, value)` | Kleiner als |
| `gte / lte` | Größer/kleiner gleich |
| `in_list(field, values)` | In einer Liste |
| `like(field, pattern)` | Pattern-Match (% als Wildcard) |
| `is_null(field)` | NULL-Check |
| `and(filters)` | UND-Verknüpfung |
| `or(filters)` | ODER-Verknüpfung |
| `order_by(field, Order::Ascending\|Descending)` | Sortierung |
| `limit(n)` | Maximale Anzahl |
| `offset(n)` | Versatz (Pagination) |

Der `Filter<T>` wird von der jeweiligen Engine in ihre native Abfragesprache übersetzt —
SQL für relationale DBs, BSON für MongoDB, etc.

---

## DbEngine-Trait

Low-Level-Schnittstelle — nur Adapter-Repos implementieren und rufen sie auf:

| Methode | Beschreibung |
|---|---|
| `open(config)` | Verbindungspool öffnen |
| `migrate()` | Ausstehende Migrationen anwenden |
| `health()` | Verbindung prüfen → `DbHealth` |
| `close()` | Pool sauber schließen |

---

## Typen

| Typ | Beschreibung |
|---|---|
| `DbConfig` | URL + `max_connections`; Hilfsmethoden `sqlite(path)`, `postgres(url)` |
| `DbHealth` | `connected`, `latency_ms`, `backend` |
| `Order` | `Asc` / `Desc` für Sortierung |

---

## Weitere Traits / Typen

| Typ / Trait | Datei | Zweck |
|---|---|---|
| `Repository<T>` | `repo.rs` | Generisches Repository Pattern (CRUD + Filter) |
| `EngineRepository<E>` | `repo.rs` | Blanket-Impl über DbEngine |
| `DbRecord` | `record.rs` | Trait: Domain-Objekt ↔ DbRow |
| `DbRowExt` | `record.rs` | Helper: get_i64 / get_string / get_bool / get_opt_* |
| `Filter<T>` | `filter.rs` | Type-safe Query Builder |
| `Order` | `filter.rs` | Ascending / Descending |
| `Migrator` | `migration.rs` | Embedded SQL-Migrations (apply_pending) |
| `WriteBuffer` | `write_buffer.rs` | Buffered Writes + Flush |
| `DbManager` | `manager.rs` | Pool-Management |
| `CrudRepo` | `repository.rs` | Älteres CRUD-Interface (SeaORM-basiert) — wird abgelöst durch Repository<T> |

---

## Migration-Strategie

Jedes Programm liefert seine eigenen Migrationen — eingebettet in die Binary als Rust-Structs.
`fs-db` stellt den `MigrationRunner`-Trait bereit:

```rust
// In jedem Programm — eigene Migration als Rust-Struct
struct AddUserEmailIndex;
impl Migration for AddUserEmailIndex {
    fn version(&self) -> u64 { 20260401_001 }
    fn description(&self) -> &str { "Add index on users.email" }
    async fn up(&self, engine: &dyn DbEngine) -> Result<(), FsError> { ... }
    async fn down(&self, engine: &dyn DbEngine) -> Result<(), FsError> { ... }
}

// Beim Start: alle ausstehenden Migrationen anwenden
migration_runner.apply_pending(&[
    Box::new(CreateUsersTable),
    Box::new(AddUserEmailIndex),
]).await?;
```

**Regel:** Migrationen sind unveränderlich. Einmal committed, nie editieren.
Korrekturen immer als neue Migration.

---

## Verwendung (Consumer)

```rust
use fs_db::{Repository, Filter, Order};
use my_domain::User;

// Repository per Dependency Injection — nie direkt instanziiert
async fn find_active_users(repo: &dyn Repository<User>) -> Result<Vec<User>, FsError> {
    repo.find(
        Filter::<User>::eq("active", true)
            .order_by("name", Order::Ascending)
            .limit(100)
    ).await
}
```

Die konkrete Engine kommt per DI zur Laufzeit — der Code weiß nicht ob SQLite oder Postgres läuft.

---

## Engines als Artifacts

```
Standard: fs-db-engine-sqlite  (Capability "db.engine.sqlite")
Optional: fs-db-engine-postgres (Capability "db.engine.postgres")
```

Programme fragen `fs-registry` nach einer Capability `db.engine.*` — welche Engine
installiert ist, entscheidet das System, nicht der Code.

---

## Repo

- Lokal: `/home/kal/Server/fs-db/`
- GitHub: `git@github.com:FreeSynergy/fs-db.git`

---

Weiter: [fs-db-engine-sqlite](fs-db-engine-sqlite.md) | [fs-db-engine-postgres](fs-db-engine-postgres.md) | [Datenspeicherung](datenspeicherung.md) | [← Index](../INDEX.md)
