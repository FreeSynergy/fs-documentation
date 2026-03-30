# fs-node

[← Zurück zum Index](../INDEX.md)

**Repo:** `FreeSynergy/fs-node` · `/home/kal/Server/fs-node/`
**Typ:** Program (Workspace: cli/)
**Capabilities:** `node.api`, `node.deploy`, `node.s3`, `node.dns`, `node.host`, `node.federation`

---

## Was ist das?

`fs-node` ist der Haupt-Server (Orchestrator) von FreeSynergy.
Er verwaltet Deployment, Auth-Gateway, S3, DNS, Hosts und Federation.
Kommuniziert über gRPC + REST.

---

## Workspace-Struktur

```
fs-node/cli/crates/
├── fs-node-core    — Kern-Typen, Config, Desired State
├── fs-node-server  — gRPC + REST API Server (tonic + axum)
├── fs-node-cli     — CLI-Binary (fsn)
├── fs-deploy       — Deployment-Engine (Quadlet, Reconciliation)
├── fs-dns          — DNS-Verwaltung
├── fs-host         — Host-Verwaltung
├── fs-s3           — S3-Storage (s3s + opendal)
├── fs-installer    — Install-Flows
├── fs-builder      — Package-Build + Publish
├── fs-template     — Konfigurationstemplates (Tera)
├── fs-wizard       — Wizard-Flows
└── fs-container    — Systemd Quadlet Integration
```

---

## Design

```
NodeServer (Facade)
    ├── NodeLayer (Trait)       — start / stop / name / health
    ├── DeployEngine            — Quadlet-Generierung, Reconciliation
    ├── AuthGateway             — Adapter → fs-auth Protokoll-Traits
    ├── S3Provider              — Adapter → fs-s3 (s3s + opendal)
    ├── ServiceProxy            — Adapter → fs-registry
    └── FederationGate          — Adapter → fs-federation (G1+)
```

---

## CLI (fsn)

```bash
# Node starten
fsn node serve

# Status
fsn node status

# Einladungen
fsn node invite create
fsn node invite accept <token>

# Capabilities abfragen
fsn node capabilities
```

---

## Invite-System

```
InviteToken  — fsn1.… HMAC-signierter Token
InviteBundle — age-verschlüsseltes TOML (Zugangsdaten für Neunode)
PortPool     — dedizierter Port pro Einladung
```

---

## Deployment-Engine

```
DeployEngine liest DesiredState → erzeugt Quadlet-Dateien → systemctl --user
Algorithm:
  1. Flatten alle Module-Instanzen (Sub-Module vor Parents)
  2. Schreibe .network + .container + .env Quadlet-Dateien
  3. systemctl --user daemon-reload
  4. Für jede Instanz: enable + start
  5. Health-Check warten
  6. Deployed-Version-Marker setzen
  7. Plugin generate-config für Services mit Plugin-Deklaration
```

---

## API

| Endpunkt                   | Methode | Beschreibung                      |
|----------------------------|---------|-----------------------------------|
| `GET /status`              | REST    | Node-Status                       |
| `GET /capabilities`        | REST    | Registrierte Capabilities         |
| `POST /invite`             | REST    | Einladung erstellen               |
| `POST /invite/accept`      | REST    | Einladung annehmen                |
| gRPC `node.NodeService`    | gRPC    | Status, Layers, Invite, Deploy    |
