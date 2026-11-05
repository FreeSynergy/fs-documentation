# Login / Konten – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.** Für diese Domäne ist der Abschnitt „Nachrecherche 2026-11-02“ dort maßgeblich; die Zitate sind dort vollständig abgelegt.

## Stand 2026-11-05

Beleg: `temp/research/geodata-projects-profile-login.md` (2026-11-05).

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **WebAuthn Level 3** (W3C Rec 2026-08-25), Passkeys | ✅ | Anmeldung |
| OAuth 2.1 (Entwurf -17, 2026-10-31); RFC 9700 = BCP 240 | ✅ | 2.1 folgen, BCP anwenden |
| **OpenID Federation 1.0** (final 2026-02-17): Trust-Anker, Trust-Ketten, **Trust-Marken**, Metadaten-Policy, automatische Registrierung | ✅ | **Föderation zwischen Instanzen (ADR 0035)** — unsere Vertrauenstabellen als Trust-Anker, Web-of-Trust-Stufen als Trust-Marken |
| FedCM | ✅ nur First Public WD (2024-08) | beobachten |
| WebFinger RFC 7033 JRD: `subject`, `aliases`, `properties`, `links` (`rel`, `type`, `href`, `titles`, `properties`) | ✅ | Auffinden: Verknüpfung zu AS2-Schauspieler, OIDC-Issuer, DID |
| SCIM RFC 7643 `User`/`Group`/Enterprise-Attribute | ✅ im Recherche-File aufgelistet | Mapping auf `account` + JSContact |
| **Kanidm 1.12.0** (2026-11-01, MPL-2.0): Passkeys, OAuth2/OIDC-Provider (Token-Austausch), schreibgeschütztes LDAPS, RADIUS | ✅ | Identity Provider im Server (ADR 0024) |
| Kanidm SCIM: **volles SCIM-API seit 1.7.0** (GET/PUT/POST, Pagination, Sortierung, Batch); seine Doku sagt weiterhin „nur sync“ — kanidm#4638, Maintainer 2026-10-28: API-Form noch in Bewegung, nicht als stabil erklärt | ✅ | hinter unserer Abstraktion nutzen; kein eigener SCIM-Server. Keine OpenID Federation → neben Kanidm ergänzen (ADR 0035) |

## Standards in dieser Domäne

| Standard | Beleg | Kernfakten (Kurzform — ausführlich im zentralen Register) |
|----------|-------|------------------------------------------------------------|
| **OpenID Connect Core 1.0, errata set 2 (2023-12-15)** | ✅ abgerufen 2026-11-02 | Identitätsebene **auf** OAuth 2.0; ID Token; Authorization Code Flow; ID-Token-Validierung; Claims über den End-User. Anmeldung: `sub` ↔ unsere User-ID |
| **OAuth 2.0 Authorization Framework, RFC 6749** | ✅ abgerufen 2026-11-02 | Okt. 2012, obsoletes RFC 5849; Aktualisierungen **RFC 8252** (Native Apps), **RFC 8996** (TLS-deprecated), **RFC 9700** (Security BCP) |
| **Web Authentication (WebAuthn) Level 2, W3C Rec. 08.04.2021** | ✅ abgerufen 2026-11-02 | „strong, attested, scoped, public key-based credentials“ pro Relying Party; starkes Authenteisieren von Nutzern |
| **SCIM, RFC 7643 (Kernschema) / RFC 7644 (Protokoll)** | ✅ Sept 2015, Proposed Standard (geprüft 2026-11-05); neuer: RFC 9865 (Cursor-Pagination), RFC 9944 (Device-Schema), RFC 9967 (SCIM-Ereignisse) | Provisioning: Konten über eine Standard-API anlegen/patchen/deaktivieren; jedes Programm spricht SCIM (ADR 0024) |
| **WebFinger, RFC 7033** | ✅ | Akteure über `acct:`/E-Mail auffinden |
| **kanidm SPN `name@domain`** | ✅ (Glossar geprüft) | instanz-übergreifend eindeutiger Anmeldecode |

## Einordnung der Schichten (Beschlüsse 2+3)

- Login-Ebene = **Konto-Identitäten** (`sub`, SPN). Keine Personenfelder hier.
- Externe Handles: `https://<instanz>/...`-IRIs (Beschluss 3); WebFinger verbindet E-Mail/`acct:` mit diesen Handles.
- **Trennung:** Login ≠ Identität. Beglaubigung von Schlüsseln und Personen-Vertrauen ist [identity/](../identity/index.md).

## Offene Standard-Punkte

- SCIM-Feldlisten (RFC 7643) und Endpunkt-Details (RFC 7644) belegen ⚠️
- OAuth 2.1 (Entwurf) beobachten; noch nicht zitierfähig
- Signatur/Token-Bindung nach innen (Cap'n-Proto-Verbindungsmetadaten) ist Implementierung, kein Standardbedarf
