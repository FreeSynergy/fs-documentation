# Wowza Streaming Engine - Description

## What the program does

Wowza Streaming Engine is a professional media server for self-hosting: it receives live streams from encoders, processes them (transcoding, recording, packaging) and delivers them in all common formats to browsers, apps and end devices. Administration, monitoring and automation happen through the manager interface, the REST API and the XML configuration.

## Advantages

- **Protocol breadth**: one server for RTMP input and HLS/DASH/CMAF/Smooth output
- **Production-ready**: nDVR, time shift, live repeater, load balancer, DRM — the features large live broadcasts need
- **Automatable**: a complete REST server API v2 for operations scripts
- **Commercial support**: documented software with a support channel (not a community-only base)

## Differentiation

| System | Difference |
|--------|------------|
| **nginx + nginx-rtmp-module** | a free DIY construction kit without manager, transcoding and DRM. |
| **Restreamer** | a finished small server for one stream; Wowza scales and differentiates per application. |
| **MediaMTX** | a lean Go router for protocols; without transcoder workflows and DRM. |
| **MistServer** | considerably lighter and also commercial; Wowza has the broader add-on/scaling ecosystem. |
| **Ant Media Server** | similarly professional, more strongly aimed at WebRTC/cluster; Wowza stronger in classic broadcast workflows. |
| **Restream (SaaS)** | a finished multistreaming service without your own servers; Wowza is your own infrastructure. |

## Technical details

- **Basis**: a Java process (JVM), installation directory `/usr/local/WowzaStreamingEngine` (Linux) respectively the program directory (Windows)
- **Ports (preset)**: 1935 (RTMP), 8086 (HTTP streaming), 443 (HTTPS/RTMPS), 8087 (REST API), 8088 (manager HTTP), 8090 (manager HTTPS) — all configurable
- **Configuration**: `conf/VHosts.xml`, per virtual host `VHost.xml`, per application `Application.xml` and others
- **Licence**: a paid instance licence (the vendor's trial/subscription models)
- **Platforms**: Linux and Windows, Docker images available

## Who it suits

- Professional organisers, broadcast-adjacent workflows and video portals with their own servers
- FreeSynergy streaming skins that are meant to mirror professional server models (virtual host → application → stream)
- Teams that want to operate DRM, multi-bitrate and scalable distribution themselves
