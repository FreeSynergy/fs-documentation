# Streaming — design

**Status: proposal (2026-11-06).** Back to the [overall plan](../roadmap.md) · [requirements](requirements.md) ·
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

**Decided by the owner (2026-11-06): open formats, as far as possible.** H.264 at most gets read. Our own output is **AV1 and
Opus**. Standards leave encoder design free, so writing an encoder is not copying.

| Option | Notes |
|--------|-------|
| **AV1** with `rav1e` (Rust) | Open, royalty-free by its alliance's terms. Sisvel disputes this; no court has ruled, per our sources |
| **Vulkan Video** (open Khronos standard) | Rust drives the graphics card's encoder, AV1 too, for live speed. Open Mesa drivers implement it |
| **Forwarding** a stream from another tool | Needs no codec of ours at all, so H.264 passes through |
| AV2 | Spec 1.0 since May 2026; no Rust encoder found. A chance to be first, too early for platforms |
| VP8, VP9 | Published. VP9 also has a Sisvel pool. Only bindings to `libvpx` found |

**The consequence:** per the research, only YouTube reliably takes AV1. So recording directly from our tool would reach
YouTube, while other platforms need H.264 from another tool or a platform-side change. "One stream for all" above describes
today's platforms, not our output. Open: which formats PeerTube and Odysee take, whether reading H.264 is itself covered
by patents, and whether encoders on the machine's own hardware or OS could be an optional provider.

All backends sit behind one `VideoEncoder` [interface](../../../interfaces/index.md).

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
