# Interfaces

**Status: catalogue draft (2026-11-06).** This applies to everything, including what is already built, which will be reworked (ADR 0045). Most
interfaces are not specified yet; the table says which are.

Every topic has **one interface, the same for every provider**, so that a provider can be swapped or added. This list
answers: what is there to standardise?

## Rules

1. **A standard comes first.** If one exists, the interface follows it. If not, we write one and offer it to others.
   **Each standard has exactly one owning program,** the point of truth, and every other program goes through its
   interface. No second model of the same thing (ADR 0050). A standard with several kinds of object, such as JSCalendar,
   is owned per kind: `Event` by `fs-calendar`, `Task` by `fs-tasks`.
2. **An interface is a target.** We define the target, and it may get sharper while we do not know it fully yet. Published as a draft, it is tested by at least two independent users of it (for a
   provider interface: two providers), then fixed as version 1.0. After that it changes only by a jump to a new version, never by gradual growth.
3. **Like a parent class.** Every provider offers all methods and attributes of its interface. If a provider lacks
   something, we look for a way to make it work anyway. If there truly is none, it answers explicitly "not possible".
   We think about how something can be done before saying that it cannot.
4. **A frontend uses what it wants.** The engine may offer more than a frontend needs.
5. **Plugins can be added and removed while running** (hot plugins); see [plugin form](#plugin-form).

## Two levels

Keeping these apart prevents much confusion:

- A **topic interface** says what people work with: *messages*. Programs and frontends use this.
- A **provider interface** says who delivers it: *mail, Matrix, Telegram*. Each is an adapter behind it. A provider can
  have two roles: as a client of someone else's server, or as the server itself.

## Topics: what people work with

| Topic | What it is for | Standard base | Owner | Status |
|-------|----------------|---------------|---------|--------|
| Messages | Saying something to someone, [AIs included](../programs/apps/assistant/index.md) | AS2, MIMI, JMAP Mail, MCP and ACP for agents | `fs-messenger` | Draft contract |
| People | Knowing who someone is and how to reach them, with [roles](roles.md) | JSContact | [`fs-people`](https://github.com/FreeSynergy/fs-people) | Draft interface, provider exists |
| Groups | Belonging together, and deciding who may do what | AS2 `Group`, SCIM | [`fs-groups`](../programs/platform/groups.md) | Draft interface, code in progress |
| Events | Being somewhere at some time | JSCalendar `Event` | `fs-calendar` | Core exists |
| Tasks | Knowing what to do next | JSCalendar `Task`, RFC 9253 | [`fs-tasks`](https://github.com/FreeSynergy/fs-tasks) | Core exists, draft interface |
| History | Remembering what I or we did | AS2 activities | [`fs-history`](https://github.com/FreeSynergy/fs-history) | Provisional draft interface, core exists |
| Resources | Knowing what we have and need | Gap | [`fs-resources`](https://github.com/FreeSynergy/fs-resources) | Provisional draft interface, core exists |
| Files | Keeping and finding anything | AS2 `Document` | [`fs-files`](../programs/apps/files/design.md) | Provisional draft interface, code in progress |
| Texts | Writing and knowing together | Own specification (ADR 0031, 0033) | `fs-wiki` | Core exists |
| Places | Knowing where | GeoJSON | `fs-maps` | Core exists |
| Decisions | Asking, and deciding together | AS2 `Question`; gap beyond it | [`fs-surveys`](https://github.com/FreeSynergy/fs-surveys) | Provisional draft interface, core exists |
| Boards | Thinking visually | Gap, own specification | [`fs-whiteboard`](https://github.com/FreeSynergy/fs-whiteboard) | Draft interface, core exists |
| Live media | Showing something as it happens | WHIP, WHEP, enhanced RTMP | [`fs-streaming`](https://github.com/FreeSynergy/fs-streaming) | Draft interface, code in progress |

## Providers: who delivers it

| Interface | What it is for | Candidate providers |
|-----------|----------------|---------------------|
| Database | Keeping objects | Turso (behind `fs-store`'s `Store`, exists) |
| File storage | Keeping bytes | Local folder, RustFS over S3, git, WebDAV |
| Mail | Sending and receiving mail, as client or server | JMAP, IMAP and SMTP clients; own server later |
| Chat networks | Reaching people elsewhere | Matrix (tuwunel), Telegram, Discord, others |
| Identity | Signing in, system access | Kanidm through a [wrapper](../programs/platform/identity.md), and our own fallback |
| Codecs | Turning a picture or sound into a stream and back; outsourced, like GStreamer | Open codecs first: AV1, Opus (ADR 0048) |
| Publishing target | Bringing a video to a platform | YouTube, Twitch, Odysee, PeerTube, others |
| AI models | Answers, translation, help with text | llama.cpp, Anthropic API, others |
| Map data | Drawing maps | PMTiles (exists in `fs-maps`) |

## Cross-cutting: used by all

| Interface | What it is for | Standard base |
|-----------|----------------|---------------|
| Trust | Showing when a person is safe, also against scammers and bots; each person sets their [own level](../programs/apps/assistant/index.md#locking-ais-out) | Web of Trust; its successor, the [Real Life Trust Protocol](https://github.com/real-life-org/trust-protocol), is the proposed target (ADR 0052, 0054) |
| Sharing and permissions | Who may see what; shares go to groups | Gap, one specification for all. Open: [role privacy](roles.md#open) |
| Envelope and activity log | Every object's outer form and history | AS2, proposed owner `fs-store` (ADR 0050) |
| Sync | Bringing devices and programs together | Activity log (ADR 0019) |
| Presence | Seeing what others do, as it happens | Gap; never stored |
| Search | Finding across programs | Gap |
| Notifications | Being told at the right moment | Gap |
| Metadata extractors | Reading what a file contains, by type | Exif, XMP, IPTC and others per type |
| Export and import | Bringing data in and out | Each topic's standard format |
| Components | Showing data without knowing its meaning | Our [component docs](../components/index.md) |
| Charts | Showing what numbers mean | Vega-Lite subset proposed, [catalogue](../components/charts.md) |
| Decision methods | Turning answers into a result | Published method descriptions |
| Plugins, packages, themes | Adding to the system | Git as distribution (ADR 0036) |

A component is not the only kind of interface; it is one row here. A workbench is a component too.

## Known limits before 1.0

- **No proven caller.** The transport only knows the system user. Every name in a request is plain text, so `fs-groups` cannot enforce
  rights yet. This is the largest gap for real use by several people; it needs the identity wrapper.
- **Lists without a cursor** in `people` and `groups` fail with `too-large` when an answer no longer fits into one message.
- **Reporting what a provider can do** is not uniform yet: some contracts have `capabilities`, some only `supportReport`.

## Plugin form

We follow what [Zentinel](https://github.com/zentinelproxy/zentinel) already does:

- **Many interfaces are only configuration,** which is validated and swapped atomically while everything keeps running.
- **Larger plugins are agents:** separate, crash-isolated processes over a local connection, which report their
  capabilities. Ours speak Cap'n Proto (ADR 0021). A frontend with built-in filters is the same idea: a mini server on an engine.
- **If an agent must draw,** it returns a scene description, and the host draws it. How it measures text is unsolved, and
  nothing has been measured yet.

## Who owns the specifications

All interfaces live in one public repository, [`fs-interfaces`](https://github.com/FreeSynergy/fs-interfaces), so that others can
implement them without our programs. Version 0.3.0 holds the common, tasks, messenger, hub, people, groups and files contracts as drafts, generated
with our own Cap'n Proto compiler. Besides the contracts it holds shared transport code for servers and clients, behind a feature and without any business logic. Errors travel as RFC 9457 problems.
