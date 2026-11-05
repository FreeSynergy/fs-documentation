# OpenProject - API documentation

## Overview

OpenProject provides an open **REST API v3** under `/api/v3`. Responses are HAL+JSON
(hypermedia links to related resources). Every instance includes an interactive **API
browser** under `/api/docs` that shows all resources available for that version.
Additional machine interfaces: webhooks (outgoing), iCal calendar feeds.

**API kinds at a glance**

| Kind | Use | Status |
|------|-----|--------|
| REST v3 (`/api/v3/...`) | work packages, projects, users, queries, master data | official, HAL+JSON |
| API browser (`/api/docs`) | self-description of your own instance | official |
| Webhooks | work package events outwards | official (module) |
| GraphQL | ❌ not available | - |
| iCal feeds | calendar subscription "my work"/activities | official |

## Authentication

- **Personal API token**: can be created in the account settings; used as `Authorization: Bearer <token>`
- **OAuth 2.0**: authorization code flow and client credentials for apps (registered OAuth application)
- **Session cookie**: works in the same browser session (respect CSRF protection)
- **Basic auth**: possible with username and API token, may be disabled per instance (version-dependent)
- **Permissions**: the API enforces the same project permissions as the UI

## Endpoints

All paths relative to the instance URL, e.g. `https://op.example.org/api/v3/work_packages`. The complete list per version comes from `/api/docs`; not every module has resources in every version (e.g. time tracking — check in the API browser, version-dependent).

### Work packages

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v3/work_packages` | list work packages (filters, sorting, pagination) |
| `POST` | `/api/v3/work_packages` | create a work package |
| `GET` | `/api/v3/work_packages/{id}` | load a single work package |
| `PATCH` | `/api/v3/work_packages/{id}` | change fields, status transition (`_links/status`) |
| `DELETE` | `/api/v3/work_packages/{id}` | delete a work package |
| `POST` | `/api/v3/work_packages/filter` | complex filter operators (AND/OR, set, date) |
| `GET` | `/api/v3/work_packages/{id}/activities` | commented activity stream (pagination) |
| `POST`/`DELETE` | `/api/v3/work_packages/{id}/watchers...` | add/remove watchers (form version-dependent) |
| `POST` | `/api/v3/work_packages/{id}/attachments` | upload an attachment (multipart) |

### Projects, users, queries

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v3/projects` | list projects |
| `POST` | `/api/v3/projects` | create a project (admin permission) |
| `PATCH` | `/api/v3/projects/{id}` | change project settings |
| `GET` | `/api/v3/memberships` | project memberships (formats per version) |
| `GET` | `/api/v3/users` | list users |
| `GET` | `/api/v3/users/{id}` | user profile |
| `GET` | `/api/v3/queries` | load saved queries |

### Master data

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v3/statuses` | work package statuses |
| `GET` | `/api/v3/priorities` | priorities |
| `GET` | `/api/v3/versions` | versions/milestones |
| `GET` | `/api/v3/activities` | project activities (feed) |

## Pagination and filters

- **Offset pagination**: `?offset=1&pageSize=25`; the response contains `total`, `count`, `pageSize`, `offset` in `_embedded`
- **Cursor pagination**: `?startAfter=<id>` for large lists (version-dependent)
- **Elements** live in `_embedded.elements`; each element carries `_links` (self, status, project, ...)

## Examples

### List work packages (personal token)

```bash
curl -s -H "Authorization: Bearer <api-token>" \
  "https://op.example.org/api/v3/work_packages?pageSize=2&offset=1"
```

Response (abridged, HAL+JSON):

```json
{
  "_type": "Collection",
  "total": 137,
  "count": 2,
  "pageSize": 2,
  "offset": 1,
  "_embedded": {
    "elements": [
      {
        "_type": "WorkPackage",
        "id": 421,
        "subject": "Test the login screen",
        "_links": {
          "self": { "href": "/api/v3/work_packages/421" },
          "status": { "href": "/api/v3/statuses/1", "title": "New" },
          "assignee": { "href": "/api/v3/users/7", "title": "anna" }
        }
      }
    ]
  }
}
```

### Create a work package

```bash
curl -s -X POST \
  -H "Authorization: Bearer <api-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "API demo",
    "_links": {
      "type": { "href": "/api/v3/types/1" },
      "project": { "href": "/api/v3/projects/5" },
      "status": { "href": "/api/v3/statuses/1" },
      "priority": { "href": "/api/v3/priorities/2" }
    }
  }' \
  "https://op.example.org/api/v3/work_packages"
```

### Filtering with operators

```bash
curl -s -X POST \
  -H "Authorization: Bearer <api-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "filters": [
      { "status": { "operator": "o", "values": [] } },
      { "project": { "operator": "=", "values": ["/api/v3/projects/5"] } }
    ],
    "sortBy": [{ "id": "updatedAt", "sort": "desc" }]
  }' \
  "https://op.example.org/api/v3/work_packages/filter"
```

## Rate limits

- OpenProject publishes **no central fixed numbers**; the instance may receive limiting via the reverse proxy (nginx/Traefik)
- Heavy `filter` queries cost more than simple `GET` lists — for scripts use lean filters and pagination
- Error case: HTTP 429 under external throttling; honour `Retry-After` if present

## Webhooks

The webhook module (administration) sends JSON to configured HTTPS endpoints:

| Event | Trigger |
|-------|---------|
| `openproject::work_package::created` | work package created |
| `openproject::work_package::updated` | work package changed (field/status change) |

The payload contains the work package as a `data` object (HAL structure). Validity and
additional events: version-dependent, visible in the administration menu "webhooks".

## SDKs and client libraries

- **No official SDK**; the API is deliberately plain REST/HAL
- **Community clients** exist for Python and JavaScript (depending on maintenance state, no warranty; staying with the REST documentation keeps scripts more version-stable)
- **Code generation**: HAL is not OpenAPI — tools read the examples in the API browser `/api/docs`
- **Import scripts**: for migrations (e.g. from Redmine) community scripts exist; officially the import assistants differ per version

## Operational notes

- API tokens are personal: run automation via a service account with minimal permissions
- `/api/docs` is publicly reachable unless the instance disables it — factor the access in

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
