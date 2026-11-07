# gethomepage (Library) - API of the library layer

## Overview

This file describes the **programming interface of the client layer**: which functions exist, which parameters they expect and what they return. Two interfaces are relevant:

1. **Browser → application**: the hook `useWidgetAPI` and the proxy URL it generates
2. **Server internal**: descriptor objects, handler functions and the tool functions in `src/utils/proxy/`

**Interface types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| JavaScript modules (ESM) | internal call within the application | authoritative interface |
| HTTP/JSON `/api/services/proxy` | data retrieval from the browser | internal, not versioned |
| npm package | ❌ Not available – the layer is not published | — |
| Webhooks | ❌ Not available | — |
| GraphQL | ❌ Not available | — |

## Authentication and security of the clients

- **No own authentication**: the layer inherits the protection of the application (host check, optional session login).
- **Service credentials** come from the configuration (`key`, `key2`, `username`/`password`, token) and are used differently per handler: query parameter, header or login flow.
- **Secrets from the environment**: `{{HOMEPAGE_VAR_*}}` and `{{HOMEPAGE_FILE_*}}` are inserted on loading, so that no keys are stored in files.
- **Cookies** for login services live in their own jar in the process and are not passed to the browser.

## Core API of the modules

### Descriptor (`src/widgets/<service>/widget.js`)

| Field | Type | Description |
|------|-----|--------------|
| `api` | String | Template, e.g. `{url}/api/v3/{endpoint}?apikey={key}` |
| `apiv5` … | String | further templates for alternative versions |
| `proxyHandler` | Function | handler module, otherwise the generic handler |
| `fields` | Object | mandatory configuration fields, e.g. `{ key: true, version: false }` |
| `mappings` | Object | permitted endpoints with `endpoint`, `method`, `body`, `params`, `optionalParams`, `segments`, `headers`, `map`, `validate` |
| `primaryField` | String | marker for the main value of the tile |

### Browser hook

```javascript
// useWidgetAPI(widget, endpoint, queryParams, swrConfig)
const { data, error, mutate } = useWidgetAPI(widget, "queue", { limit: 5 });
```

| Parameter | Meaning |
|-----------|-----------|
| `widget` | widget object from the configuration (type, URL, group name, index) |
| `endpoint` | key from `mappings`; an empty string suppresses the request |
| `queryParams` | additional parameters, as JSON in the query parameter `query` |
| `swrConfig.refreshInterval` | refresh interval in milliseconds |

Generated URL: `/api/services/proxy?group=<group>&service=<name>&index=<n>&endpoint=<ep>&query=<json>`

### Tool functions (`src/utils/proxy/api-helpers.js`)

| Function | Signature | Result |
|----------|----------|----------|
| `formatApiCall` | `(template, values)` | ready-to-use URL, placeholders replaced |
| `parseVersionForUrl` | `(version, default)` | numeric version for URL components |
| `getURLSearchParams` | `(widget, endpoint)` | `URLSearchParams` with `group`, `service`, `index` |
| `formatProxyUrl` | `(widget, endpoint, queryParams)` | proxy URL for the browser |
| `asJson` | `(data)` | parsed JSON or original |
| `jsonArrayTransform` | `(data, transform)` | transformed array |

### HTTP layer (`src/utils/proxy/http.js`)

| Function | Signature | Result |
|----------|----------|----------|
| `httpProxy` | `(url, options)` | response (status, headers, body) of a single request |
| `cachedRequest` | `(url, seconds)` | response from the cache or freshly loaded |
| Redirect handling | – | follows redirects via `follow-redirects` |

### Handler contract (`src/utils/proxy/handlers/*`)

```javascript
// every handler: async (req, res) => void
async function genericProxyHandler(req, res) {
  const widget = getServiceWidget(req.query.group, req.query.service, req.query.index);
  const url = formatApiCall(widget.api, { url: widget.url, endpoint: req.query.endpoint, key: widget.key });
  const response = await httpProxy(url, { headers, method: req.method, body: req.body });
  return res.status(response.status).json(answer);
}
```

## Endpoints of the client layer

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/services/proxy` | generic data retrieval per configured service |
| `GET` | `/api/services/proxy?endpoint=<name>` | endpoint released via `mappings` |
| `GET` | `/api/services/proxy?segments=<json>` | path segments (IDs) for endpoints with placeholders |

## Client examples per service type

| Service | Template | Authentication | Typical endpoint |
|--------|-----------|-------------------|--------------------|
| Sonarr/Radarr | `{url}/api/v3/{endpoint}?apikey={key}` | API key in query | `queue`, `series`, `history` |
| Pi-hole (V6) | `{url}/api/{endpoint}` | session/login internal | `stats/summary` |
| qBittorrent | `{url}/api/v2/{endpoint}` | login → cookie | `transfer/info`, `torrents/info` |
| Jellyfin | `{url}/api/{endpoint}` | `api_key` | `Sessions` |
| Proxmox | `{url}/api2/json/{endpoint}` | token header | `nodes`, `cluster/resources` |
| UniFi | own JSON-RPC flow | user/password | status and client lists |
| Synology | `{url}/webapi/entry.cgi` | session (`_sid`) plus OTP possible | `SYNO.API.Auth`, `SYNO.Core.*` |

## Examples

### Handler call in a test (Vitest)

```javascript
import genericProxyHandler from "utils/proxy/handlers/generic";

test("Sonarr queue", async () => {
  const req = {
    method: "GET",
    query: { group: "Media", service: "Sonarr", index: 0, endpoint: "queue" },
  };
  const res = { status: () => res, json: (body) => (res.body = body) };
  await genericProxyHandler(req, res);
  expect(res.body.totalRecords).toBeDefined();
});
```

### New endpoint in an existing service

```javascript
// src/widgets/sonarr/widget.js – excerpt
const widget = {
  api: "{url}/api/v3/{endpoint}?apikey={key}",
  proxyHandler: genericProxyHandler,
  mappings: {
    history: { endpoint: "history", validate: ["totalRecords"] },
    "series/detail": {
      endpoint: "series/{id}",
      segments: ["id"],
      map: (data) => ({ title: asJson(data).title, id: asJson(data).id }),
    },
  },
};
```

### Call from a script (against the running application)

```bash
curl -s -H "Host: homepage.example.internal" \
  "http://localhost:3000/api/services/proxy?group=Media&service=qBittorrent&index=0&endpoint=transfer%2Finfo"
```

Response (shortened):

```json
{ "speed": { "down": 1048576, "up": 20480 }, "queueing": { "active": 3, "inactive": 12 } }
```

## Rate limits, caching and timing

- **Process cache** via `memory-cache`; identical requests within the window do not hit the target service again
- **No rate limit** in the layer itself – limited by widget intervals
- **Session logic**: login cookies are reused; when a session has expired, a new login takes place
- **Recommendation**: do not set the interval below 10 seconds, so that media and DNS services are not burdened

## Events and webhooks

- **No event output**: the layer pulls (queries), it sends nothing outward
- **Reactive in the browser**: SWR triggers interval queries; `mutate` forces a new retrieval
- **Cache rebuild from outside**: `GET /api/revalidate` discards assembled dashboard data

## SDKs and own use

- **No official SDK or npm package** (checked: `@gethomepage/homepage` does not exist in the npm registry)
- **Only route**: fork the source tree, add the module, write tests, submit a pull request
- **For own projects**: rebuild the HTTP calls to the target services directly with `fetch`/`axios` or use the SDKs of the respective service

## Notes for developers

- Always release new endpoints **via `mappings`**, never via free path passing
- Secure responses with `validate`, so that changes in the target service are noticed early
- Do not output credentials in logs or error messages
- Bundle special cases (login, RPC, XML) in their own `proxy.js`, not in the descriptor
- Short documentation in the module comment: which endpoints are released and why

## See also

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md) (module and package directory)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [../homepage/api.md](../../homepage/latest/api.md)
