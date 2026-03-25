# Inventory

[← Zurück zum Index](../INDEX.md) | [Store](../programme/store/README.md) | [Registry](registry.md) | [Adapter-Pattern](adapter.md)

---

## Die vier Ebenen — Kern-Architektur-Entscheidung

```
┌─────────────────────────────────────────────────────────────────┐
│  STORE       = Das Mögliche    — "Was gibt es?"                 │
│               Git-Repo, TOML-Kataloge, Binary-URLs. Kein State. │
│                                                                 │
│  INVENTORY   = Der Jetzt-Zustand — "Was ist installiert?"       │
│               SQLite. Einzige Wahrheitsquelle. Nur Manager      │
│               schreiben. Alle anderen lesen.                    │
│                                                                 │
│  REGISTRY    = Was läuft — "Welche Capabilities sind aktiv?"    │
│               Services registrieren sich beim Start.            │
│               Bus fragt Registry für Routing.                   │
│                                                                 │
│  MANAGERS    = Das Wie — "Wie wird etwas installiert/konfiguriert?"│
│               Führen Aktionen aus, schreiben Ergebnis ins       │
│               Inventory, starten Services die sich in die       │
│               Registry eintragen.                               │
└─────────────────────────────────────────────────────────────────┘
```

**Diese Trennung ist absolut. Sie darf nie vermischt werden.**

| Ebene | Frage | Datenquelle | Schreibt wer? |
|---|---|---|---|
| **Store** | "Was gibt es?" | Git-Repo, TOML | CI/CD, Maintainer |
| **Inventory** | "Was ist installiert?" | `fs-inventory.db` (SQLite) | Nur Manager |
| **Registry** | "Was läuft gerade?" | `fs-registry.db` (SQLite) | Services selbst |
| **Managers** | "Wie macht man es?" | Deployment-Logik | — (Logik, kein Store) |

---

## Zwei Inventory-Konzepte — klar getrennt

Es gibt zwei Dinge die "Inventory" heißen — sie sind verschieden:

### 1. `InstallRecord` (Store-intern)

In `fs-store/crates/fs-store/src/inventory.rs` — intern im Store-Prozess.

- Verfolgt: welche Paket-Version ist installiert, Pin-State, Pfad
- Gespeichert in: `records.toml` (lokal auf dem System)
- Geschrieben von: `fs-store` selbst (nach erfolgreichem Download + Install)
- Gelesen von: `fs-store` (für Update-Prüfungen, Version-Anzeige)
- **Scope:** Nur für das Store-Paket-Management relevant

### 2. `fs-inventory` Service (System-weit)

Das standalone Repo `FreeSynergy/fs-inventory` — der System-weite Wahrheitsspeicher.

- Verfolgt: was ist auf dem Node installiert, welche Services laufen, auf welchen Ports
- Gespeichert in: `fs-inventory.db` (SQLite, eigene Datei)
- Geschrieben von: **nur Manager** (nach jeder erfolgreichen Aktion)
- Gelesen von: allen Programmen (Store, Desktop, Lenses, Bus, Widgets, ...)
- **Scope:** System-weit, einzige Wahrheitsquelle für den Laufzeit-Zustand

**Regel:** Was im UI angezeigt wird, kommt immer aus `fs-inventory` — nie direkt
aus `records.toml` oder direkt aus dem Store-Katalog.

---

## fs-inventory Schema

### InstalledResource — jedes installierte Paket

```rust
pub struct InstalledResource {
    pub id: String,                    // "kanidm"
    pub resource_type: ResourceType,   // App, Container, Theme, Language, ...
    pub version: String,               // "1.5.0"
    pub channel: ReleaseChannel,       // Stable, Testing, Nightly
    pub installed_at: DateTime<Utc>,
    pub status: ResourceStatus,
    pub install_path: PathBuf,         // deterministisch abgeleitet
    pub data_path: PathBuf,
    pub validation: ValidationStatus,
}

pub enum ResourceStatus {
    Active,
    Stopped,
    Error(String),
    Updating,
    Installing,
}
```

### ServiceInstance — für laufende Container-Apps und Native-Services

```rust
pub struct ServiceInstance {
    pub resource_id: String,           // → InstalledResource
    pub instance_name: String,         // vom Benutzer vergeben
    pub capabilities_provided: Vec<String>, // ["iam", "iam.oidc"]
    pub capabilities_required: Vec<String>, // ["database"]
    pub variables: Vec<ConfiguredVar>,
    pub network: Option<String>,
    pub status: ServiceStatus,         // Running, Stopped, Error, Starting
    pub port: Option<u16>,
    pub s3_paths: Vec<String>,
}

pub enum ServiceStatus {
    Running,
    Stopped,
    Starting,
    Stopping,
    Error(String),
}
```

**Hinweis:** Die Verbindung zu externen Services (welcher Adapter auf welchem Endpoint)
wird in `fs-registry` verwaltet — nicht im Inventory. Das Inventory kennt den
installierten Zustand, die Registry kennt den Laufzeit-Zustand.

---

## Status-Anzeige im UI

Jede installierte Ressource hat einen `ResourceStatus`. Das UI nutzt ihn:

| Status | Darstellung |
|---|---|
| `Active` / `Running` | Icon normal, grüner Punkt |
| `Stopped` | Icon ausgegraut, grauer Punkt |
| `Error(msg)` | Icon normal, roter Punkt (mit Tooltip) |
| `Updating` / `Installing` | Icon normal, blauer animierter Punkt |

**Regel:** Gestoppte Services werden ausgegraut dargestellt — nicht gelöscht,
nicht versteckt. Der Benutzer sieht dass das Paket installiert ist, aber nicht läuft.

---

## Wer liest das Inventory?

| Wer | Fragt was |
|---|---|
| **Store-App** | "Was ist installiert? Was braucht ein Update?" |
| **Desktop** | "Welche Programme sind installiert?" (für App-Launcher) |
| **Lenses** | "Welche Services bieten Daten zum Thema Y?" |
| **Container Manager** | "Welche Container-Apps sind installiert?" |
| **Widgets** | "Sind die required_capabilities erfüllt?" |
| **Theme Manager** | "Welches Theme ist aktiv?" |
| **Language Manager** | "Welche Sprache ist aktiv?" |

**Der Bus fragt die Registry, nicht das Inventory** — denn der Bus braucht
"wer läuft gerade auf welchem Endpoint", nicht "wer ist installiert".
Das ist die Aufgabe der Registry.

---

## Wer schreibt ins Inventory?

**Nur Manager.** Nach jeder erfolgreichen Aktion schreibt der Manager einen Eintrag:

| Aktion | Manager | Inventory-Effekt |
|---|---|---|
| App / Container installieren | Container Manager | `insert(InstalledResource)` + `insert(ServiceInstance)` |
| Service starten | Container Manager | `status → Running` |
| Service stoppen | Container Manager | `status → Stopped` |
| App / Container entfernen | Container Manager | `delete(InstalledResource)` + `delete(ServiceInstance)` |
| Theme installieren | Theme Manager | `insert(InstalledResource)` |
| Theme aktivieren | Theme Manager | `status → Active` (vorheriges: `Stopped`) |
| Sprache installieren | Language Manager | `insert(InstalledResource)` |
| Sprache aktivieren | Language Manager | `status → Active` |
| Status-Prüfung (periodisch) | Container Manager | `status → Running / Stopped / Error` |
| Bot-Paket installieren | Bot Manager | `insert(InstalledResource)` |

**Ein Paket ist installiert — egal wie.** Ob per CLI, UI oder API:
der Manager schreibt das Ergebnis. Das Inventory fragt nicht, wie es dort hinkam.
Kein Manager darf eine eigene parallele Liste führen.

---

## Das Inventory ist die EINZIGE Wahrheit

Wenn das Inventory sagt "Kanidm ist installiert (Version 1.5.0, Status Active)" —
dann ist das so. Kein anderes System darf seinen eigenen Install-Status verwalten.

Ob Kanidm gerade **erreichbar** ist (läuft der Prozess?) weiß die **Registry** —
die fragt den Container Manager via Health-Check und aktualisiert ihren Eintrag.
Inventory und Registry zusammen ergeben das vollständige Bild:

```
Inventory: "Kanidm 1.5.0 ist installiert"
Registry:  "Kanidm läuft auf http://kanidm:8443, Capability: iam"
           → kombiniert: "Kanidm ist installiert UND gerade aktiv"
```

---

Weiter: [Registry](registry.md) | [Store](../programme/store/README.md) | [Adapter-Pattern](adapter.md) | [Manager](manager.md)
