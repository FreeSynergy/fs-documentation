# Asana - API documentation

## Overview

REST v1 under `https://app.asana.com/api/1.0` (JSON). Objects: workspaces, projects, sections, tasks, subtasks, users, teams, custom fields, portfolios. Webhooks for task/project changes.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST v1 | CRUD + relationships, batch | official |
| Webhooks | `x-hook-secret` challenge, task updates | official |
| Batch API (`/batch`) | Up to 10 calls per request | official |
| GraphQL | — | ❌ |

## Authentication

- **Personal access token** (admin/developer settings): `Authorization: Bearer <token>`
- **OAuth2** for apps (authorization code)
- Data access follows the workspace memberships

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/workspaces` | Workspaces |
| `GET` | `/projects?workspace=…` | Projects |
| `POST` | `/projects/{id}/tasks` | Create a task |
| `GET/PATCH/DELETE` | `/tasks/{id}` | Detail/change/delete |
| `POST` | `/tasks/{parent}/subtasks` | Subtask |
| `GET/POST` | `/tasks/{id}/comments` | Comments |
| `POST` | `/tasks/{id}/assignments` | Assign (several) |
| `GET` | `/tasks?project=…&assignee=me&due_on=2026-11-04` | Filtered list |
| `GET` | `/workspaces/{id}/sections` (via project) | Sections |
| `POST` | `/webhooks` | Webhook subscription (resource=id) |

## Example

Request:

```http
POST /api/1.0/projects/12345/tasks HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "data": { "name": "Review the legal notice", "due_on": "2026-11-04",
  "assignee": 9876, "notes": "Needs legal sign-off afterwards" } }
```

Response: `201` → `{ "data": { "gid": "112233", "name": "Review the legal notice", "completed": false } }`

## Webhooks

The registration provides `x-hook-secret` (store it once!). Events: task completed/changed; payload with `x-hook-secret` validation.

## Rate limits

Time-based limits per app/user; on 429 the `Retry-After` header; the response contains an `Asana-Reason` header for diagnosis.

## SDKs and client libraries

- Official clients: Python (`asana`), Node (`asana`), Java/PHP; batch examples in the docs
- Zapier/Make/connectors available

## Skin note

The `gid` IDs + section/portfolio correspond to the [task structure](../../../../../data/models.md); custom fields → [fields.md](../../../../../data/fields.md).
