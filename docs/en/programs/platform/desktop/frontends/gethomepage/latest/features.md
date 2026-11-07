# gethomepage (Library) - Features

## Overview

The library layer of Homepage consists of **descriptors** (what a service can do), **handlers** (how requests are made), **configuration readers** (a widget object is built from `config/*.yaml`) and **tools** (URL building, cookies, caching, checks, log). This article describes which functions this layer offers — without user interface, without menus.

---

## 1. Service descriptors (one file per module)

- **API template**: `api: "{url}/api/v3/{endpoint}?apikey={key}"` – placeholders are filled from tile and widget entries
- **Multiple templates**: services with old/new versions (e.g. Pi-hole `api` and `apiv5`)
- **Endpoint assignments** (`mappings`): name → real endpoint, permitted method, optional query parameters, segments
- **Response shaping** (`map`): reduce fields, sort, rename — the browser only receives what is relevant
- **Response check** (`validate`): expected keys must occur, otherwise the request counts as an error
- **Standard handler or special handler**: `proxyHandler` points to a module with its own flow
- **Field requirements for the config** (`fields`): mandatory fields such as `key`, `key2`, `version`, `watch` — checked before the page is drawn

## 2. Handler types

- **Generic HTTP handler**: built on `follow-redirects`, handles redirects, timeout, status codes
- **Handler with login step**: first login (e.g. qBittorrent, Synology, UniFi), then the service request with stored cookies
- **JSON-RPC handler**: wrapper for `json-rpc-2.0` for RPC services (e.g. Docker-API-like services, media servers)
- **Special handlers**: own modules for UniFi, Synology (`entry.cgi`) and calendars (`ical.js`)
- **Raw layer**: `httpProxy` for a single request, `cachedRequest` for a request with a cache window
- **Header control**: additional headers per mapping (`mapping.headers`), e.g. Content-Type or API version

## 3. Configuration readers

- **YAML loading**: `settings.yaml`, `services.yaml`, `widgets.yaml`, `bookmarks.yaml`, `docker.yaml`, `kubernetes.yaml`, `proxmox.yaml`
- **Template and fallback**: if a file is missing, an example copy is created so the page can be drawn
- **Widget resolution**: `getServiceWidget(group, service, index)` returns name, type, URL, keys and fields of a tile
- **Service helpers**: group and service search, counter for multiple widgets of the same kind
- **Variable substitution**: `{{HOMEPAGE_VAR_*}}` and `{{HOMEPAGE_FILE_*}}` are inserted before parsing
- **Path access to values** via a small getter for nested entries
- **Validation**: parse errors report file, reason and line (also retrievable via `/api/validate`)

## 4. Request tools

- **URL building**: `formatApiCall(template, values)` replaces placeholders and removes duplicate slashes
- **Proxy URL building**: `formatProxyUrl(widget, endpoint, queryParams)` creates the address for the browser
- **Cookie storage**: own cookie jar based on `tough-cookie` for services with session login
- **Response helpers**: `asJson`, `jsonArrayTransform` and comparison/version helpers
- **Caching**: `memory-cache` with a short time window, identical keys are bundled
- **Special clients**: Docker socket (`dockerode`), Kubernetes (`@kubernetes/client-node`), system values (`systeminformation`), ping (`ping`), game servers (`gamedig`), backup (`urbackup-server-api`)

## 5. Browser-side data flow

- **Hook `useWidgetAPI(widget, endpoint, queryParams)`**: builds the proxy URL, queries via SWR, returns `{ data, error, mutate }`
- **Refresh interval**: derivable from the widget entry `refreshInterval`
- **Errors upward**: an error in the response (`data.error`) is exposed as a top-level error
- **No direct service access in the browser**: CORS problems and key leakage are thereby excluded
- **Loading state**: components show placeholders until the proxy response arrives

## 6. Logging and diagnosis

- **Structured log** with a namespace per layer (`servicesProxy`, `siteMonitor`, `config`), written via `winston`
- **Debug levels** via log level; faulty switches are not written to the log
- **Visible error sources**: unknown types, incompatible methods, unknown endpoints, manipulated segments
- **No trace of keys**: log lines name the service and endpoint, not the credentials

## 7. What the library CANNOT do

- **No own user interface**: no menus, no dialogs, no configuration view
- **No npm package**: not published as a library, therefore no `npm install` for own projects
- **No write access to services**: Homepage's widgets read; sending commands to services is deliberately not intended
- **No long-term measurement**: no history, no alerting, no curves over hours
- **No runtime plugin interface**: new clients are source code files in the repository
- **No persistence**: after a restart caches and session cookies are empty
- **No multi-tenancy**: one configuration, one set of keys, no separation by groups

## 8. Extensions and own clients

- **New service**: folder under `src/widgets/<name>/` with `widget.js` (descriptor), optionally `proxy.js` (handler) and `component.jsx` (display in the dashboard)
- **Maintain the registry**: entry in `src/widgets/widgets.js` so that `type` and fields are known
- **Unlock existing endpoints**: extend `mappings` with an entry instead of writing a new handler
- **Own data sources without code**: `customapi` widget with URL and JSON path — runs via the same generic handler
- **Tests**: `*.test.js`/`*.test.jsx` next to the file, runnable with Vitest
- **Language files**: responsible for error and label texts in the dashboard part

---

## Features at a glance

| Layer | Component | Result |
|-------|----------|----------|
| Descriptor | `widget.js` | permitted endpoints, fields, templates |
| Handler | `proxy.js`, `utils/proxy/handlers/*` | finished HTTP/RPC response |
| Config | `utils/config/*` | widget object from YAML |
| Tool | `utils/proxy/api-helpers.js`, `http.js`, `cookie-jar.js` | URL, request, cookies |
| Client | `utils/proxy/use-widget-api.js` | data in the dashboard |
| Diagnostics | `utils/logger.js`, `/api/validate` | traceable errors |

---

## See also

- [menu.md](menus.md) - Module and package directory
- [structure.md](layout.md) - Layers and call path
- [api.md](api.md) - Clients, methods and parameters
- [../homepage/index.md](../../homepage/index.md) - Dashboard application
