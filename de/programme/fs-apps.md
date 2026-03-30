# fs-apps

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-apps` · `/home/kal/Server/fs-apps/`
**Typ:** Workspace (9 App-Crates)
**Capabilities:** je App unterschiedlich (siehe unten)

---

## Was ist das?

`fs-apps` enthält alle FreeSynergy-Endnutzer-Apps als eigenständige Crates.
Jede App läuft als eigenständiges Fenster oder eingebettet in den Desktop-Shell (`fs-gui-workspace`).

---

## Apps im Workspace

| Crate             | Beschreibung                                              | Capability                 |
|-------------------|-----------------------------------------------------------|----------------------------|
| `fs-store-app`    | Paketmanager-GUI — Pakete suchen, installieren, updaten   | `store.ui`                 |
| `fs-lenses`       | Informations-Betrachter — aggregierte Cross-Service-Views | `lenses.view`              |
| `fs-theme-app`    | Theme-Manager — Farben, Fonts, Fenster-Chrome             | `theme.ui`                 |
| `fs-ai`           | KI-Assistent — lokale LLM-Chat + Modell-Verwaltung        | `ai.assistant.ui`          |
| `fs-container-app`| Container-Manager — installieren, starten, stoppen        | `container.ui`             |
| `fs-tasks`        | Task-Automation — Pipeline-Editor mit Data Offers/Accepts | `tasks.ui`, `tasks.pipeline`|
| `fs-bots`         | Bot-Manager — Bots konfigurieren, Messenger verbinden     | `bots.ui`                  |
| `fs-builder`      | Builder — Pakete analysieren, validieren, veröffentlichen | `builder.ui`               |
| `fs-managers`     | Einheitliches Manager-Panel (Sprache, Theme, Icons, Cursor)| `managers.ui`             |

---

## Architektur

```
fs-apps/crates/
├── fs-store-app/    — Paketmanager-UI
├── fs-lenses/       — Informations-Betrachter
├── fs-theme-app/    — Theme-App
├── fs-ai/           — KI-Assistent
├── fs-container-app/— Container-App
├── fs-tasks/        — Task-Automation
├── fs-bots/         — Bot-Manager
├── fs-builder/      — Build-Wizard
└── fs-managers/     — Alle Manager (Language, Theme, Icons, Cursor)
```

Jede App folgt dem **Provider Pattern**:
- Domain-Objekte mit eigener Business-Logik
- `view.rs` als einziges Bindeglied zu `fs-render` (FsView-Trait)
- Domain-Objekte importieren kein `fs-render` direkt

---

## fs-lenses — Domain-Modell

```rust
pub struct Lens {
    pub id: i64,
    pub name: String,
    pub query: String,
    pub items: Vec<LensItem>,
}

pub enum LensRole { Wiki, Chat, Git, Map, Tasks, Iam, Other(String) }

// Grupperiert Ergebnisse nach Rolle
pub fn grouped(&self) -> Vec<(LensRole, Vec<&LensItem>)>
```

---

## fs-bots — Strategy Pattern

```rust
pub trait BotStrategy {
    fn validate(&self, bot: &MessagingBot) -> Result<(), String>;
    fn apply(&self, bot: &mut MessagingBot, action: BotAction) -> Result<(), String>;
}

// BotKind gibt seine eigene Strategy zurück — kein match in Views
impl BotKind {
    pub fn strategy(&self) -> Box<dyn BotStrategy>
}
```

Konkrete Strategien: `BroadcastStrategy`, `GatekeeperStrategy`, `DefaultStrategy`

---

## fs-tasks — Pipeline-Modell

```rust
pub struct TaskPipeline {
    pub id: String,
    pub source: DataSource,    // Welcher Service liefert Daten?
    pub target: DataTarget,    // Wohin gehen die Daten?
    pub mappings: Vec<FieldMapping>,
    pub trigger: DataTrigger,  // Manual / OnEvent / Scheduled
}

pub enum FieldTransform { Direct, Template(String), Fixed(String) }
```

---

## Dependencies

| Dependency     | Zweck                                      |
|----------------|--------------------------------------------|
| `fs-libs`      | fs-types, fs-error, fs-core                |
| `fs-managers`  | Manager-Backends (Language, Theme, Icons…) |
| `fs-store`     | Katalog-Zugriff (für fs-store-app)         |
| `fs-db-desktop`| Desktop-DB-Schemas                         |
| Dioxus         | UI-Framework (Migration zu fs-render geplant — G2) |
