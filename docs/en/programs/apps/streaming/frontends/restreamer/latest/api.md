# Restreamer - API documentation

## Overview

The Restreamer has no formal public API. The access path is the interplay of **RTMP
input**, **HTTP/HLS output**, **hooks** (nginx-rtmp events to scripts/HTTP) plus
**`restreamer-cli`** and the config file for configuring from outside. The web UI's JSON
endpoints are unofficial and may change.

**Access paths at a glance**

| Path | Use | Status |
|------|-----|--------|
| RTMP(S) push | stream input | official |
| HLS/MP4 URLs | playback and download | official |
| Hooks (`on_publish` …) | your own logic on events | official (nginx-rtmp) |
| `restreamer-cli` | settings without the web UI | official |
| `/opt/restreamer/config.json` | set the declarative state | official |
| web UI JSON endpoints | internal UI calls | ⚠ unofficial, version-dependent |

## Input and output

| Purpose | Address (default) |
|---------|-------------------|
| Push (from OBS/ffmpeg) | `rtmp://<host>:1935/live/stream?key=<pushKey>` |
| HLS playlist (player) | `http://<host>:8080/hls/stream.m3u8` |
| HLS segment list/files | `http://<host>:8080/hls/…` |
| Recorded segments | `http://<host>:8080/media/…` (volume `var/media`) |
| Web interface | `http://<host>:8080`, `https://<host>:8081` |

The push key is the only secret of the input; it travels in the query parameter `key` and
can be rotated in the web UI.

## Authentication

- **Input**: a push key per stream (`?key=…`), optionally an IP restriction via nginx directives
- **Web UI**: one password (session cookie), no user concept
- **Output**: ❌ no token-protected HLS delivery (❌, protection only in front of it)

## Hooks (events)

nginx-rtmp hooks are configurable as environment variables or directives and call scripts
or HTTP endpoints:

| Hook | When |
|------|------|
| `on_publish` | the push begins (here you can refuse: HTTP != 200) |
| `on_publish_done` | the push ends |
| `on_record_done` | one recording segment is finished |
| `on_dvr` | a segment written for the recording |

### Hook example (HTTP)

```
on_publish http://hooks.example.com/restreamer/publish
```

The call is a `POST` with nginx-rtmp form data (`callid`, `streamid`, `remote_addr` …);
response status 200 allows, anything else refuses.

## Configuration from outside

```bash
# read/set a setting (syntax per version, show the help)
docker exec restreamer /opt/restreamer/bin/restreamer-cli help
docker exec restreamer /opt/restreamer/bin/restreamer-cli config set \
  --key webui_password --value 's3cret'

# declarative approach: edit the config file and restart the container
docker cp restreamer:/opt/restreamer/config.json ./config.json
# … edit …
docker cp ./config.json restreamer:/opt/restreamer/config.json
docker restart restreamer
```

## Example: testing the stream from outside

```bash
# 10 seconds of test push with ffmpeg
ffmpeg -re -f lavfi -i testsrc=size=1280x720:rate=30 \
  -f lavfi -i sine -t 10 \
  -c:v libx264 -preset veryfast -c:a aac \
  -f flv "rtmp://localhost:1935/live/stream?key=PUSHKEY"

# check the HLS
curl -s http://localhost:8080/hls/stream.m3u8 | head -5
```

## Rate limits

No documented quotas (self-operated). Practical limits: nginx workers, bandwidth and an
optionally fronted reverse proxy (`limit_req`).

## SDKs and client libraries

- ❌ no official SDK (❌)
- Ecosystem: nginx-rtmp directives, ffmpeg/OBS as push clients, any HTTP client for hooks
- `restreamer-cli` is the only automation interface shipped

## Frontend note

Input/target/segment correspond to the standard model ([models.md](../../../../../../data/models.md));
the URL and key fields follow [fields.md](../../../../../../data/fields.md).
