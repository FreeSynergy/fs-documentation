# Apple Mail

> Category: [messenger](../../index.md) · Type: e-mail · Vendor: Apple · Licence: proprietary (bundled with iOS, iPadOS, macOS)

## What it is
Apple Mail is the mail program that ships with every iPhone, iPad and Mac. It speaks IMAP and the
usual mail standards, keeps its own folders ("mailboxes") per account and adds automatic mailboxes
that collect mails across accounts. On the phone it is built around large titles, sheets and swipe
gestures. It is our reference for the "biggest counterpart / Apple" frontend type (ADR 0038).

## Notable ideas
Seen in screenshots (✅) unless marked ⚠️.

- **Smart mailboxes as a configurable list** — Inbox, VIP, Flagged, Unread, To/Cc, Attachments,
  Thread notifications, Remind Me, Follow Up, Send Later, Muted threads are not folders but saved
  views; the person ticks which appear and orders them by drag ✅. For us: saved queries over all
  accounts, shown like folders.
- **Automatic categories** — the inbox is split into Primary, Transactions, Updates, Promotions with
  chips on top, and an explanation sheet tells how many mails landed where last week ✅. Shows that
  sorting can be explained, not hidden.
- **Protect Mail Activity** — one switch that hides the IP address and loads remote content privately
  so senders cannot track opening ✅. Matches our "no tracking by default" rule.
- **VIP** — mark a person as important from the contact card; VIP mails get a star and their own
  mailbox ✅.
- **Notify Me / Mute per conversation** — from the long-press menu ✅.
- **Mark addresses** — highlight every address that does not end with given domains, as a guard
  against sending to outsiders ✅.
- **Swipe actions** — swipe a row left for More / Flag / Delete (round labelled buttons) ✅.
- **Select and move as a sheet** — selected mails appear as a stacked thumbnail above the mailbox list ✅.
- **Remind Me and Send Later** — time-based handling surfaced as mailboxes and sort keys ✅.
- **Coloured flags** — seven flag colours chosen from the action sheet ✅.
- **Mailing-list banner with one-tap unsubscribe** in the message ✅.
- **Search scope toggle** (all mailboxes / current mailbox) with top results first ✅.
- **Message navigation** — up/down arrows inside an open mail to go to the next/previous one ✅.

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [ios-26](ios-26/description.md) | 7/7 |

### ios-26

| File | Contents |
|------|----------|
| [description.md](ios-26/description.md) | Detailed description, differentiation, who it suits |
| [features.md](ios-26/features.md) | What the program can do — and what not |
| [layout.md](ios-26/layout.md) | Window structure, regions, panels |
| [menus.md](ios-26/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](ios-26/shortcuts.md) | Keyboard shortcuts |
| [api.md](ios-26/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](ios-26/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [interaction.md](ios-26/interaction.md) | Hover, focus, drag, gestures (finger, mouse, pen) |
| [states.md](ios-26/states.md) | UI states and transitions |
| [dependencies.md](ios-26/dependencies.md) | Which of our components a frontend in this style needs |
<!-- /gen:versions -->

## Protocols and standards used
Links into `data/` (protocols are not frontends): IMAP, SMTP, Exchange ActiveSync ⚠️, S/MIME ⚠️ —
see [messages standards](../../../../../data/messages/standards.md).

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| Screenshots collected by the project owner, iOS 26 on iPhone 17 Pro, one iOS 27 image, current macOS Mail, a few macOS 10.12 images (2016) | screenshots — internal, not published (ADR 0038) | 2026-11-05 |
| https://www.cubux.net/5-best-email-clients-for-mac/ | article (redirect target noted with the screenshots; not read) | 2026-11-05 |
