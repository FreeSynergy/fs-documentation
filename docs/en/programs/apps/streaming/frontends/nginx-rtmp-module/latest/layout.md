# nginx-rtmp-module - Structure & UI/UX

## Overview

The objects you operate are the `nginx.conf` and the output directory. This file describes how the inputs, paths and delivery routes work together — the template for a skin interface.

## Process and configuration structure

### Main areas

```
                    nginx (one master, several workers)
┌───────────────────────────────────────────────────────────────────┐
│  rtmp { }            http { }                                      │
│  ─────────           ──────────                                    │
│  listen 1935         listen 80/443  (TLS, CORS, cache)             │
│   application live    location /live/  → /var/www/hls/live/        │
│     live on           location /stat   → rtmp_stat all             │
│     hls on            location /dash/  → /var/www/dash/live/       │
│     hls_path /var/www/hls                                          │
└───────────────────────────────────────────────────────────────────┘
        ▲                                        │
        │ rtmp publish                           ▼ m3u8/TS files
   OBS / ffmpeg                              browser (hls.js)
```

### Input side

- `application live` is the room: the stream name yields `rtmp://host/live/<name>`
- the `on_publish` hook can refuse before the connection is set up
- `exec` commands run as a child process per stream

### Output side

- HLS: `/var/www/hls/<name>/index.m3u8` plus `indexN.ts` (with `hls_nested` one folder per stream)
- DASH: `/var/www/dash/<name>/index.mpd`
- delivery, caching, CORS and TLS are entirely normal nginx settings

### Configuration layers

| Layer | File/route |
|-------|------------|
| Main | `nginx.conf` (the `rtmp` and `http` blocks) |
| Include | `include /etc/nginx/apps/*.conf;` sensible per application |
| Hooks | `on_publish http://127.0.0.1:9000/rtmp/publish` |

## UI/UX (transfer onto a skin interface)

### Design principles

- **Configuration as the primary interface**: the view shows the application blocks and their directives
- **Make the filesystem visible**: the HLS/DASH paths and the age of the segments are directly inspectable
- **Status as an XML view**: `rtmp_stat` is the reference for live views

### Colour scheme and typography

- no interface of its own; for a skin: config blocks in monospace, status values in a table
- recommendation: application = accent colour, directives = neutral, errors (timeouts) = red

### Interactions

- reload without interruption: `nginx -t && nginx -s reload` (streams may restart in the process)
- the hook answers are the only "button" at runtime (allow/refuse access)

## Accessibility

- configuration is text → versionable, readable aloud, diffable
- status page: XML without a stylesheet is friendlier to screen readers than the XSL HTML version
- browser playback needs its own accessibility in the player (subtitles, keyboard)

## Performance

- the HLS segmentation (`hls_fragment`) determines latency; small segments raise the request load
- `out_queue`/`max_message` limit slow viewers
- `idle_streams on` keeps costing CPU/bandwidth — set it to `off` for expensive sources
- many parallel publishers scale over several nginx instances (relay via `pull`)
