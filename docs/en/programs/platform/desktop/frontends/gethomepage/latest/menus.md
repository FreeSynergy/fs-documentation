# gethomepage (Library) - Module and package directory

## Overview

This file contains **no user menu**: the library layer of Homepage has no interface. Instead, it is the **directory of modules and packages** in the source tree – what would be the menu items in an application. Numbering follows the call order: first the request from the browser, last the helper functions.

Path reference: repository `gethomepage/homepage`, directory `src/`.

## Module directory ("main menu items" of the library)

### 1. Proxy entry: `src/pages/api/services/proxy.js`
- **Function**: accepts all widget requests from the browser (`/api/services/proxy`)
- **Details**:
  - parameters: `group`, `service`, `index`, optionally `endpoint`, `segments`, `query`
  - finds the widget via `getServiceWidget` and the matching descriptor
  - maps `endpoint` via `mappings` to the real endpoint (whitelist)
  - rejects unknown types, methods and segments with `403`

### 2. Registry: `src/widgets/widgets.js`
- **Function**: central reference table of all widget types
- **Details**: links `type` → descriptor, field requirements and handler; determines which configuration keys are permitted

### 3. Service modules: `src/widgets/<service>/`
- **Function**: one folder per integrated service (over 170)
- **Details**:
  - `widget.js` – descriptor (`api` template, `mappings`, `fields`)
  - `proxy.js` – optional special handler
  - `component.jsx` – display in the dashboard (not part of data retrieval)
  - `*.test.js` / `*.test.jsx` – tests for the module

### 4. Handlers: `src/utils/proxy/handlers/`
- **Function**: carries out the actual request
- **Details**:

| File | Use |
|-------|---------|
| `generic.js` | standard for REST services with API key or open API |
| `credentialed.js` | services with username/password and session |
| `jsonrpc.js` | JSON-RPC wrapper |
| `synology.js` | Synology `entry.cgi` incl. session flow, see [../synology-dsm/api.md](../../synology-dsm/latest/api.md) |
| `unifi.js` | UniFi controller with its own login/cookie flow |

### 5. Request tools: `src/utils/proxy/`
- **Function**: building blocks that every handler uses
- **Details**:
  - `api-helpers.js` – `formatApiCall`, `formatProxyUrl`, `getURLSearchParams`, `asJson`, `jsonArrayTransform`
  - `http.js` – `httpProxy`, `cachedRequest`, redirect handling
  - `cookie-jar.js` – session cookies for login services (`tough-cookie`)
  - `validate-widget-data.js` – checks expected fields of the response
  - `use-widget-api.js` – browser hook (SWR)

### 6. Configuration layer: `src/utils/config/`
- **Function**: YAML → objects, checking, error reporting
- **Details**:

| File | Content |
|-------|---------|
| `yaml.js` | read YAML, create template, substitution of `HOMEPAGE_VAR_*`/`HOMEPAGE_FILE_*` |
| `config.js` | entry and check functions, configuration directory |
| `service-helpers.js` | service/widget search, groups, index creation |
| `widget-helpers.js` | widget fields and requirements |
| `docker.js` / `kubernetes.js` / `proxmox.js` | provider detection and labels/annotations |
| `dashboard.js` | assembled dashboard data including cache invalidation |
| `api-response.js` | uniform responses for routes |
| `shvl.js` | read values in nested structures |

### 7. Infrastructure modules
- **Function**: access to the platform instead of to services
- **Details**:
  - `src/utils/docker/` – containers via the Docker socket (`dockerode`)
  - `src/utils/kubernetes/` – pods/deployments (`@kubernetes/client-node`)
  - `src/utils/weather/` – weather providers
  - `src/utils/logger.js` – structured log (`winston`)
  - `src/utils/env.js` – environment variables of the application

### 8. External dependencies of the layer
- **Function**: ready-integrated clients
- **Details**: `follow-redirects`, `tough-cookie`, `js-yaml`, `memory-cache`, `json-rpc-2.0`, `dockerode`, `@kubernetes/client-node`, `systeminformation`, `ping`, `gamedig`, `ical.js`, `luxon`, `urbackup-server-api`, `minecraftstatuspinger`

## Cross-cutting modules (correspond to context menus)

| Module | Cross-cutting task |
|-------|---------------------|
| `src/utils/auth.js` | host check (`withAllowedHost`), session check (`withAuth`) for every route |
| `src/utils/highlights.js` | highlighting/colour rules for widget values |
| `src/utils/widget-fields.js` | checks mandatory fields per widget type |
| `src/utils/styles/` | CSS helpers for the dashboard |
| `src/utils/hooks/`, `src/utils/contexts/` | React building blocks of the dashboard part |
| `src/utils/mcp/` | tool functions for the MCP endpoint |

## Access by role

The library has no users, but there are access levels in developer operations:

### Users of the dashboard
- Sees only results; does not reach any module file
- Can inspect the proxy responses via the browser developer tools (incl. sensitive values for some services)

### Operations / admin (deployment side)
- May change `config/*.yaml`, `.env` and environment variables
- Decides on Docker socket access and the MCP endpoint
- Can adjust the log level to trace handler decisions

### Developer (source tree)
- Full access to `src/`, may change descriptors, handlers and tests
- Uses `pnpm dev` for local request trials with sample data
- Submits changes as a pull request

### Contributors / reviewers
- Check new service modules for registry entry, field requirements, test coverage and security
- Ensure that new endpoints are reachable only via `mappings`

## See also

- [structure.md](layout.md) - levels and call path
- [api.md](api.md) - clients, methods and parameters
- [features.md](features.md) - functions of the layer
- [../homepage/menu.md](../../homepage/latest/menus.md) - areas of the dashboard interface
