# Messages – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.**

## Core standard

| Standard | Evidence | Role |
|----------|----------|------|
| **Activity Streams 2.0 Vocabulary (W3C)** | ✅ | canonical payload: `Note`, `Article`; multilingualism `contentMap`/`nameMap`; audience `to`/`cc`/`bto`/`bcc` (Core, ✅) |
| **ActivityPub** (envelope) | ✅ (core rules evidenced; signature mechanisms ❌ see correction list) | `Create`/`Update`/`Delete` on `Note`/`Article` (decision 2) |

## References and interoperability

| Standard | Evidence | Role |
|----------|----------|------|
| **JMAP, RFC 8620/8621** | ✅ | reference for cleanly addressing/patching/synchronising JSON resources |
| **Mail address format, RFC 5322 §3.4.1** | ✅ | sender/recipient addresses in projections |
| **W3C Web Annotation Model** | ✅ | comments/tags on text fragments (`TextQuoteSelector`, `body`/`target`) — takes load off the message domain |
| **XMPP (RFC 6120/6121)** | ⚠️ unverified | interoperability with legacy chat systems, evidence before use |
| **MLS, RFC 9420** | ⚠️ not retrieved in this round | candidate for end-to-end encryption of groups |

## AS2 fields we evidence (✅ Core/Vocabulary read)

`@context`, `type`, `id` (absolute IRI), `actor`, `object`, `target`, `inReplyTo`, `name`, `nameMap`, `content`, `contentMap`, `summary`, `to`, `cc`, `bto`, `bcc`, `published`, `updated`, `url`, `Tag` (as a link extension: `Hashtag` is **not** in the AS2 core, ❌ evidenced — a Mastodon extension).

## Open standard points

- **Threading:** AS2 defines `inReplyTo` but no thread completion → our own rule (in [technical.md](technical.md))
- **Edit history, read receipts:** no standard → our own decision
- Signature mechanisms for ActivityPub objects: ❌ the old reference was 404 — research anew before specifying signatures
