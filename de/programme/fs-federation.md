# fs-federation

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-federation` · `/home/kal/Server/fs-federation/`
**Typ:** Library-Crate (kein laufender Prozess)
**Capabilities:** `federation.gate`, `federation.activitypub`, `federation.oidc`, `federation.scim`, `federation.webfinger`

---

## Was ist das?

`fs-federation` ist die Bibliothek für dezentrale Kommunikation im FreeSynergy-Ökosystem.
Sie bündelt:

| Modul         | Feature-Flag   | Zweck                                              |
|---------------|----------------|----------------------------------------------------|
| `gate`        | immer          | `FederationGate`-Trait — OOP-Interface für alle AP-Ops |
| `rights`      | immer          | Rechte-Kaskade (Chain-of-Responsibility)           |
| `audit`       | immer          | Audit-Log Decorator über jeden Gate-Aufruf         |
| `bus`         | immer          | Bus-Events + Topic-Konstanten für `fs-bus`         |
| `well_known`  | immer          | `.well-known/` URL-Builder + NodeInfo/HostMeta     |
| `activitypub` | `activitypub`  | AP-Typen + `activitypub_federation` Re-Exporte     |
| `oidc`        | `oidc`         | OpenID Connect Discovery + Userinfo                |
| `scim`        | `scim`         | User/Group-Provisioning zwischen Nodes             |
| `webfinger`   | `webfinger`    | RFC 7033 Ressourcen-Lookup                         |

---

## Design

```
FederationGate (Trait)
    └── ActivityPubAdapter  — implementiert ActivityPub-Protokoll
            ↑ gewrappt von
    AuditingFederationGate  — Decorator: loggt jeden Aufruf

RightsCascade (Trait)       — Chain-of-Responsibility: Allow / Deny / Abstain
    └── InMemoryRights      — in-memory Impl; nicht persistent

FederationAuditLog (Trait)  — Append-only Audit-Store
    └── InMemoryAuditLog    — Bounded Ring Buffer (Capacity konfigurierbar)

FederationEvent             — Bus-Event Envelope für fs-bus
    └── FederationPayload   — getypte Payload-Varianten (7 Stück)
```

Consumer-Code (z.B. `fs-node`) kennt **nur** die Traits —
nie die konkreten Implementierungen.

---

## Rechte-Kaskade (`rights`)

```rust
let rights = InMemoryRights::new();
rights.grant("mastodon.social", FederationRight::Follow);
rights.deny("bad.actor", FederationRight::Follow);

match rights.check("mastodon.social", FederationRight::Follow) {
    RightsDecision::Allow   => { /* erlaubt */ }
    RightsDecision::Deny    => { /* verweigert */ }
    RightsDecision::Abstain => { /* kein Eintrag → Standard des Callers */ }
}
```

### `FederationRight`-Varianten

| Recht          | Bedeutung                                       |
|----------------|-------------------------------------------------|
| `Follow`       | Remote-Actors dürfen lokalen Actors folgen      |
| `Deliver`      | Remote-Actors dürfen Activities einliefern      |
| `FollowBack`   | Lokale Actors dürfen Remote-Actors folgen       |
| `DeliverTo`    | Lokale Actors dürfen zu Remote-Inboxes liefern  |
| `Invite`       | Remote-Domain darf uns einladen                 |
| `InviteOut`    | Wir dürfen die Remote-Domain einladen           |

---

## Audit-Log (`audit`)

```rust
let log = InMemoryAuditLog::new(1000); // max 1000 Einträge
let gate = AuditingFederationGate::new(ActivityPubAdapter::new("example.com"), log);

// Jeder Aufruf wird automatisch geloggt:
gate.follow(&actor).await?;

// Einträge abfragen:
let recent = gate.audit_log().recent(10);        // neueste 10
let domain = gate.audit_log().for_domain("mastodon.social");
```

---

## Bus-Events (`bus`)

```rust
use fs_federation::bus::{topics, FederationEvent, FederationPayload};

let event = FederationEvent::new(
    topics::FEDERATION_ACTOR_FOLLOWED,
    FederationPayload::ActorFollowed { actor: actor.clone() },
);
// → auf fs-bus publishen
```

### Bus-Topics (auch in `fs-bus/src/topics.rs`)

| Topic                             | Auslöser                         |
|-----------------------------------|----------------------------------|
| `federation::invite::sent`        | Einladung gesendet               |
| `federation::invite::accepted`    | Einladung angenommen             |
| `federation::actor::followed`     | Remote-Actor folgt               |
| `federation::actor::unfollowed`   | Entfolgen                        |
| `federation::activity::announced` | Aktivität geteilt                |
| `federation::rights::updated`     | Rechte geändert                  |
| `federation::domain::blocked`     | Domain gesperrt                  |

---

## FederationGate-Trait

```rust
#[async_trait]
pub trait FederationGate: Send + Sync {
    async fn invite(&self, actor: &FederationActor)   -> Result<(), FsError>;
    async fn accept(&self, actor: &FederationActor)   -> Result<(), FsError>;
    async fn follow(&self, actor: &FederationActor)   -> Result<(), FsError>;
    async fn unfollow(&self, actor: &FederationActor) -> Result<(), FsError>;
    async fn announce(&self, activity_id: &str)        -> Result<(), FsError>;
}
```

---

## Features

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

## i18n

FTL-Keys in `fs-i18n/locales/{lang}/federation.ftl`:
- `federation-title`, `-status-*`, `-action-*`, `-right-*`
- `federation-audit-*` (Protokoll-Beschriftungen)
- `federation-error-*` (Fehlermeldungen)
