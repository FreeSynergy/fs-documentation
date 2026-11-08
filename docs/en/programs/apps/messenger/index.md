# Messenger and Instant Messaging

## In short

FreeSynergy Messenger is one place for mail, chat and AI agents. It treats a message as a message, whichever network brought it. You read, answer, search and file in one place, and connectors do the talking to the outside world. A message is only sent if it can be sent encrypted.

## What is different here

- Encrypted only: if no way to encrypt a message to all its recipients exists, it is not sent, and there is no override.
- Incoming messages are marked with what the connector really knows. Anything not proven end-to-end is never shown as secure.
- The original of every mail is kept byte for byte.
- AIs are participants, not hidden listeners. Each one is marked, none acts without a release from you, and an emergency stop wins over everything.
- Messenger owns its open interface; mail, chat and agents are connectors under one program.

## Where it stands today

Latest tag: `v0.4.0`. Today it is the core, without a window. It has a message model for mail, chat and agents, with conversations, paging that does not jump when new mail arrives, unread marks, drafts, search, pin, move, flag and forward. Encrypted-only sending refuses clearly and names the recipients that cannot be reached. Messages are stored with their original. A mail connector fetches over IMAP or JMAP and sends over SMTP or JMAP, with OpenPGP and Autocrypt; it is tested against a local Stalwart test server only. An AI guard gives each AI an invitation, a release per kind of action, questions for risky steps, keeps secrets away from AIs, and has an emergency stop.

Not there yet (planned): a window, a server, chat connectors (Matrix and others) and Telegram. Messages stay on the device they arrived on, on purpose, until the key vault exists, and account passwords cannot be stored yet. Editing and reacting to a message, scheduled sending, mail rules, HTML bodies, key discovery, STARTTLS and S/MIME answer "not possible". The rule that all members must agree before an AI joins a conversation is not built, and the guard's rules are provisional. The interface is a draft with no consumer yet.

## Planned facets

Facets are parts of a program that look like apps of their own (see [Programs](../../index.md)). Proposed for `fs-messenger`:

- Mail (proposed)
- Chat (proposed)
- Forum, possibly (proposed)

## Overview

This section contains documentation for various messengers and communication platforms.

## Available Systems

- **outlook** - Microsoft email and collaboration
- **kontact** - KDE's personal information manager
- **thunderbird** - Mozilla email client
- **element** - Matrix-based secure messaging
- **discord** - Voice, video, and text chat
- **mastodon** - Decentralized social network
- **telegram** - Cloud-based messenger with bots
- **signal** - Private messaging with E2E encryption
- **whatsapp-web** - WhatsApp web interface
- **jabber/xmpp** - Open instant messaging protocol
- **skype** - Microsoft communication platform
- **rocketchat** - Open source team chat
- **mattermost** - Open source Slack alternative

## What is a Messenger?

A messenger (instant messenger) is software for real-time communication over the internet. Messengers enable:

- Exchange text messages
- Voice and video calls
- File transfers
- Group chats and channels
- Bot integrations
- End-to-end encryption

## Application Areas

- **Team communication**: Daily team communication
- **Customer support**: Customer service via messenger
- **Community**: Community discussions and forums
- **Social networking**: Microblogging and social networks
- **Collaboration**: Collaboration with file sharing

## Security and Privacy

When using messengers, consider the following security aspects:

- **Encryption**: End-to-end encryption for secure communication
- **Server location**: Which jurisdiction applies?
- **Data privacy**: How are data stored and processed?
- **Open Source**: Is the source code reviewable?
- **Decentralization**: Is the system decentralized?

## Selection Criteria

When choosing a messenger, consider the following criteria:

- **Features**: Which features are required?
- **Security**: Encryption and privacy
- **Platforms**: On which operating systems does the system run?
- **Scalability**: How many users and groups?
- **Integration**: How well does the system fit into the existing infrastructure?
- **Cost**: Free or paid?

## Related Categories

- [Wiki](../wiki/) - Knowledge management and documentation
- [Helpdesk](../helpdesk/) - Support and ticket systems
- [Desktop](../../platform/desktop/) - Desktop applications for communication

## Quick Start

1. **Select messenger**: Choose a messenger based on requirements
2. **Installation**: Download and install the app
3. **Create account**: Create a user account
4. **Add contacts**: Invite team members and contacts
5. **Create groups**: Set up chats and channels for teams

## More Information

Further information can be found in the documentation of individual messenger systems.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (9), by function, nothing copied (ADR 0012/0013):

- [Apple Mail](frontends/apple-mail/index.md) — Apple Mail is the mail program that ships with every iPhone, iPad and Mac.
- [Discord](frontends/discord/index.md) — Discord is a proprietary communication platform for gaming communities, with voice/video and a server structure.
- [Element](frontends/element/index.md) — Element is the open-source messenger for the Matrix protocol, with a decentralised architecture and end-to-end encryption.
- [FreeSynergy Simple](frontends/freesynergy-simple/index.md) — Our own, deliberately minimal messenger frontend.
- [Kontact](frontends/kontact/index.md) — Kontact is the integrated PIM application for KDE, which unites email, calendar, contacts, tasks and notes in a single application.
- [Mastodon](frontends/mastodon/index.md) — Mastodon is an open-source microblogging network based on the ActivityPub protocol, and it is decentralised.
- [Outlook](frontends/outlook/index.md) — Outlook is Microsoft's most popular email client, part of Microsoft 365.
- [Telegram](frontends/telegram/index.md) — Telegram is a cloud-based messenger focused on speed, large groups/channels and encryption.
- [Thunderbird](frontends/thunderbird/index.md) — Thunderbird is Mozilla's open-source email client, cross-platform and email-focused.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
