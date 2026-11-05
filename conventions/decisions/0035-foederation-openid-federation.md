# 0035 – Föderation zwischen Instanzen: OpenID Federation 1.0

Status: akzeptiert (2026-11-05) · ADR 0024, 0028, 0029

## Kontext
Der Nutzer will Listen, die wie ein Identity-Broker sagen, was Menschen und Gruppen dürfen; je mehr
Vertrauen, desto mehr Freigabe. **OpenID Federation 1.0** (final 2026-02-17,
`temp/research/geodata-projects-profile-login.md`) beschreibt genau das.

## Entscheidung
- Föderation zwischen Instanzen über **OpenID Federation 1.0**:
  - **Trust Anchors** = unsere Vertrauenslisten,
  - **Trust Chains** = Vertrauen über mehrere Instanzen,
  - **Trust Marks** = Gütesiegel, u. a. Web-of-Trust-Stufen (RLTP),
  - Metadata Policy und automatische Registrierung zwischen Instanzen.
- Kanidm bleibt Identitäts-Provider (OAuth2/OIDC, Passkeys, SCIM); OpenID Federation kommt als
  Ergänzung daneben (Kanidm kann es nicht) — im Hub.
- Erfinden nur, was fehlt: ein **Trust-Mark-Profil** für Web-of-Trust-Stufen (eigene Spec).
