# YouTube Studio

> Category: [streaming](../../index.md) · Type: creator back office with live control room (SaaS) · Vendor: Google (YouTube) · Licence: proprietary

## What it is
YouTube Studio is the management area for channel owners on YouTube. For live broadcasts it contains the Live Control Room, a dashboard that shows the stream's health and real-time numbers while the broadcast runs, and an analytics area for the numbers afterwards.

## Notable ideas
- **Live control room** — stream health and audience numbers on one screen while live; a model for the operator view of our streaming program (ADR 0013).
- **Real-time versus processed analytics** — live figures (concurrent and peak viewers) are shown at once; the final figures arrive later and may differ because they are processed. Relevant for how we label numbers as preliminary.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Protocols and standards used
Ingest by RTMP(S) or other encoder protocols: Open (not verified here). See [streaming requirements](../../requirements.md).

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://support.google.com/youtube/answer/2853833 | official help page ✅ (via search summary) | 2026-11-10 |
| https://studio.youtube.com | sign-in required, not readable ⚠️ | 2026-11-10 |
