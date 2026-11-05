# MediaMTX - Structure & UI/UX

## Overview

MediaMTX is "operated" through files and ports. This file describes the inner structure (listeners, paths, readers) and the arrangement of the configuration — the template for a skin interface.

## Server structure

### Main areas

```
┌──────────────────────── MediaMTX (one process) ────────────────────────┐
│                                                                        │
│  Listener (input)                Path (internal)        Listener (output)
│  ─────────────────────           ──────────────         ─────────────────────
│  RTSP  :8554   ──┐                                        ┌── HLS :8888     │
│  RTMP  :1935   ──┤                                       ├── WebRTC :8889   │
│  SRT   :8890   ──┼──►   path "test1"  ──► reader list ──┼── RTSP :8554     │
│  WHIP  :8889   ──┘      (remux, queue)                   ├── SRT :8890      │
│                                                          └── MoQ :8892/8893 │
│                                                                        │
│  Control-API :9997   Metrics :9998   Playback :9996   PPROF :9999       │
└────────────────────────────────────────────────────────────────────────┘
```

### Input side

- publishers connect to a protocol listener and announce a path name
- alternatively MediaMTX pulls the source itself as a **proxy** (`source: rtsps://…`)
- `sourceOnDemand` starts the source with a delay (via a `runOnDemand` command)

### Output side

- every reader (`read`) gets its own remux chain: shared encoding, its own container
- HLS: segment size and count configurable (`hlsSegmentCount`, `hlsVariant`)
- WebRTC: a WHEP endpoint per path; ICE via `webrtcLocalUDPAddress` and optional STUN/TURN

### Side channels

- hooks call shell commands when connection states change
- the control API mirrors the running configuration and allows runtime changes
- recordings land in the filesystem and are offered through the playback server

## UI/UX (transfer onto a skin interface)

### Design principles

- **Declarative**: one view shows the YAML structure, not cascades of forms
- **The path as the central object**: all protocol details hang off one path entry
- **Make ports visible**: a list of the listeners with status (active/inactive) is the core of the view

### Colour scheme and typography

- no interface of its own; suggestion: a light standard interface, ports and paths in monospace
- status as a badge: `live` (green), `available` (grey), `error` (red)

### Interactions

- create/edit/delete paths through the control API, not through a file round trip
- live statistics per path (reads, bytes, bitrate) from the control API/metrics

## Accessibility

- configuration is text → fully readable aloud and versionable (Git)
- logs structured (JSONL) → good for screen readers and further processing
- for browser playback the rule is: HLS/WebRTC players have to bring subtitles and keyboard control themselves

## Performance

- `writeQueueSize` controls throughput vs. RAM; `readTimeout`/`writeTimeout` limit hanging clients
- HLS is only remuxed on demand by default (`hlsAlwaysRemux` avoids request delay)
- one path with many readers stays cheap, because it only remuxes and never transcodes
- adjust `udpMaxPayloadSize`/`udpReadBufferSize` under packet loss in networks with a small MTU
