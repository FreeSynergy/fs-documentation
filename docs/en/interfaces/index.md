# Interfaces

**Status: catalogue draft (2026-11-06).** This applies to everything, including what is already built (ADR 0045). Most
interfaces are not specified yet; the table says which are.

Every topic has **one interface, the same for every provider**, so that a provider can be swapped or added. This list
answers: what is there to standardise?

## Rules

1. **A standard comes first.** If one exists, the interface follows it. If not, we write one and offer it to others.
   **Each standard has exactly one owning program,** the point of truth, and every other program goes through its
   interface. No second model of the same thing (ADR 0050). A standard with several kinds of object, such as JSCalendar,
   is owned per kind: `Event` by `fs-calendar`, `Task` by `fs-tasks`.
2. **An interface is a target.** Published as a draft, it is tested by at least two independent implementations, then
   fixed as version 1.0. After that it changes only by a jump to a new version, never by gradual growth.
3. **Optional parts are declared up front.** Not every provider can do everything: Telegram cannot do what mail does.
   The interface names the core every provider must offer and the optional capabilities it may offer, and a provider
   declares which it has. This avoids reducing everyone to the weakest provider.
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
| Messages | Saying something to someone | AS2, MIMI, JMAP Mail | `fs-messenger` | Draft contract |
| People | Knowing who someone is and how to reach them | JSContact | `fs-people` | Core exists |
| Groups | Belonging together, and deciding who may do what | AS2 `Group`, SCIM | `fs-groups` | Planned |
| Events | Being somewhere at some time | JSCalendar `Event` | `fs-calendar` | Core exists |
| Tasks | Knowing what to do next | JSCalendar `Task`, RFC 9253 | `fs-tasks` | Model still in `fs-calendar-core`, moves |
| History | Remembering what I or we did | AS2 activities | `fs-history` | Planned |
| Resources | Knowing what we have and need | Gap | `fs-resources` | Planned |
| Files | Keeping and finding anything | AS2 `Document` | `fs-files` | Planned |
| Texts | Writing and knowing together | Own specification (ADR 0031, 0033) | `fs-wiki` | Core exists |
| Places | Knowing where | GeoJSON | `fs-maps` | Core exists |
| Decisions | Asking, and deciding together | AS2 `Question`; gap beyond it | `fs-surveys` | Planned |
| Boards | Thinking visually | Gap, own specification | `fs-whiteboard` | Planned |
| Live media | Showing something as it happens | WHIP, WHEP, enhanced RTMP | `fs-streaming` | Planned |

## Providers: who delivers it

| Interface | What it is for | Candidate providers |
|-----------|----------------|---------------------|
| Database | Keeping objects | Turso (behind `fs-store`'s `Store`, exists) |
| File storage | Keeping bytes | Local folder, RustFS over S3, git, WebDAV |
| Mail | Sending and receiving mail, as client or server | JMAP, IMAP and SMTP clients; own server later |
| Chat networks | Reaching people elsewhere | Matrix (tuwunel), Telegram, Discord, others |
| Identity | Signing in, system access | Kanidm through a [wrapper](../programs/platform/identity.md), and our own fallback |
| Video encoder | Turning a picture into a stream | Vulkan Video and `rav1e` proposed (ADR 0048) |
| Publishing target | Bringing a video to a platform | YouTube, Twitch, Odysee, PeerTube, others |
| Translation, AI | Local help with language and text | llama.cpp, others |
| Map data | Drawing maps | PMTiles (exists in `fs-maps`) |

## Cross-cutting: used by all

| Interface | What it is for | Standard base |
|-----------|----------------|---------------|
| Sharing and permissions | Who may see what; shares go to groups | Gap, one specification for all |
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

## Plugin form

Rust has no stable way to load compiled code at run time, so a plugin cannot simply be loaded as a library.

**Proposal:** a plugin is a separate small process that speaks Cap'n Proto (ADR 0021), started and stopped while
everything else keeps running. A frontend with built-in filters is the same idea: a mini server on top of an engine. If a
plugin must draw, it returns a scene description, and the host draws it. WASM components are the alternative for small
plugins that must be sandboxed. How plugins measure text is unsolved, and nothing has been measured yet.

## Who owns the specifications

Today, contracts lie in `temp/contracts/` in the docs repository. We propose a public repository for all interfaces,
`fs-interfaces`, so that others can implement them without our programs.
