# Messages

Chat, comment and mail-like communications. Canonical payload: **AS2 objects** (`Note`, `Article`) in the ActivityPub envelope (decisions 1+2).

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **ActivityStreams 2 Vocabulary, W3C** | ✅ | `Note`, `Article`, `contentMap`/`nameMap` (multilingualism) |
| **JMAP, RFC 8620/8621** | ✅ | reference for cleanly addressing/patching/synchronising JSON resources |
| **Mail address format, RFC 5322 §3.4.1** | ✅ | format of sender/recipient addresses |
| **XMPP (RFC 6120/6121)** | ⚠️ unverified | interoperability with legacy chat systems, evidence before use |

## Open points

- threading/history (parent-child relations) is not fully defined in AS2 → a rule is needed
- Mail interoperability (SMTP sending) is a transport topic of its own, not a data-model topic

## See also

- [standards.md → Activities](../standards.md)
- [comments (proposed domain)](../index.md) — for text-fragment tags/comments the **W3C Web Annotation Model** (✅) is the right standard
