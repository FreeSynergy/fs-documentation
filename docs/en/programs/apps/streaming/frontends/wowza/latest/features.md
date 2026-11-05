# Wowza Streaming Engine - Features

## Main features

- **Broad input**: RTMP/RTMPS, RTSP, SRT (from 4.6), MP4/progressive upload, HTTP pull from third-party sources (HTTP Publisher)
- **Broad output**: HLS, low-latency HLS, CMAF/chunked CMAF, MPEG-DASH, Smooth Streaming, progressive MP4, RTMP play; WebRTC depending on version/module (⚠)
- **Live transcoder**: multi-bitrate ladders, audio remixing, watermarking; templates in `TranscoderTemplates.xml`
- **nDVR and time shift**: live recording with a jump back into the running programme
- **Stream targets**: parallel restreaming to external RTMP targets (YouTube, Twitch, other servers)
- **Publisher control**: release or block individual feeders separately, also during operation
- **Security**: hash-key/token authentication for play and publish, your own auth modules, IP filter
- **DRM** (add-on): Widevine, FairPlay, PlayReady for HLS/DASH
- **Scaling**: live repeater (origin/edge chain) and the load balancer add-on for large viewer numbers
- **Extensibility**: the Java module API, hooks into the stream lifecycle (publish, play, close …)

## What Wowza does NOT do

- **No built-in CDN** — distribution through your own edge chain or an external CDN (❌ integrated)
- **No player portal / no upload website** for end users (❌, only playback URLs)
- **No chat, no community, no analytics dashboards** beyond the log viewer (❌)
- **No multi-tenancy** — one administration model per instance (❌)
- **No automatic platform connection with login** (no OAuth to YouTube/Twitch as with the SaaS services) (❌)
- **Paid**: a licence per instance, no free feature core (❌ open source)

## Editors

| Editor | Where | Purpose |
|--------|-------|---------|
| Properties masks | manager | settings without hand-editing XML |
| XML files | the `conf/` of the instance | the complete configuration (authoritative) |
| Transcoder templates | XML/manager | define the bitrate ladders |

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| Add-ons | DRM, load balancer, publisher control and others (in the subscription scope depending on the licence) |
| Java modules | your own authentication, event handling, routing |
| OBS/ffmpeg as feeders | standard RTMP/SRT push |
| Players | JW Player, Video.js, hls.js and others via the HLS/DASH URLs |
