# PeerTube

> Category: [streaming](../../index.md) · Type: federated video platform with live streaming · Vendor: Framasoft and contributors · Licence: AGPL-3.0

## What it is
PeerTube is free software for hosting videos and live streams. Each installation (an instance) is independent; instances can follow each other through ActivityPub so that videos are discoverable across them. Viewers can share load with each other through WebRTC.

## Notable ideas
- **Federation of videos over ActivityPub** — channels can be followed from Mastodon and other fediverse software or by RSS (ADR 0013).
- **Peer-to-peer delivery** — viewers relieve the server by sharing the stream with each other.
- **Instance redundancy** — instances can cache each other's videos.
- **Plugins and themes**, and the web client may be replaced.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ✅ |

## Protocols and standards used
ActivityPub, WebRTC, HLS ⚠️ (not stated in the pages read), REST with OpenAPI 3. See [data standards](../../../../data/standards.md).

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://github.com/Chocobozzz/PeerTube | source README ✅ | 2026-11-10 |
| https://docs.joinpeertube.org/ | official docs ✅ | 2026-11-10 |
