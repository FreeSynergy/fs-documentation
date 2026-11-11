# Apple Photos

> Category: [gallery](../../index.md) · Type: photo library (Apple platforms) · Vendor: Apple · Licence: proprietary

## What it is
Photos is the photo and video library app of macOS, iOS and iPadOS, synchronised through iCloud Photos.

## Notable ideas
Why this program is documented here (ADR 0013). Function analysis only, own wording.

- Live Text: text inside a photo can be interacted with (selected), which also makes images findable by their text. Details beyond the guide's one-line summary are Open.
- Duplicates album: detected automatically (macOS Ventura or later); the user merges sets, one original is kept and the others go to Recently Deleted.
- Memories, People and pets, shared albums.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ partly verified, gaps marked "Open" |

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
| https://support.apple.com/guide/photos/welcome/mac | official user guide, welcome | ✅ 2026-11-10 |
| https://support.apple.com/en-la/guide/photos/pht5a3157c1d/8.0/mac/13.0 | official guide, duplicates | ✅ 2026-11-10 |
| https://support.apple.com/guide/photos/live-text-pht5ffdb2a7d/mac | official guide index (Live Text linked, not itself read) | ⚠️ 2026-11-10 |
