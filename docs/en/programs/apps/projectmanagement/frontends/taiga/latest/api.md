# Taiga - API documentation

## Overview

REST API under `/api/v1/` (JSON) — covers user stories, tasks, issues, epics, sprints,
wiki. Authentication is OAuth2-heavy (password grant for scripts, bearer tokens);
webhooks and an official CLI.

**API kinds at a glance**

| Kind | Use | Status |
|------|-----|--------|
| REST `/api/v1/userstories|tasks|issues|epics|milestones…` | CRUD + filters | official |
| OAuth2 token (`Authorization: Bearer`) | access | official |
| Webhooks | project → HTTP POST (create/change/delete) | official |
| GraphQL | — | ❌ |

## Authentication

```
POST /api/v1/auth  {"username":"bot","password":"…"}
→ {"access_token": "…", "refresh_token": "…"}
```

then `Authorization: Bearer <access_token>`; refresh flow for long-lived jobs.

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/projects?slug=api-rework` | find a project |
| `GET/POST` | `/api/v1/userstories?project=…` | stories |
| `GET/POST` | `/api/v1/tasks?user_story=…` | subtasks |
| `GET/POST` | `/api/v1/issues` | issues |
| `GET/POST` | `/api/v1/epics` (+ `epiccustomfields`) | epics |
| `GET/POST` | `/api/v1/milestones` | sprints |
| `POST` | `/api/v1/userstories/{ref}/assign_points` | set points |
| `GET/POST` | `/api/v1/webhooks/{project_id}` | administer webhooks |

## Example

Request:

```http
POST /api/v1/userstories HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "project": 41, "ref": 14, "subject": "Rate limit headers",
  "story_points": 3, "assigned_to": 7, "milestone": 12 }
```

Response: `201` with the story JSON (`id`, `ref`, `status`, `finish_date` null …).

## Webhooks

Payload: `{ "type": "userstory.change", "project_id":…, "payload":… }` — configured in the
project's integration panel (secret/events).

## Rate limits

by default no hard limits; instance operators throttle via the reverse proxy.

## SDKs and client libraries

- **official**: `taiga` CLI (pip), taiga-events (Python), JS examples
- REST examples in the project documentation; a Postman collection exists

## Frontend note

Story/task/issue/epic/milestone = directly mappable onto the [task/sprint
models](../../../../../../data/models.md).
