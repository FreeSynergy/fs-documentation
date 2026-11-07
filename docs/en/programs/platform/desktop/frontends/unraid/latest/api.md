# Unraid - API Documentation

## Overview

For years Unraid had **no officially documented core API**: automation ran via configuration files on the USB stick and via the (undocumented) endpoints of the PHP web UI. This changes with current versions: Unraid officially adds a **GraphQL API** (`unraid-api`) with API keys, session cookies and optional OIDC authentication. Both worlds coexist — for scripts that matter to operations, the rule still applies: use only documented GraphQL fields, and file queries only as a transitional solution.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| GraphQL (`/graphql`) | system info, array, Docker, Connect settings | officially documented (current versions) |
| WebUI endpoints (PHP) | forms, plugin calls | undocumented, not stable |
| Configuration files (`/boot/config`) | shares, identification, array metadata | stable format, but not a service |
| Webhooks (outgoing) | notifications to external services | official, from version 6.12 (version-dependent) |
| Webhooks (incoming) | — | ❌ Not available |

## Authentication

- **API keys**: managed under **Settings → Management Access → API Keys** (create, roles, revoke). The key is sent in the header `x-api-key`.
- **Roles**: `admin` (full access), `connect` (remote access functions), `guest` (restricted read-only).
- **Session cookies**: WebUI sessions signed in via the browser work directly against `/graphql` — practical for testing, unsuitable for scripts.
- **SSO/OIDC**: with a configured external provider (version-dependent), API authentication runs through it.
- **Historically**: WebUI forms used the WebUI sign-in; for undocumented endpoints there was no official token authentication.

## GraphQL endpoints and schema

| Endpoint | Method | Description |
|----------|---------|--------------|
| `/graphql` | `POST` | GraphQL operations (queries and mutations) |
| `/graphql` (sandbox) | browser | interactive playground; enable under Settings → Management Access → Developer Options |

Root fields (selection, full schema in the Apollo Studio reference):

| Field | Content |
|------|--------|
| `info` | operating system, CPU, memory, motherboard |
| `array` | array status, capacity, drive list with temperature/status |
| `dockerContainers` | containers with name, state, autostart |
| `config` | server configuration (read-only) |
| `connect` | remote access/Connect settings (role `connect`/`admin`) |

## Examples

### Query: system status (curl)

```bash
curl -s -X POST http://UNRAID_IP/graphql \
  -H "Content-Type: application/json" \
  -H "x-api-key: DEIN_API_KEY" \
  -d '{"query": "query { info { os { platform distro release uptime } cpu { manufacturer brand cores threads } } }"}'
```

Response (shortened):

```json
{
  "data": {
    "info": {
      "os": { "platform": "linux", "distro": "Unraid", "release": "7.x", "uptime": "..." },
      "cpu": { "manufacturer": "Intel", "brand": "...", "cores": 8, "threads": 16 }
    }
  }
}
```

### Query: array and drive status

```bash
curl -s -X POST http://UNRAID_IP/graphql \
  -H "Content-Type: application/json" \
  -H "x-api-key: DEIN_API_KEY" \
  -d '{"query": "query { array { state capacity { disks { free used total } } disks { name size status temp } } }"}'
```

### Query: containers

```bash
curl -s -X POST http://UNRAID_IP/graphql \
  -H "Content-Type: application/json" \
  -H "x-api-key: DEIN_API_KEY" \
  -d '{"query": "query { dockerContainers { id names state status autoStart } }"}'
```

### Error format

```json
{
  "errors": [
    { "message": "Error description", "locations": ["..."], "path": ["..."] }
  ]
}
```

### Mutations (array, containers)

The schema contains mutations for array operations and Docker management; the exact field names are given only in the official schema reference (Apollo Studio or sandbox). Check them there before using scripts in production — this documentation names no unverified mutation names.

## CLI tools

| Command | Function |
|--------|----------|
| `unraid-api developer --sandbox true` | enable GraphQL sandbox (interactive: `unraid-api developer`) |
| `unraid-api status` | check status of the API component |
| `unraid-api report` | report/debug output for support |
| `unraid-api --help` | overview of all commands |

## Rate limits and operational notes

- The API implements **rate limits** (details not publicly quantified); handle responses cleanly when limits are exceeded.
- Limit query complexity — many fields and nested lists at once increase the load.
- Keep API keys rotatable and separated by role (`guest` for monitoring, `admin` only for maintenance scripts).
- Undocumented WebUI endpoints can change with every update — do not use them for production automation.

## Webhooks

- **Outgoing**: the notification service can send events (array errors, full-capacity warnings, among others) as **webhooks** to external endpoints (set up under Settings → Notifications, from version 6.12, version-dependent).
- **Incoming**: there are no webhooks/callbacks with which external systems can control Unraid; the GraphQL API is responsible for that.

## SDKs and client libraries

- **No official SDK**; the server is an Apollo/GraphQL server, and any GraphQL client (`axios-fetch`, `graphql-request`, `ApolloClient`) works.
- **`pyunraid`** (community, Python) addresses the WebUI endpoints — practical, but tied to undocumented details.
- **Schema reference**: Apollo GraphQL Studio (`Unraid-API`, variant *current*) as the only authoritative field reference.
- **Cron scripts** with `curl` + `x-api-key` remain the simplest way for homelab automation.

## File-based automation (legacy)

As long as GraphQL is not sufficient (older versions, detail values), scripts read directly on the server with:

```bash
# Basic configuration and metadata are on the boot medium
ls /boot/config            # XML files, super.dat, shares directory
cat /boot/config/ident.cfg # device ID, naming, network identification

# Diagnostics package for support/troubleshooting
diagnostics
```

Notes:

- File formats are not versioned as an interface — maintain patchers, tolerate errors.
- Writing is **not** done at this level: always make changes via WebUI or API, otherwise a status desync threatens.

## Testing and sandbox

1. **Settings → Management Access → Developer Options** → enable *GraphQL Sandbox* (or `unraid-api developer --sandbox true`).
2. Open `http://UNRAID_IP/graphql` in the browser — playground with auto-completing schema.
3. Test queries first without API key (uses the WebUI session), then switch to `x-api-key`.
4. Validate results with `jq` before they go into cron scripts.

## See also

- [index.md](../index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
