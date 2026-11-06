# Login / Konten – Technische Erklärung

## Speicherperspektive

- **Tabelle `account`** (das Konto, nicht die Person): Spalten `id` (ULID), `spn` (`name@domain`, eindeutig), `sub` (OIDC-Subjekt der externen Autorität, falls delegiert), `status` (`active`/`deactivated`), `self_card_id` (→ [people/](../people/index.md); Beschluss-Kandidat 6), `created_at`, `updated_at`, `deactivated_at`.
- **Credential-Tabelle `credential`**: `account_id`, `type` (`webauthn`/`oidc-link`/…), public Key, `sign_count`/Attestation-Referenzen (WebAuthn-Ebene). Passwörter: wenn überhaupt, nur Hash — Detail ist Betriebs-, nicht Datenmodell-Thema.
- **Login-Historie** (`login_event`): noch nicht beschlossen (offener Punkt in [index.md](index.md)).

## Fluss Authentifizierung (OIDC, ✅ belegt 2026-11-02)

1. Client leitet Authorization Code Flow ein (OIDC Core §3.1).
2. Autorität (bei uns kanidm) authentifiziert den End-User (Passwort, WebAuthn …).
3. Client erhält **ID Token** (Claims u. a. `sub`, `iss`, `aud`, `exp`, `iat`) und prüft es nach OIDC-Core-Validierung.
4. `sub` wird auf unser `account.sub` gemappt (first-login-Anlage via SCIM ⚠️ oder JIT — Entscheidung offen).
5. Access Tokens (OAuth 2.0, RFC 6749, ✅) authorisieren API-Zugriffe; Security-Vorgaben RFC 9700 (✅ Existenz per RFC-Editor-Vermerk) beachten.

## Fluss Provisioning (SCIM, ⚠️ Schema noch zu belegen)

- Externe Tools legen/patchen/deaktivieren Konten über SCIM-Endpunkte.
- **Mapping nötig:** SCIM `User`/`EnterpriseUser` ↔ unser `account` + JSContact-Card, bevor Endpunkte angeboten werden ([index.md](index.md), offener Punkt).

## WebAuthn (✅ belegt 2026-11-02)

Public-Key-Credentials sind **pro Relying Party gescoped** (W3C-Abstract). Die Credentials sind die physische Ebene; die **soziale** Beglaubigung von Schlüsseln läuft separat über [identity/](../identity/index.md) — beides nicht verwechseln.

## Projektionen

| Ziel | Projektion |
|------|------------|
| [profile/](../profile/index.md) | `sub` → Actor-IRI (Beschluss 3) |
| [people/](../people/index.md) | `self_card_id` → JSContact-Card des Menschen |
| API-Gateway | OAuth-Scope → Ressourcen-Rechte (Mapping offen) |
