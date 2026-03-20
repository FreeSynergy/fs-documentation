# Inventory — Die lokale Wahrheit

[← Zurück zum Index](../INDEX.md) | [Store](../programme/store/README.md) | [Bridges](bridges.md) | [Manager](manager.md)

---

## Die drei Ebenen — KERN-ARCHITEKTUR-ENTSCHEIDUNG

```
┌─────────────────────────────────────────────────────────────────┐
│  Store        = Das Mögliche   — "Was gibt es?"                 │
│  Inventory    = Der Jetzt-Zustand — "Was ist installiert?"      │
│  Managers     = Das Wie        — "Wie wird etwas installiert?"  │
└─────────────────────────────────────────────────────────────────┘
```

**Diese Trennung ist absolut. Sie darf nie vermischt werden.**

| Ebene | Frage | Datenquelle | Schreibt wer? |
|---|---|---|---|
| **Store** | "Was gibt es?" | Git-Repo, Kataloge | Builder, Maintainer |
| **Inventory** | "Was ist installiert?" | Eigene SQLite | Nur Manager |
| **Managers** | "Wie macht man das?" | Deployment-Logik | — (Logik, kein Store) |

### Was das bedeutet

- **Alles was im UI angezeigt wird, kommt NUR aus dem Inventory** — nie direkt aus dem Store.
- **Ein Paket ist installiert — egal wie.** Ob via Container Manager, Node, manuell, oder Skript: der Manager schreibt den Eintrag ins Inventory. Das Inventory fragt nicht, wie es dort hinkam.
- **Der Store zeigt was möglich ist.** Das Inventory zeigt was da ist. Beide Sichten sind unabhängig.
- **Kein Manager darf eine eigene Liste führen.** Jeder Status-Query geht ans Inventory.

---

## Store vs. Inventory

| | Store | Inventory |
|---|---|---|
| Frage | "Was gibt es?" | "Was habe ich?" |
| Datenquelle | Git-Repo, andere Stores, URLs | Nur lokale SQLite |
| Netzwerk | Ja (Git, HTTP) | Nein (nur lokal) |
| Inhalt | Katalog aller verfügbaren Ressourcen | Nur installierte Ressourcen + Status |
| Verantwortung | Validierung, Signatur-Check, Download | Lokaler Zustand, APIs, Bridges |

Der Store redet mit der Außenwelt. Das Inventory redet nur mit dem lokalen System.

---

## Inventory-Schema

```rust
pub struct Inventory {
    pub db: SqlitePool,  // fsn-inventory.db (EIGENE DB)
}
```

### Installierte Ressource (JEDER Typ)

```rust
pub struct InstalledResource {
    pub id: String,                   // "kanidm"
    pub resource_type: ResourceType,  // Container, Widget, Theme, ...
    pub version: String,              // "1.5.0"
    pub channel: ReleaseChannel,      // Stable, Testing, Nightly
    pub installed_at: DateTime,
    pub status: ResourceStatus,       // Active, Stopped, Error, Updating
    pub config_path: PathBuf,
    pub data_path: PathBuf,
    pub validation: ValidationStatus, // ✅ ⚠️ ❌
}

pub enum ResourceStatus {
    Active,
    Stopped,
    Error(String),
    Updating,
    Installing,
}
```

### Service-Instanz (für Container-Apps)

```rust
pub struct ServiceInstance {
    pub resource_id: String,          // → InstalledResource
    pub instance_name: String,        // Vom Benutzer vergeben
    pub roles_provided: Vec<Role>,
    pub roles_required: Vec<Role>,
    pub bridges: Vec<BridgeRef>,      // Welche Bridges aktiv
    pub variables: Vec<ConfiguredVar>,
    pub network: String,
    pub status: ServiceStatus,        // Running, Stopped, Error, Starting
    pub port: Option<u16>,
    pub s3_paths: Vec<String>,
}
```

### Bridge-Instanz

```rust
pub struct BridgeInstance {
    pub bridge_id: String,            // "kanidm-iam-bridge"
    pub role: Role,                   // "iam"
    pub service_instance: String,     // "main-iam"
    pub api_base_url: String,         // "http://kanidm:8443"
    pub status: BridgeStatus,
}
```

---

## Status-Anzeige im UI

Jede installierte Ressource hat einen `ResourceStatus`. Das UI nutzt ihn für die visuelle Darstellung:

| Status | Darstellung |
|---|---|
| `Active` / `Running` | Icon normal, grüner Punkt |
| `Stopped` | Icon **ausgegraut**, grauer Punkt |
| `Error(msg)` | Icon normal, **roter Punkt** |
| `Updating` / `Installing` | Icon normal, blauer/animierter Punkt |

**Regel:** Das Icon wird ausgegraut wenn der Service gestoppt ist — nicht gelöscht, nicht versteckt. Der Benutzer sieht dass das Paket installiert ist, aber gerade nicht läuft.

Der **Container Manager** ist dafür zuständig, den Status regelmäßig (via systemctl + healthcheck) zu prüfen und im Inventory zu aktualisieren. Kein anderes System fragt direkt nach dem Container-Status.

---

## Wer fragt das Inventory?

| Wer | Fragt was |
|---|---|
| **Bus** | "Wer hat Rolle X?" → Route Events zur richtigen Bridge |
| **Lenses** | "Welche Services bieten Daten zum Thema Y?" |
| **Search** | "Welche Services unterstützen search-Recht?" |
| **Container Manager** | "Welche Services laufen, welche sind gestoppt?" |
| **Widgets** | "Sind meine required_roles erfüllt?" |
| **Store** | "Was ist installiert? Was braucht ein Update?" |
| **Resource Builder** | "Welche Rollen sind lokal verfügbar für Tests?" |

---

## Das Inventory ist die EINZIGE Wahrheit

Wenn das Inventory sagt "Kanidm läuft auf Port 8443 mit Rolle iam" — dann ist das so. Kein anderes System darf eine eigene Liste führen. Der Bus fragt immer das Inventory, nie direkt die Services.

---

## Wer schreibt ins Inventory?

**Nur Manager.** Jeder Manager schreibt nach einer erfolgreichen Aktion ins Inventory:

| Aktion | Manager | Inventory-Effekt |
|---|---|---|
| Container-App installieren | Container Manager | `install()` + `add_service()` |
| Container-App starten | Container Manager | `status → Running` |
| Container-App stoppen | Container Manager | `status → Stopped` |
| Container-App entfernen | Container Manager | `uninstall()` + Service löschen |
| Theme installieren | Theme Manager | `install()` |
| Sprache installieren | Language Manager | `install()` |
| Status-Prüfung (periodisch) | Container Manager | `status → Running / Stopped / Error` |

**Ein Paket ist installiert — egal wie.** Der Manager kümmert sich ums Wie. Das Inventory kennt nur das Ergebnis. Ob die Installation über CLI, API oder UI ausgelöst wurde, ist dem Inventory egal.

---

Weiter: [Store](../programme/store/README.md) | [Bridges](bridges.md) | [Bus](bus.md) | [Manager](manager.md)
