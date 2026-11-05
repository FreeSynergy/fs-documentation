# Login / accounts – examples

Only terms evidenced by the OIDC quote in the central register (standards.md → follow-up research 2026-11-02) or as a ✅ entry. No further claims/inventions.

## 1. ID token payload (OIDC, ✅ — claims `sub`, `iss`, `aud`, `exp`, `iat`)

```json
{
  "iss": "https://auth.example.org",
  "sub": "kanidm:018ebf83-345c-7d89-93c4-ab0cd141dc1b",
  "aud": "fs-web",
  "exp": 1793642100,
  "iat": 1793638500
}
```

**Our mapping:** `sub` → `account.sub`; only then is a session bound to an account. Person fields then live in [contacts/](../contacts/index.md), not here.

## 2. Account identifiers side by side

```json
{
  "id": "018ebf84-3cba-730f-9274-db4ac2d2cd14",
  "spn": "anna@example.org",
  "sub": "kanidm:018ebf83-345c-7d89-93c4-ab0cd141dc1b",
  "status": "active",
  "self_card_id": "018ebf32-b118-750d-ab8a-a9ec3e7d5c2a"
}
```

## 3. WebAuthn credential (registration, schema sketchy — field names from everyday API usage, ⚠️ not evidenced field by field)

```json
{
  "account_id": "018ebf84-3cba-730f-9274-db4ac2d2cd14",
  "type": "webauthn",
  "credential_id": "o2n...base64...",
  "public_key_alg": -7,
  "scoped_to": "https://fs.example.org"
}
```

The **principle** is evidenced (W3C: public key-based, attested, scoped per relying party). The concrete storage form is our own decision.

## 4. SCIM provisioning — **sketch only, ⚠️ RFC 7643/7644 unverified**

```json
{
  "userName": "anna@example.org",
  "active": true
}
```

> Deliberately kept minimal: before we offer SCIM endpoints, the `User`/`EnterpriseUser` schema must be evidenced and mapped onto `account` + JSContact ([index.md](index.md)).

## 5. WebFinger query (RFC 7033, ✅) — email → account handle

Request: `GET /.well-known/webfinger?resource=acct:anna@example.org`
Answer (resource form sketched): links to our profile (`profile/` IRI) and the authority handle. The exact response body will be added once the WebFinger JRD structure is evidenced (⚠️ JRD field names not yet quoted field by field).
