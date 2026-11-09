# Owncast

> Category: [streaming](../../index.md) · Type: self-hosted live video and chat server · Vendor: Owncast project · Licence: MIT

## What it is
Owncast is a server for one streamer: it takes a stream from broadcasting software over RTMP, serves it to viewers in the browser and offers a built-in web chat. It is written in Go with a React web client and uses ffmpeg.

## Notable ideas
- **One-person, one-server model** — a small, complete stack (video, chat, admin, directory entry) instead of a platform; matches our self-hosting goal (ADR 0013).
- **The server is a fediverse actor** — it is a single account of type Service; accounts on compatible services can follow it. Federation is an optional social layer, not the core.
- **Plugins in JavaScript or Python and web APIs** for bots, overlays and integrations.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Protocols and standards used
RTMP ingest; ActivityPub, WebFinger, HTTP Signatures, NodeInfo for federation. See [data standards](../../../../data/standards.md).

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://owncast.online/docs/ | official docs ✅ | 2026-11-10 |
| https://github.com/owncast/owncast | source README ✅ | 2026-11-10 |
| https://owncast.online/docs/api/activitypub | official docs ✅ (via search summary) | 2026-11-10 |
| https://owncast.online/dev-docs/activitypub-and-federation-engineering-reference | official dev docs ✅ (via search summary) | 2026-11-10 |
