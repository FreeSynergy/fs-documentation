# fs-db-engine-postgres

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-db-engine-postgres` ist der PostgreSQL-Adapter für die FreeSynergy-Datenbankabstraktion.
Er implementiert den `DbEngine`-Trait aus `fs-db` via sqlx + PostgreSQL und läuft als
eigenständiger Microservice mit gRPC- und REST-Endpunkt.
Beim Start registriert er die Capability `db.engine.postgres` in `fs-registry`.

---

## Architektur

```
fs-db (DbEngine-Trait — keine Engine-Abhängigkeit)
    └── fs-db-engine-postgres
            PostgresEngine  → implementiert DbEngine (sqlx PgPool)
            GrpcEngine      → tonic DbEngineService
            REST router     → axum /health, /migrate, /execute
            capability      → "db.engine.postgres" für fs-registry
```

**Adapter Pattern**: Consumer kennen nur den `DbEngine`-Trait — nie dieses Crate direkt.

---

## Capability

| Feld | Wert |
|---|---|
| ID | `db.engine.postgres` |
| Registriert in | `fs-registry` |
| Endpunkt | `http://0.0.0.0:8082` (konfigurierbar) |

Beim Start öffnet der Service die Registry-DB (`FS_REGISTRY_PATH`) und registriert
`service_id = "fs-db-engine-postgres"`.  Bei sauberem Shutdown erfolgt automatische
Deregistrierung.

---

## API

### gRPC (Port 50052)

Proto-Datei: `proto/db_engine.proto` (geteilt mit `fs-db-engine-sqlite`)

| RPC | Beschreibung |
|---|---|
| `Open` | Verbindung öffnen (URL + max. Connections) |
| `Close` | Verbindung schließen |
| `Migrate` | DDL-Migrationen ausführen |
| `Execute` | SQL ausführen (SELECT oder DML) |
| `Health` | Verbindungsstatus + PostgreSQL-Version |

### REST (Port 8082)

| Methode | Pfad | Beschreibung |
|---|---|---|
| `GET` | `/health` | Health-Probe: Status + Version |
| `POST` | `/migrate` | Migrationen ausführen |
| `POST` | `/execute` | SQL ausführen (`{"sql":"...","params":[...]}`) |
| `GET` | `/swagger-ui` | OpenAPI-Dokumentation |

---

## Konfiguration (Umgebungsvariablen)

| Variable | Standard | Beschreibung |
|---|---|---|
| `FS_DB_URL` | `postgres://freesynergy:freesynergy@localhost:5432/freesynergy` | PostgreSQL Connection URL |
| `FS_GRPC_PORT` | `50052` | gRPC-Port |
| `FS_REST_PORT` | `8082` | REST-Port |
| `FS_REGISTRY_PATH` | `/var/lib/freesynergy/registry.db` | Pfad zur fs-registry SQLite-DB |
| `FS_LANG` | `en` | Aktive Sprache (en / de / fr / es) |

Integration-Tests benötigen `FS_TEST_PG_URL` (werden sonst übersprungen).

---

## i18n

Alle user-facing Fehlermeldungen kommen aus `fs-i18n/locales/{lang}/db.ftl`:

| Key | Variable | Beschreibung |
|---|---|---|
| `db-engine-postgres-name` | — | Anzeigename der Capability ("PostgreSQL") |
| `db-error-connection-failed` | `$url` | Verbindungsfehler |
| `db-error-query-failed` | `$reason` | Abfrage-/DML-Fehler |
| `db-error-health-failed` | `$reason` | Health-Check-Fehler |

---

## Tests

```bash
# Integration-Tests (brauchen laufende PG-Instanz)
FS_TEST_PG_URL=postgres://user:pass@localhost/test cargo test

# Ohne FS_TEST_PG_URL werden Tests übersprungen (kein Fehler)
cargo test
```

---

## Repo

- Lokal: `/home/kal/Server/fs-db-engine-postgres/`
- GitHub: `git@github.com:FreeSynergy/fs-db-engine-postgres.git`

---

Weiter: [fs-db-engine-sqlite](fs-db-engine-sqlite.md) | [Datenspeicherung](datenspeicherung.md)
