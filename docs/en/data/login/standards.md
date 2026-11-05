# Login / accounts – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.** For this domain the section "follow-up research 2026-11-02" there is authoritative; the quotations are stored in full there.


## State 2026-11-05

Evidence: `temp/research/geodata-projects-profile-login.md` (2026-11-05).

| Standard | Evidence | Role |
|----------|----------|------|
| **WebAuthn Level 3** (W3C Rec 2026-08-25), passkeys | ✅ | sign-in |
| OAuth 2.1 (draft -17, 2026-10-31); RFC 9700 = BCP 240 | ✅ | follow 2.1, apply BCP |
| **OpenID Federation 1.0** (final 2026-02-17): trust anchors, trust chains, **trust marks**, metadata policy, automatic registration | ✅ | **candidate for federation between instances** — our trust lists as trust anchors, Web-of-Trust levels as trust marks |
| FedCM | ✅ First Public WD (2024-08) only | watch |
| WebFinger RFC 7033 JRD: `subject`, `aliases`, `properties`, `links` (`rel`, `type`, `href`, `titles`, `properties`) | ✅ | discovery: link to AS2 actor, OIDC issuer, DID |
| SCIM RFC 7643 `User`/`Group`/enterprise attributes | ✅ listed in the research file | mapping to `account` + JSContact |
| **Kanidm 1.12.0** (2026-11-01, MPL-2.0): passkeys, OAuth2/OIDC provider (token exchange), read-only LDAPS, RADIUS | ✅ | identity provider in the server (ADR 0024) |
| Kanidm SCIM: **inbound sync source only**, no provisioning server; no OpenID Federation | ✅ | gaps → our own SCIM server; OpenID Federation as sidecar |

## Standards in this domain

| Standard | Evidence | Core facts (short form — in detail in the central register) |
|----------|----------|--------------------------------------------------------------|
| **OpenID Connect Core 1.0, errata set 2 (2023-12-15)** | ✅ retrieved 2026-11-02 | identity layer **on top of** OAuth 2.0; ID token; authorization code flow; ID token validation; claims about the end user. Sign-in: `sub` ↔ our user ID |
| **OAuth 2.0 Authorization Framework, RFC 6749** | ✅ retrieved 2026-11-02 | Oct. 2012, obsoletes RFC 5849; updates **RFC 8252** (native apps), **RFC 8996** (TLS deprecated), **RFC 9700** (security BCP) |
| **Web Authentication (WebAuthn) Level 2, W3C Rec. 08.04.2021** | ✅ retrieved 2026-11-02 | "strong, attested, scoped, public key-based credentials" per relying party; strong authentication of users |
| **SCIM, RFC 7643 (core schema) / RFC 7644 (protocol)** | ✅ Sept 2015, Proposed Standard (checked 2026-11-05); newer: RFC 9865 (cursor pagination), RFC 9944 (device schema), RFC 9967 (SCIM events) | provisioning: create/patch/deactivate accounts via a standard API; every program speaks SCIM (ADR 0024) |
| **WebFinger, RFC 7033** | ✅ | discover actors via `acct:`/email |
| **kanidm SPN `name@domain`** | ✅ (glossary verified) | login code unique across instances |

## Positioning of the layers (decisions 2+3)

- Login layer = **account identities** (`sub`, SPN). No person fields here.
- External handles: `https://<instance>/...` IRIs (decision 3); WebFinger connects email/`acct:` to these handles.
- **Separation:** login ≠ identity. Attesting keys and person trust is [identity/](../identity/index.md).

## Open standard points

- Evidence the SCIM field lists (RFC 7643) and endpoint details (RFC 7644) ⚠️
- Watch OAuth 2.1 (draft); not yet citable
- Signature/token binding inwards (Cap'n Proto connection metadata) is implementation, not a standards need
