# MistServer - Structure & UI/UX

## Overview

MistServer has a lean web interface on port `4242` that mirrors the API exactly. This file describes the pages, the process structure and the port landscape.

## Window structure

### Main areas

```
┌──────────────────────────── MistServer (port 4242) ─────────────────────────┐
│ Login (when not localhost; localhost is authorised automatically)          │
├──────────────┬──────────────────────────────────────────────────────────────┤
│ Navigation   │  Content (one of the three pages)                          │
│              │                                                              │
│ Protocol     │  Table of the connectors + columns: status, port, type     │
│ Streams      │  Table of the streams + status, right-click menu           │
│ Push         │  Rules per stream: target, trigger, status                 │
│ API docs     │  built-in reference of the JSON commands                   │
└──────────────┴──────────────────────────────────────────────────────────────┘
```

### Process and socket structure

```
   MistController  ──unix sockets──►  MistIn_<type>    (input, decoder)
        │                              MistOut_<type>   (output, muxer)
        │                              MistConnector_*  (protocols)
        ▼
   config.json  /  /etc/mistserver.conf
```

### Protocol page

- a list of all active protocols with their port
- "default protocols" sets HTTP 8080, HTTPS 4433, RTMP 1935, RTSP 5554, SRT 8889 (udp), WebRTC 18203 (udp)
- the documentation's note: ports below 1024 need admin rights; for dedicated servers 80/443/554 are recommended

### Streams page

- blue entries = active but not created (right-click → create)
- white entries = configured; the status shows live/available
- the source field shows, for `push://`, the concrete push target addresses per protocol

### Push page

- two modes: automatic (a rule) and single (one-off)
- target types as a dropdown, including file recording

## UI/UX

### Design principles

- **Tables instead of forms**: everything is a list plus a detail page
- **Right-click instead of buttons**: stream actions in the context menu
- **API visibility**: the API docs are part of the interface — a learning path from the click to the command

### Colour scheme

- standard: dark tables, blue for active/blue streams, grey for inactive things
- status in colour: live, available, error

### Interactions

- create a stream: name + source; changes to the sources replace the source completely
- delete a push: only removes the rule, not the running push
- stream keys: a field below the push targets, generate/replace the token

## Accessibility

- the interface is database-like and tabular → readable as a table with a screen reader
- no keyboard navigation beyond the standard, no ARIA improvements documented
- media output (HLS/WebRTC) needs its own player accessibility

## Performance

- one process per protocol → the failure of a connector only affects that one
- the DVR buffer sits in RAM, its size configurable per stream (milliseconds)
- tracks are decoded at the first viewer; VoD streams start on demand
