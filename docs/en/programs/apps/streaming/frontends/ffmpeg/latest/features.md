# FFmpeg - Features

## Main features

- **Transcoding**: decode → filter → encode in one pass; `-c copy` only rewrites the container without re-encoding
- **Muxing/demuxing**: containers mp4, mkv/matroska, webm, ts, nut plus HLS (`-f hls`) and DASH as segment writers
- **Analysis with `ffprobe`**: `-show_streams -show_format`, output as json/csv/xml — the machine-readable statement about any file
- **Filter graph (libavfilter)**: `scale`, `overlay`, `concat`, `drawtext`, `crop`, `fps`, `volume`, `amix`, `loudnorm` (EBU R128); chaining with `,`, graphs with `-filter_complex` and `-map`
- **Playback with `ffplay`**: SDL-based minimal player for quick tests
- **Self-help**: `ffmpeg -h`, `-h full`, topic-specific `-h encoder|decoder|filter|muxer|protocol`

## Codecs

| Family | Codec / library |
|--------|-----------------|
| H.264 | `libx264`, `libx264` parameters `-crf`, `-preset`, `-tune` |
| H.265 | `libx265` |
| AV1 | `libaom`, `libsvtav1` (SVT-AV1) |
| VP9 / VP8 | `libvpx-vp9`, `libvpx` |
| Audio | `libopus`, `aac` (native encoder), `libfdkAAC` (optional, build flag), `libmp3lame` |
| Professional | `prores`, DNxHD |
| Image | `png`, `mjpeg` |

## Hardware acceleration

| Backend | Encoder / route |
|---------|-----------------|
| NVIDIA | `h264_nvenc`, `hevc_nvenc`, decoding `-hwaccel cuda` |
| Intel | `qsv` (`h264_qsv`, `hevc_qsv`), `-hwaccel qsv` |
| Linux general | `vaapi`, `v4l2m2m` |
| Apple | `videotoolbox` (`h264_videotoolbox`) |

## Protocols / IO

| Direction | Protocols |
|-----------|-----------|
| Input | RTMP, RTSP, SRT, HLS/DASH (client), UDP/RTP, HTTP(S), `pipe:`, devices: `v4l2`, `alsa`, `dshow`, `avfoundation` |
| Output | RTMP, SRT, UDP/RTP, HTTP(S), HLS/DASH segments on the filesystem, `pipe:1` into other processes |

FFmpeg is **client and segment writer**, but not a server: HLS/DASH are written as files or pushed via protocol; accepting incoming streams is done by a server such as MediaMTX or nginx-rtmp.

## Performance and operation

- `-progress pipe:1` delivers a machine-readable progress stream, `-stats` the human display
- `-f null -` forces complete decoding without output — a compute-load/analysis benchmark
- CPU load scalable via `-threads`; `-preset` controls speed/compression
- GPU encoders (nvenc/qsv/vaapi) noticeably relieve the CPU in live chains

## What FFmpeg does NOT do

- **No GUI** — no window, no mouse control, everything runs on the command line (❌)
- **No scene or picture mixer function** — no interactive switching of sources as in OBS (❌)
- **No live streaming server** — it does not accept incoming publish streams and does not distribute them (❌)
- **No timeline/editing interface** — cuts only arise through parameters such as `-ss`/`-t` (❌)
- **No platform APIs** — no OAuth, no automatic YouTube upload, no chat (❌)
- **No DRM and no licence-check delivery** — it only encrypts what the container permits (❌)

## See also

Streaming production is done by [OBS Studio](../../obs-studio/index.md); stream acceptance and distribution by [MediaMTX](../../mediamtx/index.md) or the [Restreamer](../../restreamer/index.md); as a pipeline library with its own operation, [GStreamer](../../gstreamer/index.md) alternates.
