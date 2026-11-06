# Redmine - API documentation

## Overview

Redmine contains a **REST API** in the core: every collection or detail resource is
reachable under its path with the extension `.xml` or `.json` (JSON is officially fully
supported since Redmine 4.0). Additionally Redmine provides **Atom feeds** (`.atom`) and
**ICS calendar feeds**. GraphQL, a WebSocket API or webhooks do not exist in the core.

**API kinds at a glance**

| Kind | Use | Status |
|------|-----|--------|
| REST (`/issues.json` etc.) | issues, projects, users, time tracking, master data | official (XML/JSON) |
| Atom feeds (`.atom`) | issues, activities, the account's activity feed | official |
| ICS feeds | calendar subscription (URL with token) | official (path version-dependent) |
| Webhooks | ❌ not in the core — plugins only | - |
| GraphQL / WebSocket | ❌ not available | - |

## Authentication

- **API key**: can be created under "my account"; passed as `?key=<apikey>` or header `X-Auth-Token: <apikey>`
- **Basic auth**: username/password in the authorization header
- **Session cookie**: API calls made from within the browser session
- The API key is personal; permissions match the account's project roles

## Endpoints

All paths relative to the instance URL, e.g. `https://redmine.example.org/issues.json`. Not every module has endpoints — **wiki pages** have no REST endpoints in the core (workarounds: plugin or browser automation).

### Issues

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/issues.(xml\|json)` | list issues; filters: `project_id`, `tracker_id`, `status_id`, `assigned_to_id`, `created_on`, `limit`, `offset` |
| `GET` | `/issues/{id}.(xml\|json)` | detail; `?include=children,journals,attachments,relations,watchers,changesets,allowed_statuses` |
| `POST` | `/issues.(xml\|json)` | create an issue (project by name or ID) |
| `PUT` | `/issues/{id}.(xml\|json)` | change fields, append a note, change status |
| `DELETE` | `/issues/{id}.(xml\|json)` | delete an issue |
| `GET` | `/issues/{id}/children.(xml\|json)` | sub-issues |
| `PUT`/`DELETE` | `/issues/{id}/watchers.(xml\|json)` | add/remove watchers (user ID in the body) |

### Projects, users, time tracking

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/projects.(xml\|json)` | list projects |
| `GET` | `/projects/{id}.(xml\|json)` | project details (`?include=trackers,issue_categories,versions,members`) |
| `POST`/`PUT`/`DELETE` | `/projects.(xml\|json)` | administer projects (admin) |
| `GET` | `/projects/{id}/issue_categories.(xml\|json)` | the categories of a project |
| `GET` | `/projects/{id}/memberships.(xml\|json)` | memberships and roles |
| `GET` | `/users.(xml\|json)` | list users (admin) |
| `GET` | `/users/current.(xml\|json)` | the signed-in account |
| `GET` | `/time_entries.(xml\|json)` | time entries with filters |
| `POST`/`PUT`/`DELETE` | `/time_entries/{id}.(xml\|json)` | create/change/delete a time entry |

### Master data, attachments, other

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/enumerations.(xml\|json)` | status, priorities, activities, document categories |
| `GET` | `/trackers.(xml\|json)` | trackers |
| `GET` | `/issues/{id}/attachments/{attachment_id}` | download an attachment |
| `DELETE` | `/attachments/{id}.(xml\|json)` | delete an attachment |
| `POST` | `/uploads.(xml\|json)?filename=NAME` | upload a file, returns the token for issue attachments |
| `GET` | `/queries.(xml\|json)` | public queries |
| `GET` | `/news.(xml\|json)` | project news (filter `project_id`) |
| `GET` | `/projects/{id}/versions.(xml\|json)` | milestones/versions |

## Pagination

- Parameters `limit` (maximum **100**) and `offset`
- Response attributes: `total_count`, `limit`, `offset` (JSON: `limit`/`offset`/`total_count` at the top level, XML: attributes of the root element)

## Examples

### Fetch issues

```bash
curl -s -H "X-Auth-Token: <apikey>" \
  "https://redmine.example.org/issues.json?project_id=core&status_id=open&limit=2"
```

Response (abridged):

```json
{
  "issues": [
    {
      "id": 1234,
      "project": { "id": 5, "name": "Core" },
      "tracker": { "id": 1, "name": "Bug" },
      "status": { "id": 1, "name": "New" },
      "priority": { "id": 2, "name": "Normal" },
      "subject": "Login aborts",
      "author": { "id": 7, "name": "Anna Berg" },
      "created_on": "2026-10-30T09:12:00Z",
      "spent_on": null
    }
  ],
  "total_count": 87,
  "limit": 2,
  "offset": 0
}
```

### Create an issue

```bash
curl -s -X POST \
  -H "X-Auth-Token: <apikey>" \
  -H "Content-Type: application/json" \
  -d '{
    "issue": {
      "project_id": "core",
      "tracker_id": 1,
      "subject": "Document the API connection",
      "priority_id": 2,
      "description": "collect curl examples",
      "assigned_to_id": 7,
      "notes": "created via the API"
    }
  }' \
  "https://redmine.example.org/issues.json"
```

Success: HTTP 201, the response contains the complete issue object.

### Upload an attachment (two steps)

```bash
# 1. upload the file -> token
curl -s -X POST --data-binary "@report.pdf" \
  -H "X-Auth-Token: <apikey>" \
  "https://redmine.example.org/uploads.json?filename=report.pdf"

# 2. pass the token when creating the issue
curl -s -X POST -H "X-Auth-Token: <apikey>" \
  -H "Content-Type: application/json" \
  -d '{"issue":{"project_id":"core","tracker_id":1,"subject":"Attachment",
       "uploads":[{"token":"<token>","filename":"report.pdf","content_type":"application/pdf"}]}}' \
  "https://redmine.example.org/issues.json"
```

## Rate limits

- Redmine ships **no built-in rate limiting**
- Throttling via the web server/proxy (nginx `limit_req`, Apache `mod_ratelimit`) recommended
- Heavy list queries without `limit` slow down the instance instead of the client — always use `limit`/`offset`

## Webhooks

- **Not in the core**: outgoing webhooks only as a plugin (e.g. "redmine_webhook"-style extensions; availability and event scope version-dependent)
- **Incoming**: the repository post-receive URL (`/repositories/{identifier}/fetch_changesets?key=...`) updates changesets; issue comments via e-mail delivery are also possible (setup effort)

## SDKs and client libraries

- **Python**: `redminelib` (widespread community client)
- **Ruby/PHP/JavaScript**: community clients of varying maintenance, without official affiliation
- **Officially**: no SDKs — REST with `curl`, `requests` or `httpx` is the standard way
- **CLI alternative**: `rails runner` scripts on the server for bulk side work (administration, not a public-API substitute)

## Operational notes

- Rotate the API key if automation accounts appear compromised (settings in the user account)
- `.xml`/`.json` is part of the path — content negotiation via `Accept` does not work as a substitute

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
