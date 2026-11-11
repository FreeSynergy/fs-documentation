# StreamYard

> Category: [streaming](../../index.md) · Type: browser-based live studio (SaaS) · Vendor: StreamYard · Licence: proprietary

## What it is
StreamYard is a live-streaming and recording studio that runs in the browser. The host sends a link, guests join with a camera and microphone from their own browser, and the host puts everyone on screen and broadcasts to connected platforms.

## Notable ideas
- **Guests join by link, no software, no account by default** — the host can optionally require a sign-in. This lowers the barrier for interviews; relevant to how our program admits guests (ADR 0013).
- **Host-run studio** — the host controls who is on screen; guests are not operators.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Protocols and standards used
Browser capture (WebRTC is implied by third-party reviews ⚠️). See [streaming requirements](../../requirements.md).

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://support.streamyard.com/hc/en-us/articles/4405100913428 | official help ✅ (via search summary) | 2026-11-10 |
| https://support.streamyard.com/hc/en-us/articles/360043733751 | official help, guests need no login ✅ (via search summary) | 2026-11-10 |
| https://support.streamyard.com/hc/en-us/articles/360051855952 | official help, phone guests ✅ (via search summary) | 2026-11-10 |
| https://streamyard.com/blog/invite-guests-to-stream-for-free | vendor blog ⚠️ | 2026-11-10 |
