# OBS Studio - Features

## Main features

### Scenes and sources
- unlimited numbers of scenes, grouped in folders, with transitions (cut, swipe, fade, custom)
- sources: window, screen, browser source, image, video file, media source, text (GDI+/Freetype), colour source, slideshow, camera, audio input/output, virtual camera
- grouping and transformation (position, scale, rotation, edge, crop), animations via scene change

### Composition and filters
- per source: scaling filters (bicubic, Lanczos, bicubic), colour correction, chroma key, masks, scrolling, delay
- per scene: audio filters, transition filters
- overlays, lower thirds, browser overlays (alerts, chat), green screen

### Audio
- multi-track mixer with channels, noise gate, noise suppression, compressor, limiter, delay
- monitoring (output only / monitor only), multi-track recording (up to 6 tracks)

### Output
- streaming: RTMP/RTMPS, SRT, RIST (per version), several targets via the multi-encoder plugin
- recording: MKV/MP4/MOV, container re-mux, new recording without a gap ("reconnect")
- encoders: x264, NVENC, AMD AMF, QuickSync, Apple VideoToolbox

### Production aids
- studio mode (preview vs. program with "execute transition")
- replays (replay buffer), captions, fast scene switching via hotkey
- virtual camera (output as a webcam for meetings)

## What OBS Studio does NOT do

- **No video editing / no post-processing** — timeline, audio tracks, effects afterwards (❌)
- **No multiview reception of other streams** as a source without a browser source/extra plugins (❌ native)
- **No platform-side transcoding/restreaming** — OBS sends to one target, multipathing only via plugins/the Restream service
- **No collaborative multi-operator control** without obs-websocket scripts (❌ built in)
- **No built-in chat/stats dashboard** (❌, only via a browser source)

## Extensions and integrations

| Integration | Way |
|-------------|-----|
| obs-websocket 5.x | built-in WebSocket server with a JSON protocol |
| obs-ffmpeg-mux / FFMpeg video filter | official extra plugin collection |
| obs-multi-encoder (community) | streaming to several targets at the same time |
| obs-browser / obs-nvenc | hardware encoding |
| scripts | Python/Lua via obs-scripting |
| virtual camera | official (Windows/Linux/macOS) |
