# Bridges — Standardisierte Rollen-APIs

[← Zurück zum Index](../INDEX.md) | [Rollen](rollen.md) | [Bus](bus.md)

---

## Was Bridges sind

Bridges machen Services **austauschbar**. Jede Rolle hat eine standardisierte API. Jede Container-App braucht eine Bridge die diese Standard-API auf die echte Service-API mappt.

```
Standard-API (identisch für alle):     Bridge übersetzt:          Echte API:
  iam.user.create(name, email)    →    POST /v1/person {...}     (Kanidm)
  iam.user.create(name, email)    →    POST /admin/users {...}   (KeyCloak)
  iam.user.create(name, email)    →    POST /api/v1/users {...}  (Authentik)
```

Der Bus, Lenses, Search — alles redet nur die Standard-API. Die Bridge übersetzt.

---

## Rollen-API-Definitionen

### Rolle: iam

```
user.create(name: String, email: Email) → UserId
user.get(id: UserId) → User
user.find(query: String) → [User]
user.update(id: UserId, fields: Map) → bool
user.delete(id: UserId) → bool
user.list(limit: u32, offset: u32) → [User]

group.create(name: String) → GroupId
group.get(id: GroupId) → Group
group.list() → [Group]
group.add_user(group_id: GroupId, user_id: UserId) → bool
group.remove_user(group_id: GroupId, user_id: UserId) → bool
group.members(group_id: GroupId) → [User]

auth.token_exchange(code: String) → Token
auth.validate_token(token: String) → TokenInfo
auth.revoke_token(token: String) → bool
```

### Rolle: wiki

```
page.create(title: String, body: Markdown, collection: String?) → PageId
page.get(id: PageId) → Page
page.update(id: PageId, body: Markdown) → bool
page.delete(id: PageId) → bool
page.search(query: String) → [PageResult]
page.list(collection: String?) → [Page]

collection.create(name: String) → CollectionId
collection.list() → [Collection]
```

### Rolle: git

```
repo.create(name: String, description: String?) → RepoId
repo.get(id: RepoId) → Repo
repo.list() → [Repo]
repo.delete(id: RepoId) → bool

commit.list(repo_id: RepoId, limit: u32) → [Commit]
commit.get(repo_id: RepoId, hash: String) → Commit
branch.list(repo_id: RepoId) → [Branch]
```

### Rolle: chat

```
room.create(name: String) → RoomId
room.get(id: RoomId) → Room
room.list() → [Room]

message.send(room_id: RoomId, text: String) → MessageId
message.list(room_id: RoomId, limit: u32) → [Message]
message.search(query: String) → [Message]
```

### Rolle: database

```
status() → DatabaseStatus
backup.create() → BackupId
backup.list() → [Backup]
backup.restore(id: BackupId) → bool
```

### Rolle: cache

```
status() → CacheStatus
slot.list() → [SlotInfo]
slot.assign(slot: u8, service_id: String) → bool
slot.info(slot: u8) → SlotInfo
flush(slot: u8?) → bool
```

Cache hat 16 Slots (0-15). Jeder Service bekommt einen Slot. Der Cache regelt intern welcher Slot wem gehört (Zähler im Cache-Objekt). Wenn voll, dann voll.

### Rolle: smtp

```
send(to: Email, subject: String, body: String) → bool
status() → SmtpStatus
```

### Rolle: llm

```
chat(prompt: String, model: String?) → Response
models() → [Model]
pull(model_name: String) → bool
status() → LlmStatus
```

### Rolle: map

```
point.create(lat: f64, lon: f64, name: String, description: String?) → PointId
point.list(bounds: BoundingBox?) → [Point]
layer.list() → [Layer]
layer.create(name: String, geojson: String) → LayerId
```

### Rolle: tasks

```
task.create(title: String, description: String?, project: String?) → TaskId
task.get(id: TaskId) → Task
task.list(filter: TaskFilter?) → [Task]
task.update(id: TaskId, fields: Map) → bool
task.complete(id: TaskId) → bool
```

### Rolle: monitoring

```
logs(service: String?, limit: u32) → [LogEntry]
metrics(service: String?) → Metrics
alerts.list() → [Alert]
alerts.acknowledge(id: AlertId) → bool
```

---

## Bridge als Ressource

```toml
[package]
id = "kanidm-iam-bridge"
name = "Kanidm IAM Bridge"
type = "bridge"
tags = ["kanidm", "iam", "oidc", "bridge"]

[bridge]
target_role = "iam"
target_service = "kanidm"

[[bridge.methods]]
standard = "user.create"
http_method = "POST"
endpoint = "/v1/person"
request_mapping = { name = "attrs.name[0]", email = "attrs.mail[0]" }
response_mapping = { id = "uuid" }

[[bridge.methods]]
standard = "user.find"
http_method = "GET"
endpoint = "/v1/person?name={query}"
response_mapping = { id = "uuid", name = "attrs.name[0]", email = "attrs.mail[0]" }
```

---

## Zusammenspiel: Inventory + Bus + Bridge

```
Lens fragt: "Alle Users der Gruppe Köln"
  → Bus fragt Inventory: "Wer hat Rolle iam?"
    → Inventory: "Kanidm, Instanz main-iam, Bridge: kanidm-iam-bridge"
      → Bus ruft Bridge: iam.group.list() → findet "Köln"
        → Bus ruft Bridge: iam.group.members("Köln") → User-Liste
```

**Inventory** weiß WER was kann. **Bus** weiß WIE man dahin kommt. **Bridge** weiß WIE man übersetzt.

---

Weiter: [Rollen](rollen.md) | [Bus](bus.md) | [Inventory](inventory.md)
