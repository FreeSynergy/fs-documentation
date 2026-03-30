# fs-sync

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-sync` · `/home/kal/Server/fs-sync/`
**Typ:** Library-Crate (kein laufender Prozess)
**Capabilities:** `sync.crdt`, `sync.websocket`

---

## Was ist das?

`fs-sync` ist die CRDT-Sync-Infrastruktur für FreeSynergy.
Sie wrapp [Automerge](https://automerge.org/) für konfliktfreies verteiltes State-Sync zwischen Nodes.

---

## Design

```
SyncDoc<T>     — CRDT-Dokument für einen serialisierbaren Wert
SyncPeer       — Sync-Zustand mit einem Remote-Peer
SyncEngine     — Factory + Koordinator für Docs und Peers
AuditEntry     — Änderungsprotokoll (Actor, Zeitstempel, Beschreibung)
WsTransport    — WebSocket-Transport für Automerge-Nachrichten (Feature `ws`)
SyncSession<T> — Live-Sync über einen WsTransport (Feature `ws`)
```

**Pattern:** Facade (`SyncDoc` versteckt Automerge-Komplexität), Strategy (`SyncPeer` per Remote-Peer)

---

## SyncDoc<T>

Hält einen beliebigen serialisierbaren Wert in einem Automerge-Dokument.
Alle Änderungen erzeugen Automerge-Commits — Merges sind immer konfliktfrei.

```rust
let mut doc: SyncDoc<Config> = SyncDoc::with_value("node-a".into(), &config)?;

// Wert lesen
let current: Config = doc.get()?;

// Wert updaten
doc.set(&updated_config)?;

// Dokument speichern / laden
let bytes = doc.save();
let loaded: SyncDoc<Config> = SyncDoc::load("node-a".into(), &bytes)?;
```

---

## SyncPeer + Sync-Protokoll

Jeder Remote-Peer braucht einen eigenen `SyncPeer`.
Nachrichten sind binary-encoded Automerge-Sync-Frames.

```rust
let mut peer_b = SyncPeer::new("node-b");

// Nachricht generieren (None wenn nichts Neues)
if let Some(msg) = doc.generate_sync_message(&mut peer_b) {
    send_to_node_b(msg).await?;
}

// Nachricht empfangen und anwenden
doc.receive_sync_message(&mut peer_b, &received_bytes)?;
```

---

## SyncEngine (Factory)

```rust
let engine = SyncEngine::new("node-a".into());
let doc: SyncDoc<MyState>  = engine.new_doc();
let peer: SyncPeer         = engine.new_peer("node-b");
```

---

## WsTransport + SyncSession (Feature `ws`)

Verbindet einen `SyncDoc` mit einem WebSocket-Peer für Live-Sync.

```rust
let transport = WsTransport::connect("ws://peer.example.com/sync").await?;
let mut session = SyncSession::new(doc, peer, transport);

// Sync bis Konvergenz
session.run_until_synced().await?;

// Resultat auslesen
let merged: MyState = session.into_doc().get()?;
```

### Einzelne Operationen

```rust
session.push().await?;  // lokal → remote
session.pull().await?;  // remote → lokal
```

---

## AuditEntry

```rust
let entry = AuditEntry::now(
    "node-a".into(),
    "settings-doc",
    "Updated theme to dark",
);
```

| Feld           | Typ    | Beschreibung                    |
|----------------|--------|---------------------------------|
| `actor`        | String | Node/User der Änderung          |
| `timestamp_ms` | u64    | Unix-Zeitstempel in Millisekunden|
| `doc_id`       | String | Dokument-Identifier             |
| `description`  | String | Menschenlesbare Beschreibung    |

---

## Cargo.toml

```toml
[dependencies]
fs-sync = { path = "../fs-sync" }

# Mit WebSocket-Transport:
fs-sync = { path = "../fs-sync", features = ["ws"] }
```
