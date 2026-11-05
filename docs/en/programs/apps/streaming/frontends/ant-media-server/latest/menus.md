# Ant Media Server - Menu items

## Overview

AMS has a **web panel** (standard ports: HTTP `5080`, HTTPS `5443`). Almost every panel action has a counterpart in the REST API (`/rest/v2/…`).

## Main menu items

### 1. Apps / application management

- **Purpose**: create and manage applications (`live`, `WebRTCAppEE`, your own app names)
- **Details**:
  - create a new application (RTMP streaming app, WebRTC app)
  - application settings (recording, transcoding, token security)
  - delete an app / view an app's REST base path

### 2. Live streaming

- **Purpose**: create, start, stop and watch streams
- **Details**:
  - "create new stream" (broadcast types: live stream, IP camera, stream source, list)
  - stream list with status, viewer count, bitrate, runtime
  - "copy stream URLs" (RTMP input, HLS/WebRTC/player outputs)
  - "join the stream" (test player in the panel)
  - start/stop recording, dashboard charts

### 3. VoD

- **Purpose**: manage recordings and uploaded videos
- **Details**: upload, list with status (processing/ready), delete, direct links

### 4. Dashboard / statistics

- CPU, RAM, network, active streams, viewer counts, bitrate history

### 5. Settings

| Area | Content |
|------|---------|
| General | server name, ports, RTMP port |
| Advanced | data settings, recording defaults, logging |
| Security | IP filter for REST, play/publish tokens, JWT |
| Restreaming | targets (YouTube, Twitch, …) and forwarding |
| Cluster / Redis | cluster mode, edge/origin nodes |
| SSL certificates | upload PEM/PFX |

## Context menus

| Object | Actions |
|--------|---------|
| Stream tile | start, stop, delete, copy URLs, record, statistics |
| VoD entry | play, download, delete, rename |
| Application | settings, REST path, delete |

## Menus by user role

| Role | Access |
|------|--------|
| Admin (panel login) | all menu items, settings, cluster |
| API user | REST v2 per app, secured via IP filter or JWT |
| Viewer | only the media endpoints (HLS/WebRTC player), no panel |
| Publisher | RTMP/SRT/WebRTC ingest with a stream ID (and token, if enabled) |
