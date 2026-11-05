# Jira - API documentation

## Overview

The REST API under `https://<site>.atlassian.net/rest/api/3/…` (formerly `/rest/api/2`; both maintained, v3 is the official one). JQL in `search`, issues/fields/boards separate; webhooks via connect apps or the platform's own automation.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST `/rest/api/3/issue`, `/search`, `/field` | Issue CRUD, JQL, metadata | official |
| REST agile `/rest/agile/1.0` | Boards, sprints, backlog | official |
| Webhook subscriptions (connect/forge) | issue_created/updated… | official |
| GraphQL | Only selected areas | ❌ generally not |

## Authentication

- **Cloud**: HTTP basic `e-mail:API token` or OAuth2 (3LO/apps); **data center**: PAT (`Authorization: Bearer`)
- Permissions = Jira roles (the API sees what the user sees)

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/rest/api/3/issue` | Create an issue (fields object) |
| `GET` | `/rest/api/3/issue/{key}` | Detail |
| `PUT/PATCH` | `/rest/api/3/issue/{key}` | Change (`update` operations) |
| `POST` | `/rest/api/3/issue/{key}/transitions` | Status change (transition ID) |
| `GET` | `/rest/api/3/search?jql=…` | JQL search (also POST /search/jql) |
| `GET` | `/rest/api/3/issue/{key}/comment` | Comments |
| `GET` | `/rest/agile/1.0/board/{id}/sprint` | Sprints |
| `GET` | `/rest/api/3/field` | Field catalogue |
| `POST` | `/rest/api/3/issue/{key}/attachments` | File (base64/multipart) |

## Example

Request:

```http
POST /rest/api/3/issue HTTP/1.1
Authorization: Basic base64(bot@mail.com:API_TOKEN)
Content-Type: application/json

{ "fields": {
  "project": {"key": "WEB"},
  "summary": "Login-Formular validieren",
  "issuetype": {"name": "Task"},
  "assignee": {"accountId": "5d1b…"},
  "labels": ["frontend"] } }
```

Response: `201` → `{ "id": "10042", "key": "WEB-15", "self": "…/issue/10042" }`

Status change:

```json
{ "transition": { "id": "31" } }
```

## Rate limits

Cloud: tiered (~4,000 requests per 10-second window per user across all apps; app and product limits additionally) — headers `X-RateLimit-*`/429 `Retry-After`.

## SDKs and client libraries

- Official clients (the Atlassian Python API community `atlassian-python-api`), connect/forge apps as the app model
- CLI: `atlas` (Atlassian Labs, beta status), JQL in scripts

## Skin note

The status transitions (edges with permissions) are the reference pattern for workflow skins; JQL field names → [fields.md](../../../../../data/fields.md).
