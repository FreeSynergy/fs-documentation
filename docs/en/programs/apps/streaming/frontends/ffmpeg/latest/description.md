# FFmpeg - Description

## What the program does

FFmpeg is not an off-the-shelf appliance but the engine: it reads almost any input format, decodes it, pushes it through a freely wireable filter graph and writes it into almost any output format — as a file, as a segment batch (HLS/DASH) or as a stream to a neighbour (RTMP/SRT/UDP). `ffprobe` supplies the structured diagnosis, `ffplay` the instant playback. All of it without an interface, but fully automatable.

## Advantages

- **Format universality**: practically every codec/container combination in and out
- **Full automation**: one invocation is a reproducible work step — ideal for batch and CI
- **Filter graph as the swiss army knife**: scaling, overlay, watermark, loudness normalisation in a single pass
- **Hardware attachment**: nvenc/qsv/vaapi/videotoolbox make real-time encoding possible on inexpensive hardware
- **Embedded everywhere**: OBS, MediaMTX, Ant Media, Restreamer and dozens of tools use FFmpeg as their backend

## Differentiation

| System | Difference |
|--------|------------|
| **OBS Studio** | an interactive control room with scenes, sources and a mixer; FFmpeg cannot switch anything, it only processes what you give it (see [obs-studio](../../obs-studio/index.md)) |
| **GStreamer** | the same class of task, but as a pipeline library with gst tooling and a graph model; FFmpeg stays process-based with argument syntax (see [gstreamer](../../gstreamer/index.md)) |
| **MediaMTX** | a protocol server: it accepts streams and distributes them; FFmpeg is often only the backend there for relay/recording (see [mediamtx](../../mediamtx/index.md)) |
| **Restreamer** | a finished streaming box with a web interface; FFmpeg is the transcoding engine used inside it (see [restreamer](../../restreamer/index.md)) |
| **Commercial encoder (TMPGEnc, HandBrake)** | graphical encode interfaces; HandBrake and many converters themselves build on FFmpeg/libav |

## Technical details

- **Project umbrella**: FFmpeg projects (ffmpeg.org), development via mailing lists, regular release branches (currently 6.x/7.x)
- **Libraries**: libavformat, libavcodec, libavfilter, libswscale, libswresample, libavutil
- **Language**: C with hand-optimised assembler paths (x86/ARM)
- **Build options**: `--enable-gpl`, `--enable-libx264`, `--enable-libfdk-aac` and many more determine the feature scope
- **Licence**: LGPL for the core; GPL build with `--enable-gpl`, effectively GPL as soon as GPL libraries such as x264/x265 are linked
- **Platforms**: Linux, macOS, Windows, BSD, Android/iOS derivatives, embedded

## Typical usage patterns

| Pattern | Command sketch |
|---------|----------------|
| Archive conversion | `ffmpeg -i vhs.mkv -c:v libx264 -crf 20 -c:a aac archive.mp4` |
| HLS delivery | `ffmpeg -i live.mp4 -f hls -hls_time 6 -hls_playlist_type vod master.m3u8` |
| Loudness normalisation | `ffmpeg -i podcast.wav -af loudnorm out.wav` |
| Thumbnail | `ffmpeg -ss 5 -i video.mp4 -frames:v 1 preview.png` |
| Stream analysis | `ffprobe -of json -show_streams source.ts` |

## Character

FFmpeg is deliberately tool-like: no assistant, no defaults for matters of taste (container choice, CRF), no detours around errors. In return every work step is exactly reproducible, versionable and castable into scripts — which makes FFmpeg the foundation of all the other streaming tools in the skin catalogue.

## Limits in a team

| Point | Meaning |
|-------|---------|
| No GUI | onboarding needed for new team members |
| No project files | settings sit in each invocation — wrapper scripts centralise them |
| Version dependence | options and encoder listings differ between 6.x and 7.x |
| Licence question | check LGPL build vs. GPL build (with x264/x265) before distribution |

## Who it suits

- Encoding operations, batch conversion and archiving
- FreeSynergy skins that embed FFmpeg as the processing engine (transcode, thumbnail, loudness)
- Prototyping filter chains before rebuilding them in OBS/GStreamer
- Less suitable for live direction without prior knowledge — for that OBS or the Restreamer is the interface, FFmpeg stays the engine behind it
