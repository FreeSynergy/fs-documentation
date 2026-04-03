# fs-managers

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-managers` · `/home/kal/Server/fs-managers/`
**Typ:** Workspace (10 Manager-Crates)
**Capabilities:** `managers.language`, `managers.theme`, `managers.icons`, `managers.cursor`, `managers.ai`, `managers.bots`, `managers.container`, `managers.auth`, `managers.zentinel`, `managers.mail`

---

## Was ist das?

`fs-managers` enthält die Backend-Crates für alle FreeSynergy-Manager.
Jeder Manager ist eine eigenständige Library mit CLI-Binaries, die von `fs-apps` (UI-Crates) genutzt werden.

---

## Manager im Workspace

| Crate                    | Capability           | Beschreibung                                              |
|--------------------------|----------------------|-----------------------------------------------------------|
| `fs-manager-language`    | `managers.language`  | Sprachpakete installieren, aktivieren, herunterladen      |
| `fs-manager-theme`       | `managers.theme`     | Themes laden, aktivieren, als Artifact nachladen          |
| `fs-manager-icons`       | `managers.icons`     | Icon-Sets verwalten, nach Theme filtern                   |
| `fs-manager-cursor`      | `managers.cursor`    | Mauszeiger-Sets verwalten                                 |
| `fs-manager-ai`          | `managers.ai`        | LLM-Modelle verwalten (Download, Aktivierung)             |
| `fs-manager-bots`        | `managers.bots`      | Bot-Instanzen konfigurieren                               |
| `fs-manager-container`   | `managers.container` | Container-Apps konfigurieren                              |
| `fs-manager-auth`        | `managers.auth`      | Kanidm-Setup-Wizard + OIDC-Client-Verwaltung              |
| `fs-manager-zentinel`    | `managers.zentinel`  | Zentinel-Routen-Verwaltung (Facade + Auto-Routing via Bus)|
| `fs-manager-mail`        | `managers.mail`      | Stalwart-Setup-Wizard + Domain-Konfiguration              |

---

## Workspace-Struktur

```
fs-managers/
├── language/    — Sprachpack-Manager (fs-manager-language)
├── theme/       — Theme-Manager
├── icons/       — Icon-Set-Manager
├── cursor/      — Cursor-Manager
├── ai/          — AI-Modell-Manager
├── bots/        — Bot-Konfigurations-Manager
├── container/   — Container-App-Manager
├── auth/        — Kanidm-Setup-Wizard (State Machine)
├── zentinel/    — Zentinel-Routen-Facade (ZentinelManager + BusHandler)
└── mail/        — Stalwart-Setup-Wizard (State Machine)
```

---

## fs-manager-language — Domain-Modell

```rust
pub struct Language {
    pub id: String,           // ISO 639-1 Code ("de", "en")
    pub display_name: String, // Nativer Name ("Deutsch")
    pub locale: String,       // BCP-47 Locale ("de-DE")
}

pub enum DateFormat { DmY, MdY, Ymd }   // DD.MM.YYYY / MM/DD/YYYY / YYYY-MM-DD
pub enum TimeFormat { H24, H12 }         // 24h / 12h
pub enum NumberFormat { EuropeDot, UsComma, SpaceComma }
```

---

## G5 — ManagerLayout-Trait (✅ 2026-04-01)

Jeder Manager hat eine `view.rs` als einziges Bindeglied zu `fs-render`:

| Crate                  | Sektionen                                          |
|------------------------|----------------------------------------------------|
| `fs-manager-language`  | list / active / download / preview (4 Module)      |
| `fs-manager-cursor`    | list / active / preview (3 Module)                 |
| `fs-manager-theme`     | list / active (in view.rs)                         |
| `fs-manager-icons`     | list / active (in view.rs)                         |
| `fs-manager-container` | list / active (running) (in view.rs)               |

Trait-Signatur (in `fs-render/src/manager.rs`):
```
ManagerLayout::title()         → &'static str
ManagerLayout::sidebar_items() → Vec<ManagerSidebarItem>
ManagerLayout::content_for()   → Box<dyn FsWidget>
```

FTL-Keys für alle Sektionen in `fs-i18n/locales/{en,de}/managers.ftl`.

---

## H8 — bot-db aufgeteilt (✅ 2026-04-01)

`bot-db/src/lib.rs` (735 Zeilen) → 9 Domain-Module:
`audit` / `poll` / `room` / `subscription` / `collection` / `join` / `child` / `meta` / `sync`

---

## Bekannter Bug

`fs-manager-language`: Nutzt alte gix-API (pre-gix 0.65).
`prepare_push` und `SignatureRef` müssen auf neue gix-API migriert werden.
Betrifft: `language/src/git.rs`

---

## Dependencies

| Dependency    | Zweck                                         |
|---------------|-----------------------------------------------|
| `fs-i18n`     | Sprachmetadaten, FTL-Strings                  |
| `gix`         | Git-Operationen (Language-Packs pushen)        |
| `fs-db`       | DbEngine-Trait (Spracheinstellungen speichern) |
