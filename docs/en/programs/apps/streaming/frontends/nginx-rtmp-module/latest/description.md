# nginx-rtmp-module - Description

## Overview

The nginx-rtmp-module is the classic open-source basis for streaming servers of your own: an nginx process receives RTMP and delivers HLS/DASH. It is deliberately a module, not a platform.

## What the nginx-rtmp-module does

nginx gains an additional RTMP listener. Publishers send to an `application`, the module muxes along and writes HLS/DASH files into the filesystem. nginx itself serves those files to browsers. Everything else — transcoding, auth, upload — happens through hooks and `exec`.

## Advantages

- **One process, one configuration file**: no second runtime, no database
- **Familiar operations technology**: the nginx logic (TLS, vhosts, rate filters, caching) applies automatically
- **Predictable**: streams are directories on disk, checkable with `ls`
- **In use for years**: very well documented, countless examples
- **Licence**: BSD, freely combinable

## Differentiation from other systems

### nginx-rtmp vs. MediaMTX

- MediaMTX is its own server with YAML, a control API, WebRTC/SRT/MoQ and Prometheus
- nginx-rtmp is older, smaller in scope, but right in the middle of the nginx world
- MediaMTX can do modern protocols without extra tools; nginx-rtmp needs ffmpeg and your own scripts

### nginx-rtmp vs. MistServer

- MistServer configures through a JSON API and has DVR and push rules
- nginx-rtmp configures only through files; in return every file is a normal nginx directive
- MistServer brings WebRTC, nginx-rtmp does not

### nginx-rtmp vs. Restreamer

- the Restreamer **is** nginx plus nginx-rtmp-module plus a web UI and ffmpeg integration
- anyone who does not need the web UI runs more leanly and more versionably with the bare module

## Technical details

- **Backend**: a C module for nginx 1.18+ (build with `--add-module`)
- **Database**: none — configuration in `nginx.conf`, state in the process
- **Frontend**: the status page `rtmp_stat` (XML, optionally with an XSL stylesheet)
- **Authentication**: only through HTTP hooks (`on_publish`, `on_play`)
- **Hosting**: wherever nginx runs; Docker images exist (unofficial)

## Who the module suits

- Teams with existing nginx infrastructure and simple RTMP→HLS requirements
- Learning and reference projects in which every line must be configurable/versionable
- as the basis of the Docker Restreamer
- **not** suitable when WebRTC, SRT, RTMPS or multi-bitrate renditions are needed — choose MediaMTX/Ant Media/Wowza for that
