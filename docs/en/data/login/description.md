# Login / accounts – description

**What this domain is:** the **access** to FreeSynergy. It answers two separate questions:

1. **Authentication** — who may log in? (OIDC, OAuth 2.0, WebAuthn)
2. **Provisioning** — how do accounts come into being and change? (SCIM ✅ RFC 7643/7644, kanidm as the reference implementation)

**What it covers:**

- Account identities: `sub` claim (OIDC), SPN `name@domain` (kanidm pattern, ✅ glossary verified)
- Authorization for APIs and integrations (OAuth 2.0)
- Passwordless sign-in with public-key credentials (WebAuthn)
- Discovering actors via `acct:`/email (WebFinger, RFC 7033, ✅)

**What it does NOT cover (basic rule from decision 3):**

| Topic | Where it lives |
|-------|----------------|
| Person **data** | [people/](../people/index.md) (JSContact card, linked to the account) |
| Social identity, profile | [profile/](../profile/index.md) |
| Belief/key attestation | [identity/](../identity/index.md) — **a login proves no identity** |

**Mnemonic:** a login is not a data model but the access to one. The login layer only knows account identifiers.
