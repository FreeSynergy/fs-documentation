# nginx-rtmp-module - Menu items

## Overview

There is **no interface**. The "menu items" are the configuration blocks in `nginx.conf` and the status page; everything else is done by hooks and `exec` commands.

## Configuration blocks

| Block | Content |
|-------|---------|
| `rtmp { server { … } }` | the RTMP server, `listen 1935`, timeouts, `chunk_size` |
| `application <name> { … }` | one "app" = one stream room (`live`, `stream`, …) |
| `live on` | live mode: pass through instead of playing a file |
| `hls on` + `hls_path` | HLS output (segments + playlist into the directory) |
| `dash on` + `dash_path` | MPEG-DASH output |
| `record all\|video\|audio` | recording, `record_path`, `record_unique` |
| `exec` / `exec_async` | start external commands (usually ffmpeg) per publish |
| `pull rtmp://…` | relay: pull the stream from another instance |
| `on_publish` / `on_play` | HTTP hooks for access control |
| `http { … rtmp_stat all; }` | status page as XML, optionally with `stat.xsl` |

## Important directives (a selection)

| Directive | Default | Meaning |
|-----------|---------|---------|
| `listen` | `1935` | RTMP port |
| `timeout` | `180s` | inactivity timeout |
| `drop_idle_publisher` | `10s` | discards publishers that do not send |
| `ping_interval` / `ping_timeout` | `8s` / `8s` | keepalive to the client |
| `chunk_size` | `4096` | RTMP chunk size |
| `interleave` | `on` | mix audio/video into one channel |
| `wait_key` / `wait_video` | `on` / `on` | only send starting from a keyframe |
| `idle_streams` | `on` | keep running streams without viewers |
| `publish_notify` | `off` | client notifications on status changes |
| `hls_fragment` / `hls_playlist_length` | `5s` / `30s` | HLS segmentation |
| `hls_nested` | `off` | its own subfolder per stream |
| `record_append` / `record_unique` | `off` / `off` | the behaviour of recording |

## Status page

```nginx
http {
    server {
        location /stat  { rtmp_stat all; rtmp_stat_stylesheet stat.xsl; }
        location /      { root /var/www/hls; }   # HLS/DASH delivery
    }
}
```

## Menus by role

| Role | Access |
|------|--------|
| Publisher | `rtmp://host/live/<streamname>` — access can only be secured through `on_publish` |
| Viewer | HLS/DASH through nginx (`/live.m3u8`) or RTMP play |
| Operator | `nginx.conf`, `nginx -t`, `nginx -s reload` |
| Automation | HTTP hooks and `exec` scripts |
