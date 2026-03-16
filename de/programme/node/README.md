# Node — Der Projektverwalter

[← Zurück zum Index](../../INDEX.md) | [Conductor](../conductor/README.md) | [Architektur](../../architektur/uebersicht.md)

---

## Was Node macht

Node ist das zentrale Verwaltungsprogramm für ein FreeSynergy-Projekt. Es verwaltet:

- **Hosts** — Server die zum Projekt gehören (hinzufügen, entfernen, Status)
- **Services** — Installation und Verwaltung über den [Conductor](../conductor/README.md)
- **Projekte** — Ein Projekt = eine Gruppe von Hosts + Services + Konfiguration
- **Einladungen** — Join-Tokens für neue Hosts und Desktop-Clients
- **Föderation** — Beitritt zu und Verwaltung von [Föderationen](../../konzepte/foederation.md)
- **Netzwerk** — Später: VPN-Verbindungen, öffentlich/privat Topologie

## Interfaces

| Interface | Beispiel |
|---|---|
| CLI | `fsn host add`, `fsn invite create`, `fsn project list` |
| API | `GET /api/hosts`, `POST /api/invite`, `GET /api/services` |
| UI | Über [Desktop](../desktop/README.md) (ruft API auf) |

## Invite-System

Node generiert verschlüsselte Invite-Dateien:

```toml
[invite]
token = "a1b2c3.x9y8z7w6v5u4t3s2"
ca_hash = "sha256:4f8a..."
host = "node1.example.com:9443"
network_id = "uuid-..."
created_at = "2026-03-16T12:00:00Z"
expires_at = "2026-03-17T12:00:00Z"
permissions = "full"
```

Der Empfänger gibt die Datei ein (CLI: `fsn join invite.toml`, Desktop: Datei-Upload). Der Port in der Invite-Datei kann für jede Einladung unterschiedlich sein — der Port wird nur solange geöffnet wie die Einladung gültig ist.

## Eigenständigkeit

Node läuft OHNE Desktop, OHNE Store, OHNE Internet. Es braucht nur seine eigene Konfiguration und kann lokal alles verwalten. Wenn Store verfügbar ist, nutzt es ihn. Wenn Desktop angeschlossen wird, bedient es dessen API-Anfragen.

## Repo

https://github.com/FreeSynergy/Node

## Bibliotheken

| Crate | Zweck |
|---|---|
| `fsn-types` | Shared Types |
| `fsn-config` | TOML-Konfiguration |
| `fsn-db` | SQLite (fsn-core.db) |
| `fsn-sync` | Automerge CRDT |
| `fsn-crypto` | age, mTLS, Tokens |
| `fsn-auth` | OAuth2, JWT |
| `fsn-federation` | OIDC, SCIM, ActivityPub |
| `fsn-bus` | Message Bus |
| `russh` | SSH für Remote-Host-Management |
| `clap` | CLI-Framework |
| `axum` | HTTP-API-Server |

---

Weiter: [Conductor](../conductor/README.md) | [Invite-System](../../technik/installation.md)
