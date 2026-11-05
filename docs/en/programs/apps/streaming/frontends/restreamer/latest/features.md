# Restreamer - Features

## Main features

- **Push input**: RTMP(S) with a push key, alternatively RTSP/SRT input in new versions
- **Browser player** with HLS and (optional) WebRTC, embedding snippet, direct download of the segments
- **Restreaming**: simultaneous forwarding to several RTMP targets (multi-target)
- **Recording** into segments (default: 2-minute intervals) on a volume, optional transcoding via ffmpeg
- **Snippets/tools**: generate a preview image, statistics, support log package
- **Simple operation**: one Docker image, configured via the UI or `restreamer-cli`

## What the Restreamer does NOT do

- **No picture mixer / no scenes** — it forwards what arrives (❌)
- **No platform APIs** (no automatic YouTube upload management, no chat) (❌)
- **No adaptive multi-bitrate packaging** (only one HLS variant; no HLS master with several levels) (❌)
- **No DRM and no token-protected HLS delivery** out of the box (❌)
- **No monitoring/alerting** beyond logs (❌)

## Extensions and integrations

| Integration | Way |
|-------------|-----|
| ffmpeg | integrated for transcoding/recording |
| nginx-rtmp-module | the basis of reception, directives configurable |
| `restreamer-cli` | official command line for settings and hooks |
| Hooks | `on_publish`, `on_publish_done`, `on_record_done` via script/HTTP |
| Storage | Docker volumes `statistics` and `records` |
