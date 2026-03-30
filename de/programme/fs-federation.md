# fs-federation

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-federation` · `/home/kal/Server/fs-federation/`
**Typ:** Library-Crate (kein laufender Prozess)
**Capabilities:** `federation.gate`, `federation.activitypub`, `federation.oidc`, `federation.scim`, `federation.webfinger`

---

## Was ist das?

`fs-federation` ist die Bibliothek für dezentrale Kommunikation im FreeSynergy-Ökosystem.
Sie bündelt:

| Protokoll    | Feature-Flag   | Zweck                                             |
|--------------|----------------|---------------------------------------------------|
| ActivityPub  | `activitypub`  | Dezentrale Aktivitäts-Feeds (Mastodon-kompatibel) |
| OIDC         | `oidc`         | OpenID Connect Discovery + Userinfo               |
| SCIM 2.0     | `scim`         | User/Group-Provisioning zwischen Nodes            |
| WebFinger    | `webfinger`    | RFC 7033 Ressourcen-Lookup                        |
| WellKnown    | immer          | `.well-known/` URL-Builder + NodeInfo/HostMeta    |
| Gate         | immer          | `FederationGate`-Trait (OOP-Interface)            |

---

## Design

```
FederationGate (Trait)
    └── ActivityPubAdapter  — implementiert ActivityPub-Protokoll
```

Consumer-Code (z.B. `fs-node`) kennt **nur** den `FederationGate`-Trait —
nie die konkrete `ActivityPubAdapter`-Implementierung.

---

## FederationGate-Trait

```rust
#[async_trait]
pub trait FederationGate: Send + Sync {
    async fn invite(&self, actor: &FederationActor)  -> Result<(), FsError>;
    async fn accept(&self, actor: &FederationActor)  -> Result<(), FsError>;
    async fn follow(&self, actor: &FederationActor)  -> Result<(), FsError>;
    async fn unfollow(&self, actor: &FederationActor) -> Result<(), FsError>;
    async fn announce(&self, activity_id: &str)       -> Result<(), FsError>;
}
```

### Methoden

| Methode      | Beschreibung                                              |
|--------------|-----------------------------------------------------------|
| `invite`     | Föderations-Einladung an einen Remote-Actor senden        |
| `accept`     | Eingehende Einladung eines Remote-Actors annehmen         |
| `follow`     | Remote-Actor abonnieren (Activity-Stream)                 |
| `unfollow`   | Abo eines Remote-Actors beenden                           |
| `announce`   | Aktivität an alle Follower boosten/teilen                 |

---

## FederationActor

```rust
pub struct FederationActor {
    pub id:   String,   // ActivityPub Actor-ID URL
    pub name: String,   // Anzeigename
}
```

---

## ActivityPubAdapter

Konkrete Implementierung von `FederationGate`.
Phase G1+ — alle Methoden sind aktuell Stubs (geben `FsError::internal` zurück).

```rust
let adapter = ActivityPubAdapter::new("mynode.example.com");
let actor   = FederationActor { id: "https://remote.example.com/users/alice".into(), name: "Alice".into() };

adapter.follow(&actor).await?;
```

---

## Features

Cargo.toml-Beispiel:

```toml
[dependencies]
fs-federation = { path = "../fs-federation", features = ["oidc", "webfinger"] }
```

| Feature       | Zusätzliche Deps                          |
|---------------|-------------------------------------------|
| `oidc`        | `reqwest`, `tokio`                        |
| `scim`        | `reqwest`, `tokio`                        |
| `activitypub` | `activitypub_federation`, `url`           |
| `webfinger`   | `reqwest`, `tokio`                        |

---

## Geplante Implementierung (G1+)

| Phase | Inhalt                                      |
|-------|---------------------------------------------|
| P2    | Federation-Grundstruktur (HTTP-Signaturen)  |
| P3    | Rechte-Kaskade + Audit-Log                  |
| P4    | Föderaler Bus (Aktivitäten über fs-bus)     |
