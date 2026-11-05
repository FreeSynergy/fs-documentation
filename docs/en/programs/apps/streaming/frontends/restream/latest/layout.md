# Restream - Structure & UI/UX

## Overview

Restream is a web dashboard with a studio view. This file describes the layout, the plan tiers and the embedding — without naming prices (those change often).

## Window structure

### Main areas

```
┌────────────────────────────── Restream Dashboard ───────────────────────────┐
│ Logo │ Account/plan │ Notifications                                         │
├───────────────┬─────────────────────────────────────────────────────────────┤
│ Navigation    │ Content                                                    │
│               │                                                            │
│ Live          │ Status, ingest data (RTMP URL + key), target status        │
│ Studio        │ Preview window, scene list, source list, controls          │
│ Channels      │ Tiles per platform (connected/not), custom RTMP           │
│ Events        │ Calendar, event detail (pre-roll, recording)               │
│ Chat          │ One column per platform, input line                       │
│ Analytics     │ Charts (viewers, watch time), filter by event/platform    │
│ Video         │ Library, upload, embed links                              │
│ Settings      │ Account, branding, security, billing, API                 │
└───────────────┴─────────────────────────────────────────────────────────────┘
```

### Studio view

- top: preview window with scene/layout selection
- left: scene and source lists, add dialogs
- right: chat overlay, chat input, controls (microphone, camera, screen sharing)
- bottom: "go live", recording, rehearsal (preview without sending)

## UI/UX

### Design principles

- **Task-oriented**: "go live" and the connected targets dominate the start page
- **Little configuration**: platforms are coupled via login, not via port/protocol
- **Everything in the browser**: production, moderation and analytics without local tools

### Colour scheme

- light, blue accents; status green (live/connected), grey (disconnected), red (error)
- studio is dark (video preview)

### Interactions

- drag & drop for sources into scenes
- connect/disconnect targets via tile buttons
- chat tabs per platform, one uniform input field

### Plan tiers (qualitatively)

| Tier | typical scope |
|------|---------------|
| Free | multistreaming with few targets, provider branding |
| Premium | more targets, own brand, longer streaming time |
| Business/Team | team logins, expanded analytics, further channels |
| Enterprise | API/integration scope by agreement |

## Accessibility

- standard web operation (tab order, form labels), but no documented accessibility certification
- the studio lives on camera/microphone — keyboard alternatives are limited
- captions: not documented as a core feature

## Performance

- latency depends on the provider and the target platforms (the WebRTC/HLS variant is not freely choosable)
- studio requirement: a stable upstream bandwidth and an up-to-date browser
- analytics charts get sluggish on long events — filter the time ranges
