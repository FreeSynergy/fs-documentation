# Outlook

> Category: [messenger](../../index.md)

## What it is

Outlook is Microsoft's most popular email client, part of Microsoft 365.

## Notable ideas

Seen in screenshots of the current Microsoft 365 release (✅) — details in
[m365-2026-11](m365-2026-11/features.md).

- **Schedule send** — the Send button is a split button; send later with two suggested times or a
  custom date/time ✅. Our `message.schedule`.
- **Undo send with a chosen delay** — 0–10 s set by a slider; a bottom bar with "undo" while the mail
  waits ✅. Shows that the delay is a setting, not a fixed value.
- **Recall a sent message** — inside the organisation, with a confirmation and a recall report mail ✅.
- **Snooze ("remind again")** — later today / tomorrow / this weekend / next week / pick a date;
  snoozed mails wait in their own folder ✅.
- **Follow-up flags with due dates and reminders** — today, tomorrow, this week, next week, custom
  (classic) ✅; flags become to-do items.
- **Pin** — pinned mails stay in a "Pinned" group on top of the list ✅.
- **Categorised search folders** — starring a colour category puts a folder for it into Favourites ✅.
- **Focused / Other** — automatic split of the inbox, on desktop and mobile ✅.
- **Offline mode with scope** — choose folders and number of days to keep locally, attachments on/off ✅;
  classic Outlook adds a "work offline" switch and send/receive groups ✅.
- **Invitations answered in the list and in the reading pane** — RSVP chip in the row; accept /
  tentative / decline / propose a new time with an optional note ✅.
- **Upcoming-event chip in the title bar** — the next meeting is always visible from mail ✅.
- **Contact hover card** — presence, role, contact details and manager line on hover ✅.
- **Notification settings per type** (mail, reactions, mentions, calendar, documents) ✅.
- **Picture themes and density** — light/dark/system plus image themes and a density setting ✅.

## Review 2026-11-05

- **Version seen:** none — no file under `latest/` names a product version; the text describes an
  unspecified recent state. Reviewed on 2026-11-05 (docs state of commit `3fe3d7d1`) while deriving
  [requirements](../../requirements.md). Folder `latest/` is to be renamed to the real version after
  re-research (`temp/frontend-versions-missing.txt`).
- **Quality:** thin; partly generic. Features known from the product but **missing here**: reactions,
  threads, schedule send, snooze, undo send, swipe actions (where the product has them) ⚠️.
- Planned as a **reference frontend** in suite context (Microsoft 365), see ADR 0038; needs re-research with screenshots.
- Version **`m365-2026-11`** documented from screenshots on 2026-11-05 (no version number visible;
  current Microsoft 365 release, new Outlook for Windows/web + mobile, some classic Outlook images):
  [m365-2026-11](m365-2026-11/description.md). Screenshots are internal and not published (ADR 0038).
- **Capabilities this frontend shows** (from the *Seen in* column of the requirements, ⚠️ = only
  known from the product):
  - Required:
  - `account.add`, `account.remove`, `account.edit`
  - `conversation.list`
  - `conversation.move`, `mailbox.create`
  - `conversation.open`, `message.open`
  - `message.send`
  - `message.send`, `key.discover`
  - `message.reply` ⚠️
  - `message.forward`
  - `message.delete`
  - `message.flag` ⚠️
  - `message.read`
  - `message.search`
  - `attachment.add`, `attachment.save`
  - `message.compose`
  - `draft.save`, `draft.list`
  - `group.create`, `group.invite`, `group.leave`
  - `contact.lookup`
  - `rule.create`, `rule.run`
  - Optional:
  - `Insert emoji in text`
  - `message.label`
  - `message.junk`
  - `message.schedule` ⚠️
  - `conversation.snooze` ⚠️
  - `Signatures appended to mails`
  - `Print a message`
  - `Calendar invitations answered in place (accept / d`

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 7/7 |
| [m365-2026-11](m365-2026-11/description.md) | 7/7 |

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

### m365-2026-11

| File | Contents |
|------|----------|
| [description.md](m365-2026-11/description.md) | Detailed description, differentiation, who it suits |
| [features.md](m365-2026-11/features.md) | What the program can do — and what not |
| [layout.md](m365-2026-11/layout.md) | Window structure, regions, panels |
| [menus.md](m365-2026-11/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](m365-2026-11/shortcuts.md) | Keyboard shortcuts |
| [api.md](m365-2026-11/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](m365-2026-11/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [interaction.md](m365-2026-11/interaction.md) | Hover, focus, drag, gestures (finger, mouse, pen) |
| [states.md](m365-2026-11/states.md) | UI states and transitions |
| [dependencies.md](m365-2026-11/dependencies.md) | Which of our components a frontend in this style needs |
<!-- /gen:versions -->
