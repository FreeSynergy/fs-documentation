# gethomepage (Library) - Description

## Overview

Behind every live value on a Homepage dashboard sits the same code layer: the **service client library** of `gethomepage/homepage`. It translates a configuration entry (`_sonarr: {}` on a tile) into an authenticated HTTP call against the API of the target service, shortens the response and delivers JSON to the React component. It has no screen, no menu and no settings of its own.

## What the library does

The library consists of three interacting parts: **descriptors** describe per service which API endpoints exist and how responses are to be shaped (`api` template, `mappings`, `validate`, `map`). **Handlers** carry out the request: a generic HTTP handler, a handler for services with a login step, a JSON-RPC handler and special cases such as UniFi or Synology. **Helper functions** handle URL building, cookie storage, caching, translation of the YAML configuration, logging and the check whether expected fields are present in the response. The browser never queries the target service directly, but always the route `/api/services/proxy` – keys and session cookies thus remain in the process.

## Advantages

- **One pattern for over 170 services**: new service = descriptor plus optionally a special handler
- **Secrets stay server-side**: API keys and passwords do not leave the browser
- **CORS-free**: the browser only talks to the same origin
- **Endpoint whitelist**: only endpoints stored in `mappings` can be called; paths are escaped segment by segment
- **Robustness**: response validation, errors as JSON instead of as an exception, restart-friendly logging
- **Caching and bundling**: identical queries within the time window hit the target service only once
- **Testability**: each module has a test file (Vitest), handlers can be checked without a UI

## Distinction from other systems

### gethomepage library vs. Homepage dashboard
- **Dashboard** = pages, grid, themes; **library** = data retrieval under the hood
- **Dashboard** configurable via YAML, **library** extensible only in the source code
- Documentation of the dashboard: [../homepage/index.md](../../homepage/index.md)

### gethomepage library vs. Homer
- **Homer** has no clients: there, tiles only show static links, live data is missing
- **gethomepage** ships ready-made client modules including the authentication flow
- **Homer** is pure static, **gethomepage** needs a Node process for the proxy layer

### gethomepage library vs. Heimdall
- **Heimdall** integrates via PHP app packages on its own server, **gethomepage** via JS modules in the Node process
- **Heimdall** stores integration keys in the database, **gethomepage** reads them from YAML/environment
- **gethomepage** is geared toward queries (read-only), **Heimdall** likewise, but with a different runtime

### gethomepage library vs. Dashy
- **Dashy** queries status endpoints directly from the browser or via a small Node server, **gethomepage** centrally via a proxy route
- **Dashy** offers its own widget syntax in `conf.yml`, **gethomepage** defines endpoints in the code
- **gethomepage** covers significantly more specialist services, **Dashy** more general HTTP/status checks

## Technical details

- **Backend**: JavaScript (ESM) in Node.js, embedded in a Next.js application (pages router)
- **Database**: **none** – states are process caches (`memory-cache`) and cookies in memory
- **Frontend part**: only one hook (`useWidgetAPI`) for reloading via SWR; presentation belongs to the dashboard
- **Authentication**: varies per service – API key in query/header, session login with cookie storage, Basic auth, token (Proxmox), certificates for internal HTTPS services
- **Hosting**: runs in the same container as the dashboard (`ghcr.io/gethomepage/homepage`), alternatively as a source tree with `pnpm dev`
- **No npm package**: the modules are part of the repository and are not published as a separate library; use is by fork and contribution

## Who is the library suited for?

- **Developers** who want to connect a new service or correct an existing descriptor
- **Advanced users** who want to understand which request a widget actually sends (log, browser network tab)
- **Security-conscious operations** that want to trace why keys never reach the browser
- **Less suited** as a general integration library for own projects: it is tailored to the configuration form of the Homepage dashboard
