# Pol.is - API Documentation

## Overview

The **Data API** (`https://pol.is/api/v3/…`, documented at developers.pol.is) returns conversations, comments, ratings and clusters **read-only**. Writing happens through the embedded application (participant actions).

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| Data API read (`/api/v3/conversations/{id}/…`) | Comments, votes, clusters, math report | official |
| Embed (iframe/JS) | Participation on your own page | official |
| Write API for content | Organiser import (access provisioning) | limited |
| Webhooks/GraphQL | — | ❌ |

## Authentication

- Public conversations: API key (request it from the operator) for data exports
- Private conversations: session-based (organiser account)

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/v3/conversations/{id}/summary` | Key figures |
| `GET` | `/api/v3/conversations/{id}/comments` | All comments (moderation status) |
| `GET` | `/api/v3/conversations/{id}/votes` | Ratings (anonymous-voter-id) |
| `GET` | `/api/v3/conversations/{id}/math-report` | Cluster mathematics (group votes) |

## Example

```http
GET /api/v3/conversations/12345/comments HTTP/1.1
x-api-key: <key>
```

Response (excerpt):

```json
[ { "comment_id": 903, "txt": "More trees, fewer parking strips",
    "moderation": 0, "aggregate_authorship_display": true } ]
```

## Rate limits

Depends on the API key; large exports via batch download in the organiser panel.

## Skin note

Result skin: embed `math-report` as consensus and group widgets in the wiki. Avoid personal references (anonymised voter IDs stay anonymised).
