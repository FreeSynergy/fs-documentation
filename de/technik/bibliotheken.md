# Bibliotheken

[← Zurück zum Index](../INDEX.md)

---

## fsn-* Crates (FreeSynergy/Lib)

Alle wiederverwendbaren Libraries. Können auch von Drittprojekten (Wiki.rs, Decidim.rs) genutzt werden.

| Crate | Zweck | Wichtige Dependencies |
|---|---|---|
| `fsn-types` | Shared Types, Enums, IDs | `serde`, `uuid` |
| `fsn-error` | Fehlerbehandlung, Error-Typen | `thiserror`, `miette` |
| `fsn-config` | TOML laden/speichern | `serde`, `toml` |
| `fsn-i18n` | Sprach-Snippets, Fluent | `fluent`, `fluent-bundle`, `unic-langid` |
| `fsn-db` | SQLite-Abstraktion | `sea-orm`, `rusqlite`, `sqlx` |
| `fsn-sync` | CRDT-Synchronisation | `automerge` |
| `fsn-store` | Store-Client | `reqwest`, `toml` |
| `fsn-pkg` | Paket-Management, OCI | `oci-distribution` |
| `fsn-plugin-sdk` | Plugin-API für WASM | `wit-bindgen` |
| `fsn-plugin-runtime` | WASM-Host | `wasmtime` |
| `fsn-federation` | OIDC, SCIM, ActivityPub | `activitypub_federation`, `openidconnect` |
| `fsn-auth` | OAuth2, JWT, Tokens | `oauth2`, `jsonwebtoken` |
| `fsn-bus` | Message Bus | `tokio::broadcast`, `serde_json` |
| `fsn-channel` | Messenger-Adapter | Feature-flagged (siehe unten) |
| `fsn-bot` | Bot-Framework | `fsn-bus`, `fsn-channel` |
| `fsn-llm` | LLM-Integration | `reqwest` (Ollama API) |
| `fsn-bridge-sdk` | Service-zu-Service-Bridges | `fsn-bus` |
| `fsn-container` | Quadlet/systemctl-Interface | `tokio::process` |
| `fsn-template` | Tera-Templates | `tera` |
| `fsn-health` | Health-Checks | `reqwest`, `tokio` |
| `fsn-crypto` | age-Encryption, mTLS | `age`, `rcgen`, `ed25519-dalek` |
| `fsn-theme` | Theme-Laden, Prefix-System | `toml`, `fsn-config` |
| `fsn-help` | Hilfe-System | `fsn-i18n` |
| `fsn-ui` | Dioxus-Komponenten | `dioxus`, `fsn-theme` |

## Externe Dependencies

| Crate | Wofür | Benutzt von |
|---|---|---|
| `dioxus` 0.7.x | UI-Framework | Desktop |
| `axum` | HTTP-Server/API | Node, Conductor |
| `clap` | CLI | Alle Programme |
| `serde` / `serde_json` / `toml` | Serialisierung | Alle |
| `tokio` | Async Runtime | Alle |
| `reqwest` | HTTP-Client | Store, Desktop, LLM |
| `sea-orm` | ORM für SQLite/Postgres | Alle mit DB |
| `tera` | Template-Engine | Conductor, Templates |
| `fluent` | i18n Localization | i18n |
| `automerge` | CRDT | Sync, Offline-First |
| `teloxide` | Telegram Bot | Channel (feature: telegram) |
| `matrix-sdk` | Matrix Client | Channel (feature: matrix) |
| `serenity` + `poise` | Discord Bot | Channel (feature: discord) |
| `slack-morphism` | Slack Client | Channel (feature: slack) |
| `lettre` | Email senden | Channel (feature: email) |
| `russh` | SSH-Client | Node (Host-Management) |
| `age` | Encryption | Crypto |
| `wasmtime` | WASM-Runtime | Plugin-Runtime |
| `serde_yaml` | YAML parsen | Conductor |

## Feature-Flags bei fsn-channel

```toml
[features]
default = []
telegram = ["teloxide"]
matrix = ["matrix-sdk"]
discord = ["serenity", "poise"]
slack = ["slack-morphism"]
email = ["lettre"]
xmpp = ["xmpp-rs"]
irc = ["irc"]
```

---

Weiter: [Datenspeicherung](datenspeicherung.md) | [i18n](i18n.md)
