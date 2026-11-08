# Helpdesk — Requirements

What `FreeSynergy.Helpdesk` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Channels (owner, 2026-11-09)

Every channel is a provider of `fs-messenger`; the helpdesk is a suite over tasks (Tickets), messenger, people and wiki.

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| **Chat widget for any website**: one snippet in the page, visitors talk to the team; the knowledge base from the wiki inside the widget | Chatwoot, Intercom, Zammad | messages; widget in Rust/WASM with a minimal loader | planned |
| **Telephony over SIP**: incoming calls show the caller's record, calls become part of the ticket history | Zammad (CTI), Freshdesk | SIP (RFC 3261), new provider interface *telephony* | planned |
| **Other messengers** (Matrix, Telegram, Signal, e-mail …) in one inbox | Chatwoot, Zammad | messenger providers | planned |
| Who is answering right now (collision detection), shared drafts | Zammad | live presence | proposed |
| Customer sidebar with history | Help Scout | people, history | proposed |

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Not planned (deliberately)
