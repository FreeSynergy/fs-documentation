# TrueNAS - API Documentation

## Overview

The middleware (`middlewared`) provides the complete feature set as **API v2.0**: a versioned **JSON-RPC 2.0** interface over HTTP (`/api/v2.0`) and WebSocket. Every UI action is a method call (`pool.query`, `app.start`, `sharing.smb.create` …). Authentication uses an **API key as bearer token** (HTTP) or login methods (WebSocket). This includes job tracking (`core.get_jobs`) and event subscriptions (`core.subscribe`). Legacy TrueNAS CORE used the legacy API v1 (`/api/v1.0`) — only relevant for existing installations.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| JSON-RPC 2.0 (HTTP `POST /api/v2.0`) | all management methods | official (newer versions, version-dependent) |
| JSON-RPC 2.0 (WebSocket) | same methods + event subscriptions | official; endpoint path under `/api/docs/` on the device |
| Legacy REST v1 (`/api/v1.0`) | CORE installations | deprecated |
| CLI `midclaw` / `midclt` | method call on the device | official |
| Webhooks | — | ❌ Not available |

## Authentication

- **API keys**: can be created per user via the **user menu (top right) → API Keys** (or method `api_key.create`). Keys have a name, role and optional expiry.
- **HTTP**: header `Authorization: Bearer <api-key>` for JSON-RPC calls against `https://<host>/api/v2.0`.
- **WebSocket**: after connecting, `auth.login` (user/password, OTP-capable), `auth.login_with_api_key` or `auth.login_with_token`; then `auth.me` to check.
- **2FA**: if two-factor is active for UI sessions, scripts are cleanest run via API keys (OTP-free, revocable).
- **Roles**: access follows the privileges of the API key holder (granular depending on version).

## JSON-RPC format

Request:

```json
{ "jsonrpc": "2.0", "method": "core.ping", "params": [], "id": 1 }
```

Response:

```json
{ "jsonrpc": "2.0", "result": "pong", "id": 1 }
```

Error:

```json
{ "jsonrpc": "2.0",
  "error": { "code": 1, "message": "[ENOSYS] Method not found", "data": {} },
  "id": 1 }
```

## Methods (selection)

| Method | Description |
|---------|--------------|
| `core.ping` | connection test |
| `core.get_methods` | list all methods |
| `core.get_jobs` / `core.job_wait` | check/await job status |
| `core.subscribe` / `core.unsubscribe` | subscribe to event channels (WebSocket) |
| `system.version`, `system.info` | version and system info |
| `api_key.create/query/delete` | manage API keys |
| `pool.query`, `pool.dataset.query` | read pools and datasets |
| `pool.dataset.create/update/delete` | change datasets (job) |
| `pool.snapshot.create/query` | snapshots |
| `pool.snapshottask.run` | run scheduled snapshot job |
| `app.query`, `app.start`, `app.stop`, `app.upgrade` | apps (SCALE) |
| `sharing.smb.query/create` | SMB shares |
| `replication.create/run` | replication tasks |
| `service.control` | start/stop services |
| `alert.list` | active alerts |
| `auth.me` | own session info |

## Examples

### curl: JSON-RPC over HTTP

```bash
curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"system.version","params":[],"id":1}'
```

Response (shortened):

```json
{ "jsonrpc": "2.0",
  "result": "TrueNAS-SCALE-24.10.2",
  "id": 1 }
```

### curl: datasets with filter

```bash
curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"pool.dataset.query","params":[[["name","=", "tank/media"]],{"select":["name","used","available"]}],"id":2}'
```

### Jobs: wait for pool expansion

```bash
# Call returns a job ID in the result field
curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"pool.expand","params":[1],"id":3}'

curl -sk -X POST https://truenas.local/api/v2.0 \
  -H 'Authorization: Bearer DEIN_API_KEY' -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"core.get_jobs","params":[[["id","=","abc123"]]],"id":4}'
```

### CLI on the device

```bash
# SCALE (current)
midclaw call core.ping
midclaw call pool.dataset.query '[]'

# CORE / older versions
midclt call system.version
```

## Events instead of webhooks

- TrueNAS **does not send webhooks** to external systems and has **no incoming webhooks**.
- Real-time information comes via **JSON-RPC notifications**: WebSocket connection with `core.subscribe` to channels (e.g. jobs, pool/app events) — the way to live dashboards.
- Outgoing **alert services** (email, team channels; scope version-dependent) notify on alerts, but are not a generic callback.

## Rate limits and operational notes

- **No documented rate limit** for the middleware API — nevertheless choose polling intervals sensibly (prefer events) and rotate keys.
- API documentation of your own version: `https://<host>/api/docs/` or api.truenas.com (check version-specific method names).
- Self-signed certificates: `curl -k` only in the lab; better store the internal CA certificate.
- API key is visible only once; if lost, create a new one and revoke the old one.

## SDKs and client libraries

| Library | Language | Note |
|------------|---------|-----------|
| `truenas-api` (TrueNAS API client, github.com/truenas/api_client) | Python | official WebSocket JSON-RPC package incl. CLI reference |
| `py-nas` | Python | community WebSocket client (basis of older integrations) |
| Ansible modules `community.general.truenas_*` | YAML | declarative tasks via the API |
| `midclaw`/`midclt` | CLI | directly on the device, JSON arguments |

## Testing and reference

1. **Open your own API documentation**: `https://<host>/api/docs/` (version-specific method lists) or api.truenas.com.
2. **Create a key**: user menu → API Keys, choose the role deliberately (read-only for dashboards).
3. **Check the connection**: `core.ping` → `pong`; then test real read methods.
4. **Try events**: WebSocket client with `auth.login_with_api_key` + `core.subscribe` to see job/pool events live.

## See also

- [index.md](../index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
