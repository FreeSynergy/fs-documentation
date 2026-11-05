# Login / accounts – standards

> The evidence lives centrally in [standards.md](../standards.md) — **do not reload anything from the web.** For this domain the section "follow-up research 2026-11-02" there is authoritative; the quotations are stored in full there.

## Standards in this domain

| Standard | Evidence | Core facts (short form — in detail in the central register) |
|----------|----------|--------------------------------------------------------------|
| **OpenID Connect Core 1.0, errata set 2 (2023-12-15)** | ✅ retrieved 2026-11-02 | identity layer **on top of** OAuth 2.0; ID token; authorization code flow; ID token validation; claims about the end user. Sign-in: `sub` ↔ our user ID |
| **OAuth 2.0 Authorization Framework, RFC 6749** | ✅ retrieved 2026-11-02 | Oct. 2012, obsoletes RFC 5849; updates **RFC 8252** (native apps), **RFC 8996** (TLS deprecated), **RFC 9700** (security BCP) |
| **Web Authentication (WebAuthn) Level 2, W3C Rec. 08.04.2021** | ✅ retrieved 2026-11-02 | "strong, attested, scoped, public key-based credentials" per relying party; strong authentication of users |
| **SCIM, RFC 7643/7644** | ⚠️ **still unverified** (retrieval on 2026-11-02 aborted, not repeated on instruction) | provisioning: create/patch/deactivate account — evidence before use |
| **WebFinger, RFC 7033** | ✅ | discover actors via `acct:`/email |
| **kanidm SPN `name@domain`** | ✅ (glossary verified) | login code unique across instances |

## Positioning of the layers (decisions 2+3)

- Login layer = **account identities** (`sub`, SPN). No person fields here.
- External handles: `https://<instance>/...` IRIs (decision 3); WebFinger connects email/`acct:` to these handles.
- **Separation:** login ≠ identity. Attesting keys and person trust is [identity/](../identity/index.md).

## Open standard points

- Evidence the SCIM field lists (RFC 7643) and endpoint details (RFC 7644) ⚠️
- Watch OAuth 2.1 (draft); not yet citable
- Signature/token binding inwards (gRPC metadata) is implementation, not a standards need
