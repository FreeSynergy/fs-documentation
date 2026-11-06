# Messenger — Requirements

What `FreeSynergy.Messenger` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.
One program covers e-mail, chat and messengers and sends **encrypted only** (ADR 0018).

Status: `implemented` · `planned` · `proposed`

**Seen in** — analysed frontends: [Di](frontends/discord/index.md) Discord ·
[El](frontends/element/index.md) Element · [Ko](frontends/kontact/index.md) Kontact ·
[Ma](frontends/mastodon/index.md) Mastodon · [Ou](frontends/outlook/index.md) Outlook ·
[Te](frontends/telegram/index.md) Telegram · [Th](frontends/thunderbird/index.md) Thunderbird ·
[Ap](frontends/apple-mail/index.md) Apple Mail (iOS 26). Outlook (Ou) also from screenshots, version `m365-2026-11`.
*arch.* = required by our architecture or principles, not by counting.
⚠️ = not (or not clearly) in our frontend files; known from the products, to be verified there first.

**Rule:** a capability is *Required* when at least four of the seven frontends show it, or when
our architecture needs it. The capability id in backticks (`<object>.<action>`) is a proposal
for the capability list (see the open point on the entry format) — a capability is an action on
the object, never a menu item or a gesture.

Data references: [messages standards](../../../data/messages/standards.md) ·
[messages technical](../../../data/messages/technical.md) (log mapping, encryption state) ·
[contacts](../../../data/people/index.md) · [identity](../../../data/identity/index.md).

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Manage several accounts in one program — mail, Matrix, MIMI (`account.add`, `account.remove`, `account.edit`) | Ko, Ou, Th, Te; *arch.* (one program, ADR 0018) | connectors: JMAP RFC 8620/8621, IMAP, SMTP, Matrix v1.19, MIMI protocol `-07` | proposed |
| List conversations across all accounts, newest first (`conversation.list`) | Di, El, Ko, Ma, Ou, Te, Th | AS2 `context` = conversation; JMAP `threadId`; Matrix room; MIMI room | proposed |
| Organise conversations: folders, categories, pinned (`conversation.move`, `mailbox.create`) | Ko, Ou, Th (folders, move/copy); Di (channel categories); El (pinned rooms); Te (sorting) | JMAP `Mailbox` + `mailboxIds`; chat folders: gap → own profile | proposed |
| Open a conversation and read its messages, flat (chat) or as a tree (mail) (`conversation.open`, `message.open`) | Di, El, Ko, Ma, Ou, Te, Th | AS2 `Note`, `context`, `inReplyTo`; original kept (MIME / MIMI CBOR / Matrix event) | proposed |
| Send a message to a person or a group (`message.send`) | Di, El, Ko, Ma, Ou, Te, Th | `Create`; MIMI content `-10`; MIME RFC 5322 via SMTP/JMAP submission; Matrix `m.room.message` | proposed |
| Send encrypted only; find an encrypted path (keys, counterpart) and explain when none exists (`message.send` precondition, `key.discover`) | El (default E2EE), Te (secret chats), Ko, Ou, Th (OpenPGP/S/MIME); *arch.* ADR 0018 | MLS RFC 9420; OpenPGP RFC 9580 + Header Protection RFC 9788; Autocrypt (v2 draft) | proposed |
| Show the encryption state of every message; mark unencrypted incoming, with a link to the library guide (`message.encryption`) | El, Te (security hints); *arch.* ADR 0018/0031 | `freesynergy.net:encryption` = `mls` · `openpgp` · `megolm` · `transport-only` · `none` | proposed |
| Let an AI into a conversation only if everyone agrees beforehand; anyone joining later accepts it too or stays out; no history from before it entered (`participant.consent`) | *arch.* ADR 0054 | Marked participant (JSContact `kind` `application`); MLS Add; Matrix: no `shared_history` keys for an AI | proposed |
| Verify signatures, keys and devices; trust a contact's key (`key.verify`, `device.list`) | Ko, Th (verify GPG signature); El, Te (device management) | OpenPGP RFC 9580; MLS credentials; Web of Trust ([identity](../../../data/identity/index.md)) | proposed |
| Reply to a message — to the sender or to all (`message.reply`) | Di, El, Ko, Ou, Te, Th; Ma (reply ⚠️) | `Create` with `inReplyTo`; `In-Reply-To` header; Matrix `m.in_reply_to`; MIMI reply | proposed |
| Forward a message (`message.forward`) | Di, El, Ko, Ou, Te, Th | new `Create`, original as `attachment` (e-mail: `message/rfc822`) ⚠️ no MIMI forward type | proposed |
| Quote a part of a message (`message.quote`) | Di, El, Ma, Te; Ko, Th (paste as quote) | W3C Web Annotation `TextQuoteSelector` on the source (ADR 0033); in mail additionally quoted text | proposed |
| Edit a sent message; the first version's id stays (`message.edit`) | Di, El, Ma, Te | `Update`; MIMI edit; Matrix `m.replace`; e-mail: gap | proposed |
| Delete a message — for me, or for everyone where the transport allows (`message.delete`) | Di, El, Ko, Ma, Ou, Te, Th | `Delete` + tombstone; MIMI empty body; Matrix redaction; JMAP move to trash / destroy | proposed |
| Flag / mark a message for later ⚠️ "Mark" in the menus is ambiguous (flag vs. select) (`message.flag`) | Di, El, Ko, Ou, Te, Th ⚠️ | JMAP keyword `$flagged`; chat: gap → own vendor keyword | proposed |
| Mark as read / unread; jump to the next unread (`message.read`, `conversation.markRead`) | Te (mark chat as read); El, Ma (next unread); Ko, Ou, Th (mark) | `Read` activity; JMAP `$seen`; Matrix `m.receipt`; MIMI message-status; batched "read up to X" is a gap | proposed |
| Search messages — in a conversation and across all accounts, full text (`message.search`) | Di, El, Ko, Ou, Te, Th; Ma (hashtags) | full text over extracted fields (technical.md); JMAP `Email/query` filter model | proposed |
| Send, preview and save attachments (drag & drop is a frontend path) (`attachment.add`, `attachment.save`) | Di, El, Ma, Te; Ko, Th (save attachments); Ou | AS2 `attachment`; JMAP blobs RFC 9404; MIMI encrypted external parts; descriptor for encrypted attachments in AS2: gap | proposed |
| Preview media inline (images, video, documents) (`attachment.preview`) | Di, El, Ma, Te | `mediaType` of the attachment; thumbnails derived locally | proposed |
| Format text when composing (bold, italic, code, quote, lists, links) (`message.compose` with format) | El, Ma (Markdown); Ko, Ou, Th (formatting bar) | e-mail: `multipart/alternative` text/plain + text/html; chat: MIMI body part `text/markdown` ⚠️ | proposed |
| Keep drafts automatically and resume them (`draft.save`, `draft.list`) | Di, El, Ko, Ma, Ou, Te, Th (auto-save) | JMAP keyword `$draft` + Drafts mailbox; chat drafts: local only (gap) | proposed |
| Notification settings per conversation — all, mentions only, mute (`conversation.notify`) | Di, El, Te (channel/room notifications); Ma (notification types); Ko, Th (system notifications) | program setting; Matrix push rules map onto it; no common standard ⚠️ | proposed |
| Group conversations: create, name, describe, invite, leave (`group.create`, `group.invite`, `group.leave`) | Di, El, Te; Ko, Ou, Th (contact groups / distribution lists) | MLS group membership (Add/Remove); MIMI room policy `-04`; AS2 `Invite`, `Join`, `Leave`; JSContact `kind: group` | proposed |
| Roles and permissions inside a group (`group.role`) | Di, El, Te; Ma (moderators) | MIMI room policy `-04`; Matrix power levels | proposed |
| Moderate: remove, ban, block, report (`member.remove`, `actor.block`, `message.report`) | Di, El, Ma, Te | AS2 `Remove`, `Block`, `Flag` | proposed |
| Use contacts: pick recipients from the address book, open a sender's card (`contact.lookup` — borrowed, ADR 0020) | Ko, Ou, Th (address book); Di, El, Ma, Te (open profile) | JSContact RFC 9553 ([contacts](../../../data/people/index.md)), live reference into the contacts program | proposed |
| Edit the own profile: name, picture, short text (`profile.edit`) | Di, El, Ma, Te | AS2 actor; JSContact for the own card; [profile](../../../data/profile/index.md) | proposed |
| Rules and filters: sort, label, move, mute automatically (`rule.create`, `rule.run`) | Ko, Ou, Th (filter rules); Ma (word/user filters); Di (AutoMod) | Sieve via JMAP RFC 9661 for mail; the same rule model applied to chat ⚠️ (gap) | proposed |
| Work offline and stay in sync across devices (`sync`) | Ko, Th (offline mode); El (synchronisation); Te (cloud) | `fs-store` + `fs-hub`, object-level sync (ADR 0019); local, encrypted at rest (ADR 0024) | proposed |
| Do not load remote content or tracking images unless the person asks (`message.open` default) | Th (tracking protection); *arch.* (privacy) | rule in our renderer; MIME `cid:` parts allowed, remote URLs blocked by default | proposed |

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| React to a message with an emoji (`message.react`) — likely Required once verified | ⚠️ Di, El, Te, Ma (not in our files) | `Like` / FEP-c0e0 `EmojiReact`, undo via `Undo`; MIMI reaction; Matrix `m.annotation`; e-mail: gap | proposed |
| Threads: answer in a side thread without flooding the main conversation (`thread.open`) | ⚠️ Di, El (not in our files); Th (grouped view) | AS2 `context` / `inReplyTo`; Matrix `m.thread`; MIMI topic; thread profile is a gap (FEPs compete) | proposed |
| Show delivered / read state of sent messages; sending receipts is the person's choice (`message.status`) | Di, El, Te (read receipts) | MIMI message-status draft `-02`; `Read`; Matrix `m.receipt`; mail DSN / MDN RFC 9007; "delivered" in AS2 is a gap | proposed |
| Insert emoji in text | Di, El, Ou (emoji picker) | Unicode; custom emoji as `attachment` ⚠️ | proposed |
| Mention a person and notify them (`message.mention`) | Di, El (mention); Ma (mention notifications) | AS2 `tag` of type `Mention`; Matrix mentions; MIMI ⚠️ | proposed |
| Presence: online, away, busy, last seen — opt-in (`presence.set`) | Di, El, Te | Matrix `m.presence`; no AS2/MIMI standard → gap | proposed |
| Labels / categories with colour (`message.label`) | Ko, Ou, Th (categorise) | JMAP keywords | proposed |
| Sort and group the list (date, sender, subject, conversation) | Th (sort, group); Te (chat sorting) | view parameter of `conversation.list` | proposed |
| Spam / junk handling with learning (`message.junk`) — required at stage 2 (own mail server) | Ou (Clutter), Th (spam filter); Ko, Ou, Th (junk folder) | JMAP keywords `$junk` / `$notjunk`; Junk mailbox role | proposed |
| Schedule send (`message.schedule`) | ⚠️ Ou, Te (not in our files) | JMAP `EmailSubmission` with `sendAt` (FUTURERELEASE) ⚠️; chat: held locally until due | proposed |
| Snooze: hide a conversation until a time (`conversation.snooze`) | ⚠️ Ou (not in our files) | JMAP: no standard snooze ⚠️ → vendor keyword + date | proposed |
| Undo send within a few seconds (`message.send` with delay) | ⚠️ (not in our files) | local delay before `Create` leaves the device | proposed |
| Bookmark / save a message across conversations (`message.bookmark`) | Ma (bookmark); Te (saving bot) | own collection of references (AS2 `Collection`) | proposed |
| Disappearing messages with a timer (`message.expire`) | Te (self-destruct) | MIMI expiry; AS2 expiry: gap | proposed |
| Signatures appended to mails | Ko, Ou, Th | text block per account/identity; Web Annotation point anchor (ADR 0033) for variables ⚠️ | proposed |
| Pin conversations to the top | El (pinned rooms) | per-account ordering preference | proposed |
| Polls in a conversation (`poll.create`) | El, Te (via bots) | AS2 `Question` with `oneOf` / `anyOf` | proposed |
| Broadcast channels and following public timelines (`channel.follow`) | Te (channels); Ma (timelines, hashtags) | ActivityPub `Follow`, AS2 `Collection`; scope with a social program open ⚠️ | proposed |
| Boost / re-share a public post (`message.announce`) | Ma | AS2 `Announce` | proposed |
| Content warning / sensitive media (`message.sensitive`) | Ma | AS2 `summary` + `sensitive` ⚠️ (de-facto); our sensitive marking (ADR 0029) | proposed |
| Alt text for images (`attachment.describe`) — recommended for accessibility | Ma | AS2 `name` on the attachment | proposed |
| Clear the history of a conversation (for me) | Di, El, Te | local `Delete` of the range, not sent | proposed |
| Import / export messages (EML, mbox) (`message.export`, `message.import`) | Th (EML); Te (export messages) | RFC 5322 `.eml`; mbox ⚠️ | proposed |
| Print a message | Ou, Th | print layout from the extracted fields | proposed |
| Voice and video calls, screen sharing, call history (`call.start`) | Di, El, Te | MLS-protected media keys ⚠️; Matrix calls (MatrixRTC) ⚠️; scope open (own program?) | proposed |
| Voice messages (record, play) | ⚠️ Te, El (not in our files) | `attachment` with `audio/*` | proposed |
| Link preview generated by the sender, never fetched by the reader (`message.compose`) | ⚠️ El, Te (not in our files) | AS2 `Link` / `Page` as attachment ⚠️ | proposed |
| Bots and automation through our own contract | Di, El, Te (bots, webhooks) | Cap'n Proto → JSON / CLI / MCP (ADR 0021) — no separate bot API | proposed |
| Calendar invitations answered in place (accept / decline) | Ko, Ou, Th (mail + calendar together) | iMIP / JSCalendar, handled by the calendar program (ADR 0017), shown via its widget | proposed |
| Search and send GIFs, stickers, images from **Git repositories** (own, community, free offers) (`media.search`) | Di, El (GIF search as an idea) | packages via Git (ADR 0036); no tracking lookups | proposed |
| Bridges to other networks (Telegram, Discord, WhatsApp, …), installable on demand (`bridge.install`) | El (bridges) ⚠️ | Matrix bridges, self-hosted; marked "not end-to-end" (ADR 0018) | proposed |
| Saved views / smart mailboxes: a stored search shown like a folder (`view.save`) | Ou (search folders), Ap (smart mailboxes) | stored query over the envelope fields; JMAP `Email/query` filter as model | proposed |
| Automatic categories / focused inbox with explanation (`message.classify`) | Ou (Focused/Other), Ap (categories) | local classification only (no cloud), result as JMAP keyword / vendor property | proposed |
| Follow-up reminder on a message (`message.followup`) | Ou, Ap | JSCalendar `Task` linked via `relatedTo` | proposed |
| Pin a conversation (`conversation.pin`) | Ou | JMAP keyword | proposed |
| Recall a sent message (`message.recall`) | Ou | only where both sides are ours / MIMI delete; mail: best effort ⚠️ | proposed |
| VIP senders (`contact.vip`) | Ap | contacts: JSContact vendor property `freesynergy.net:vip` | proposed |
| Protect privacy when opening mail: remote content via proxy, hide IP (`privacy.proxy`) | Ap (Protect Mail Activity) | fits ADR 0018/0029; hub as proxy | proposed |
| Warn about recipients outside a trusted set (`recipient.warn`) | Ap (Mark Addresses) | contacts + trust (Web of Trust) | proposed |
| One-click unsubscribe from mailing lists (`list.unsubscribe`) | Ap | RFC 2369 `List-Unsubscribe`, RFC 8058 one-click ⚠️ verify | proposed |
| Automatic replies / out of office (`autoreply.set`) | Ou | Sieve vacation (RFC 5230) ⚠️ verify | proposed |
| Mute / ignore a conversation (`conversation.ignore`) | Ou (ignore), Ap (mute) | JMAP keyword | proposed |
| Message priority / importance (`message.priority`) | Ou | MIME `Importance` header; chat: vendor property | proposed |
| Sending aliases per account (`account.alias`) | Ap | JMAP `Identity` | proposed |
| Offline: choose which folders and how many days are kept (`sync.scope`) | Ou | `fs-store` sync policy (ADR 0019) | proposed |
| Summarise a long message (`message.summarize`) | Ou | **local model only** (no cloud, ADR 0029) ⚠️ | proposed |

## AIs as participants (provisional, ADR 0054)

From contract draft 0.2, which is still in review. See the [assistant](../assistant/index.md).

| Capability | What it does |
|------------|--------------|
| `toolcall.show` | Show what an AI wants to do or has done |
| `toolcall.decide` | A person allows or refuses a tool call, on their own device only |
| `turn.stop` | Stop what an AI is doing right now |
| `conversation.usage` | Show what a conversation used and cost |
| `text.stream` | Show an answer as it is being written |

**`toolcall.decide` is never offered to an AI.** It is never generated as an MCP tool, because an AI could otherwise approve its own actions.

## Not planned (deliberately)

| Feature | Seen in | Why not |
|---------|---------|---------|
| Sending unencrypted (TLS-only chats, plain mail) | Di, Ma, Te (default chats), Ko, Ou, Th (optional encryption) | encrypted only; the program asks for or looks for an encrypted way (ADR 0018) |
| Encryption as a separate, opt-in chat mode | Te (secret chats) | encryption is always on, not a mode (ADR 0018) |
| Paid tiers that unlock larger files, more accounts, more members | Di (Nitro), Te (Premium) | free forever, no poverty discrimination (ADR 0016) |
| Ads, sponsored messages | — | ADR 0016 |
| Loading tracking pixels / remote content by default; silent read receipts | (mail in general) | privacy; receipts and remote content are the person's choice |
| Plaintext kept in a provider cloud | Te (cloud storage) | content stored encrypted at rest (ADR 0024) |
| Bridged chats shown as end-to-end | — | bridges optional, self-hosted, visibly "not end-to-end" (ADR 0018) |
| Lookups to **tracking** third-party services while typing | Di, El (GIF services) | leaks what people type → instead: GIF/sticker search over Git repositories (see Optional, ADR 0036) |
| Vendor-locked office / cloud integrations | Ou (Microsoft 365, Teams, OneDrive, SharePoint, Power Automate) | other FreeSynergy programs share standard data instead (ADR 0017) |
| Calendar, contacts, tasks, notes built into the messenger | Ko, Ou, Th | separate programs; the messenger borrows them by live reference (ADR 0017, 0020) |
| Own login, 2FA, password handling | Di, El, Te | platform identity (Kanidm), not the messenger |
| Newsgroups (NNTP), RSS/Atom reading | Ko, Th | not a conversation; belongs to a reader program ⚠️ |
| XMPP, IRC connectors | — | not planned in `data/messages/standards.md` |

## Capabilities → contract

Candidate Cap'n Proto interface groups for `fs-messenger` (ADR 0021) — names only, no schema yet.
Two reference frontends (ADR 0022) must both run on them: the "show mails and swipe them away"
frontend uses only the first four; the Outlook-style frontend uses almost all.

- `Capabilities` — what this program offers, contract version range (manifest, ADR 0021)
- `Accounts` — accounts, connectors, identities, signatures
- `Conversations` — list, open, organise (folders/labels), notify, snooze, pin
- `Messages` — read, flag, label, mark read, react, edit, delete, forward, status
- `Compose` — drafts, recipients, formatting, attachments, encryption precondition, schedule
- `Encryption` — keys, devices, verification, trust, encryption state
- `Attachments` — upload, download, preview, blobs
- `Search` — queries, saved searches
- `Rules` — filters (Sieve for mail, same model for chat)
- `Groups` — members, roles, invitations, moderation
- `Presence` — own status, others' status (opt-in)
- `Events` — live stream of changes for the frontend (new message, read, typing, status)
- `Calls` — only if calls stay in this program (open)

Contacts, calendar invitations and profile are **not** own groups: they are borrowed from the
contacts, calendar and profile programs (ADR 0017, 0020).
