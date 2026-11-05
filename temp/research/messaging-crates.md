# fs-messenger: Rust crates for e-mail, chat, messengers, calendar and contacts

Researched: 2026-11-05 · by: Claude subagent · status: ⚠️ unless marked ✅

**Scope.** We want one program (`fs-messenger`) for e-mail, chat and messengers, with
**encrypted messages only**, plus calendar and contact exchange. Project rules: 100 % Rust,
licence MIT OR Apache-2.0, free forever. The options are:
(a) Matrix only, plus bridges; (b) our own stack built from crates;
(c) a middle way: our own data model with connectors (matrix-rust-sdk, IMAP/SMTP/JMAP crates,
OpenPGP), and tuwunel as the Matrix homeserver.

**Method / legend.**
- ✅ = checked today at the primary source. For crates that means the crates.io API
  (`https://crates.io/api/v1/crates/<name>`: licence field of the newest version, max version,
  `updated_at`, which is effectively the date of the last release). For repos it means the GitHub
  API or raw files (`api.github.com/repos/<repo>`: SPDX id, `pushed_at` = last push, archived flag,
  latest release) or the repo's own README, Cargo.toml or SPDX file headers.
- ⚠️ = unverified, inferred, or my own assessment.
- "Date" = the crates.io `updated_at` date, i.e. the last publish. "Last push" = GitHub `pushed_at`.

---

## 0. Key findings (read this first)

1. ✅ **Stalwart pulled several of its formerly permissive libraries into its AGPL monorepo in
   Oct 2026.** `calcard`, `jmap-tools` and `sieve` are now **archived** standalone repos. Their
   READMEs say "Development … has moved to the Stalwart repository". In the monorepo,
   `crates/calcard`, `crates/smtp-proto`, `crates/jmap-tools`, `crates/imap-proto`,
   `crates/jmap-proto` and `crates/dav-proto` carry
   `SPDX-License-Identifier: AGPL-3.0-only OR LicenseRef-SEL` and `publish = false`.
   - Sources: https://github.com/stalwartlabs/calcard, https://github.com/stalwartlabs/jmap-tools,
     https://github.com/stalwartlabs/stalwart/tree/main/crates
   - **Consequence:** the last MIT/Apache releases on crates.io are frozen: `calcard 0.3.14`,
     `jmap-tools 0.1.8` and `smtp-proto 0.2.5`. The smtp-proto standalone repo is not archived
     yet, but its last push was 2026-10-01. Future fixes will come only under AGPL. ⚠️ This is a
     real risk for `mail-parser`, `mail-builder`, `mail-auth` and `mail-send` as well. They are
     still separate, not archived and MIT/Apache (last pushes 2026-10-30 to 2026-11-02), but the
     same move could happen.
2. ✅ **sequoia-openpgp is `LGPL-2.0-or-later`**, not MIT/Apache.
   - Source: crates.io API and https://gitlab.com/sequoia-pgp/sequoia/-/raw/main/openpgp/Cargo.toml
   - **rPGP (`pgp` crate) is `MIT OR Apache-2.0`** and is the OpenPGP engine of Delta Chat.
3. ✅ **There is no usable, permissively licensed Rust IMAP *server*.** Only protocol building
   blocks exist: `imap-codec`/`imap-types` 1.0.0 and `imap-next`. Everything above the codec has
   to be written: the mailbox store, UID/MODSEQ semantics, IDLE, CONDSTORE/QRESYNC, search and
   so on. The only complete Rust IMAP servers are Stalwart (AGPL) and toy or immature projects.
4. ✅ **There is no maintained, permissive Rust SMTP *server* framework either.** `samotop` was
   last released in 2022 and `mailin-embedded` in 2024. Parsers exist (`smtp-proto` 0.2.5,
   now frozen), and so does DKIM/SPF/DMARC/ARC (`mail-auth`). Queueing, retry, DSN, TLS policy
   and anti-abuse would be ours to write.
5. ✅ **Delta Chat / chatmail core is a Rust library under MPL-2.0.** It already does
   "encrypted chat over e-mail": Autocrypt, rPGP, async-imap, async-smtp, SQLCipher.
   Source: https://github.com/chatmail/core (Cargo.toml `license = "MPL-2.0"`).
6. ✅ **The Matrix side is in good shape and permissive.** matrix-rust-sdk and vodozemac are
   Apache-2.0, ruma is MIT and tuwunel is Apache-2.0. **The bridges are not:** the mature ones
   (mautrix) are Go and AGPL-3.0, and Rust bridges are immature.

So the user's belief ("only IMAP has to be written ourselves") is **partly wrong**:
- On the **client** side it is roughly true, and even an IMAP client already exists.
- On the **server** side, both IMAP and SMTP server logic would be ours, as would CalDAV/CardDAV
  server logic (unless we run RustiCal (AGPL) or Stalwart (AGPL) as separate services).

---

## 1. IMAP

| Crate / project | URL | Licence | Version · date | Activity | Side | Notes |
|---|---|---|---|---|---|---|
| imap-codec + imap-types | https://github.com/duesee/imap-codec | ✅ MIT OR Apache-2.0 (crates.io) | ✅ 1.0.0 · 2026-11-02 | ✅ last push 2026-11-02 | client **and server** (codec only) | ✅ README: "rock-solid and complete codec … to build IMAP4rev1 clients and servers", fuzz-tested. ⚠️ NLnet-funded. Only parsing/serialising, no I/O and no mailbox logic. |
| imap-next | https://github.com/duesee/imap-next | ✅ MIT OR Apache-2.0 | ✅ 0.3.4 · 2026-02-18 | ✅ last push 2026-04-24 | client **and server** (sans-I/O flows) | ✅ README: "thin sans I/O abstraction" for literals, AUTHENTICATE and IDLE, "paving the ground for higher-level client or server implementations". Pre-1.0, 22 stars. |
| async-imap | https://github.com/async-email/async-imap (repo moved) | ✅ MIT OR Apache-2.0 | ✅ 0.12.0 · 2026-09-30 | active | client | ✅ Used by Delta Chat core. Built on `imap-proto`. Widely used (about 2.2 M downloads). |
| imap (rust-imap) | https://github.com/jonhoo/rust-imap | ✅ Apache-2.0 OR MIT | ✅ 2.4.1 · 2025-02-08 | ⚠️ slow (3.0 alphas have been pending for years) | client, sync | Mature but sync and stagnant. |
| imap-proto | https://github.com/djc/imap-proto | ✅ MIT OR Apache-2.0 | ✅ 0.17.0 · 2026-09-28 | active | client parser | ✅ The duesee README says it lacks types reusable for servers. |
| io-imap (Pimalaya) | https://github.com/pimalaya/io-imap | ✅ MIT OR Apache-2.0 | ✅ 0.8.1 · 2026-11-03 | ✅ very active (created 2026-06) | client (sans-I/O) | ⚠️ Young. Part of the Pimalaya (himalaya) ecosystem, built on imap-codec. |
| Stalwart `imap` / `imap_proto` | https://github.com/stalwartlabs/stalwart/tree/main/crates | ✅ AGPL-3.0-only OR LicenseRef-SEL | ✅ in-tree 1.0.3, not published | ✅ very active | server | Complete and production-grade, but **AGPL**. Not reusable in an MIT/Apache codebase. |
| mailsis-imap, rusmes-server, kiss-mail, elektromail (EUPL-1.2), IMAPServer (2019) | crates.io | various | under 2,100 downloads each | ⚠️ | server | ✅ Download counts are tiny. ⚠️ Not production candidates. |

**Verdict.**
- IMAP **client**: solved. Use async-imap (proven in Delta Chat), or imap-codec/imap-next/io-imap
  if you want sans-I/O.
- IMAP **server**: only the codec layer exists (imap-codec/imap-next). The server logic is ours,
  and it is large (see §9).

## 2. SMTP and mail formats

| Crate | URL | Licence | Version · date | Side | Notes |
|---|---|---|---|---|---|
| lettre | https://github.com/lettre/lettre | ✅ MIT | ✅ 0.11.23 · 2026-08-03 | client (submission) + message builder | ✅ The most widely used (23 M downloads). Last push 2026-10-02. |
| mail-send (Stalwart) | https://github.com/stalwartlabs/mail-send | ✅ Apache-2.0 OR MIT | ✅ 0.7.0 · 2026-11-01 | client, with DKIM signing | ⚠️ Risk of a move to AGPL (see §0). |
| async-smtp | https://github.com/async-email/async-smtp | ✅ MIT OR Apache-2.0 | ✅ 0.10.2 · 2025-05-13 | client | ✅ Used by Delta Chat core. |
| smtp-proto (Stalwart) | https://github.com/stalwartlabs/smtp-proto | ✅ Apache-2.0 OR MIT (crate 0.2.5) | ✅ 0.2.5 · 2026-10-01 | client + **server** parser | ✅ The monorepo copy is now AGPL OR SEL with `publish = false`. Treat 0.2.5 as **frozen**. |
| mailin / mailin-embedded | https://code.alienscience.org/alienscience/mailin | ✅ MIT OR Apache-2.0 | ✅ 0.6.5 / 0.8.3 · 2024-08-31 | **server** (receive only) | ⚠️ Low activity. A small embeddable SMTP receiver. |
| samotop | https://gitlab.com/BrightOpen/Samotop/ | ✅ MIT OR Apache-2.0 | ✅ 0.13.2 · 2022-01-30 | server | Effectively abandoned. |
| smtp-server (kannader) | https://github.com/Ekleog/kannader | ✅ MIT OR Apache-2.0 | ✅ 0.1.0 · 2022-10-09 | server | Abandoned. |
| smtpbis | https://github.com/zerospam/smtpbis | ✅ GPL-3.0+ | ✅ 0.1.7 · 2021 | server | Wrong licence and dead. |
| mail-parser (Stalwart) | https://github.com/stalwartlabs/mail-parser | ✅ Apache-2.0 OR MIT | ✅ 1.0.1 · 2026-11-02 | both | ✅ Not archived. Very robust MIME parser, 5.2 M downloads. |
| mail-builder (Stalwart) | https://github.com/stalwartlabs/mail-builder | ✅ Apache-2.0 OR MIT | ✅ 2.0.1 · 2026-11-02 | both | ✅ Used by Delta Chat core. |
| mail-auth (Stalwart) | https://github.com/stalwartlabs/mail-auth | ✅ Apache-2.0 OR MIT | ✅ 0.15.1 · 2026-10-30 | both | DKIM, ARC, SPF, DMARC, plus ⚠️ MTA-STS/TLS-RPT report parsing. |
| mailparse | https://github.com/staktrace/mailparse | ✅ 0BSD | ✅ 0.18.0 · 2026-10-05 | both | Simple and very widely used (16 M downloads). Used by Delta Chat. |
| email-encoding | https://github.com/lettre/email-encoding | ✅ MIT OR Apache-2.0 | ✅ 0.4.2 · 2026-07-27 | both | Low-level helpers. |
| sieve-rs (Stalwart) | https://github.com/stalwartlabs/sieve | ✅ AGPL-3.0-only (0.7.3); repo **archived** | ✅ 0.7.3 · 2026-09-22 | server | Not usable for us. |

**Verdict.**
- SMTP **client** and message parse/build: solved, all permissive.
- SMTP **server/MTA**: no maintained permissive framework. Inbound acceptance (mailin-style)
  is small. A full MTA (queue, retry, DSN, DANE/MTA-STS, rate limits, spam) is large.

## 3. JMAP (RFC 8620/8621, Contacts RFC 9610, Calendars draft)

| Crate | URL | Licence | Version · date | Side | Notes |
|---|---|---|---|---|---|
| jmap-client (Stalwart) | https://github.com/stalwartlabs/jmap-client | ✅ Apache-2.0 OR MIT | ✅ 0.4.3 · 2026-09-28 | client | Mail + core, ⚠️ plus Sieve. GitHub reports Apache-2.0. Not archived. |
| io-jmap (Pimalaya) | https://github.com/pimalaya/io-jmap | ✅ MIT OR Apache-2.0 | ✅ 0.7.0 · 2026-11-03 | client | ✅ Created 2026-06. Young. |
| crate-jmap family (`jmap-server`, `jmap-base-client`, `jmap-mail-types`, `jmap-contacts-types`, `jmap-calendars-*`, `jmap-chat-*`, …) | https://github.com/MarkAtwood/crate-jmap | ✅ MIT OR Apache-2.0 (crates.io) | ✅ 0.5.0 · 2026-11-03 | client **and server** (backend-agnostic method handlers) | ✅ Created 2026-05-02, 2 GitHub stars, under 1,400 downloads per crate. ⚠️ Very young, single author, unproven. But it is the **only permissive JMAP server toolkit** and covers Contacts (RFC 9610), Calendars, Tasks and a JMAP Chat draft. Worth watching or evaluating. |
| jmap-tools (Stalwart) | https://github.com/stalwartlabs/jmap-tools | ✅ Apache-2.0 OR MIT (0.1.8) | ✅ 0.1.8 · 2026-08-20 | helpers | ✅ Repo **archived** and moved into the AGPL monorepo. Frozen. |
| Stalwart `jmap` / `jmap_proto` | monorepo | ✅ AGPL-3.0-only OR SEL | in-tree | server | Most complete JMAP server (Mail, Contacts, Calendars, ⚠️ Files/Sharing). AGPL. |
| `jmap` (2016) | crates.io | — | ✅ 0.0.5 · 2016 | — | Dead. |

## 4. CalDAV / CardDAV / iCalendar / vCard / JSCalendar / JSContact

| Crate / project | URL | Licence | Version · date | Side | Notes |
|---|---|---|---|---|---|
| calcard (Stalwart) | https://github.com/stalwartlabs/calcard | ✅ Apache-2.0 OR MIT (0.3.14) | ✅ 0.3.14 · 2026-09-15 | data formats | ✅ iCal, vCard, JSCalendar and JSContact, with conversion between them and RRULE expansion. **Archived**: development moved to the AGPL monorepo, so 0.3.14 is the last permissive version. Forkable. |
| icalendar | https://github.com/hoodie/icalendar | ✅ MIT/Apache-2.0 (crates.io field, i.e. MIT OR Apache-2.0) | ✅ 0.17.17 · 2026-10-26 | data | Mature builder/parser, about 1 M downloads. |
| ical-rs, vcard-rs (Pimalaya) | https://github.com/pimalaya/ical, https://github.com/pimalaya/vcard | ✅ MIT OR Apache-2.0 | ✅ 0.7.0 / 0.6.0 · 2026-11-03 | data | ⚠️ Young (2026). |
| ical (Peltoche) | https://github.com/Peltoche/ical-rs | ✅ crates.io says "non-standard" licence | ✅ 0.11.0 · 2024-03-13 | data | Licence unclear, so avoid. |
| vcard (magiclen) | https://github.com/magiclen/vcard | ✅ MIT | ✅ 0.6.0 · 2026-10-17 | data | Low usage. |
| jscontact | https://github.com/Its-Just-Nans/jscontact | ✅ MIT | ✅ 0.2.1 · 2025-01-29 | data | RFC 9553 types. |
| jscalendar / jscalendar-kit | crates.io | ⚠️ | ✅ 0.1.0 · 2026 | data | Tiny (under 50 downloads). |
| libdav | https://git.sr.ht/~whynothugo/libdav | ✅ ISC | ✅ 0.11.2 · 2026-10-30 | **client** (CalDAV + CardDAV) | ⚠️ Used by pimsync/vdirsyncer-rs. ISC is permissive and MIT-compatible. |
| fast-dav-rs | https://github.com/Goopil/fast-dav-rs | ✅ LGPL-3.0 | ✅ 0.19.0 · 2026-10-04 | client | Wrong licence. |
| dav-server | https://github.com/messense/dav-server-rs | ✅ Apache-2.0 | ✅ 0.11.0 · 2026-02-21 | **server** (WebDAV only) | ✅ Last push 2026-10-30. WebDAV only, no CalDAV/CardDAV semantics. ⚠️ Could be a base layer. |
| mailrs-dav | https://github.com/goliajp/mailrs | ✅ Apache-2.0 OR MIT | ✅ 2.0.0 · 2026-10-22 | **server** handlers (CalDAV RFC 4791, CardDAV RFC 6352) | ✅ "framework-agnostic" server handlers. Repo has 8 stars. ⚠️ Young and unproven. |
| RustiCal | https://github.com/lennart-k/rustical | ✅ AGPL-3.0 | ✅ v0.18.0 · 2026-10-31 | **server** (complete) | ✅ README: "under active development", tested with DAVx5, GNOME, Evolution and Apple. Usable as a *separate service*. Code not reusable under MIT/Apache. |
| Stalwart `dav`, `dav-proto`, `groupware` | monorepo | ✅ AGPL-3.0-only OR SEL | in-tree | server | Complete. AGPL. |

## 5. OpenPGP, Autocrypt, S/MIME

| Crate | URL | Licence | Version · date | Notes |
|---|---|---|---|---|
| pgp (rPGP) | https://github.com/rpgp/rpgp | ✅ MIT OR Apache-2.0 | ✅ 0.21.0 · 2026-10-03 | ✅ Pure Rust, RFC 9580. Used by Delta Chat. Last push 2026-11-04, 7.5 M downloads. ⚠️ Has had independent security audits (per project claims; not re-checked). |
| sequoia-openpgp | https://gitlab.com/sequoia-pgp/sequoia | ✅ **LGPL-2.0-or-later** | ✅ 2.4.2 · 2026-10-14 | Most complete OpenPGP in Rust. LGPL in a statically linked Rust binary brings relinking obligations, so ⚠️ it is not "MIT OR Apache" compatible in spirit. Avoid if the licence rule is strict. |
| sequoia-autocrypt | same | ✅ LGPL-2.0-or-later | ✅ 0.26.0 (0.27.0-pqc.1) · 2025-11-12 | Same issue. |
| autocrypt | crates.io | ⚠️ | ✅ 0.1.0 · 2017 | Dead. ✅ Delta Chat implements Autocrypt itself on top of rPGP (in MPL-2.0 core). |
| openpgp-card | https://codeberg.org/openpgp-card/openpgp-card | ✅ MIT OR Apache-2.0 | ✅ 0.7.0 · 2026-07-23 | Smartcard/YubiKey support. |
| rasn-smime | https://github.com/librasn/rasn | ✅ MIT OR Apache-2.0 | ✅ 0.30.0 · 2026-11-02 | S/MIME ASN.1 *types* only. |
| smime-tree | https://github.com/MarkAtwood/crate-mime | ✅ MIT OR Apache-2.0 | ✅ 0.3.3 · 2026-06-16 | S/MIME sign, verify, encrypt and decrypt. ⚠️ Very young (273 downloads). |
| RustCrypto `cms` | ⚠️ not checked | ⚠️ MIT OR Apache-2.0 | ⚠️ | CMS/PKCS#7 building blocks. |

**Verdict.** OpenPGP is rPGP (permissive). Autocrypt logic is small: either our own, or borrowed
conceptually from Delta Chat. S/MIME support in Rust is thin. Treat it as receive/verify only, or
leave it for later.

## 6. Matrix

| Project | URL | Licence | Version · date | Notes |
|---|---|---|---|---|
| matrix-sdk (matrix-rust-sdk), plus matrix-sdk-crypto and matrix-sdk-ui | https://github.com/matrix-org/matrix-rust-sdk | ✅ Apache-2.0 | ✅ 0.19.1 · 2026-09-18 | ✅ Last push 2026-11-05. README: "considered production ready and backs … Element X". Client side. E2EE via matrix-sdk-crypto on top of vodozemac. Still 0.x, so API churn is to be expected. |
| vodozemac | https://github.com/matrix-org/vodozemac | ✅ Apache-2.0 | ✅ 0.11.1 · 2026-09-30 | ✅ Pure-Rust Olm/Megolm, replacing libolm. ⚠️ Audited by Least Authority in 2022 (not re-checked). |
| ruma | https://github.com/ruma/ruma | ✅ MIT | ✅ 0.17.2 · 2026-10-24 | Matrix types and APIs, used by the SDK and by servers. |
| tuwunel | https://github.com/matrix-construct/tuwunel | ✅ Apache-2.0 | ✅ v1.9.4 · 2026-10-10. Last push 2026-11-05. 2,736 stars | ✅ README: "official successor to conduwuit", "used by many companies … full-time staff", "primarily sponsored by the government of Switzerland". Migrates in place from conduwuit and Conduit (RocksDB). Synapse migration "not yet". ⚠️ No paid or open-core parts found. |
| continuwuity | https://github.com/continuwuity/continuwuity | ✅ Apache-2.0 | last push 2026-11-05 | Community fork of conduwuit (the alternative). |
| Conduit | https://gitlab.com/famedly/conduit (mirror: github timokoesters/conduit) | ✅ Apache-2.0 | last push 2026-11-05 | The original. Fewer features. |
| mautrix bridges (whatsapp, signal, telegram, …) | https://github.com/mautrix/whatsapp | ✅ AGPL-3.0, **Go** | ✅ whatsapp v0.2610.0 · 2026-10-16 | Mature and the de-facto standard. Not Rust, not permissive. Fine to *run* as separate services. |
| Rust bridges (`matrix-bridge-whatsapp/-telegram/-discord/...`, palpo-im) | crates.io | ✅ Apache-2.0 (crate field) | ✅ 0.1.x · 2026-02-28 | ✅ 24 to 59 downloads; the GitHub repo for -whatsapp returns 0 stars, no README found. ⚠️ Toy-level. Not production. |

**How bridges handle E2EE** (✅ https://docs.mau.fi/bridges/general/end-to-bridge-encryption.html):
- The bridge is a Matrix client that **decrypts on the bridge host**. This is "end-to-bridge
  encryption". Traffic to the remote network (e.g. Signal) is encrypted by that network's own
  protocol.
- So E2EE is **broken at the bridge**: whoever runs the bridge sees the plaintext.
- Element clients show warnings for messages from bridge "ghost" users even with invisible crypto.
- **Implication for "encrypted messages only":** bridges only work if the user runs the bridge
  themselves (on their own FreeSynergy node). Even then the bridge holds plaintext.

## 7. Stalwart (licensing in detail)

- ✅ **Licence:** dual **AGPL-3.0-only** and **Stalwart Enterprise License v2 (LicenseRef-SEL,
  proprietary)**. Each file has a REUSE/SPDX header.
  Source: https://github.com/stalwartlabs/stalwart README, section "License".
- ✅ **Open-core:** the README says "About 85% of Stalwart's features are free and open source
  under the AGPL-3.0. The rest make up the Enterprise edition". Named examples: **multi-tenancy,
  SCIM provisioning, sharded storage, live telemetry** (full list: https://stalw.art/compare/).
  An Enterprise licence comes free with OpenCollective sponsorship of $5 or more per month.
- ✅ **Latest release:** v1.0.3, 2026-11-04. Very active (last push 2026-11-04, 15.7 k stars).
- ✅ **Monorepo crates** (all AGPL OR SEL): calcard, common, crypto, dav-proto, dav, directory,
  email, groupware, http(-proto), imap(-proto), jmap(-proto), jmap-tools, managesieve, pop3,
  sieve, smtp(-proto), smtp-report, spam-filter, store, and others.
- ✅ **Separately licensed and still reusable (Apache-2.0 OR MIT, standalone repos):** mail-parser
  1.0.1, mail-builder 2.0.1, mail-auth 0.15.1, mail-send 0.7.0, jmap-client 0.4.3, and smtp-proto
  0.2.5 (but frozen).
- ✅ **Frozen-permissive (archived, last MIT/Apache version):** calcard 0.3.14, jmap-tools 0.1.8.
- ✅ **Not reusable:** sieve-rs (AGPL even on crates.io).
- ⚠️ **Assessment:** running Stalwart as a *separate, unmodified service* is AGPL-compliant.
  But FreeSynergy code cannot link it, and the trend is toward fewer permissive pieces.

## 8. Other relevant projects

| Project | URL | Licence | Version · date | Notes |
|---|---|---|---|---|
| **chatmail core (Delta Chat core)** | https://github.com/chatmail/core | ✅ **MPL-2.0** | ✅ v2.67.0 · 2026-11-02. Last push 2026-11-05 | ✅ Rust (edition 2024) crate `deltachat`. **Not on crates.io** (git dependency). Uses `async-imap`, `async-smtp`, `pgp` 0.21 (with `pqc`), `mail-builder`, `mailparse`, `rusqlite` + **sqlcipher**, and `iroh` (P2P realtime). Offers a JSON-RPC server, FFI and Python bindings. Encrypted chat over plain IMAP/SMTP with Autocrypt; ⚠️ guaranteed E2EE in current versions. MPL-2.0 is file-level copyleft: it can be used as a dependency from MIT/Apache code, but changes to MPL files must stay MPL. |
| chatmail relay | https://github.com/chatmail/relay | ✅ MIT | last push 2026-11-04 | ✅ README: interoperable MTAs that require DKIM **and OpenPGP-encrypted** messages, auto-delete, no state. ⚠️ It is deployment scripts for Postfix/Dovecot plus Python filters, not Rust. Conceptually it is exactly "encrypted messages only" on the server side. |
| xmpp-rs (`xmpp`, `tokio-xmpp`, `xmpp-parsers`) | https://gitlab.com/xmpp-rs/xmpp-rs | ✅ MPL-2.0 | ✅ xmpp 0.7.0 / tokio-xmpp 6.0.0 · 2026-06-11 | Client. ⚠️ No OMEMO E2EE support in the high-level crate (not checked in detail). Server side: none in Rust worth naming. |
| email-lib / Pimalaya (himalaya) | https://github.com/pimalaya/core | ✅ MIT | ✅ 0.27.0 · 2026-02-19 | High-level e-mail client library (IMAP, SMTP, Maildir, PGP). ✅ The new `io-*` sans-I/O crates (io-imap, io-smtp, io-jmap, io-webdav) were published 2026-06 to 11 and are MIT OR Apache-2.0. Good permissive client-side building blocks. |

---

## 9. Effort estimate (⚠️ = my assessment)

### What can be reused (client side, all permissive) ✅
- IMAP: async-imap or imap-codec/imap-next.
- SMTP: lettre, mail-send or async-smtp.
- MIME: mail-parser, mail-builder, mailparse.
- DKIM/SPF/DMARC: mail-auth.
- OpenPGP: rPGP.
- Matrix: matrix-sdk with vodozemac.
- JMAP: jmap-client or io-jmap.
- CalDAV/CardDAV: libdav.
- Formats: icalendar, calcard 0.3.14 (frozen) and the Pimalaya ical/vcard crates.

### What we must write ourselves

| Piece | (b) own stack | (c) middle way | Size ⚠️ | Notes |
|---|---|---|---|---|
| Unified data model (conversation, message, identity, key, contact, event) + local encrypted store | yes | yes | **medium–large** | The core of fs-messenger, whichever option we pick. |
| Connector: Matrix (matrix-sdk) | yes | yes | small–medium | The SDK does sync, E2EE and verification. We map rooms to conversations. |
| Connector: mail (IMAP/SMTP/JMAP) | yes | yes | medium | Sync state, folders, threading, offline queue. |
| Autocrypt + "encrypted-only" policy on mail (key discovery, gossip, setup message, refusing plaintext) | yes | yes | small–medium | Alternative: embed chatmail core (MPL-2.0), which already does this. |
| CalDAV/CardDAV client sync + iTIP/iMIP invites | yes | yes | medium | Formats are covered by crates. Sync and scheduling logic is ours. |
| **IMAP server** (store, UIDs, MODSEQ/CONDSTORE/QRESYNC, IDLE, SEARCH, ACL, quota) | yes | no (use an existing server) | **large** (months; interop with real clients is the hard part) | Only imap-codec/imap-next exist. |
| **SMTP server/MTA** (inbound, queue, retries, DSN, TLS/DANE/MTA-STS, DKIM signing, spam, rate limits, deliverability) | yes | no | **large**, plus permanent operational work | mail-auth and smtp-proto (frozen) help. Deliverability and abuse handling are the ongoing cost. |
| JMAP server | optional | no | large | crate-jmap is very young. |
| CalDAV/CardDAV server | yes | no (RustiCal/Stalwart as a separate AGPL service, or later mailrs-dav/dav-server) | medium–large | |
| Matrix homeserver | no (use tuwunel) | no (tuwunel) | — | Apache-2.0, so it can even be embedded or forked. |
| Bridges to WhatsApp/Signal/Telegram | Go/AGPL mautrix as separate services, or none | same | large if written in Rust | Bridges break E2EE at the bridge. |

### Main risks
1. ✅ **Licence drift at Stalwart** (calcard, jmap-tools, smtp-proto already moved to AGPL).
   Pin versions and be ready to fork the mail-* crates.
2. **Server-side mail is an operations problem, not a coding problem.** Deliverability, IP
   reputation and abuse handling are the risk for (b).
3. The mail "encrypted-only" rule cuts us off from most of the e-mail world: plaintext senders.
   We need a policy: reject, quarantine, or read-only.
4. Bridges contradict "encrypted only" unless they are self-hosted.
5. matrix-sdk is still 0.x, so API churn means connector maintenance.
6. LGPL Sequoia is tempting because it is feature-rich, but it breaks the licence rule. Stay with rPGP.

## 10. Recommendation (opinion ⚠️, kept separate from the facts above)

**Option (c), the middle way, with two adjustments.**

1. **Client side: our own data model plus connectors, all from permissive crates.**
   - matrix-sdk (Matrix chat, E2EE)
   - async-imap or imap-next with lettre/mail-send and mail-parser/mail-builder (mail)
   - rPGP + our own Autocrypt layer (encryption-only mail)
   - libdav + calcard 0.3.14/icalendar (calendar and contacts)
   - jmap-client/io-jmap (JMAP servers such as Stalwart or Fastmail)

   Seriously evaluate **embedding chatmail core (MPL-2.0)** as the "encrypted e-mail chat"
   connector instead of writing Autocrypt and the chat-over-mail logic ourselves. It is the only
   mature, maintained Rust implementation of exactly the "encrypted messages only over e-mail"
   idea, and it is built on the same crates we would choose. MPL-2.0 is compatible with an
   MIT/Apache project if we do not relicense its files.

2. **Server side: do not write IMAP/SMTP servers now.**
   - **tuwunel** (Apache-2.0) as the Matrix homeserver.
   - For mail, run an existing server as a separate service: Stalwart (AGPL, without Enterprise
     features) or a chatmail relay. Then revisit writing our own only if a hard requirement
     appears.
   - The user's assumption that "only IMAP must be written" holds for the client. On the server,
     IMAP **and** SMTP **and** CalDAV are each large pieces of work, and SMTP is mostly an
     operations burden.

3. **Option (a), Matrix only plus bridges, is weaker against our own requirements.**
   - The mature bridges are Go/AGPL.
   - They break E2EE at the bridge.
   - They do not give us e-mail or calendar natively.

   Keep bridges as optional, self-hosted add-ons.

4. **Option (b), a fully own stack, is not justified now.**
   - The server parts are large.
   - The only permissive server toolkits (imap-codec, crate-jmap, mailrs-dav) are young or
     codec-only.
