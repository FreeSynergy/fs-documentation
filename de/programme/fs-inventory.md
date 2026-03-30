# fs-inventory

**Lokales Paket-Inventar für FreeSynergy — "Was ist installiert?"**

Beantwortet die Frage, welche Ressourcen auf diesem Node installiert sind und
welche Service-Instanzen laufen. Single Source of Truth — kein anderer
Dienst darf eine eigene Installations-Liste führen.

**Repository:** `FreeSynergy/fs-inventory` — Service-Crate (Daemon + CLI)

---

## Das Inventar-Problem (und wie fs-inventory es löst)

**Ohne Inventar:**
```
Store installiert kanidm → schreibt irgendwo eine Datei
Init startet → prüft eine andere Stelle
ContainerAppManager fragt → hat keine Ahnung
Ergebnis: Chaos, Doppel-Installationen, fehlende Startprüfungen
```

**Mit fs-inventory:**
```
Store installiert kanidm → sendet Bus-Event "installer.package.installed"
fs-inventory empfängt   → schreibt in fs-inventory.db
Init, ContainerAppManager, ContainerApp fragen fs-inventory
Ergebnis: eine Wahrheit, alle einig
```

---

## Architektur

```
InventoryStore (Trait)          — Repository-Interface
    │
    └── Inventory               — SQLite-Backend (fs-inventory.db)

InventoryBusHandler             — lauscht auf installer.# Bus-Events
    └── bridget zu Inventory

API
    ├── gRPC (tonic)  Port 50052  — InventoryService
    └── REST (axum)   Port 8082   — /resources, /services, /status
                                   + Swagger UI unter /swagger-ui

CLI
    └── fs-inventory list / status / uninstall / services / serve
```

---

## Domain-Modelle

### InstalledResource

| Feld           | Typ               | Bedeutung                              |
|----------------|-------------------|----------------------------------------|
| `id`           | `String`          | Primärschlüssel, z. B. `"kanidm"`     |
| `resource_type`| `ResourceType`    | App / Container / Theme / Plugin / … |
| `version`      | `String`          | Installierte Version, z. B. `"1.5.0"` |
| `channel`      | `ReleaseChannel`  | Stable / Testing / Nightly             |
| `installed_at` | `String`          | ISO-8601 Timestamp                     |
| `status`       | `ResourceStatus`  | Active / Stopped / Error / …          |
| `config_path`  | `String`          | Pfad zur Konfigurationsdatei           |
| `data_path`    | `String`          | Pfad zum Datenverzeichnis              |
| `validation`   | `ValidationStatus`| Ok / Incomplete / Failed               |

### ResourceStatus

| Variant         | Bedeutung                                      |
|-----------------|------------------------------------------------|
| `Active`        | Läuft normal                                   |
| `Stopped`       | Installiert, aber nicht aktiv                  |
| `Installing`    | Wird gerade installiert                        |
| `Updating`      | Wird gerade aktualisiert                       |
| `SetupRequired` | Ersteinrichtung noch nicht abgeschlossen       |
| `Error(msg)`    | Fehler mit Beschreibung                        |

### ServiceInstance

| Feld              | Typ                | Bedeutung                              |
|-------------------|--------------------|----------------------------------------|
| `id`              | `String`           | UUID der Instanz                       |
| `resource_id`     | `String`           | Referenz auf InstalledResource         |
| `instance_name`   | `String`           | Benutzer-Name, z. B. `"main-iam"`     |
| `roles_provided`  | `Vec<Role>`        | Capabilities dieser Instanz            |
| `roles_required`  | `Vec<Role>`        | Abhängigkeiten zu anderen Instanzen    |
| `network`         | `String`           | Docker-Netzwerk                        |
| `status`          | `ServiceStatus`    | Running / Stopped / Starting / Error   |
| `port`            | `Option<u16>`      | Exponierter Host-Port                  |
| `s3_paths`        | `Vec<String>`      | S3-Pfade für persistente Daten         |

---

## InventoryStore-Trait

```rust
#[async_trait]
pub trait InventoryStore: Send + Sync {
    // Ressourcen
    async fn upsert_resource(&self, resource: &InstalledResource) -> Result<(), InventoryError>;
    async fn uninstall(&self, id: &str) -> Result<(), InventoryError>;
    async fn list_resources(&self) -> Result<Vec<InstalledResource>, InventoryError>;
    async fn get_resource(&self, id: &str) -> Result<Option<InstalledResource>, InventoryError>;
    async fn set_resource_status(&self, id: &str, status: &ResourceStatus) -> Result<(), InventoryError>;

    // Services
    async fn upsert_service(&self, svc: &ServiceInstance) -> Result<(), InventoryError>;
    async fn list_services(&self) -> Result<Vec<ServiceInstance>, InventoryError>;
    async fn services_with_role(&self, role: &str) -> Result<Vec<ServiceInstance>, InventoryError>;
    async fn set_service_status_by_name(&self, name: &str, status: &ServiceStatus) -> Result<(), InventoryError>;
}
```

**Idempotenz:** `upsert_resource` / `upsert_service` können beliebig oft aufgerufen werden —
bei bestehendem Eintrag wird nur der Status aktualisiert.

---

## Bus-Integration

`InventoryBusHandler` abonniert das Topic-Pattern `installer.#` auf dem fs-bus:

| Topic                        | Payload                    | Aktion                   |
|------------------------------|----------------------------|--------------------------|
| `installer.package.installed`| `PackageInstalledPayload`  | `upsert_resource()`      |
| `installer.package.removed`  | `PackageRemovedPayload`    | `uninstall()`            |

Fehlerhafte oder unbekannte Nachrichten werden gelogged und ignoriert — der Bus läuft weiter.

---

## gRPC-API

Proto-Definition: `proto/inventory.proto` — Service `InventoryService`

| RPC              | Request                   | Response                  |
|------------------|---------------------------|---------------------------|
| `UpsertResource` | `UpsertResourceRequest`   | `UpsertResourceResponse`  |
| `Uninstall`      | `UninstallRequest`        | `UninstallResponse`       |
| `ListResources`  | `ListResourcesRequest`    | `ListResourcesResponse`   |
| `GetResource`    | `GetResourceRequest`      | `GetResourceResponse`     |
| `UpsertService`  | `UpsertServiceRequest`    | `UpsertServiceResponse`   |
| `ListServices`   | `ListServicesRequest`     | `ListServicesResponse`    |
| `GetStatus`      | `GetStatusRequest`        | `GetStatusResponse`       |

Port: **50052**

---

## REST-API

Swagger UI: `http://localhost:8082/swagger-ui`

| Method   | Pfad                 | Bedeutung                              |
|----------|----------------------|----------------------------------------|
| `GET`    | `/health`            | Liveness-Probe                         |
| `GET`    | `/status`            | Anzahl Ressourcen + Services           |
| `GET`    | `/resources`         | Alle installierten Ressourcen          |
| `POST`   | `/resources`         | Ressource upserten (JSON-Body)         |
| `GET`    | `/resources/{id}`    | Einzelne Ressource nach ID             |
| `DELETE` | `/resources/{id}`    | Ressource deinstallieren               |
| `GET`    | `/services`          | Alle Services (optional: `?role=iam`)  |
| `POST`   | `/services`          | Service-Instanz upserten               |

Port: **8082**

---

## CLI

```sh
# Daemon starten
fs-inventory serve

# Alle Ressourcen auflisten
fs-inventory list

# Status einer Ressource
fs-inventory status kanidm

# Ressource entfernen
fs-inventory uninstall kanidm

# Services anzeigen (optional nach Rolle filtern)
fs-inventory services
fs-inventory services --role iam
```

Umgebungsvariablen:

| Variable           | Default                                     |
|--------------------|---------------------------------------------|
| `FS_INVENTORY_DB`  | `/var/lib/freesynergy/inventory.db`         |
| `FS_GRPC_PORT`     | `50052`                                     |
| `FS_REST_PORT`     | `8082`                                      |

---

## Datenbank-Schema

SQLite (`fs-inventory.db`), angelegt beim ersten Start:

```sql
CREATE TABLE installed_resources (
    id            TEXT PRIMARY KEY NOT NULL,
    resource_type TEXT NOT NULL,
    version       TEXT NOT NULL,
    channel       TEXT NOT NULL DEFAULT 'stable',
    installed_at  TEXT NOT NULL,
    status        TEXT NOT NULL DEFAULT '{"state":"active"}',
    config_path   TEXT NOT NULL DEFAULT '',
    data_path     TEXT NOT NULL DEFAULT '',
    validation    TEXT NOT NULL DEFAULT 'incomplete'
);

CREATE TABLE service_instances (
    id             TEXT PRIMARY KEY NOT NULL,
    resource_id    TEXT NOT NULL REFERENCES installed_resources(id),
    instance_name  TEXT NOT NULL,
    roles_provided TEXT NOT NULL DEFAULT '[]',
    roles_required TEXT NOT NULL DEFAULT '[]',
    variables      TEXT NOT NULL DEFAULT '[]',
    network        TEXT NOT NULL DEFAULT '',
    status         TEXT NOT NULL DEFAULT '{"state":"stopped"}',
    port           INTEGER,
    s3_paths       TEXT NOT NULL DEFAULT '[]'
);
```

JSON-Felder: `resource_type`, `channel`, `status`, `validation`, `roles_provided`,
`roles_required`, `variables`, `s3_paths` sind JSON-Strings (serde_json).

---

## Abhängigkeiten

| Crate        | Zweck                                      |
|--------------|--------------------------------------------|
| `fs-types`   | `ResourceType`, `Role`, `ValidationStatus` |
| `fs-error`   | `FsError`                                  |
| `fs-db`      | `DbConfig` (SQLite-Konfiguration)          |
| `fs-bus`     | `TopicHandler`-Trait, Bus-Events           |
| `fs-i18n`    | FTL-Keys für Status + Fehlermeldungen      |
| `sea-orm`    | Entity-Derive-Makros (intern)              |
| `tonic`      | gRPC-Server                                |
| `axum`       | REST-Server                                |
| `utoipa`     | OpenAPI-Dokumentation                      |
| `clap`       | CLI-Parsing                                |
