# Proxmox VE - API Documentation

## Overview

The Proxmox REST API is the complete, official interface of the platform: every button in the web interface corresponds to an API call. The base is `https://<host>:8006/api2/json` (JSON output; `/api2/exttype` provides format-specific output). Authentication is optionally done with **login ticket + CSRF token** (interactive) or an **API token** (for scripts, recommended). Long actions are asynchronous and return a task ID (UPID).

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| REST `/api2/json` | entire administration scope | official, stably documented (pve-api-docs) |
| `pvesh` CLI | REST calls directly on the node | official |
| `qm` / `pct` / `pvesm` / `pveum` | domain commands | official |
| Webhooks | — | ❌ Not available |

## Authentication

### Ticket login (browser/script simulation)

```bash
curl -sk -X POST https://pve1:8006/api2/json/access/ticket \
  -d 'username=root@pam' -d 'password=SECRET'
```

Response (shortened):

```json
{ "data": {
    "ticket": "PVE:... uzun",
    "CSRFPreventionToken": "3A2B...",
    "username": "root@pam"
} }
```

Subsequent requests send the ticket as `Cookie: PVEAuthCookie=<ticket>` (alternatively `Authorization: PVEAuthCookie=<ticket>`).
- For **every non-GET request** additionally `X-CSRF-Prevention-Token: <token>`.
- Tickets expire after a few hours — use API tokens for automation.

### API token (recommended)

Create in the UI (Datacenter → Permissions → API Tokens) or via CLI:

```bash
pveum user token add automation@pve ci-token --privsep 0
```

Every request carries:

```
Authorization: PVEAPIToken=automation@pve!ci-token:<uuid-secret>
```

- Token rights can be restricted via roles/ACL, optionally node binding and expiry date.
- The secret is **only visible at creation**; if lost, create a new token.

### Realms

`pam` (Linux user of the node), `pve` (own store), `ldap`, `ldap2`, `ad`, `keycloak`/OIDC (version-dependent). Tokens exist per user, independent of the realm.

## Endpoints (selection)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api2/json/version` | version information of the API |
| `GET` | `/cluster/status` | nodes, quorum, cluster name |
| `GET` | `/cluster/resources?type=vm` | all VMs/containers (inventory) |
| `GET` | `/nodes` | nodes with status |
| `GET` | `/nodes/{node}/qemu` | VMs of the node |
| `POST` | `/nodes/{node}/qemu` | create VM (parameters as JSON) |
| `GET` | `/nodes/{node}/qemu/{vmid}/config` | VM configuration |
| `SET/PUT` | `/nodes/{node}/qemu/{vmid}/config` | change VM setting |
| `POST` | `/nodes/{node}/qemu/{vmid}/status/start` | start VM |
| `POST` | `/nodes/{node}/qemu/{vmid}/status/shutdown` | shut down VM |
| `POST` | `/nodes/{node}/qemu/{vmid}/status/stop` | emergency stop |
| `POST` | `/nodes/{node}/qemu/{vmid}/migrate` | (live) migration |
| `GET` | `/nodes/{node}/qemu/{vmid}/snapshots` | list snapshots |
| `POST` | `/nodes/{node}/qemu/{vmid}/snapshot` | create snapshot |
| `GET` | `/nodes/{node}/lxc` | containers of the node |
| `POST` | `/nodes/{node}/lxc/{ctid}/status/start` | start container |
| `GET` | `/nodes/{node}/storage` | storage status of the node |
| `GET` | `/storage` | storage pools (API version 8.x) |
| `GET` | `/cluster/backup` | backup jobs |
| `POST` | `/nodes/{node}/vzdump` | trigger backup of a VM |
| `GET` | `/cluster/tasks` | task history (UPIDs) |
| `GET` | `/nodes/{node}/tasks/{upid}` | single task status |
| `GET` | `/access/users` | users (admin) |
| `GET` | `/access/realms` | realms (admin, version-dependent) |
| `GET` | `/access/acl` | ACL assignments |
| `GET` | `/pools` | pools |

## Examples

### Retrieve inventory with token

```bash
curl -sk -H 'Authorization: PVEAPIToken=automation@pve!ci-token:SECRET' \
  'https://pve1:8006/api2/json/cluster/resources?type=vm' \
  | jq -r '.data[] | "\(.vmid) \(.name) \(.status)"'
```

### Start VM (asynchronous)

```bash
curl -sk -X POST \
  -H 'Authorization: PVEAPIToken=automation@pve!ci-token:SECRET' \
  https://pve1:8006/api2/json/nodes/pve1/qemu/101/status/start
```

Response: `202 Accepted`, `data` = UPID, e.g.

```json
{ "data": "UPID:pve1:0012AB34:00005678:4C9D0001:start:101:qemu:root@pam:" }
```

Track status:

```bash
curl -sk -H 'Authorization: PVEAPIToken=...' \
  https://pve1:8006/api2/json/nodes/pve1/tasks/UPID:pve1:0012AB34:00005678:4C9D0001:start:101:qemu:root@pam:
```

### Create VM with ticket + CSRF

```bash
TICKET=... ; CSRF=...
curl -sk -X POST https://pve1:8006/api2/json/nodes/pve1/qemu \
  -H "Cookie: PVEAuthCookie=$TICKET" \
  -H "X-CSRF-Prevention-Token: $CSRF" \
  -d 'vmid=200' -d 'name=testvm' -d 'memory=2048' -d 'cores=2' \
  -d 'disk=local-lvm:32'
```

### pvesh (on the node)

```bash
pvesh get /cluster/resources --type vm --output-format json
pvesh set /nodes/pve1/qemu/101/status/start
pvesh create /nodes/pve1/qemu --vmid 201 --name demo
```

## Rate limits and operational notes

- **No built-in rate limiting** of the API — protection via firewall rules, reverse proxy or fail2ban (GUI/ticket logins).
- Errors `401/403` for wrong token/missing ACLs; `429` only if upstream systems apply limits.
- Asynchronous actions: check for UPID completion instead of guessing sleep intervals.
- API documentation of your own version: *Documentation → API Viewer* tab in the UI or `pvesh help`.
- Check HTTPS certificates (`-k` only in labs), manage tokens separately by purpose.

## Webhooks and notifications

- **No webhooks** (neither incoming nor outgoing) documented.
- From Proxmox VE 8.1 there is a **notification system** (*Notifications* tab): matching rules send alerts to mail/Jabber/SMS targets (version-dependent) — no generic HTTP callback.
- Automation workaround: cron/poller against `/cluster/tasks` or monitoring agents (Prometheus exporter) on the nodes.

## SDKs and client libraries

| Library | Language | Note |
|------------|---------|-----------|
| `proxmoxer` | Python | de facto standard, supports ticket and token auth |
| Terraform provider `bpg/proxmox` | HCL | declarative VM/container management |
| Ansible collection `community.proxmox` (successor of the old `proxmox` modules) | YAML | VM/storage modules |
| Perl `PVE::API2` | Perl | directly on the nodes |
| `pvesh` | CLI | official, JSON-capable, ideal for scripts |

## See also

- [index.md](../index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
