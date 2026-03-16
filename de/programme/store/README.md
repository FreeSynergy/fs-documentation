# Store — Das Wissen

[← Zurück zum Index](../../INDEX.md)

---

## Was der Store ist

Der Store ist NICHT nur eine Download-Plattform. Er ist ein **Wissensspeicher** der allen Programmen hilft.

Drei Hauptfunktionen:

1. **Bereitstellen:** Pakete zum Download (Plugins, Sprachen, Themes, Widgets, Bots, Tasks)
2. **Wissen:** Der Conductor fragt "Kennst du diesen Service?" → Store liefert Metadaten, Rollen, Variablen-Typen
3. **Versionierung:** Jedes Paket hat Version + Tag → Updates, Rollbacks, Changelogs

## Eigenständigkeit

Der Store funktioniert **ohne jedes andere FreeSynergy-Programm**. Er ist ein Git-Repository, das man klonen und komplett offline nutzen kann. Wenn Internet da ist, kann er auch von einer URL geladen werden.

Die gleichen Funktionen die in der GUI verfügbar sind — suchen, filtern, installieren, aktualisieren — sind auch über **CLI** und **API** erreichbar. Business-Logik einmal implementiert, drei Interfaces.

## Paket-Typen

| Typ | Inhalt |
|---|---|
| `container` | Service-Modul (Quadlet + Config) |
| `language` | Sprach-Snippets (.ftl) |
| `theme` | Visuelles Theme |
| `widget` | Desktop-Widget |
| `bot` | Bot-Definition |
| `bridge` | Service-Bridge |
| `task` | Automatisierungs-Template |

## Paket-Metadaten

```toml
[package]
id = "kanidm"
name = "Kanidm"
version = "1.5.0"
type = "container"
description = "Modern identity management"
icon = "kanidm"
tags = ["iam", "oidc", "scim", "mfa", "webauthn", "identity", "rust"]
author = "Kanidm Project"
license = "MPL-2.0"
homepage = "https://kanidm.com"
source = "https://github.com/FreeSynergy/Store"
```

---

## Tag-System

Tags sind das **primäre Suchinstrument** des Stores. Jedes Paket muss aussagekräftige Tags haben — ohne gute Tags ist ein Paket praktisch unsichtbar.

### Welche Tags ein Paket braucht

| Pakettyp | Tag-Regeln |
|---|---|
| `container` | Alle Rollen die der Service hat, alle Unterrollen, alle kompatiblen Standards |
| `language` | Sprach-Code (de, en, fr), Region (de-AT), Programm-ID (node, desktop) |
| `theme` | Farb-Namen (dark, light, cyan, rose), Stil (minimal, glass, retro) |
| `widget` | Funktion (clock, monitor, notes), Datenquelle (system, network, calendar) |
| `bot` | Plattform (telegram, matrix), Funktion (broadcast, gatekeeper, reminder) |
| `task` | Quell-Service, Ziel-Service, Funktion (sync, backup, notify) |

**Beispiele:**

```toml
# Mail-Server (Stalwart)
tags = ["mail", "smtp", "imap", "dkim", "dmarc", "spf", "webmail", "rust"]

# Postgres
tags = ["database", "sql", "postgres", "relational", "backup"]

# Outline (Wiki)
tags = ["wiki", "docs", "knowledge", "collaboration", "editor"]

# Deutsch (Sprache)
tags = ["language", "de", "german", "i18n"]
```

### Filter-Kombinationen

Der Store unterstützt kombinierte Filter:

```
# Alle IAM-Services
tags contains "iam"

# Alle Rust-basierten Container
type = "container" AND tags contains "rust"

# Alles rund um Mail
tags contains "mail" OR tags contains "smtp" OR tags contains "imap"

# Deutsche Sprach-Pakete für Desktop
type = "language" AND tags contains "de" AND tags contains "desktop"
```

Mehrere Tags in einer Suche → AND-Verknüpfung (alle müssen passen). Freitext-Suche → durchsucht Name, Beschreibung, Tags (OR-Verknüpfung).

---

## Verzeichnisstruktur

```
Store/
├── shared/          ← Für ALLE Programme
│   ├── i18n/
│   ├── themes/
│   ├── widgets/
│   ├── bots/
│   └── tasks/
├── node/            ← Für Node
│   ├── modules/
│   └── bridges/
├── desktop/         ← Für Desktop
└── catalog.toml     ← Maschinenlesbarer Gesamt-Index
```

### catalog.toml

Der Katalog ist der maschinenlesbare Index aller Pakete. Programme laden ihn einmal und arbeiten lokal damit.

```toml
[[packages]]
id = "kanidm"
name = "Kanidm"
version = "1.5.0"
type = "container"
description = "Modern identity management"
tags = ["iam", "oidc", "scim", "mfa"]
icon = "kanidm"
path = "node/modules/kanidm/"
checksum = "sha256:abc123..."
```

---

## CLI-Interface

Der Store ist ohne GUI bedienbar. Alle Befehle arbeiten auf dem lokalen Store-Klon oder über eine URL.

```bash
# Pakete suchen
fsn store search "mail"
fsn store search --type container --tag smtp
fsn store search --type theme --tag dark

# Paket-Details
fsn store info kanidm
fsn store info --version 1.4.0 kanidm

# Installieren / Aktualisieren
fsn store install kanidm
fsn store update kanidm
fsn store update --all

# Deinstallieren
fsn store remove kanidm
fsn store remove --keep-data kanidm

# Installierte Pakete
fsn store list
fsn store list --type container
fsn store list --outdated

# Catalog aktualisieren
fsn store sync
fsn store sync --offline          # Nur lokalen Cache nutzen
fsn store sync --url https://...  # Alternativer Store
```

---

## API-Interface

Der Store-Dienst (wenn laufend) stellt eine REST-API bereit. Identische Funktionen wie CLI und GUI.

### Suche & Abfrage

```
GET /api/store/packages
    ?q=kanidm              # Freitext
    &type=container        # Typ-Filter
    &tags=iam,oidc         # Tag-Filter (AND)
    &installed=true        # Nur installierte

GET /api/store/packages/:id
GET /api/store/packages/:id/versions
GET /api/store/packages/:id/changelog
```

### Installation

```
POST /api/store/install
    { "id": "kanidm", "version": "1.5.0" }

POST /api/store/update
    { "id": "kanidm" }

DELETE /api/store/packages/:id
    ?keep_data=true
```

### Catalog

```
GET /api/store/catalog          # Gesamter Katalog
POST /api/store/sync            # Catalog von Remote laden
GET /api/store/status           # Sync-Status, letzte Aktualisierung
```

### Wissen (für andere Programme)

Programme fragen den Store gezielt nach Metadaten. Das macht den Conductor intelligenter ohne dass er selbst alles wissen muss.

```
GET /api/store/know/service/:id
    # Liefert: Rollen, Variablen-Typen, Default-Ports, Health-Check-Muster

GET /api/store/know/variable/:name
    # Liefert: Typ-Vermutung für einen Variablen-Namen

GET /api/store/know/compatible?role=iam
    # Welche installierten Services haben diese Rolle?
```

**Beispiel — Conductor fragt:**
```json
GET /api/store/know/service/kanidm

{
  "id": "kanidm",
  "roles": ["iam", "iam.oidc", "iam.scim"],
  "variables": [
    { "name": "KANIDM_DOMAIN", "type": "hostname", "role": null },
    { "name": "KANIDM_ADMIN_PASSWORD", "type": "password", "role": null }
  ],
  "offers": ["iam.oidc-discovery-url", "iam.admin-api"],
  "healthcheck": "https://$KANIDM_DOMAIN/status"
}
```

---

## Wie Programme den Store nutzen

Programme binden `fsn-store` als Library ein (nicht die GUI) und kommunizieren direkt:

```rust
use fsn_store::StoreClient;

// Pakete suchen
let results = StoreClient::search()
    .package_type(PackageType::Container)
    .tag("iam")
    .tag("oidc")
    .run().await?;

// Paket installieren
StoreClient::install("kanidm").await?;

// Service-Wissen abfragen
let meta = StoreClient::know_service("kanidm").await?;
let oidc_url = meta.offer("iam.oidc-discovery-url");
```

Der `StoreClient` abstrahiert ob der Store lokal (Git-Klon), per HTTP (laufender Store-Dienst) oder gebündelt (eingebetteter offline-Fallback) ist.

---

## Repo

https://github.com/FreeSynergy/Store

---

Weiter: [Desktop](../desktop/README.md) | [Pakete](../../konzepte/pakete.md)
