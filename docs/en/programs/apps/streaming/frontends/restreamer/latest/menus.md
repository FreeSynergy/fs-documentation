# Restreamer - Menu items

## Web UI areas (left menu)

| Area | Description |
|------|-------------|
| Start / dashboard | status: running push streams, player preview, statistics |
| Push key | the secret key for the input (`?key=<pushKey>`), regenerate |
| Player | embedded HLS/HTTP player, direct links, embed code |
| Settings | basic settings, ports, authentication, storage location |
| Advanced settings | nginx-rtmp directives, transcoding, WebRTC, recording interval |
| Multi-target (RTMP restream) | targets with a name and RTMP URL, enable/disable |
| Logs / diagnostics | nginx, Node and ffmpeg logs, support package |

## Settings (selection)

| Field | Content |
|-------|---------|
| HTTP port / HTTPS port | web interface and stream delivery |
| RTMP port | standard input 1935 |
| Web UI password | access protection for the interface |
| Recording | interval (segment size), folder, retention |
| Transcoding | ffmpeg profiles, resolution/FPS, audio codec |
| WebRTC / low latency | optionally switchable on |
| Auto-start | begin the stream when the container starts |

## Menus by role

| Role | Visible |
|------|---------|
| anonymous | player and stream URLs (if allowed) |
| web UI user | all areas after entering the password |
| admin (container) | environment variables, volumes, restart via Docker |
