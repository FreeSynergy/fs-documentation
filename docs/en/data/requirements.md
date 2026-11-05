# Data – conversation record and work order (2026-11-02)

This file preserves **what was decided in the conversation** — so the state survives and we do not have to start from scratch. Status: **working document**, not yet a specification. The decisions of 2026-11-01 ([standards.md](standards.md)) remain in force; this document continues from them.

## 1. Basic order

- It is about **the data — and how one can store it**.
- First we need **all the standards**. Whether **ISO, DIN, RFC, W3C** and so on.
- What has already been done (standards register, decisions 1–5, domain directories) is **continued**, not reinvented.
- **Name directories in English**, like all other areas.
- **For now only maintain `docs/de/`; `docs/en/` comes later.** (explicit instruction 2026-11-02)
- Discuss first, then write it down — this file is the preserved conversation record; improvement in small steps.

## 2. The domains mentioned (in the words of the person commissioning the work)

| Domain (English directory) | What was said about it |
|----------------------------|------------------------|
| `login/` | logins — e.g. **OAuth**, **SCIM** — and **Anton's Web of Trust**, for which he runs a real-life project: <https://github.com/real-life-org/web-of-trust> |
| `person/` | **The human who signs in.** (probably vCard — or something like that) |
| `profile/` | Every person can have **profiles**, so that one **shows the sides of oneself one wants to show**. Example: with dating it can become **dangerous** if one's sexuality becomes known. → visibility is a core problem of this domain. |
| `events/` | The appointments one enters in a calendar and the like. |
| `projects/` | For PMs (project management) — open question: **is there a standard for that?** → research needed. |
| `messages/` | messages — not yet elaborated; derive it from the apps. |

Plus the domains that already existed: `contacts/` (contact models), `identity/` (Web of Trust), `geodata/` (places/addresses).

## 3. Order: derive it from the apps

> "Look at the apps — and look at what could be stored there. All of that has to be standardised somehow. Find out what belongs where."

→ Next concrete step: **data inventory per app** in [docs/de/programs/](../programs/) (every app has or will get an `api.md`), assigning the data found to the domains. The result goes into this document or into the respective domain.

## 4. Structure per domain (newly defined 2026-11-02)

Every domain directory henceforth contains:

| File | Content |
|------|---------|
| `index.md` | overview + standards table + open points |
| `description.md` | **description** — what the domain is, what it covers, differentiation from other domains |
| `technical.md` | **technical explanation** — storage perspective, keys, flow, projections |
| `standards.md` | **standard texts** — the relevant standards with evidence status and field lists/excerpts |
| `examples.md` | **examples** — concrete JSON/text examples |

Additions are expressly welcome (e.g. per standard a subdirectory with `description.md` + `storage.md`, as already planned for JSContact).

## 5. Directory names: English (renamed on 2026-11-02)

| old (German) | new (English) |
|--------------|---------------|
| `kontakt/` | `contacts/` |
| `profil/` | `profile/` |
| `projekte/` | `projects/` |
| `identitaet/` | `identity/` |
| `geodaten/` | `geodata/` |
| `events/`, `login/`, `messages/` | unchanged |
| — | `person/` **considered, but not yet created** — see decision candidate 6 (open question 6.4) |

**Newly considered differentiation:** `person/` = the human (the real person behind an account) · `contacts/` = contact records (also about others) · `profile/` = what one **shows** about oneself · `login/` = the **access** · `identity/` = whom one **trusts**.

## 5a. Evidence status 2026-11-02 (research completed — **do not download again**)

All retrieved facts stand **in full** in [standards.md → "follow-up research 2026-11-02"](standards.md). Summary:

- **OIDC Core 1.0 (errata set 2, 2023-12-15)** ✅ evidenced — ⚠️→✅
- **OAuth 2.0 RFC 6749** ✅ evidenced (updates: RFC 8252, 8996, 9700) — ⚠️→✅
- **WebAuthn Level 2 (W3C Rec. 2021-04-08)** ✅ evidenced — new in the register
- **SCIM RFC 7643/7644** ⚠️ still unverified (retrieval aborted, not repeated on instruction)
- **Anton's WoT repo reviewed:** WoT Spec v0.1.0-draft = W3C Verifiable Credentials + DIDComm v2.1 + Ed25519 + ECIES; `did:key`; principle "Verification ≠ Trust"; successor RLTP (gen 3) in `real-life-org/trust-protocol`. All details in standards.md.
- **Projects:** ISO 21502:2020 ✅ (process guide, **not a data format**); MSPDI/`mspdi_pj12.xsd` ✅ (de-facto export format); W6C ⚠️ unevidenced; **no open RFC/W3C data spec for boards/tasks** → own spec stays spec candidate no. 3.

## 6. Open questions from the conversation

1. **projects:** does a PM standard exist? → **answered 2026-11-02:** no open data standard; ISO 21502 = process, MSPDI = proprietary. Own spec stays. (Details in standards.md → follow-up research)
2. **messages:** what exactly — chat, comments, mail? → derive from the app inventory
3. **profile:** implement field groups / purpose binding (dating example: sensitive fields like `sexualOrientation` belong **not** in the work/calendar context; BDSG/GDPR special categories ⚠️ to evidence)
4. **person:** **open — decision candidate no. 6.** The agent's proposal: **no `person/` directory of its own.** Reasoning: the person data of the human is already covered — a JSContact `Card` with role "individual" in `contacts/`, linked to the account (`sub` from `login/`) and the social actor (`profile/`). What remains are genuinely **two** domains as said in the conversation: `identity/` (whom does one trust — WoT, DIDs, Verifiable Credentials) and `profile/` (what does one show to whom). `person/` would only be a projection without data of its own. → **please confirm or reject.**
5. **identity:** Anton's repo `real-life-org/web-of-trust` **reviewed 2026-11-02** — facts in standards.md → follow-up research; `mapping.md` (AS2 `Relationship`/`publicKey`) still outstanding

## 7. Next steps (tick the boxes so one can see where we stand)

- [x] conversation preserved (this file)
- [x] directories renamed (English), `person/` newly created
- [x] every domain equipped with `description.md` / `technical.md` / `standards.md` / `examples.md` (first draft) — **actually finished on 2026-11-02** (8 domains × 4 files; `person/` waits for decision candidate 6)
- [ ] app data inventory (docs/de/apps/) → assignment "what belongs in which domain"
- [x] evidence added 2026-11-02: OIDC ✅, OAuth ✅, WebAuthn ✅, Anton's WoT ✅, projects researched; **left open: SCIM ⚠️, MLS ⚠️, DID Core/VC ⚠️, W6C ⚠️** (do not download again — everything existing is in standards.md)
- [x] Anton's WoT repo reviewed (facts in standards.md); → `identity/mapping.md` still open
- [ ] `en/` translation once `de/` is complete
