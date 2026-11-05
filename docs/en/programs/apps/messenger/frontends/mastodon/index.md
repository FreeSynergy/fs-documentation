# Mastodon

> Category: [messenger](../../index.md)

## What it is

Mastodon is an open-source microblogging network based on the ActivityPub protocol, and it is decentralised.

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

## Review 2026-11-05

- **Version seen:** none — no file under `latest/` names a product version; the text describes an
  unspecified recent state. Reviewed on 2026-11-05 (docs state of commit `3fe3d7d1`) while deriving
  [requirements](../../requirements.md). Folder `latest/` is to be renamed to the real version after
  re-research (`temp/frontend-versions-missing.txt`).
- **Quality:** thin; partly generic. Features known from the product but **missing here**: reactions,
  threads, schedule send, snooze, undo send, swipe actions (where the product has them) ⚠️.
- Mastodon is microblogging (ActivityPub), not a messenger in the narrow sense; kept as reference for public timelines and `Note` handling.
- **Capabilities this frontend shows** (from the *Seen in* column of the requirements, ⚠️ = only
  known from the product):
  - Required:
  - `conversation.list`
  - `conversation.open`, `message.open`
  - `message.send`
  - `message.reply` ⚠️
  - `message.quote`
  - `message.edit`
  - `message.delete`
  - `message.read`
  - `message.search`
  - `attachment.add`, `attachment.save`
  - `attachment.preview`
  - `message.compose`
  - `draft.save`, `draft.list`
  - `conversation.notify`
  - `group.role`
  - `member.remove`, `actor.block`, `message.report`
  - `contact.lookup`
  - `profile.edit`
  - `rule.create`, `rule.run`
  - Optional:
  - `message.react` ⚠️
  - `message.mention`
  - `message.bookmark`
  - `channel.follow`
  - `message.announce`
  - `message.sensitive`
  - `attachment.describe`

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
<!-- /gen:versions -->
