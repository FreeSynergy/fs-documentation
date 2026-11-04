# Hotjar - API documentation

## Overview

Hotjar's API is a **read API for organisation/recordings/surveys** plus the **Identify API** inside the tracking script. Heatmap raw data is not exposed via the API (only UI/reports).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST `https://data.hotjar.com/v1/…` (team token) | Recordings, survey answers | official |
| Identify API (`hj('identify', id)`) | User assignment in the tracking | official |
| Site management (API) | Sites/members | limited |
| Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Authentication

- API token per team (settings → API): `Authorization: Bearer <token>` (data API)
- Identify: script configuration, no token in the public code

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/v1/sites/{site_id}/recordings` | Recordings (filter created/pages) |
| `GET` | `/v1/sites/{site_id}/recordings/{uuid}` | Metadata of a session |
| `GET` | `/v1/sites/{site_id}/surveys/{id}/responses` | Survey responses |

*(Endpoint names according to the current developer docs; check the version/plan.)*

## Example

```http
GET /v1/sites/123456/recordings?limit=50&after=2026-10-01 HTTP/1.1
Authorization: Bearer <team-token>
```

Response: `{ "recordings": [ { "id": "…", "pages": [...],
"rage_click_count": 2, "visitor_id": "…" } ] }`

Identify (in the page code):

```js
_hj('identify', 'teilnehmer-4711');
```

## Rate limits

Documented per team (moderate); interview/recording volumes limited per subscription.

## Skin note

Data-protection reservation: replays only with consent + masks; the FreeSynergy skin links heatmap findings onto issue skins (rage click → bug ticket via a Zapier chain).
