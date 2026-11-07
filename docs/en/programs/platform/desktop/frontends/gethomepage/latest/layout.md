# gethomepage (Library) - Structure & call path

## Overview

The library has no window; the equivalent concept is its **layer structure**. It is organized into **five levels**: browser hook, API route, descriptor/registry, handler and tools. Below these lie the configuration readers, which turn YAML into objects. This article describes this structure, not the screen layout of the dashboard.

## Window structure (layers of the library)

```
┌──────────────────────────────────────────────────────────────────────┐
│  Browser (dashboard)                                                 │
│  component.jsx ──► useWidgetAPI(widget, endpoint, queryParams)       │
│                        │  formatProxyUrl() → /api/services/proxy     │
├──────────────────────────────────────────────────────────────────────┤
│  Next.js process                                                     │
│  withAuth → withAllowedHost → services/proxy.js                      │
│      │  getServiceWidget(group, service, index)   (utils/config)     │
│      │  widgets[type]  (registry: descriptor + fields)               │
│      │  mappings[endpoint] → real endpoint, method, parameters        │
├──────────────────────────────────────────────────────────────────────┤
│  Handler layer (utils/proxy/handlers)                                │
│  generic │ credentialed │ jsonrpc │ synology │ unifi │ <service>/proxy│
│      │  formatApiCall(api template, values)                          │
│      │  cookie-jar (login cookies)  ·  http.js (httpProxy/cached)    │
├──────────────────────────────────────────────────────────────────────┤
│  Target                                                              │
│  Sonarr · Pi-hole · qBittorrent · Proxmox · Docker socket · K8s API  │
│      Response (JSON/XML/RPC) → map() → validate() → JSON to the hook │
└──────────────────────────────────────────────────────────────────────┘
```

## Levels and files

| Level | Location in the source tree | Task | Result |
|-------|------------------|---------|----------|
| Display | `src/widgets/<service>/component.jsx` | present values | tile in the grid |
| Data hook | `src/utils/proxy/use-widget-api.js` | query, interval, errors | `{data, error, mutate}` |
| Route | `src/pages/api/services/proxy.js` | check parameters, map endpoint | HTTP response |
| Protection | `src/utils/auth.js` | host and session check | `400`/`401` |
| Registry | `src/widgets/widgets.js` | type → descriptor | handler selection |
| Descriptor | `src/widgets/<service>/widget.js` | templates, `mappings`, `fields` | permitted requests |
| Handler | `src/utils/proxy/handlers/*`, `src/widgets/<service>/proxy.js` | execute request | raw data |
| Tools | `src/utils/proxy/{api-helpers,http,cookie-jar,validate-widget-data}.js` | URL, cookies, check | clean response |
| Config | `src/utils/config/*` | YAML → objects | widget object |
| Platform | `src/utils/{docker,kubernetes,weather,logger,env}/**` | system data, log | additional values |

## Call path (example Sonarr queue)

```
1  services.yaml:  - Jellyfin …  - Sonarr, _sonarr: {}
2  getServiceWidget("Media", "Sonarr", 0)
      → { type: "sonarr", url: "http://192.168.1.20:8989", key: "…", fields: […] }
3  descriptor sonarr: api = "{url}/api/v3/{endpoint}?apikey={key}"
4  mappings["queue"] → endpoint "queue", validate ["totalRecords"]
5  genericProxyHandler: formatApiCall →
      http://192.168.1.20:8989/api/v3/queue?apikey=…
6  http.js: follow-redirects, timeout, status check
7  validate-widget-data: is "totalRecords" present?
8  response → { totalRecords, records: […] } → hook → tile
```

## UI/UX of the library

### Design principles of the layer

- **Whitelist instead of freedom**: only stored endpoints are reachable
- **Thin adapters**: the descriptor contains no business logic, only assignments
- **One exit**: everything runs via `http.js`, so that redirects, cookies and caching are uniform
- **Errors as data**: responses contain `error` fields instead of exceptions all the way to the top

### Naming and storage conventions

- **Module name in lowercase**, identical to the widget `type`
- **Fixed file names**: `widget.js`, `proxy.js`, `component.jsx`
- **Tests alongside**: `widget.test.js`, `proxy.test.js`, `component.test.jsx`
- **Constants in the descriptor**, no hard-coding in the handler

### Internal "interactions"

- **Caching**: `cachedRequest(url, seconds)` decides between network request and cache hit
- **Bundling**: same keys within the time window trigger only one request
- **Cookies**: held per service target in a jar until the session expires
- **Reloading the cache**: `GET /api/revalidate` discards dashboard data

### Maintainability and testability

- **No UI needed** to check handlers: tests call `handler(req, res)` with fake objects
- **Mock profiles** for services with login (login first, then the service request)
- **Snapshot-like checks**: expected fields are secured via `validate`

### Responsive design and accessibility

- **Not applicable**: the library renders no interface; accessibility is the concern of the dashboard ([../homepage/structure.md](../../homepage/latest/layout.md))
- **Textual output**: only error messages that appear in components – short and without credentials

### Performance

- **One process, no pool**: requests run concurrently via Node.js; long timeout chains do not block
- **Cache window** limits the load on target services
- **Reduce response size**: `map` cuts off fields before data reaches the browser
- **Sluggish services** slow only their own tile, since each hook loads separately
- **Recommendation**: at most one endpoint per tile per interval; limit large lists via `map`

## See also

- [menu.md](menus.md) - module and package directory
- [features.md](features.md) - functions of the layer
- [api.md](api.md) - clients and methods
- [shortcuts.md](shortcuts.md) - build and dev commands
- [../homepage/api.md](../../homepage/latest/api.md) - endpoints of the application
