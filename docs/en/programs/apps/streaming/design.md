# Streaming — design

**Status: proposal (2026-11-06).** Back to the [roadmap](../roadmap.md) · [requirements](requirements.md).

## Idea and assessment

Receive live media, forward it, record it. Calls are a separate program built on the same parts (ADR 0037).

**How hard is it? It splits into two very different parts:**

| Stage | What | Assessment |
|-------|------|------------|
| **1: forward** | Receive, forward, repackage and record without decoding the picture | **Manageable.** Rust building blocks exist |
| **2: process** | Convert quality levels, overlays, mixing; anything that decodes and encodes video | **Hard.** Encoding is CPU-intensive and pure-Rust options are limited |

We recommend documenting and planning everything now, but building only stage 1, and only after the other five programs.

## Stage 1

| Purpose | Candidate (2026-11-06) | Notes |
|---------|------------------------|-------|
| WebRTC | `str0m` 0.25 | Sans-IO, so it fits our own networking; actively released |
| WHIP and WHEP gateway | `moq-rtc` 0.3 | Built on `str0m`. Fast-changing API, so to be pinned |
| Low-latency delivery | MoQ (`moq-lite` 0.17) | Still young; a bet in the sense of ADR 0026 |
| Receiving | WHIP (RFC 9725) first | RTMP and SRT for existing tools such as OBS, later and checked separately |
| Packaging for many viewers | HLS | No crate chosen yet |

A viewer can use the browser's own decoder. Therefore stage 1 needs no encoder at all, provided the sender already
delivers a suitable format.

## Stage 2 is the hard part

| Purpose | Candidate | Limit |
|---------|-----------|-------|
| AV1 encoding | `rav1e` 0.8 | Rust, but last released 2025-06; live use is demanding |
| AV1 decoding | `rav1d` 1.1 | Rust port |
| H.264 | `openh264` 0.9 | Wraps Cisco's C++ library, so **not pure Rust** |

We found no mature pure-Rust H.264 encoder (not an exhaustive search). Blinc's own `blinc_media` also uses OpenH264 for
video on the desktop, so the question already arises in our GUI stack. Hardware encoders would be the fast route, and
they too go through C interfaces.

That conflicts with "100 % Rust" (ADR 0015), so it needs a decision: allow a limited exception, stay AV1-only and accept
the limits, or do without stage 2. Our recommendation is to decide when stage 2 starts, since the options will change.

## Data

| Piece | Standard | Notes |
|-------|----------|-------|
| Stream as an announced event | AS2 `Video`, JSCalendar `Event` for scheduling | |
| Recording | `fs-files` object, AS2 `Video` | |
| Chat beside a stream | Messenger workbench | Not duplicated (ADR 0037) |

## Patterns

| Pattern | Use |
|---------|-----|
| Strategy | Ingest and output protocols behind one interface |
| Pipeline | Ingest → route → outputs, with steps added per stream |
| Observer | Viewers subscribe to tracks |
| State | Stream status: `idle`, `live`, `ended`, `error` |
| Adapter | Each foreign crate behind our own trait |

## Components

Existing: `media-player` (needs a live mode), `video`, `audio`, `call-controls`, `message-list`. New: `stream-tile`,
`level-meter`, workbench `stream-studio`. See [planned components](../../../components/planned.md).

## Stages

1. Forward: WHIP in, WHEP out, access control, recording to `fs-files`.
2. Multiple outputs, HLS, RTMP and SRT, restreaming to other platforms.
3. Processing, after the decision above.

## Open questions

1. **What is the main use?** Team meetings, public events or gaming differ a great deal. It affects whether MoQ, HLS or
   WebRTC comes first.
2. **Calls:** do they share the first code with streaming? ADR 0037 makes them a separate program on shared parts.
3. **Encoder:** see above.
