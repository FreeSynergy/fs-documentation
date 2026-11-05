# Restreamer - Structure and UI/UX

## Overview

The Restreamer consists of three processes in one Docker container (nginx with
nginx-rtmp-module, Node.js web UI, ffmpeg) and a single web interface. This file describes
the web UI screens, player embedding and the process/port structure.

## Web UI (default layout)

```
┌────────────────────────────────────────────────────────────────────┐
│ Restreamer                                    [language] [logout]  │
├───────────────┬────────────────────────────────────────────────────┤
│ Menu          │  Content of the chosen screen                      │
│ ▸ Start       │   Start: status banner (stream offline/online),    │
│   Push Key    │   player preview, statistics (viewers, bitrate),   │
│   Player      │   shortcuts for the push/play URLs                 │
│   Settings    │   Push Key: show/copy/regenerate the key           │
│   Advanced    │   Player: preview player, direct links,            │
│   Logs        │            embedding snippet                       │
│               │   Settings / Advanced: forms (see menu.md)         │
└───────────────┴────────────────────────────────────────────────────┘
```

- Screens are simple forms or info panels; actions are always buttons inside the screen
- Status (running stream yes/no) at the top of the start screen, additionally coloured (green = live)

## Process and port structure

```
Docker container "restreamer"
 ├── nginx + nginx-rtmp-module   RTMP reception :1935, HLS delivery :8080
 ├── Node.js web UI              admin interface + internal API :8080/:8081
 └── ffmpeg                      transcoding and segment recording (on_demand)
```

- Persistence via volumes: `/opt/restreamer/var/media` (segments), `/var/statistics`
- HTTPS (port 8081) with a self-generated certificate, switchable off

## Player embedding

- The player screen shows a ready-made `<iframe>` snippet (HLS player) to copy; size adjustable via attributes
- Alternatively direct links: the HLS playlist (`…/hls/stream.m3u8`) and MP4 segments for download
- Embedding works in any web page/FreeSynergy gallery frontend, since only HTTP is needed

## UI/UX

- Plain light-dark layout with no theme options; the web UI is functional, not designable
- Every screen contains explanatory text directly above the fields (self-service without studying the docs)
- Risky actions (regenerating the push key) come with a confirmation prompt

## Interactions

- Configuration almost exclusively via forms; saving takes effect after restarting the container
- Logs are viewable, but without live streaming of the logs in the UI (download/support package)

## Responsive design

| Platform | Behaviour |
|----------|-----------|
| Desktop browser | full layout with a fixed side menu |
| Mobile browser | menu collapsible, forms single-column |
| Native apps | ❌ none (access only via the browser) |

## Accessibility

- Simple HTML forms, tab order present; screen-reader testing only limited (⚠)
- Status not only coloured but also as text ("online"/"offline")
- No official shortcuts (see [shortcuts.md](shortcuts.md))

## Performance

- One push source, any number of HLS readers; scaling via nginx workers and a CDN in front of the player
- Transcoding optional — without an ffmpeg profile the stream runs on minimal CPU
