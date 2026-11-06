# Streaming — design

**Status: draft interface; [stage 1](https://github.com/FreeSynergy/fs-streaming) in progress (2026-11-06): RTMP in, many RTMP or RTMPS targets out, FLV recording, no decoding.** Back to the [roadmap](../roadmap.md) · [requirements](requirements.md).
[research](https://github.com/FreeSynergy/fs-documentation/blob/main/temp/research/streaming-landscape.md).

## What it is for

**Record once, and bring it everywhere:** YouTube, Odysee and other platforms at once, live and not live, with no SaaS
provider in between. And recording must be far simpler than OBS.

No open tool we found is simple, multi-platform and self-hosted at once. Restreamer and MediaMTX are for server rooms, and
OBS with a multi-output plugin is the usual workaround, with the plugin breaking across OBS versions.

Calls are a separate program using the same parts (ADR 0037).

## Three parts

| Part | Effort | Notes |
|------|--------|-------|
| **Distribute live** | Manageable | One encoded stream forwarded to many targets, no re-encoding |
| **Publish not live** | Manageable | Upload through each platform's interface; shares a "publish" layer with live |
| **Simple recording** | Hard | Means encoding, see below |

Video management, versions and sync belong to [`fs-files`](../files/design.md), and recordings land there. A live stream
is not a file, so that part stays here.

## Simple means automatic

The person picks their targets. The program works out the settings, and checks before going live whether everything will
work: connection, keys, and whether the chosen targets accept the format. Scenes, bitrates and keyframes stay hidden
unless someone wants them. A rich frontend for experts can show them all on the same engine.

## One stream for all

From the research: H.264, AAC-LC, constant bitrate, 2-second keyframes, 1080p at 30 fps and about 5 Mbps fits all the
platforms examined, with LinkedIn and Vimeo setting the limits. AV1 and HEVC only help on YouTube. Vertical video needs a
second encode.

## Platforms

| Platform | Live | Not live |
|----------|------|----------|
| YouTube | Enhanced RTMP: H.264, HEVC, AV1 | API, documented at 100 uploads per day |
| Twitch | RTMP; codec beyond H.264 unclear ⚠️ | Not applicable |
| Odysee | Custom RTMP | No official API found |
| Rumble | ⚠️ not verified | No API found |

Twitch allows simulcasting without an exclusivity deal, but restricts merging other platforms' activity into the stream,
according to secondary sources ⚠️. The publishing targets need review before use, since terms change.

## Encoding

**Decided (2026-11-06): codecs are outsourced, much as in GStreamer. Each is a provider behind one
[interface](../../../interfaces/index.md). We start with the open ones.** Once that is done, we look at others. We only
release what is free; anyone else may provide H.264 themselves. We want to be able to read it.

| Codec provider | Notes |
|----------------|-------|
| **AV1** with `rav1e` (Rust) | Open, royalty-free by its alliance's terms. Sisvel disputes this; no court has ruled, per our sources |
| **AV1 by hardware**, through Vulkan Video (open Khronos standard) | Live speed. Open Mesa drivers implement it |
| **Opus** with `mousiki` (Rust) | For sound. Young, to be tested |
| AV2 | Spec 1.0 since May 2026; no Rust encoder found. A chance to be first, too early for platforms |
| VP8, VP9 | Published. VP9 also has a Sisvel pool. Only bindings to `libvpx` found |

**Transport is a separate matter.** RTMP is no codec: it carries one. [Enhanced RTMP](https://github.com/veovera/enhanced-rtmp) is
an open specification (Apache-2.0) that adds AV1 among others, so it brings open codecs to platforms, but only those that
accept them. Forwarding a stream from another tool needs no codec of ours, so H.264 from elsewhere passes through.

**The consequence, accepted:** per the research, only YouTube reliably takes AV1. So our own recordings reach YouTube first,
and other platforms through forwarded streams. Open: which formats PeerTube and Odysee take, and whether reading H.264 is
itself covered by patents.

## Patterns

| Pattern | Use |
|---------|-----|
| Strategy | Encoders, ingest and output protocols, publishing targets |
| Pipeline | Capture → encode → route → targets |
| Observer | Status for the interface |
| State | `idle`, `checking`, `live`, `ended`, `error` |
| Adapter | Each foreign crate behind our own trait |

## Candidates

`str0m` 0.25 (WebRTC), `moq-rtc` 0.3 (WHIP and WHEP gateway), `xcap` (screen capture), `nokhwa` (camera), `ash` and
`gpu-video` (Vulkan, not checked), `rav1e` 0.8, `mousiki` (Opus in Rust). None checked for C dependencies yet.

## Stages

1. Forward: receive one stream, send to many, recording into `fs-files`.
2. Publish not live, with per-platform titles and scheduling.
3. Simple recording with screen and camera, automatic settings and a pre-flight check.
4. Second encode for vertical video, overlays.

## Open questions

1. How do we reach platforms that need H.264? See above. 2. Which platforms first?
