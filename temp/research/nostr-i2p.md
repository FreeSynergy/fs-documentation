# Research: Nostr (NIP-17/44/59, MLS over Nostr, Rust SDK) and I2P (routers, SAM, I2CP, I2P-Bote)

Research date: 2026-11-08. All "last seen" dates are the date this research read the page. Sources are official project pages (specification repos, project GitHub repos, docs.rs, crates listings, project sites). Where only a search snippet or a third-party page was available, this is stated. Anything not confirmed on a page is marked **not verified**.

---

## Part 1: Nostr

### 1a. NIP-17, NIP-44, NIP-59

**NIP-17 (Private Direct Messages)**
- Status: the page is marked `draft`, `optional`, `relay`. Last seen 2026-11-08. No commit date shown. Source: https://github.com/nostr-protocol/nips/blob/master/17.md
- Specifies: encrypted chat built on NIP-44 and NIP-59. A chat is defined by its set of `p` tags; a changed recipient set starts a new room. Source: https://github.com/nostr-protocol/nips/blob/master/17.md
- Kinds used: 14 (chat message), 15 (file message), 7 (reactions, from NIP-25), 13 (seal), 1059 (gift wrap, one per receiver and per sender), 10050 (preferred DM relays), 5 (delete). Source: https://github.com/nostr-protocol/nips/blob/master/17.md
- Hidden per the spec: participant identities, real date/time, event kinds and other tags of the message; wrapper keys are random per message; `created_at` is randomized up to two days back. Source: https://github.com/nostr-protocol/nips/blob/master/17.md
- Visible per the spec: the outer kind 1059 event carries the receiver's `p` tag in plain text; kind 10050 relay lists are public. Relays are asked to serve kind 1059 only to the tagged user, enforced via NIP-42 AUTH. Source: https://github.com/nostr-protocol/nips/blob/master/17.md
- Limit stated in the spec: each message is sent separately to each receiver; group chats above 10 participants should use a different scheme. Source: https://github.com/nostr-protocol/nips/blob/master/17.md
- Also documented at the rust-nostr project site: https://rust-nostr.org/sdk/nips/17.html (not separately re-read for status)

**NIP-44 (Encrypted Payloads, Versioned)**
- Status: labelled `optional`. No draft/final label on the page. Last seen 2026-11-08. No commit date shown. Source: https://github.com/nostr-protocol/nips/blob/master/44.md
- Scheme (version 2): secp256k1 ECDH, HKDF, padding, ChaCha20, HMAC-SHA256, base64. Random 32-byte nonce per message; plaintext padded to power-of-two buckets with 32-byte minimum; MAC over nonce and ciphertext; outer Schnorr signature must be validated before decryption. Source: https://github.com/nostr-protocol/nips/blob/master/44.md
- Version byte: first byte of payload; `0x00` reserved, `0x01` deprecated/undefined, `0x02` the algorithm above. Source: https://github.com/nostr-protocol/nips/blob/master/44.md
- Audit: the page states the v2 standard was audited by Cure53 in December 2023. Source: https://github.com/nostr-protocol/nips/blob/master/44.md (audit report itself not verified)
- Not hidden per the page: sender identity (events are signed, so no deniability); `created_at` (part of NIP-01 event); approximate message size (padding only partly hides length); IP address to relays/intermediaries; no forward secrecy or post-compromise security; no post-quantum security. Source: https://github.com/nostr-protocol/nips/blob/master/44.md

**NIP-59 (Gift Wrap)**
- Status: labelled `optional` and `relay`. No draft/final label shown. Last seen 2026-11-08. Source: https://github.com/nostr-protocol/nips/blob/master/59.md
- Scope: encapsulates any Nostr event; the page states it does not define a messaging protocol. Source: https://github.com/nostr-protocol/nips/blob/master/59.md
- Three layers: rumor (unsigned event); seal (kind 13, rumor NIP-44 encrypted, signed by real author, empty tags); gift wrap (kind 1059, seal NIP-44 encrypted, signed by a random one-time key, `p` tag for recipient). Ephemeral variant kind 21059 (relays must not store). Source: https://github.com/nostr-protocol/nips/blob/master/59.md
- Hidden: rumor content and real author at the gift-wrap layer; seal reveals only its signer. Visible: the recipient (`p` tag on kind 1059) and that a wrap exists. Source: https://github.com/nostr-protocol/nips/blob/master/59.md
- Timestamps: rumor `created_at` is canonical; other timestamps "SHOULD be tweaked" (a recommendation, not a MUST); example code randomizes up to two days back. Source: https://github.com/nostr-protocol/nips/blob/master/59.md
- Anti-spam: relays may require NIP-42 auth because random keys defeat key-based spam filtering. Source: https://github.com/nostr-protocol/nips/blob/master/59.md

**NIP index status**: the NIP README table shows no draft/final status for NIP-17, 42, 44, 59; NIP-EE is marked "unrecommended: superseded by the Marmot Protocol"; Marmot kinds 443, 444, 445, 10051 are listed. Last seen 2026-11-08. Source: https://github.com/nostr-protocol/nips/blob/master/README.md

**Adoption (1d)**: a search snippet names Damus, Amethyst, Primal, 0xchat, Coracle as clients implementing NIP-17 (partial list, not a census). Source: https://rust-nostr.org/sdk/nips/17.html and https://opensats.org/topics/private-dms (search snippets; pages not fetched for this claim). Number of relays or clients using NIP-17: **not verified**.

### 1b. MLS over Nostr (Marmot Protocol)

- Marmot Protocol: the repo README states "Status: adopted", and that "The MIP-era documents describe a deprecated version of the protocol." Source: https://github.com/marmot-protocol/marmot (last seen 2026-11-08; no release or commit date shown; 199 commits on master shown).
- Marmot README: "Perfect metadata privacy is not possible in a decentralized messaging system." Security model document described as non-normative. Source: https://github.com/marmot-protocol/marmot
- NIP-EE (E2EE Messaging using MLS) is marked "unrecommended: superseded by the Marmot Protocol" in the NIP index. Source: https://github.com/nostr-protocol/nips/blob/master/README.md
- Marmot kinds listed in the NIP index: 443 KeyPackage, 444 Welcome, 445 Group Event, 10051 KeyPackage Relays List. Source: https://github.com/nostr-protocol/nips/blob/master/README.md
- MIP numbering and per-MIP status (MIP-00 to MIP-05 as shown in a search snippet): **not verified**. The repo README fetched did not list MIPs; a `mip-coverage.md` file is referenced but its content was not read. Search snippet source (not official): https://marmot-protocol.github.io/marmot-ts/guide/architecture.html
- MLS library: OpenMLS, "a Rust implementation of the Messaging Layer Security (MLS) protocol, as specified in RFC 9420." MIT (per page badge; SPDX text not shown on page). Minimum Rust version shown only in a badge: 1.94+. No release date shown. Last seen 2026-11-08. Source: https://github.com/openmls/openmls
- Marmot's Rust SDK, MDK: repo https://github.com/marmot-protocol/mdk. Licence MIT (file LICENSE). Described as "OpenMLS-backed group state machine" in `cgka-engine`. Crate map shown on page includes `cgka-engine`, `cgka-traits`, `transport-nostr`, `marmot-session`, `wn-cli` and others (the earlier search snippet's crate names `mdk-core` are not on the page read). Note: the page says nightly builds are "for testing only: pin a formal release for anything you ship." Latest formal release tag/date: **not verified** (page shows a 0.13.0 to 0.14.0 upgrade guide; Releases section empty). Source: https://github.com/marmot-protocol/mdk
- Audit: the MDK page mentions a "dependency audit" in a PR pre-check, and formal models (Tamarin, TLC); no third-party security audit is stated on the page. Source: https://github.com/marmot-protocol/mdk. A third-party review (Least Authority, November 2025) exists per a search snippet, https://leastauthority.com/white-noise-marmot-protocol-review-summary-report/ (not an official source; not relied on).
- Known caveat on the OpenMLS-backed engine: unoptimized OpenMLS can overflow the default 2 MiB thread stack. Source: https://github.com/marmot-protocol/mdk

### 1c. Rust: nostr-sdk and nostr crates

- `nostr-sdk`: latest version seen on docs.rs: **0.45.6**, published "2026-11-03" (as listed on the page). Last seen 2026-11-08. Source: https://docs.rs/crate/nostr-sdk/latest
- Licence: MIT. Source: https://docs.rs/crate/nostr-sdk/latest
- Repository: https://github.com/nostrdevkit/nostr (the owner is the `nostrdevkit` organization; the URL `rust-nostr/nostr` redirects there). Source: https://docs.rs/crate/nostr-sdk/latest and https://github.com/rust-nostr/nostr
- Maintainers: individual maintainers **not verified**. The GitHub owner shown is the `nostrdevkit` organization. Source: https://github.com/nostrdevkit/nostr
- MSRV: workspace `rust-version = "1.85.0"`, edition `2024`, in `[workspace.package]`. Source: https://github.com/nostrdevkit/nostr/blob/master/Cargo.toml. The per-crate MSRV on docs.rs is not stated (not verified).
- Async runtime and dependency weight: 16 normal dependencies (15 required, `nostr-memory` optional) and 6 dev dependencies; includes `tokio` (>=1.37), `async-utility` (^0.3), `async-wsocket` (^0.17), `nostr` (^0.45), `nostr-database` (^0.45), `nostr-gossip` (^0.45). Source: https://docs.rs/crate/nostr-sdk/latest
- NIPs listed as implemented and tested behind feature flags: NIP-17, NIP-44, NIP-59, NIP-42. Legend: a checkmark means "implemented and tested behind the relevant feature flag." Source: https://github.com/rust-nostr/nostr (page redirected to nostrdevkit/nostr; read 2026-11-08)
- Relay pool: the crate page and dependencies point at `async-wsocket` and a client builder (search snippet https://docs.rs/nostr-sdk/latest/nostr_sdk/all.html). Explicit "relay pool" feature statement: **not verified** on a read page.
- Maturity statement by the project: "These libraries are in ALPHA state." and "the API will change in breaking ways." Source: https://github.com/nostrdevkit/nostr (read 2026-11-08)
- Latest GitHub release: the Releases tab reads "There aren't any releases here" (https://github.com/rust-nostr/nostr/releases, read 2026-11-08); crates.io versions are the publishing channel instead.
- crates.io page itself was not readable via WebFetch (returned only title): https://crates.io/crates/nostr-sdk
- Crate `nostr` (separate crate, version and date): **not verified** as a separate read.

### 1d. Maturity and known limits (summary)
- NIP-17 status draft per the page; NIP-44 and NIP-59 optional. (Sources in 1a.)
- NIP-17 limit: separate send per recipient; group limit about 10 participants. (Source 1a.)
- NIP-44 known limits: no forward secrecy, no PCS, no PQ security, sender signed. (Source 1a.)
- Client/relay counts: **not verified**.

---

## Part 2: I2P

### 2a. What I2P is
- Project self-description: "I2P is an anonymizing network, offering a simple layer that identity-sensitive applications can use to securely communicate." Source: https://github.com/i2p/i2p.i2p (read 2026-11-08)
- Official downloads: https://i2p.net/en/downloads/ (linked from the repo; contents not read)
- Java I2P (i2p/i2p.i2p): requires Java SDK 17 or higher; some embedded subsystems need only Java 6. Source: https://github.com/i2p/i2p.i2p
- Licence of i2p/i2p.i2p: the page says "See LICENSE.txt"; SPDX identifier **not verified**. Source: https://github.com/i2p/i2p.i2p
- Latest release tag and date: **not verified** (the repo page links to the downloads page only).
- Transports named on the repo page: none (not verified). Transports (NTCP2, SSU2) are named in the emissary README instead: https://github.com/eepnet/emissary
- i2pd (C++ router): "a full-featured C++ implementation of I2P client"; "All communications over I2P are anonymous and end-to-end encrypted." Licence: BSD-3-Clause, file LICENSE (per README). Source: https://github.com/PurpleI2P/i2pd (read 2026-11-08). Latest release date: **not verified**. SAM support: **not verified** on the page read.
- 2025-10-16 I2P project blog on new routers: lists emissary (Rust, "quite new", developed by altonen), go-i2p (Go, "getting closer to completion"), and i2p-cs (C#, "dormant"); "the existing Java and C++ routers... suffer from being difficult to use outside of their own ecosystems." Source: https://www.i2p.net/en/blog/2025/10/16/new-i2p-routers/ (the post does not mention ire).

### 2b. Rust routers and SAM clients

**Routers**
- **emissary** (Rust I2P router). Repository: https://github.com/eepnet/emissary (the `altonen/emissary` URL redirected to this repo in the read on 2026-11-08). README describes it as "lightweight and embeddable I2P router"; transports NTCP2 and SSU2; client protocols I2CP and SAMv3; proxies HTTP and SOCKSv5. No explicit maturity/stability statement on the README (checked 2026-11-08). Source: https://github.com/eepnet/emissary
  - Crate `emissary-cli`: version 0.4.0, published "Apr 12, 2026", MIT (SPDX MIT). Source: https://lib.rs/crates/emissary-cli (lib.rs listing, not crates.io itself). The lib.rs page shows "5 releases (3 breaking)" and no unstable/experimental wording.
  - Repo releases tab: empty (https://github.com/eepnet/emissary, read 2026-11-08). The repo's own text calls the README "tokio-based" for `emissary-cli` only.
  - Licence in repo: MIT and Apache-2.0 license files; no single SPDX expression stated (repo sidebar: "MIT, Apache-2.0 licenses found"). Source: https://github.com/eepnet/emissary
  - MSRV: **not verified**.
- **ire** (Rust, str4d). Repository: https://github.com/str4d/ire. README status: "Ire is in pre-alpha; much of the internal architecture still needs to be defined and implemented." Primarily a binary. Licence: LICENSE.txt, copyright "2017-2023 The Ire Developers"; SPDX **not verified**. Last commit date: not shown. Source: https://github.com/str4d/ire (read 2026-11-08)

**SAM v3 clients in Rust**
- **yosemite**: docs.rs latest 0.7.0, published "2026-03-31", licence MIT, repository https://github.com/eepnet/yosemite, description "Asynchronous SAMv3 library". No unstable/alpha statement on the page. MSRV not stated. Source: https://docs.rs/crate/yosemite/latest (read 2026-11-08). Sync/async APIs and tokio/smol support: per search snippet only, not verified on the page read.
- Other SAM crates seen only in search results, not read: `i2p_client` (0.2.9), `ri2p` (1.0.0), `i2p` (0.0.1). Source: https://docs.rs/crate/i2p_client/latest/source ; licence/maintenance **not verified**.

### 2c. SAM and I2CP (what a program needs)
- SAM v3 (official spec page): version 3.0 introduced in I2P 0.7.3; 3.1 is "Recommended minimum"; 3.2 adds ports, protocols, authorization, SSL, PING/PONG; 3.3 adds PRIMARY sessions and subsessions. 3.2 and 3.3 are "Not fully supported by i2pd." Quoted: "SAM version 3 was introduced in I2P release 0.7.3 (May 2009) and is a stable and supported interface." Source: https://i2p.net/en/docs/api/samv3 (read 2026-11-08; page's own last-updated date not shown)
- Commands a client uses: HELLO (VERSION, optional MIN/MAX, 3.2 adds USER/PASSWORD); SESSION CREATE (STYLE, ID, DESTINATION or TRANSIENT, SIGNATURE_TYPE=7 recommended, `i2cp.leaseSetEncType=6,4` or `4`, PORT/HOST for datagram forwarding); STREAM CONNECT, STREAM ACCEPT, STREAM FORWARD; DATAGRAM (UDP). Source: https://i2p.net/en/docs/api/samv3
- Tunnel builds "can take a minute or more"; the page advises not to use short timeouts. Source: https://i2p.net/en/docs/api/samv3
- Default ports: SAM TCP 7656; datagram UDP 7655. Source: https://i2p.net/en/docs/api/samv3
- I2CP: the spec page at https://i2p.net/en/docs/protocol/i2cp returned no content on read; its purpose and version: **not verified**. The `i2p.net/en/docs/api/i2cp` URL returned HTTP 404 on read.
- Rust-side requirement summary (from the above): a program needs a running local router (Java I2P, i2pd, or emissary) exposing SAM on 127.0.0.1:7656, or embeds an I2CP-capable router (emissary). Whether the SAM port is bound by default in each router: **not verified**.

### 2d. I2P-Bote
- What it is: "I2P-Bote is a plugin for I2P that allows users to send and receive emails while preserving privacy." Also "a serverless, encrypted e-mail application." Source: https://github.com/i2p/i2p.i2p-bote (read 2026-11-08)
- Repository status: "This repository was archived by the owner on Jan 10, 2026. It is now read-only." Source: https://github.com/i2p/i2p.i2p-bote
- Licence: `license.txt` plus a `licenses` folder; SPDX **not verified**. A search snippet of an old readthedocs page said GPL (not verified as current). Source (search snippet): https://bote.readthedocs.io/en/latest/old/v3/info/
- Latest release: not shown on the repo page (Releases section empty). Last commit date: not shown. Counts shown: 2,147 commits, 64 open issues, 4 open PRs.
- Build: Java 1.7+, Apache Ant 1.8+, Gradle 2.14.1 wrapper; Android build notes. Source: https://github.com/i2p/i2p.i2p-bote
- Protocol documentation: the repo has a `doc` folder and a Wiki link, not read. A search snippet points to the V3 protocol doc at bote.readthedocs.io (old). Current protocol spec: **not verified**.
- Android companion (i2p/i2p.i2p-bote.android): marked DEPRECATED in a search snippet; not read on repo: https://awesome.ecosyste.ms/projects/github.com%2Fi2p%2Fi2p.i2p-bote.android (**not verified** on official page).
- Independent C++ implementation pboted: a standalone client (search snippets only): https://pboted.readthedocs.io/ states BSD 3-clause; version line 0.7.X alpha; transition to beta planned in 0.9.X. Not read directly; **not verified**.

---

## Part 3: Table

| Candidate | licence | last release | official link | maturity statement of the project itself |
|---|---|---|---|---|
| nostr-sdk 0.45.6 (nostrdevkit/nostr) | MIT | 2026-11-03 (docs.rs listing) | https://docs.rs/crate/nostr-sdk/latest | "These libraries are in ALPHA state"; "the API will change in breaking ways" (https://github.com/nostrdevkit/nostr) |
| Marmot MDK (marmot-protocol/mdk) | MIT (file LICENSE) | not verified (no release shown) | https://github.com/marmot-protocol/mdk | "for testing only: pin a formal release for anything you ship" (nightly builds) |
| Marmot Protocol spec (marmot-protocol/marmot) | MIT (file LICENSE) | not verified (no release shown) | https://github.com/marmot-protocol/marmot | "Status: adopted" |
| OpenMLS 0.x (openmls/openmls) | MIT (file LICENSE; SPDX text not shown) | not verified (no release shown) | https://github.com/openmls/openmls | No maturity or audit statement on page |
| emissary-cli 0.4.0 (eepnet/emissary) | MIT (SPDX MIT, per lib.rs); repo also has Apache-2.0 file | 2026-04-12 (lib.rs listing) | https://github.com/eepnet/emissary | README: "lightweight and embeddable I2P router"; no stability statement |
| ire (str4d/ire) | not verified (LICENSE.txt, no SPDX on page) | not verified (no date shown) | https://github.com/str4d/ire | "Ire is in pre-alpha" |
| yosemite 0.7.0 (eepnet/yosemite) | MIT | 2026-03-31 (docs.rs) | https://github.com/eepnet/yosemite | "Asynchronous SAMv3 library"; no stability statement |
| i2p (Java I2P, i2p/i2p.i2p) | not verified (LICENSE.txt; SPDX not shown) | not verified (downloads page not read) | https://github.com/i2p/i2p.i2p | "I2P is an anonymizing network, offering a simple layer that identity-sensitive applications can use to securely communicate." |
| i2pd (PurpleI2P/i2pd) | BSD-3-Clause (file LICENSE) | not verified (no tag shown) | https://github.com/PurpleI2P/i2pd | "a full-featured C++ implementation of I2P client" |
| I2P-Bote (i2p/i2p.i2p-bote) | not verified (license.txt; SPDX not shown) | none shown; repository archived 2026-01-10 | https://github.com/i2p/i2p.i2p-bote | "a serverless, encrypted e-mail application"; read-only archive |

---

## Not verified / open questions

1. NIP-17/44/59 final status: the pages label NIP-17 `draft`, NIP-44 and NIP-59 `optional`; no commit dates shown; treat as "as labelled on the page, 2026-11-08".
2. Number of relays and clients using NIP-17: not verified (only a partial client list from search snippets).
3. MIP-00 to MIP-05 numbering, status and content: not verified against the repo (the repo README does not list them; search snippet from marmot-ts docs conflicts on numbering).
4. Marmot "v2 breaking" status: not verified (search snippet only).
5. Latest formal release and date for marmot-protocol/mdk and openmls/openmls: not verified (no release shown on pages read).
6. Least Authority review of Marmot (Nov 2025) and the Cure53 NIP-44 audit (Dec 2023): the Cure53 claim is on the NIP-44 page; the audit report itself not verified. The Least Authority report is not an official source and is not relied upon.
7. nostr crate (separate from nostr-sdk) version, date and MSRV: not verified.
8. nostr-sdk per-crate MSRV on docs.rs: not stated; workspace MSRV 1.85.0 from Cargo.toml only.
9. nostr-sdk relay pool API statement: not verified on a read page.
10. nostr-sdk maintainer names: not verified (organization `nostrdevkit` only).
11. Whether `altonen/emissary` or `eepnet/emissary` is canonical: the altonen URL redirected to eepnet in the read; the I2P blog names altonen. Current owner/canonical repo: not verified beyond the redirect.
12. emissary MSRV, SPDX expression and whether SAM is enabled by default: not verified.
13. ire licence (SPDX) and last commit date: not verified.
14. I2P Java latest release tag and date, and SPDX licence: not verified (downloads page not read).
15. I2CP specification (purpose, version): not verified (page returned no content / 404).
16. SAM support in i2pd (version 3.x coverage beyond the note "Not fully supported by i2pd"): not verified.
17. yosemite async runtime support (tokio/smol) and sync API: from search snippet only; not verified on docs.rs page read.
18. Other Rust SAM crates (`i2p_client` 0.2.9, `ri2p` 1.0.0, `i2p` 0.0.1): licence, date, maintenance not verified.
19. I2P-Bote licence (SPDX), current protocol documentation, and whether any release exists after archival (2026-01-10): not verified. Current I2P-Bote protocol spec: not verified.
20. pboted (C++ I2P-Bote implementation) licence and status: from search snippet/docs, not read directly.
21. Go router go-i2p, C# i2p-cs: only mentioned in the 2025-10-16 blog; not evaluated (not Rust).

Source count: 22 distinct official or project-hosted pages were read and cited above (nips repo ×5 incl. README, marmot ×2, openmls, docs.rs ×3, Cargo.toml, rust-nostr/nostrdevkit ×2, i2p.net ×2 + blog, i2p.i2p, i2p.i2p-bote, i2pd, emissary ×2, yosemite, ire, lib.rs emissary-cli). Plus search-snippet-only pages cited with that label.

Unverified items: 21 (numbered list above).
