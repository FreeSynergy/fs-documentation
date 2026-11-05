# Restream - Features

## Overview

Restream is a SaaS service: it takes over ingest, forwarding, chat bundling and analytics. FreeSynergy documents it as a reference for a cross-platform multistreaming interface.

## Main features

### 1. Multistreaming

- one input (RTMP/SRT from OBS, ffmpeg or straight from the studio) → many targets
- 30+ platforms coupled via login: YouTube, Twitch, Facebook, LinkedIn, TikTok, Vimeo and others
- Custom targets through RTMP URL and key
- Target count and parallelism depend on the plan

### 2. Restream Studio (browser production)

- scenes, sources (camera, screen sharing, media, browser overlay), layouts
- overlays, texts, images, backdrops
- guests via link; interview/panel views
- rehearsing without going live (soundcheck, preview)

### 3. Events and schedule

- planned lives with countdown/pre-roll
- automatic recording and transfer into the video library
- reminders and shareable event pages

### 4. Chat and moderation

- all platform chats in one view
- moderator functions, filters, spam protection
- answering from a single console

### 5. Analytics

- viewer history, watch time, interactions
- breakdown per platform and per event
- export/reports depending on the plan

### 6. Video and embedding

- VOD library, uploads, playlists
- embeddable player (branding according to plan) for your own pages

## Editors

| Editor | Purpose |
|--------|---------|
| Restream Studio | complete production in the browser |
| external encoders | OBS/ffmpeg send to the Restream ingest |
| event planner | scheduling, pre-rolls |

## What Restream does NOT do

- **No self-hosting** — data and infrastructure sit with the provider (❌)
- **No direct access to server configuration** (ports, protocols, transcoding profiles) (❌)
- **No unlimited number of targets** — plans limit targets and streaming time (❌)
- **No DRM and no private video cloud** in the sense of your own CDN (❌)
- **No API access to all dashboard features** (studio scenes cannot be controlled via API) (❌)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| OBS Studio / ffmpeg | RTMP/SRT ingest as per the dashboard |
| embedded player | iframe snippet on your own pages |
| chat widgets | chat embedding for streams |
| REST/WebSocket APIs | automation of targets, events, status |
