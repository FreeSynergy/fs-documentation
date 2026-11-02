# Login / Konten – Beispiele

Nur Begriffe, die durch das OIDC-Zitat im zentralen Register (standards.md → Nachrecherche 2026-11-02) oder als ✅-Eintrag belegt sind. Keine weiteren Claims/Erfindungen.

## 1. ID-Token-Payload (OIDC, ✅ — Claims `sub`, `iss`, `aud`, `exp`, `iat`)

```json
{
  "iss": "https://auth.example.org",
  "sub": "kanidm:01HTZR6D2W9P4S7H5B1K8M3Q0V",
  "aud": "fs-web",
  "exp": 1793642100,
  "iat": 1793638500
}
```

**Unser Mapping:** `sub` → `account.sub`; erst damit ist eine Sitzung an ein Konto gebunden. Personenfelder stehen danach in [contacts/](../contacts/index.md), nicht hier.

## 2. Konto-Identifikatoren nebeneinander

```json
{
  "id": "01HTZR8F5T2C7N4X6V9B1D5K8M",
  "spn": "anna@example.org",
  "sub": "kanidm:01HTZR6D2W9P4S7H5B1K8M3Q0V",
  "status": "active",
  "self_card_id": "01HTZK5C8R4M6YQ2N9XGZ7TQ1A"
}
```

## 3. WebAuthn-Credential (Registrierung, Schema skizzenhaft — Feldnamen nach API-Alltag, ⚠️ nicht feldgenau belegt)

```json
{
  "account_id": "01HTZR8F5T2C7N4X6V9B1D5K8M",
  "type": "webauthn",
  "credential_id": "o2n...base64...",
  "public_key_alg": -7,
  "scoped_to": "https://fs.example.org"
}
```

Belegt ist das **Prinzip** (W3C: public key-based, attested, pro Relying Party scoped). Die konkrete Speicherform ist eigene Festlegung.

## 4. SCIM-Provisioning — **nur Skizze, ⚠️ RFC 7643/7644 ungeprüft**

```json
{
  "userName": "anna@example.org",
  "active": true
}
```

> Bewusst minimal gehalten: bevor wir SCIM-Endpunkte anbieten, muss das `User`/`EnterpriseUser`-Schema belegt und auf `account` + JSContact gemappt werden ([index.md](index.md)).

## 5. WebFinger-Anfrage (RFC 7033, ✅) — E-Mail → Account-Handle

Anfrage: `GET /.well-known/webfinger?resource=acct:anna@example.org`
Antwort (Ressourcen-Form skizziert): Links auf unser Profil (`profile/`-IRI) und den Autorität-Handle. Der genaue Antwort-Body wird nach Beleglage der WebFinger-JRD-Struktur ergänzt (⚠️ JRD-Feldnamen noch nicht feldgenau zitiert).
