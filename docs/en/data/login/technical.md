# Login / accounts – technical explanation

## Storage perspective

- **Table `account`** (the account, not the person): columns `id` (UUIDv7), `spn` (`name@domain`, unique), `sub` (OIDC subject of the external authority, if delegated), `status` (`active`/`deactivated`), `self_card_id` (→ [people/](../people/index.md); decision candidate 6), `created_at`, `updated_at`, `deactivated_at`.
- **Credential table `credential`**: `account_id`, `type` (`webauthn`/`oidc-link`/…), public key, `sign_count`/attestation references (WebAuthn layer). Passwords: if at all, only hashed — the detail is an operational, not a data-model topic.
- **Login history** (`login_event`): not yet decided (open point in [index.md](index.md)).

## Authentication flow (OIDC, ✅ evidenced 2026-11-02)

1. The client initiates the authorization code flow (OIDC Core §3.1).
2. The authority (kanidm in our case) authenticates the end user (password, WebAuthn …).
3. The client receives the **ID token** (claims including `sub`, `iss`, `aud`, `exp`, `iat`) and validates it per OIDC Core validation.
4. `sub` is mapped onto our `account.sub` (first-login creation via SCIM ⚠️ or JIT — decision open).
5. Access tokens (OAuth 2.0, RFC 6749, ✅) authorise API access; respect the security requirements of RFC 9700 (✅ existence per RFC Editor note).

## Provisioning flow (SCIM, ⚠️ schema still to be evidenced)

- External tools create/patch/deactivate accounts via SCIM endpoints.
- **Mapping needed:** SCIM `User`/`EnterpriseUser` ↔ our `account` + JSContact card, before endpoints are offered ([index.md](index.md), open point).

## WebAuthn (✅ evidenced 2026-11-02)

Public-key credentials are **scoped per relying party** (W3C abstract). The credentials are the physical layer; the **social** attestation of keys runs separately through [identity/](../identity/index.md) — do not confuse the two.

## Projections

| Target | Projection |
|--------|------------|
| [profile/](../profile/index.md) | `sub` → actor IRI (decision 3) |
| [people/](../people/index.md) | `self_card_id` → JSContact card of the person |
| API gateway | OAuth scope → resource permissions (mapping open) |
