# Dashy - API Documentation

## Overview

Dashy provides an **optional REST API** for reading and writing the configuration. It is served by the Node server and is therefore available in container and bare-metal installations, but **not** with purely static hosting (Netlify, Vercel, CDN). The API is disabled by default.

**Interfaces at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST (`/api/config/...`) | Read/write configuration files, sections and tiles | Officially documented, opt-in |
| Configuration file | `user-data/conf.yml` or `conf.json` as the main interface | Official |
| JSON schema | `ConfigSchema.json` for validating the configuration | Official |
| OpenSearch | `/opensearch.xml` for browser search fields | Official |
| Webhooks | ❌ Not available | — |

## Activation

```yaml
# docker-compose.yml (excerpt)
services:
  dashy:
    image: lissy93/dashy
    environment:
      - ENABLE_API=true
```

Without `ENABLE_API=true`, all `/api/*` requests respond with `404`.

## Authentication

- **Existing server authentication**: Access the API with a regular Dashy login. Read endpoints require a signed-in person, write endpoints require the **admin** role.
- **HTTP Basic**: when Basic auth is enabled (`ENABLE_HTTP_AUTH` or `BASIC_AUTH_USERNAME` / `BASIC_AUTH_PASSWORD`), it can be used with `curl -u`.
- **OIDC / Keycloak / Zitadel**: send the identity token as a Bearer token.
- **API token**: set `API_TOKEN` and send it as `Authorization: Bearer <token>`. A valid token grants full (admin) access and works alongside any other method. If no other protection is configured, the token protects the API against anonymous access.
- Without any authentication the API is open — like the rest of the installation.

```bash
curl -u alice:example-password https://dashy.local/api/config
curl -H 'Authorization: Bearer <id-token>' https://dashy.local/api/config
curl -H 'Authorization: Bearer <API_TOKEN>' https://dashy.local/api/config
```
## Endpoints

`:filename` is a YAML file in the user folder (`conf.yml` or a subpage such as `home-lab.yml`). `:key` is one of the top-level keys `pageInfo`, `appConfig`, `sections` or `pages`. `:sid` and `:iid` are either zero-based indices (`0`, `1`, …) or exact names (URL-encoded).

### Configuration files

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/config` | List configuration files |
| `GET` | `/api/config/:filename` | Complete file as JSON |
| `PUT` | `/api/config/:filename` | Replace the file completely |
| `GET` | `/api/config/:filename/:key` | Read a top-level key |
| `PUT` | `/api/config/:filename/:key` | Replace a top-level key |

### Sections

| Method | Endpoint | Description |
|---------|----------|--------------|
| `POST` | `/api/config/:filename/sections` | Create a section (`name` required) |
| `GET` | `/api/config/:filename/sections/:sid` | Read a section |
| `PATCH` | `/api/config/:filename/sections/:sid` | Change fields of a section |
| `DELETE` | `/api/config/:filename/sections/:sid` | Delete a section |

### Tiles (items)

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/config/:filename/sections/:sid/items` | List tiles of a section |
| `POST` | `/api/config/:filename/sections/:sid/items` | Create a tile (`title` required) |
| `GET` | `/api/config/:filename/sections/:sid/items/:iid` | Read a single tile |
| `PATCH` | `/api/config/:filename/sections/:sid/items/:iid` | Change fields of a tile |
| `DELETE` | `/api/config/:filename/sections/:sid/items/:iid` | Delete a tile |

**Semantics**: `PATCH` performs a shallow merge — submitted fields are changed, nested values (such as the `items` array of a section) are replaced completely. `PUT` replaces the target completely. All bodies are JSON; errors respond with an appropriate status code.

```json
{ "success": false, "message": "Section not found" }
```

## Examples

### List files

```bash
curl -H 'Authorization: Bearer <API_TOKEN>' https://dashy.local/api/config
```

```json
{
  "success": true,
  "files": ["conf.yml", "home-lab.yml"]
}
```

### Create a tile

```bash
curl -X POST -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"title":"Grafana","url":"https://grafana.local","icon":"hl-grafana"}' \
  https://dashy.local/api/config/conf.yml/sections/0/items
```

Response (paraphrased):

```json
{
  "success": true,
  "item": {
    "title": "Grafana",
    "url": "https://grafana.local",
    "icon": "hl-grafana"
  }
}
```

### Rename a section

```bash
curl -X PATCH -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Monitoring"}' \
  https://dashy.local/api/config/conf.yml/sections/Medien
```

### Set a theme

```bash
curl -X PUT -H 'Authorization: Bearer <API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{"theme":"nord-frost"}' \
  https://dashy.local/api/config/conf.yml/appConfig
```

Reload the page after each change until the new configuration appears.

## Configuration file as interface

Alongside the API, the file itself is the regular way:

The user folder `user-data/` contains `conf.yml` (main file), the files of the subpages, custom widget components and the folder `config-backups/` with the backups.

Important top-level sections:

| Key | Content |
|-----------|--------|
| `pageInfo` | Title, description, logo, footer |
| `appConfig` | Theme, search, default view, status checks, language, authentication |
| `sections` | Sections with `name`, `displayData`, `items`, `widgets` |
| `pages` | References to subpages |

The main file is checked against the bundled JSON schema when saved; invalid content is rejected.

## Limits and behavior when writing

- Comments, anchors and custom formatting are lost when writing (in the file and via the API)
- Before every write, a backup is stored in `user-data/config-backups/` (can be disabled with `DISABLE_CONFIG_BACKUPS=true`)
- Configuration files are limited to **256 KB**
- Concurrent write requests follow "last one wins", without locking or version checks
- Subpage files are **not** checked against the schema, because they may contain only parts

## Rate limits

- Dashy does not ship with a **documented rate limit** for the API.
- Meaningful protection comes from the reverse proxy (nginx `limit_req`, Traefik middleware) and from authentication.

## Webhooks and internal eventing

- **No webhooks**, no event output, no notifications from the API.
- **Internal**: the Node server answers status checks for tiles at intervals; the interface updates the indicators and widgets by polling again.

## SDKs and client libraries

- **No official SDK.** The API is classic JSON over HTTP and is used with `curl`, `fetch`, `axios`, `requests` or Python `httpx`.
- **JSON schema** (`ConfigSchema.json`) can be used in pipelines for validation before a file is rolled out.

## Security notes

- Choose a long, random `API_TOKEN` (for example `openssl rand -hex 32`) and send it only over HTTPS
- Restrict write access to admin accounts or the token

## See also

- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
