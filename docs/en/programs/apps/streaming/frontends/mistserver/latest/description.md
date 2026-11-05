# MistServer - Description

## Overview

MistServer is a C++ streaming server that manages without databases and without transcoding: sources are registered as streams and distributed through the activated protocol connectors. Everything — the interface included — runs over a JSON API.

## What MistServer does

MistServer manages named streams each with one source (live push, file, folder, pull URL, MPEG-TS/UDP). The activated connectors produce the output side (HTTP, HLS, DASH, WebRTC, RTMP, RTSP, SRT). Automatic-push rules record or forward to other servers/platforms.

## Advantages

- **Tiny footprint**: one process, no runtime dependencies, runs on weak hardware
- **Everything through one API**: interface, automation and configuration use the same interface
- **DVR from the factory**: a buffer per stream, with no extra add-on
- **Push as the core concept**: forwarding and recording follow the same mechanism
- **Predictable**: no hidden defaults — whoever deletes a stream has to register it completely anew

## Differentiation from other systems

### MistServer vs. MediaMTX

- both without transcoding; MistServer configures through the JSON API/interface, MediaMTX through YAML
- MistServer offers DVR and automatic-push rules; MediaMTX offers MoQ, JWT/HTTP auth and Prometheus
- MediaMTX is a single-file binary, MistServer has connector processes and Unix sockets

### MistServer vs. nginx-rtmp-module

- nginx-rtmp hangs off nginx and needs ffmpeg scripts for anything else; MistServer is stand-alone
- MistServer can do WebRTC and SRT, nginx-rtmp cannot; nginx-rtmp can do DASH without an extra tool
- Maintenance situation: nginx-rtmp has had no substantial development for years, MistServer is active

### MistServer vs. Ant Media Server

- Ant Media is a platform (Java/Tomcat) with transcoding, tokens, cluster and panel
- MistServer deliberately stays small: no renditions, no panel comfort, no cluster
- For FreeSynergy skins MistServer is the simplest template, Ant Media the most feature-rich

## Technical details

- **Backend**: C++, controller process plus connector processes (HTTP, RTMP, …) over Unix sockets
- **Configuration**: `config.json` next to the binary, or `/etc/mistserver.conf` as a service
- **Frontend**: the shipped single-page interface on port `4242`
- **Authentication**: login with a challenge hash (`MD5(MD5(password) + challenge)`); localhost without login
- **Hosting**: bare metal, Docker, VMs; ports freely choosable (below 1024 only with privileges)

## Who MistServer suits

- small to medium self-hosted streaming instances (club, campus, event)
- teams that want to configure everything through automation (one API, no GUI logic)
- low-latency viewer access over WebRTC/HLS without licence costs of the community edition
- Not suitable when transcoding, multi-bitrate renditions or DRM are needed
