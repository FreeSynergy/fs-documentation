# MediaMTX - Menu items

## Overview

MediaMTX has **no interface**. It is operated through the configuration file `mediamtx.yml`, the command line and the control API. The "menu items" are the sections of the configuration.

## Configuration sections (`mediamtx.yml`)

| Section | Content |
|---------|---------|
| `logLevel`, `logDestinations`, `logStructured` | logging (stdout, file, syslog; JSONL) |
| `readTimeout`, `writeTimeout`, `writeQueueSize` | timings and the send queue |
| `authMethod` (`internal`/`http`/`jwt`) + `authInternalUsers` | users, actions (`publish`, `read`, `playback`, `api`, `metrics`, `pprof`), IP lists |
| `rtsp`, `rtmp`, `hls`, `webrtc`, `srt`, `moq` | protocol listeners on/off and addresses |
| `api`, `metrics`, `pprof`, `playback` | additional servers (9997, 9998, 9999, 9996) |
| `pathDefaults` | defaults for all paths |
| `paths` | per path: `source`, `sourceProtocol`, `runOn*` hooks, `record`, `recordPath` |
| `runOnConnect`, `runOnDisconnect` | global hooks (environment variables `MTX_CONN_TYPE`, `MTX_CONN_ID`) |

## Protocol listeners (default ports)

| Protocol | Address | Note |
|----------|---------|------|
| RTSP | `:8554` | TCP handshake, UDP/multicast optional |
| RTSPS | `:8322` | encrypted |
| RTMP / RTMPS | `:1935` / `:1936` | |
| HLS | `:8888` | `hlsVariant`: `lowLatency`, `fmp4`, `mpegts` |
| WebRTC | `:8889` | WHIP/WHEP; ICE-UDP `:8189` |
| SRT | `:8890` (UDP) | |
| MoQ | `:8892` (HTTP/2+HTTP/3), `:8893` (QUIC) | |
| Control API | `:9997` | requires `api: yes` |
| Metrics | `:9998` | Prometheus |
| PPROF | `:9999` | profile reports |
| Playback | `:9996` | download recordings |

## Paths (streams)

| Field | Meaning |
|-------|---------|
| `all`, `all_others`, `test1`, RegExp with `~` | path matching |
| `source: publisher` | received from publishers (default) |
| `source: rtsp://…` / `rtmp://…` / `udp+mpegts://…` | pull from another source (proxy) |
| `sourceOnDemand` | only start the source on demand |
| `record: yes` + `recordPath` | recording (e.g. `/recordings/%path/%Y-%m-%d_%H-%M-%S-%f`) |

## Menus by role

| Role | Access |
|------|--------|
| anonymous | paths according to the `authInternalUsers` permission |
| `publish` | sending to paths (encoder, OBS) |
| `read`/`playback` | consuming and loading recordings |
| `api` | control API, only localhost or explicitly enabled |
| operations | the file `mediamtx.yml`, `systemctl`, Docker environment variables |
