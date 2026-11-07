# Apache Airflow - API Documentation

## Overview

**Stable REST API v2** (`/api/v2`, JSON) replaces the former unstable API: DAGs, DAG runs, task instances, connections/variables, import of DAG files. Complemented by the CLI (same capabilities) and event-driven triggers (datasets, triggerer).

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST `/api/v2/dags`, `/dagRuns`, `/taskInstances` | Management/status | officially stable |
| `POST /api/v2/importDags` | Upload DAG code (DAGs folder writable) | official |
| CLI `airflow …` | everything incl. RBAC | official |
| Incoming webhooks | not built in (build yourself via API trigger/triggerer) | ❌ native |
| GraphQL | — | ❌ |

## Authentication

- Session login (UI/cookies), **HTTP Basic** (local accounts via FAB/RBAC), JWT (configurable)
- Recommendations: dedicated API users with `Observer`/`Triggerer` roles

## Core endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/api/v2/dags` | DAG list (filters `paused`, `tags`) |
| `PATCH` | `/api/v2/dags/{dag_id}` | Pause on/off |
| `POST` | `/api/v2/dags/{dag_id}/dagRuns` | Start run (`logical_date`, `conf`) |
| `GET` | `/api/v2/dags/{dag_id}/dagRuns` | History |
| `GET` | `/api/v2/dags/{dag}/tasks/{task}/instances` | Task states |
| `GET` | `/api/v2/…/taskInstances/{task}/{run}/logs/{try}` | Log file |
| `POST` | `/api/v2/importDags/{file_token}` | DAG file upload |
| `GET/POST/PATCH` | `/api/v2/connections`, `/variables` | Configuration |

## Example

Start a run:

```http
POST /api/v2/dags/etl_nightly/dagRuns HTTP/1.1
Authorization: Basic <api_user>
Content-Type: application/json

{ "logical_date": "2026-10-30T00:00:00Z",
  "conf": { "kunde": 4711 } }
```

Response: `200` → `{ "dag_run_id": "manual__…", "state": "queued", "conf": {…} }`

## Event pattern (instead of webhooks)

- **Datasets**: `dag A >> outlet="s3://x/events"`, `dag B >> inlet=` → automatic triggering
- Triggerer sensors start DAGs on external conditions (own sensor class polls the API)

## Rate limits

Not built in; capacity is governed by the API server/reverse proxy.

## SDKs and client libraries

- `apache-airflow-client` (official Python SDK, generated from OpenAPI)
- OpenAPI spec (`/api/v2/openapi.json`) → own clients

## Skin note

DAG/task-instance model as reference for planned workflows in [models.md](../../../../../../data/models.md); configuration via connections/variables mirrors credential models.
