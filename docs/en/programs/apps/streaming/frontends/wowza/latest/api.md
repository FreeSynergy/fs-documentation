# Wowza Streaming Engine - API documentation

## Overview

The access route is the **REST server API v2** (standard port `8087`): it mirrors the manager functions (connections, applications, restream targets, restarts) as JSON/HTTP. Reference: the vendor's developer documentation (`wowza.com/developer`). For your own behaviour inside streams there is additionally the **Java module API**.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST server API v2 | Connections, apps, properties, restream, restart | official |
| Java module API | your own auth, event hooks in the stream lifecycle | official |
| Manager session | web interface only | ❌ not for automation |
| Wowza Streaming Cloud (WSC) | the former cloud service | ⚠ discontinued, do not use any more |

## Authentication

Basic auth with the manager account (accounts in `managernames.properties`).

### Header

```
Authorization: Basic base64(user:pass)
Content-Type: application/json
```

## Endpoints (a selection)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/connections` | active inputs/outputs |
| GET | `/v2/instances` | instances (`_definst_`) |
| GET | `/v2/instances/{id}/applications` | list the applications |
| POST | `/v2/instances/{id}/applications/{app}/start` | start the application |
| POST | `/v2/instances/{id}/applications/{app}/stop` | stop the application |
| POST | `/v2/instances/{id}/applications/{app}/restart` | restart the application |
| GET | `/v2/instances/{id}/applications/{app}/restream` | read the restream targets |
| PUT | `/v2/instances/{id}/applications/{app}/restream` | set the restream targets |
| GET | `/v2/instances/{id}/applications/{app}/properties/{propName}` | read a property |
| PUT | `/v2/instances/{id}/applications/{app}/properties/{propName}` | set a property |
| GET | `/v2/instances/{id}/applications/{app}/streamgroups` | running live groups |

## Examples

### Restart an application

```bash
curl -s -u admin:secret -X POST \
  http://localhost:8087/v2/instances/_definst_/applications/live/restart
```

### Python

```python
import requests

BASE = "http://wowza.example.com:8087/v2"
AUTH = ("admin", "secret")

for app in requests.get(f"{BASE}/instances/_definst_/applications",
                        auth=AUTH).json()["Applications"]["Application"]:
    print(app["name"], app["status"])
```

## Events (input/output)

❌ no built-in webhooks (❌). The substitute: Java modules with lifecycle callbacks (`onPublish`, `onPlay`, `onPublishDone` …) that send the HTTP calls to your own services from there.

## Rate limits

No documented quotas (self-hosted). Protection through a reverse proxy and firewalls; on the network side the API belongs behind administrative access.

## SDKs and client libraries

- **officially**: the Java module API (in the installation tree), the REST documentation with examples
- **Community**: REST wrappers for Python/Node, admin scripts (included in the Docker images)
- **On the player side**: hls.js, video.js, Shaka and others via the playback URLs

## Frontend note

Virtual host → application → stream correspond to the standard model ([models.md](../../../../../../data/models.md)); the URL, key and field properties follow [fields.md](../../../../../../data/fields.md).
