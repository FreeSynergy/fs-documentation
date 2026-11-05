# Ant Media Server - API documentation

## Overview

AMS provides a **REST API v2** that covers the same capabilities as the web panel. The complete method reference: `antmedia.io/rest` (Swagger/OpenAPI).

## Base URLs

| Service | Base path |
|---------|-----------|
| Broadcasts | `https://<host>:5443/{application}/rest/v2/broadcasts/…` |
| VoDs | `https://<host>:5443/{application}/rest/v2/vods/…` |
| Management (panel APIs) | `https://<host>:5443/rest/v2/…` |
| Cluster | `https://<host>:5443/rest/v2/cluster/…` |
| HTTP (test) | `http://<host>:5080/{application}/rest/v2/…` |

`{application}` is usually `live`, `WebRTCAppEE` or your own app.

## Authentication

| Method | Effect |
|--------|--------|
| **IP filter** | only approved sender IPs may call REST (app setting) |
| **JWT** | `Authorization: Bearer <token>`, token from your own IdP or issued by AMS |
| Panel session | only for the web panel, not for REST |

### Header

```
Authorization: Bearer <jwt>
Content-Type: application/json
```

## Endpoints (a selection)

### Broadcasts

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/rest/v2/broadcasts/create` | create a stream (JSON: streamId, name, type, …) |
| GET | `/rest/v2/broadcasts/list/{offset}/{size}` | list the streams |
| GET | `/rest/v2/broadcasts/{streamId}` | stream details |
| POST | `/rest/v2/broadcasts/{streamId}/stop` | stop the stream |
| POST | `/rest/v2/broadcasts/{streamId}/delete` | delete the stream |
| POST | `/rest/v2/broadcasts/{streamId}/record/start` | start recording |
| POST | `/rest/v2/broadcasts/{streamId}/record/stop` | stop recording |
| POST | `/rest/v2/broadcasts/{streamId}/restream` | forward to targets (enterprise) |
| GET | `/rest/v2/broadcasts/{streamId}/track-list` | tracks/codecs of a stream |
| GET | `/rest/v2/broadcasts/{streamId}/viewer-count` | active viewers |

### VoD

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/rest/v2/vods/list/{offset}/{size}` | list recordings/uploads |
| POST | `/rest/v2/vods/upload` | file upload (multipart) |
| POST | `/rest/v2/vods/{vodId}/delete` | delete the VoD |

> The exact spelling of some sub-paths varies with the server version — the Swagger docs at `antmedia.io/rest` are authoritative.

## Examples

### Create a stream

```bash
curl -s -X POST http://localhost:5080/live/rest/v2/broadcasts/create \
  -H 'Content-Type: application/json' \
  -d '{"streamId":"concert-1","name":"Concert","type":"livestream",
       "metaData":"{\"mainTrack\":\"concert-1\"}"}'
```

### Start recording

```bash
curl -s -X POST http://localhost:5080/live/rest/v2/broadcasts/concert-1/record/start
```

### Python

```python
import requests

BASE = "https://ams.example.com/live/rest/v2"
HEAD = {"Authorization": "Bearer <jwt>", "Content-Type": "application/json"}

r = requests.post(f"{BASE}/broadcasts/create", headers=HEAD,
                  json={"streamId": "meeting-42", "type": "livestream"})
print(r.json()["streamId"])

for b in requests.get(f"{BASE}/broadcasts/list/0/20", headers=HEAD).json():
    print(b["streamId"], b.get("status"))
```

## Rate limits

- **no documented rate limits** (self-hosted)
- the IP filter and reverse-proxy limits (`limit_req`) are the usual protection

## Webhooks

- AMS can **send webhooks per application**: events such as publish start/end, recording finished, viewer changes
- the target URL and the events are set in the app settings; the payload is JSON
- alternative: interval polling via `viewer-count` and the broadcast details

## SDKs and client libraries

- **JavaScript**: `@antmedia/webrtc_adaptor` (WebSocket/WebRTC, WHIP/WHEP-like), the panel players
- **Android**: the Ant Media Android SDK (Kotlin/Java)
- **iOS**: the Ant Media iOS SDK (Swift/Obj-C)
- **Flutter**: the Ant Media Flutter plugin (enterprise)
- **REST**: any HTTP client (requests, fetch, axios, curl)

## See also

- [menus.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [layout.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [api.md](api.md) (this file)
