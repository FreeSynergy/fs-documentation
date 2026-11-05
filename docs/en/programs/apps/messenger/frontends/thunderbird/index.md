# Thunderbird

> Category: [messenger](../../index.md)

## What it is

Thunderbird is Mozilla's open-source email client, cross-platform and email-focused.

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

## Review 2026-11-05

- **Version seen:** none — no file under `latest/` names a product version; the text describes an
  unspecified recent state. Reviewed on 2026-11-05 (docs state of commit `3fe3d7d1`) while deriving
  [requirements](../../requirements.md). Folder `latest/` is to be renamed to the real version after
  re-research (`temp/frontend-versions-missing.txt`).
- **Quality:** thin; partly generic. Features known from the product but **missing here**: reactions,
  threads, schedule send, snooze, undo send, swipe actions (where the product has them) ⚠️.
- **Error:** layout.md attributes the **Address Book to Lightning** (lines 38, 49). Lightning was the calendar add-on, integrated into Thunderbird since version 78 ⚠️ verify; the address book never was Lightning.
- **Capabilities this frontend shows** (from the *Seen in* column of the requirements, ⚠️ = only
  known from the product):
  - Required:
  - `account.add`, `account.remove`, `account.edit`
  - `conversation.list`
  - `conversation.move`, `mailbox.create`
  - `conversation.open`, `message.open`
  - `message.send`
  - `message.send`, `key.discover`
  - `key.verify`, `device.list`
  - `message.reply` ⚠️
  - `message.forward`
  - `message.quote`
  - `message.delete`
  - `message.flag` ⚠️
  - `message.read`
  - `message.search`
  - `attachment.add`, `attachment.save`
  - `message.compose`
  - `draft.save`, `draft.list`
  - `conversation.notify`
  - `group.create`, `group.invite`, `group.leave`
  - `contact.lookup`
  - `rule.create`, `rule.run`
  - `Work offline and stay in sync across devices (`syn`
  - `message.open`
  - Optional:
  - `thread.open` ⚠️
  - `message.label`
  - `Sort and group the list (date, sender, subject, co`
  - `message.junk`
  - `Signatures appended to mails`
  - `message.export`, `message.import`
  - `Print a message`
  - `Calendar invitations answered in place (accept / d`

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
