# Wowza Streaming Engine - Structure and UI/UX

## Overview

Wowza consists of the media process and the manager web app. This file describes the manager layout, the configuration hierarchy and the port structure.

## Window structure (manager)

### Main areas

```
┌──────────────────────────────── Wowza Streaming Engine Manager ─────────────────────┐
│ Wowza logo │ instance name │ licence notice          signed in │ Logout            │
├──────────────────┬──────────────────────────────────────────────────────────────────┤
│ Menu             │  Content (the chosen level)                                      │
│                  │                                                                  │
│ Applications     │  Applications: table of the apps (name, type, status, restart)   │
│  Add Application │  Streaming Publishers: active feeders + [block]                  │
│ Streaming        │  Connections: viewers (IP, stream, duration) + [disconnect]      │
│  Publishers      │  Connections: list of ports (RTMP 1935, HTTP 8086 …)             │
│ Connections      │  Application detail: tabs playback options / properties /        │
│ Restart          │                  security / stream targets / restart application  │
│ Log Viewer       │  Log viewer: a rolling log window                                │
└──────────────────┴──────────────────────────────────────────────────────────────────┘
```

### Configuration hierarchy

```
Instance (WowzaStreamingEngine-<version>)
 ├── conf/VHosts.xml                      registers the virtual hosts
 ├── [vhost]/VHost.xml                    ports, handlers, limits
 │    └── [app]/Application.xml           behaviour per application (DVR, security…)
 │         └── [stream]/Stream.xml        individual streams (generated at runtime)
 ├── TranscoderTemplates.xml              bitrate ladders
 └── logs/                                access/error logs
```

### Port structure (preset)

```
Media    RTMP/RTMPS   :1935 / :443
         HTTP play    :8086   HTTPS play :443
Admin    Manager      :8088   Manager HTTPS :8090
         REST API     :8087
```

## UI/UX

- the manager is functional and text-heavy; tables + forms, no dashboards/charts
- standard classic layout, a light interface
- dangerous actions (restart, block) as buttons that ask for confirmation

## Interactions

- create an application through an assistant (name, type) — immediately playback-capable afterwards
- the properties mask writes straight into `Application.xml` when saving
- "playback options" shows all the stream's playback URLs for copying

## Responsive design

| Platform | Behaviour |
|----------|-----------|
| Desktop browser | full layout |
| Mobile browser | the manager simply scales (tables get narrow), ❌ no dedicated mobile layout |
| Native apps | ❌ none |

## Accessibility

- simple HTML tables/forms; the tab order is there but not audited (⚠)
- status as text (running/not started) and in colour
- the log viewer as a pure text area (good for screen readers)

## Performance

- the JVM heap can be set through the start scripts; transcoding scales with CPU cores
- the origin/edge separation (live repeater) keeps viewer load apart from feeding/transcoding
- the log viewer only shows an excerpt — the long history stays in the log files
