# Login / accounts – examples

Only terms evidenced by the OIDC quote in the central register (standards.md → follow-up research 2026-11-02) or as a ✅ entry. No further claims/inventions.

## 1. ID token payload (OIDC, ✅ — claims `sub`, `iss`, `aud`, `exp`, `iat`)

```json
{
  "iss": "https://auth.example.org",
  "sub": "kanidm:01HTZR6D2W9P4S7H5B1K8M3Q0V",
  "aud": "fs-web",
  "exp": 1793642100,
  "iat": 1793638500
}
```

**Our mapping:** `sub` → `account.sub`; only then is a session bound to an account. Person fields then live in [contacts/](../contacts/index.md), not here.

## 2. Account identifiers side by side

```json
{
  "id": "01HTZR8F5T2C7N4X6V9B1D5K8M",
  "spn": "anna@example.org",
  "sub": "kanidm:01HTZR6D2W9P4S7H5B1K8M3Q0V",
  "status": "active",
  "self_card_id": "01HTZK5C8R4M6YQ2N9XGZ7TQ1A"
}
```

## 3. WebAuthn credential (registration, schema sketchy — field names from everyday API usage, ⚠️ not evidenced field by field)

```json
{
  "account_id": "01HTZR8F5T2C7N4X6V9B1D5K8M",
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
