# Messenger — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Messenger` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Apple Mail](apple-mail/index.md) | [ios-26](apple-mail/ios-26/description.md) | Apple Mail is the mail program that ships with every iPhone, iPad and Mac. |
| [Delta Chat](delta-chat/index.md) | [latest](delta-chat/latest/description.md) | Delta Chat is a chat messenger that delivers end-to-end encrypted messages through mail-like relays. |
| [Discord](discord/index.md) | [latest](discord/latest/description.md) | Discord is a proprietary communication platform for gaming communities, with voice/video and a server structure. |
| [Element](element/index.md) | [latest](element/latest/description.md) | Element is the open-source messenger for the Matrix protocol, with a decentralised architecture and end-to-end encryption. |
| [Fastmail](fastmail/index.md) | [latest](fastmail/latest/description.md) | Fastmail is a hosted e-mail service with calendar and contacts; its Masked Email creates one random address per sign-up. |
| [FreeSynergy Simple](freesynergy-simple/index.md) | [0.1](freesynergy-simple/0.1/description.md) | Our own, deliberately minimal messenger frontend. |
| [HEY](hey/index.md) | [latest](hey/latest/description.md) | HEY is a hosted e-mail service that sorts mail by approved sender and kind (Screener, Imbox, Feed, Paper Trail). |
| [Kontact](kontact/index.md) | [latest](kontact/latest/description.md) | Kontact is the integrated PIM application for KDE, which unites email, calendar, contacts, tasks and notes in a single application. |
| [Mastodon](mastodon/index.md) | [latest](mastodon/latest/description.md) | Mastodon is an open-source microblogging network based on the ActivityPub protocol, and it is decentralised. |
| [Outlook](outlook/index.md) | [latest](outlook/latest/description.md), [m365-2026-11](outlook/m365-2026-11/description.md) | Outlook is Microsoft's most popular email client, part of Microsoft 365. |
| [Signal](signal/index.md) | [latest](signal/latest/description.md) | Signal is a private, end-to-end encrypted messenger run by a non-profit. |
| [Spark](spark/index.md) | [latest](spark/latest/description.md) | Spark is an e-mail client with team comments, shared drafts and shared inboxes. |
| [Superhuman Mail](superhuman/index.md) | [latest](superhuman/latest/description.md) | Superhuman Mail is a keyboard-first e-mail client with a split inbox and a command palette. |
| [Telegram](telegram/index.md) | [latest](telegram/latest/description.md) | Telegram is a cloud-based messenger focused on speed, large groups/channels and encryption. |
| [Thunderbird](thunderbird/index.md) | [latest](thunderbird/latest/description.md) | Thunderbird is Mozilla's open-source email client, cross-platform and email-focused. |
| [Zulip](zulip/index.md) | [latest](zulip/latest/description.md) | Zulip is a team chat in which every message belongs to a topic. |

## File set per program (ADR 0012)

```
programs/apps/messenger/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
