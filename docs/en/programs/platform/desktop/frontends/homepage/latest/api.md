# Homepage - API Documentation

## Overview

Homepage has **no public administration API**: the dashboard is controlled exclusively via YAML files under `config/`. What exists are **internal Next.js API routes** under `/api/...`. They serve two purposes: as a **proxy** they bring the data of the connected services into the browser (keys stay on the server, CORS is not needed), and they supply auxiliary data such as config hashes, status messages or search suggestions.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| HTTP/JSON under `/api/...` | service proxy, info widgets, Docker/Kubernetes status, helper functions | Internal, not versioned as a stable interface |
| Config interface | `config/*.yaml` + environment variables | Officially documented (authoritative route) |
| MCP (`/api/mcp`) | AI assistants read/change configuration files | Opt-in via `HOMEPAGE_MCP_ENABLED` |
| Webhooks | ❌ Not available | — |
| GraphQL | ❌ Not available | — |
| Write API for layout/widgets | ❌ Not available (exception: MCP with write permission) | — |

## Authentication

- **Default: none.** The routes are reachable without credentials as soon as someone can reach the page. Protection is provided by the reverse proxy (Basic Auth, OAuth proxy, Authentik, VPN/Tailscale).
- **Host validation**: every route checks the `Host` header against `HOMEPAGE_ALLOWED_HOSTS` (plus `localhost:<PORT>`). If the host does not match, Homepage responds with `400` and a note in the log.
- **Optional session sign-in**: with `HOMEPAGE_AUTH_ENABLED`, every route checks a NextAuth session token (`NEXTAUTH_SECRET` or `HOMEPAGE_AUTH_SECRET`). Without a valid session the route responds with `401 {"error":"Unauthorized"}`. This protects the routes, but does not replace roles.
- **Service secrets**: API keys and passwords are stored in the config and inserted via `{{HOMEPAGE_VAR_*}}` / `{{HOMEPAGE_FILE_*}}`. They leave the server only in the direction of the respective target service.
- **MCP token**: for the MCP endpoint, `HOMEPAGE_MCP_TOKEN` (at least 32 characters) is required unless session sign-in is active. Passed via `Authorization: Bearer <token>` or `X-Homepage-MCP-Token: <token>`.

## Endpoints

The routes are defined within the project and may change between versions. Parameters are passed as query parameters.

### Service proxy (service widgets)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/services/proxy` | Retrieve data of a configured service (`group`, `service`, `index`) |
| `GET` | `/api/services/proxy?endpoint=<name>` | Retrieve a single endpoint of the service stored in the widget |
| `GET` | `/api/services/proxy?...&query=<json>` | Pass additional, permitted query parameters to the target service |
| `GET` | `/api/services/proxy?...&segments=<json>` | Insert permitted path segments (e.g. IDs) |
| `POST` | `/api/services/proxy?...&endpoint=<name>` | Only for services with a stored POST assignment; unknown types/endpoints respond with `403`, invalid parameters with `400` |
| `GET` | `/api/services/index` | Metadata of the configured services (groups, names, types) |

### Information widgets

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/widgets/resources` | CPU, RAM and disk usage of the host |
| `GET` | `/api/widgets/weather` | Weather (internal provider) |
| `GET` | `/api/widgets/openweathermap` | Weather data from OpenWeatherMap |
| `GET` | `/api/widgets/openmeteo` | Weather data from Open-Meteo |
| `GET` | `/api/widgets/stocks` | Prices from the `stocks` widget |
| `GET` | `/api/widgets/glances` | Measurements of a Glances instance |
| `GET` | `/api/widgets/kubernetes` | Cluster overview for the info widget |
| `GET` | `/api/widgets/longhorn` | Longhorn storage values |
| `GET` | `/api/widgets/customapi` | Filter any JSON source by JSON path |

### Infrastructure status

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/docker/statuses` | Container status from the Docker socket |
| `GET` | `/api/docker/stats` | CPU/RAM per container |
| `GET` | `/api/kubernetes/status` | Pod/deployment status |
| `GET` | `/api/kubernetes/stats` | Utilisation values from the cluster |
| `GET` | `/api/proxmox/stats` | Status values of a Proxmox host |
| `GET` | `/api/siteMonitor?groupName=&serviceName=` | HTTP reachability and response time of a configured tile |
| `GET` | `/api/ping?groupName=&serviceName=` | ICMP ping to a configured tile |

### Page, configuration and maintenance

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/theme` | active colour scheme (`color`, `theme`) |
| `GET` | `/api/bookmarks` | Bookmarks from `bookmarks.yaml` |
| `GET` | `/api/search/searchSuggestion` | Search suggestions of the configured provider |
| `GET` | `/api/releases` | Latest GitHub releases of the project (update notice) |
| `GET` | `/api/hash` | Hashes of the config files (change detection) |
| `GET` | `/api/validate` | YAML validation with file, reason and line |
| `GET` | `/api/revalidate` | Discard caches for dashboard data |
| `GET` | `/api/healthcheck` | Returns `up` (container health check) |
| `GET` | `/api/config/<path>` | Access to config contents for internal functions |
| `POST` | `/api/mcp` | Model Context Protocol: read/change config (opt-in) |
| `GET/POST` | `/api/auth/*` | Session sign-in, only with `HOMEPAGE_AUTH_ENABLED` |

## Widget data sources

Service widgets address the API of the respective service, not that of Homepage. Examples from the widget descriptors:

| Service | Target pattern | Note |
|--------|-----------|-----------|
| Sonarr/Radarr/Lidarr | `{url}/api/v3/{endpoint}?apikey={key}` | `endpoint` e.g. `queue`, `series`, `command` |
| qBittorrent | `{url}/api/v2/{endpoint}` | session login is performed internally |
| UniFi | `{url}/proxy/network/...` | own JSON-RPC handler |
| Synology (Disk Station) | `{url}/webapi/entry.cgi` | own handler, see [../synology-dsm/api.md](../../synology-dsm/latest/api.md) |
| Proxmox | `{url}/api2/json/{endpoint}` | token auth |

## Examples

### Retrieve service widget data

```bash
curl -s \
  -H "Host: homepage.example.internal" \
  "http://localhost:3000/api/services/proxy?group=Media&service=Sonarr&index=0&endpoint=queue"
```

Response (shortened):

```json
{
  "totalRecords": 4,
  "page": 1,
  "pageSize": 10,
  "records": [
    { "title": "Episode 12", "sizeLeft": 524288000, "status": "downloading" }
  ]
}
```

### Status indicator of a tile

```bash
curl -s "http://localhost:3000/api/siteMonitor?groupName=Network&service=Pi-hole"
```

Response:

```json
{ "status": 200, "ok": true, "duration": 42 }
```

### Validate configuration

```bash
curl -s "http://localhost:3000/api/validate"
```

Response in case of errors:

```json
{
  "status": "error",
  "errors": [
    { "name": "YAMLException", "config": "services.yaml", "reason": "bad indentation of a mapping entry", "mark": { "line": 17 } }
  ]
}
```

### Using the MCP endpoint

```bash
curl -s -X POST "http://localhost:3000/api/mcp" \
  -H "Authorization: Bearer $HOMEPAGE_MCP_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

## Rate limits

- Homepage ships **no own rate limit** for `/api/...`.
- Responses are briefly cached within the process (`memory-cache`); identical queries within the cache window do not hit the target service again.
- The actual load is determined by the query intervals of the widgets (default: in the minute range) and the number of tiles.
- Recommendation: rate limiting at the reverse proxy (`limit_req` in nginx, `ratelimit` middleware in Traefik) and intervals of 30 seconds or more.

## Webhooks

- **No webhooks**: Homepage sends no events to the outside.
- **Other route**: the MCP endpoint accepts changes from outside; external scripts can call `GET /api/revalidate` so that cached dashboard data is discarded.
- **Monitoring**: `/api/healthcheck` returns `up` and is suitable for container health checks; `siteMonitor`/`ping` do not replace a monitoring stack.

## SDKs and client libraries

- **No official SDK** for the internal routes.
- The **service clients themselves** are located in the source tree under `src/utils/proxy/` and `src/widgets/<service>/proxy.js`; description of this layer: [../gethomepage/api.md](../../gethomepage/latest/api.md).
- For own scripts, `curl`, `fetch` or `requests` with the query parameters above are sufficient.
- For the **target services**, their own SDKs apply (Sonarr/Radarr clients, Docker API, Kubernetes client, Proxmox API).

## Notes for operation

- Set `HOMEPAGE_ALLOWED_HOSTS` correctly — the check protects against Host header abuse and otherwise also blocks legitimate calls.
- The routes are an **SSRF tool**: they must not be publicly reachable. Proxy protection, VPN or firewall are mandatory.
- Never write secrets into the config; insert them via `HOMEPAGE_VAR_*`/`HOMEPAGE_FILE_*`.
- Changes to routes are internal details: for automation, better use the YAML files (Git).

## See also

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [../gethomepage/index.md](../../gethomepage/index.md)
