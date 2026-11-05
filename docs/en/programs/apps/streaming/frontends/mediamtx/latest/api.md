# MediaMTX - API documentation

## Overview

MediaMTX offers a **REST control API (v3)** on port `9997` (requires `api: yes`, by default only reachable from `localhost`), plus **hooks** (the server calls commands/HTTP), **Prometheus metrics** (`9998`) and a **playback server** (`9996`).

## Authentication

The API uses the same permission system as the media protocols:

| Method | Configuration |
|--------|---------------|
| `internal` | `authInternalUsers` with `action: api`, IP lists (default: `127.0.0.1` may use `api`) |
| `http` | `authHTTPAddress` — one POST per request, 20x = allowed |
| `jwt` | `authJWTJWKS`, claim `mediamtx_permissions`; token in the `Authorization` header |

### Header

```
Authorization: Bearer <jwt>      # with authMethod: jwt
Content-Type: application/json
```

### URL format

```
http://<host>:9997/v3/<area>/<action>[/<name>]
```

## Endpoints (a selection)

### Paths

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v3/paths/list` | active paths with reads, bytes, remote |
| GET | `/v3/paths/get/{name}` | details of a path |

### Configuration at runtime

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v3/config/paths/list` | configured paths |
| POST | `/v3/config/paths/add/{name}` | create a path (JSON body) |
| POST | `/v3/config/paths/edit/{name}` | change a path |
| POST | `/v3/config/paths/remove/{name}` | delete a path |
| POST | `/v3/config/paths/healthcheck/{name}` | check the source |
| GET | `/v3/config/global/get` | global settings |

### Connections and protocol bridges

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v3/connections/list` | active connections incl. type/remote |
| GET/POST | `/v3/rtsp_to_webrtc/list` … | RTSP↔WebRTC bridges |
| POST | `/v3/rtsp_to_webrtc/add/{name}` | create a bridge |
| GET | `/v3/restransmission/list` … | retransmission (UDP hole punching) |

## Examples

### List the active paths

```bash
curl -s http://localhost:9997/v3/paths/list | jq .
```

```json
{
  "itemCount": 1,
  "items": [{
    "name": "test1",
    "ready": true,
    "readers": ["RTSP/TCP client", "HLS client"],
    "bytesReceived": 1048576,
    "bytesSent": 3145728
  }]
}
```

### Create a dynamic path

```bash
curl -X POST http://localhost:9997/v3/config/paths/add/camera2 \
  -H 'Content-Type: application/json' \
  -d '{"source":"rtsp://10.0.0.12:554/stream1","sourceOnDemand":true}'
```

### Python

```python
import requests

api = "http://localhost:9997/v3"
for p in requests.get(f"{api}/paths/list").json()["items"]:
    print(p["name"], p["ready"], len(p["readers"]))

requests.post(f"{api}/config/paths/add/test2",
              json={"source": "publisher"})
```

## Hooks (server → your own application)

Hooks are not webhooks in the classical sense but configuration fields that trigger commands or HTTP calls:

| Hook | Moment |
|------|--------|
| `runOnConnect` / `runOnDisconnect` | connection setup/teardown (variables `MTX_CONN_TYPE`, `MTX_CONN_ID`, `RTSP_PORT`) |
| `runOnPublish` / `runOnPublishDone` / `runOnUnpublish` | a publisher registers/deregisters |
| `runOnReady` / `runOnUnready` | a path becomes ready/not ready |
| `runOnDemand` | the source is started at the first reader |

The HTTP auth hook: `authHTTPAddress` receives a POST with `action`, `path`, `user`, `ip` and decides via the status code.

## Rate limits

- **no documented rate limits** (self-hosted)
- protection through a reverse proxy (nginx/Caddy), `apiTrustedProxies` and a firewall on `9997`

## Webhooks

- no webhooks; event handling runs through hooks or by polling the control API

## SDKs and client libraries

- **OpenAPI/Swagger**: sits in the repository (`apifile.yaml`) → a client can be generated
- **Go**: `github.com/bluenviron/mediamtx` usable as a library
- **An HTTP client in any language** (requests, fetch, axios) — the API is plain JSON
- **Playback SDKs**: hls.js, video.js, the webrtc adapter, ffmpeg/VLC as consumers

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
