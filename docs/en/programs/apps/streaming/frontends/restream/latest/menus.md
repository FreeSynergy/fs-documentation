# Restream - Menu items

## Overview

Restream is operated through the web dashboard (`restream.io` → login). The navigation is arranged at the side; reach and details depend on the subscription plan.

## Main menu items

### 1. Live / dashboard

- **Purpose**: the central streaming view
- **Details**:
  - "Go live" / stream status
  - ingest data (RTMP URL and stream key for OBS/ffmpeg)
  - active target platforms with status

### 2. Studio

- **Purpose**: browser production without local encoders
- **Details**:
  - scenes and sources (camera, screen sharing, media, browser source)
  - overlays, backdrops, text, layouts
  - invite guests via link (interview mode)

### 3. Channels / destinations

- **Purpose**: connect target platforms
- **Details**:
  - couple platforms via login (YouTube, Twitch, Facebook, LinkedIn, …)
  - custom RTMP targets with target URL and key
  - number of available targets depending on the plan

### 4. Events

- **Purpose**: manage planned streams
- **Details**: schedule, pre-roll/countdown, recording after the stream, sharing reminders

### 5. Chat

- **Purpose**: one uniform chat across all connected platforms
- **Details**: moderation, filtered words, answering from a single view

### 6. Analytics

- **Purpose**: viewer and interaction figures
- **Details**: viewers over time, watch time, per platform, export/reports (plan-dependent)

### 7. Video / library

- upload and management of VOD material, embed links, playlists

### 8. Settings / account

| Area | Content |
|------|---------|
| Account | email, password, 2FA |
| Branding | logo, watermark, player design |
| Security | reset the stream key |
| Billing / plans | tariff, invoices |
| API | API access/token (plan-dependent) |

## Context menus

| Object | Actions |
|--------|---------|
| Channel/target | connect, disconnect, rename, open this channel's chat |
| Scene/source | duplicate, lock, reorder, remove |
| Event | edit, duplicate, delete, share |

## Menus by user role

| Role | Access |
|------|--------|
| Account holder | everything including billing and API |
| Team/editorial member (team plans) | studio, chat, events according to permission |
| Viewer | only the embedded player, no dashboard |
