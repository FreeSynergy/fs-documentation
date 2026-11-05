# Ant Media Server - Structure & UI/UX

## Overview

AMS is a Tomcat process with a panel (standard ports `5080`/`5443`) and media ports. This file describes the panel layout, the process architecture and the arrangement of applications and streams.

## Window structure

### Main areas (panel)

```
┌───────────────────────────────────── Ant Media Server Panel ─────────────────────────┐
│ Logo │ Application picker (live ▾) │ Admin menu (Settings, Cluster, SSL, Logout)     │
├──────────────┬───────────────────────────────────────────────────────────────────────┤
│ Sidebar      │  Content                                                             │
│              │                                                                       │
│ Home / Apps  │  Stream tiles: status, viewers, bitrate, actions (●/■/🔗/⏺)         │
│ Live Stream  │  "Create New Stream" + buttons                                      │
│ VoD          │  VoD table (status, preview, actions)                               │
│ Dashboard    │  Charts (CPU, RAM, throughput, viewers)                             │
│ Settings     │  Forms (security, restreaming, cluster)                             │
└──────────────┴───────────────────────────────────────────────────────────────────────┘
```

### Process and port structure

```
Tomcat (one JVM process)
 ├── Panel + REST v2          HTTP :5080   HTTPS :5443
 ├── RTMP Ingest              :1935 (RTMPS configured)
 ├── RTSP / SRT Ingest        camera-specific ports
 ├── WebRTC Signalling        WebSocket over HTTP/HTTPS
 ├── HLS / DASH Delivery      over HTTP(S)
 └── Cluster (Redis)          Origin ⇄ Edge nodes
```

### Application → stream → outputs

- the **application** (`live`, `WebRTCAppEE`, your own) is the top level; each app has its own settings and a REST path
- a **stream** (broadcast) belongs to exactly one app; the stream ID is the key for URLs and the API
- per stream several output forms exist: `…/streams/<id>.m3u8` (HLS), the WebRTC play URL, RTMP play

## UI/UX

### Design principles

- **A tile per stream**: status at a glance, actions right on the tile
- **App context first**: almost everything presupposes the chosen application
- **URL picker instead of guesswork**: "copy stream URLs" shows all output variants in one dialog

### Colour scheme

- panel: light, blue accents; status green (live), red (error/offline), grey (ready/VoD)
- dashboard charts in standard material colours

### Interactions

- start/stop as an icon on the stream tile
- recording as a second state of the same tile
- token dialogs and URL dialogs as modals

## Accessibility

- the panel is a standard web UI (tab order present, but not extensively audited)
- charts are graphical; numeric values only partly available as text
- the media player in the panel (WebRTC test) has no subtitle control

## Performance

- transcoding eats CPU — only run adaptive bitrate with enough cores/GPU
- the edge/origin separation keeps viewer load apart from transcoding processes
- recording and VoD processing run asynchronously (processing status in the VoD table)
- watch Redis and the panel statistics with very many streams (memory)
