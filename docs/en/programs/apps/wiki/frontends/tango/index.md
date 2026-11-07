# Tango

> Category: [wiki](../../index.md)

## What it is

Tango turns recorded clicks into step-by-step guides; not a wiki, documented for its capture-to-guide idea.

It is a process-documentation and in-app guidance product. It is not a general wiki or knowledge base. Its own help centre describes Tango as a tool "for documenting processes" with Guide Me, Pins, an AI Agent, Workspaces and plans Free, Pro, Enterprise ([help centre, llms.txt](https://help.tango.ai/llms.txt)).

## Identity check: tango.io is not this product

- `tango.io` returns a page of a services company named "Tango" (product engineering, AI pilots, staff augmentation; "© 2026 Tango"). It describes no capture or guide product ([tango.io](https://tango.io/)).
- The product is at `tango.ai` (help centre `help.tango.ai`). Third-party listings also show the older name "tango.us" ([TrustRadius comparison](https://www.trustradius.com/compare-products/stack-overflow-for-teams-vs-tango.us)). Vendor's update feed announces a rebrand on 2026-09-30 ([updates](https://updates.tango.ai/)); the rebrand content was not read.
- Other "Tango" products (Tango Card rewards API, Tango Analytics real-estate platform, a federal data API) are unrelated.

## Notable ideas (verified)

- **Capture to guide.** The user works in the app as normal. The browser extension records each click as a step and creates a screenshot, highlight and description automatically ([start capture](https://help.tango.ai/en/articles/5971654-how-do-i-start-capturing-a-workflow), [documentation how-to](https://help.tango.ai/en/articles/7966907-how-do-i-use-tango-for-documentation)).
- **Voice transcription** can write step titles and descriptions while recording (browser capture only, per [where it works](https://help.tango.ai/en/articles/17359491-where-does-tango-work)). Plan gating: see [features](latest/features.md).
- **Same guide, several viewers.** One guide is shown as a scrolling link view, an embed slideshow, an interactive "Guide Me" walkthrough inside the live app, or an export ([documentation how-to](https://help.tango.ai/en/articles/7966907-how-do-i-use-tango-for-documentation)).
- **Guide Me and Pins** show guidance inside the live web app. Enterprise lists "Pins, Guide Me, and Automations" ([pricing](https://www.tango.ai/pricing)).
- **Multi-path workflows** (branching) let one guide cover several valid paths ([branching](https://help.tango.ai/en/articles/14063444-how-does-branching-work-in-tango)). Enterprise only per [pricing](https://www.tango.ai/pricing).
- **Redaction at capture.** Live Blur hides elements while recording; Secure Blur and custom redactions are Enterprise ([secure blur](https://help.tango.ai/en/articles/7225709-how-to-use-secure-blur)).
- **Delivery to AI assistants.** Tango MCP lets an AI assistant answer from a team's guides. Live on Enterprise since 2026-11-04 ([updates](https://updates.tango.ai/), [MCP](https://help.tango.ai/en/collections/19799192-tango-mcp)).

## Version facts

Vendor publishes no version number for the web product. Documentation here is `latest/` = state seen on 2026-11-07. The vendor also names a **Tango Desktop 2.0** app ([help centre](https://help.tango.ai/llms.txt), [desktop collection](https://help.tango.ai/en/collections/3462416-desktop)).

| Version | Date seen | Files |
|---|---|---|
| [latest](latest/description.md) | 2026-11-07 | description, features, layout, menus, shortcuts, api, themes, limits, dependencies |

No changelog.md: only one version documented.

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 7/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](latest/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [limits.md](latest/limits.md) | Known limitations |
| [dependencies.md](latest/dependencies.md) | Which of our components a frontend in this style needs |
<!-- /gen:versions -->

## Sources

- Help centre: https://help.tango.ai/en/
- Pricing: https://www.tango.ai/pricing
- Product page: https://www.tango.ai/product/create
- Update feed: https://updates.tango.ai/
- Other articles: cited inline in each file.
