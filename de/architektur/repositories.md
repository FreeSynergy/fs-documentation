# Repository-Übersicht

[← Zurück zum Index](../INDEX.md) | [Gesamtübersicht](uebersicht.md)

---

## Prinzip

FreeSynergy ist kein klassisches Programm — es ist ein Betriebssystem-artiges Platform. Deshalb sind die Komponenten nach **Verantwortlichkeit** getrennt, nicht nach technischen Schichten.

**Grundregel:** Ein Repository = eine klare Antwort auf eine klare Frage.

---

## System-Schicht (Reihenfolge beim Start)

```
fs-init
  └─ lädt fs-store → Store installiert den Rest
       ├─ fs-bus         (Kommunikation)
       ├─ fs-config      (Konfiguration lesen/schreiben)
       ├─ fs-registry    (Welche Dienste laufen gerade?)
       ├─ fs-auth        (kanidm-Fork: Authentifizierung)
       │    └─ fs-session (Wer ist eingeloggt + offene Programme)
       └─ fs-inventory   (Was ist installiert auf diesem Node?)
```

### fs-init
**Frage:** "Was muss beim Start passieren?"
- Bootet das System
- Lädt **nur** den Store — nichts weiter
- Repository: `FreeSynergy/fs-init`

### fs-bus
**Frage:** "Wie kommunizieren Programme miteinander?"
- Async Event-Bus mit Topic-Routing
- Pub/Sub: Programme abonnieren Topics, keine direkte Kopplung
- Kein Daemon nötig — Library, die in jeden Prozess eingebettet wird
- Repository: Teil von `FreeSynergy/fs-libs` (Crate: `fs-bus`)

### fs-config
**Frage:** "Wie liest und schreibt ein Programm seine Konfiguration?"
- TOML-Loader mit Validierung, Schema und Auto-Repair
- Kein Daemon — Live-Updates laufen über Bus-Events (`config::changed::*`)
- Repository: Teil von `FreeSynergy/fs-libs` (Crate: `fs-config`)

### fs-registry
**Frage:** "Welche Dienste und Capabilities laufen gerade auf diesem Node?"
- Dienste registrieren sich beim Start (`iam`, `mail`, `storage`, ...)
- Der Bus fragt die Registry wenn er weiß welche Capability er braucht
- Ersetzt das alte Bridge-Konzept — kein dynamischer Bridge-Executor mehr
- Repository: `FreeSynergy/fs-registry`

### fs-session
**Frage:** "Wer ist eingeloggt und welche Programme sind offen?"
- Speichert aktiven User + Liste der offenen Programme mit Window-State
- Löst das Minimize-Problem: minimiertes Programm ist `Minimized`, nicht weg
- Beim Restore: bestehender Eintrag wird aufgemacht, kein neues Fenster
- Repository: `FreeSynergy/fs-session`

### fs-inventory
**Frage:** "Was ist auf diesem Node installiert?"
- SQLite-Datenbank: installierte Ressourcen + laufende Service-Instanzen
- Einzige Wahrheitsquelle — kein anderes Programm darf eine eigene Liste führen
- Repository: `FreeSynergy/fs-inventory` (eigenständig, nicht in fs-libs)

---

## Libraries (fs-libs Monorepo)

`FreeSynergy/fs-libs` ist ein Cargo-Workspace mit allen gemeinsamen Crates.
Hier landen Sachen die **mehrere Programme gemeinsam brauchen**, aber kein
eigenes Deployment brauchen.

### Core
| Crate | Frage |
|---|---|
| `fs-types` | Welche Basis-Typen teilen alle? (ResourceType, Role, SemVer, ...) |
| `fs-error` | Wie behandeln wir Fehler? (Repairable, Validation) |
| `fs-config` | Wie liest ein Programm seine Config? (TOML, Schema, Auto-Repair) |
| `fs-crypto` | Wie verschlüsseln wir? (age, mTLS, JWT, Signing) |
| `fs-health` | Wie prüft ein Programm ob es gesund ist? |
| `fs-db` | Wie reden wir mit SQLite/Postgres? (SeaORM-Abstraktion) |
| `fs-bus` | Wie kommunizieren Programme? (Event-Bus, Topic-Routing) |
| `fs-sync` | Wie synchronisieren wir CRDT-Daten? (Automerge) |
| `fs-template` | Wie rendern wir Templates? (Tera-Wrapper) |
| `fs-sysinfo` | Was weiß das System über sich selbst? |

### UI
| Crate | Frage |
|---|---|
| `fs-theme` | Wie sieht das System aus? (theme.toml → CSS-Variablen) |
| `fs-help` | Wie zeigen wir kontextsensitive Hilfe? |
| `fs-i18n` | Wie übersetzen wir? (Fluent-Bundles) |
| `fs-render` | Wie abstrahieren wir den Renderer? (ViewRenderer-Trait) |
| `fs-components` | Welche UI-Komponenten gibt es? (Dioxus-Primitives) |
| `fs-ui` | Wie bauen wir UIs? (Komponenten-Sammlung) |

### Extension
| Crate | Frage |
|---|---|
| `fs-pkg` | Wie installiert man Pakete? (OCI, Hooks, Lifecycle) |
| `fs-plugin-sdk` | Wie schreibt man ein Plugin? (WASM, Traits) |
| `fs-plugin-runtime` | Wie läuft ein Plugin? (WASM-Host) |
| `fs-container` | Wie verwaltet man Container? (Podman Quadlet) |

### Network
| Crate | Frage |
|---|---|
| `fs-auth` | Wie prüfen wir Rechte? (JWT, RBAC, OAuth2) |
| `fs-federation` | Wie föderieren wir? (OIDC, SCIM, ActivityPub) |
| `fs-channel` | Wie senden wir Nachrichten? (Matrix, Telegram) |
| `fs-llm` | Wie reden wir mit LLMs? (Ollama, Claude, OpenAI-kompatibel) |
| `fs-bot` | Wie bauen wir Bots? (Command-Framework, Registry) |

**Was NICHT in fs-libs gehört:**
- Dinge mit eigenem Deployment-Lifecycle → eigenes Repo
- Dinge die andere Repos nicht brauchen → im jeweiligen Repo
- Domain-Objekte die nur ein Programm kennt → im Programm-Repo

---

## Programme (Deployable)

### fs-store
**Frage:** "Wo findet man und installiert man Pakete?"
- Katalog-Leser, Package-Typen, Store-Inventory (Catalog-Sicht)
- Binary `fs-store`: erkennt automatisch Display → GUI oder Fehlermeldung
- Repository: `FreeSynergy/fs-store`
- Crates: `fs-store` (Library), `fs-store-app` (Binary: `fs-store`), `fs-store-cli`

### fs-node
**Frage:** "Wie verwaltet man ein Projekt?"
- Projekt-Verwaltung, S3-Server, Node-API
- Repository: `FreeSynergy/fs-node`

### fs-desktop
**Frage:** "Wie sieht der Benutzer das System?"
- GUI-Shell, Fenster-Management, Desktop-Umgebung
- Repository: `FreeSynergy/fs-desktop`

### fs-apps (Monorepo)
**Frage:** "Welche Anwendungen gibt es?"
- 10 Apps: Store-App, Browser, Lenses, Theme, Builder, Tasks, Bots, AI, Container, Managers
- Repository: `FreeSynergy/fs-apps`

---

## Adapter-Pattern (ersetzt Bridge)

Es gibt **keine** Bridge-Library mehr. Stattdessen:

```rust
// Adapter um kanidm — implementiert unseren Standard-Trait
struct KanidmAdapter;
impl AuthService for KanidmAdapter { ... }

// Adapter um Stalwart — implementiert unseren Standard-Trait
struct StalwartAdapter;
impl MailService for StalwartAdapter { ... }
```

Der Bus routet zu wer auch immer den passenden Trait implementiert und in der
Registry registriert ist. Kein dynamischer Executor, keine Bridge-Schicht.

Vorteile:
- Typ-sicher (Compiler prüft den Kontrakt)
- Testbar (Mock-Adapter für Tests)
- Einfach (kein generischer Dispatcher)

---

## Drittanbieter-Forks

| Was | Lokal | Original |
|---|---|---|
| Identity/IAM | `fs-kanidm` | `kanidm/kanidm` |
| Matrix-Server | `fs-tuwunel` | `matrix-construct/tuwunel` |
| Reverse Proxy | `fs-zentinel` | `zentinelproxy/zentinel` |
| Mail-Server | `fs-stalwart` | `stalwartlabs/stalwart` |
| LLM-Inferenz | `fs-mistral` | `EricLBuehler/mistral.rs` |

Forks bekommen Patches via Adapter (kein Fork-Merge-Chaos).

---

## Automatisches Store-Publishing

Wenn ein Service-Repo bereit ist:

```
git tag v1.0.0 && git push --tags
  → GitHub Actions baut das Binary
  → Erstellt Package-Manifest
  → Öffnet PR in FreeSynergy/Store
  → Nach Merge: im Store verfügbar
```

Details: [Store-Konzept](../programme/store/README.md)
