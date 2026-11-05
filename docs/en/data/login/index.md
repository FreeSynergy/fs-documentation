# Login / accounts

**Two questions, handled separately:** (a) *how do you sign in?* → authentication; (b) *how does an account come into being?* → provisioning. Reference implementation in the project: **kanidm** (OAuth/OIDC + SCIM).

## Standards in this domain

| Standard | Evidence | Role in FreeSynergy |
|----------|----------|---------------------|
| **OIDC Core 1.0 (errata set 2)** | ✅ retrieved 2026-11-02 | sign-in: `sub` claim ↔ our user ID; quote/details in [standards.md → follow-up research](../standards.md) |
| **SCIM, RFC 7643/7644** | ⚠️ unverified (retrieval on 2026-11-02 aborted) | provisioning: create/patch/deactivate accounts via a standard API |
| **OAuth 2.0, RFC 6749** | ✅ retrieved 2026-11-02 | authorization for APIs and integrations; updates RFC 8252/8996/9700 |
| **WebAuthn Level 2 (W3C, Rec. 08.04.2021)** | ✅ retrieved 2026-11-02 | passwordless public-key sign-in; docking point for `identity/` keys |
| **WebFinger, RFC 7033** | ✅ | discover actors via `acct:`/email |
| **kanidm SPN `name@domain`** | ✅ (glossary verified) | login code unique across instances; pattern like Matrix `@user:domain` |

## Basic rule (from decision 3)

The login layer only knows **account identities** (`sub`, SPN). Person **data** stays in [contacts/](../contacts/) (JSContact), social identity in [identity/](../identity/) and [profile/](../profile/). A login is not a data model but the access to one.

## Open points

- SCIM schema ↔ JSContact: SCIM has its own `User`/`EnterpriseUser` schema — mapping needed before we offer SCIM endpoints
- "login history" (when signed in where) would be a model of its own (`LoginEvent`) — not yet decided

## See also

- [standards.md → activities/API cross-section](../standards.md)
- [standards.md → follow-up research 2026-11-02](../standards.md) (OIDC/OAuth/WebAuthn evidenced)
- [identity/](../identity/index.md)
