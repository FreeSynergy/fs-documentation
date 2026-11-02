# Login / Konten – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.** Für diese Domäne ist der Abschnitt „Nachrecherche 2026-11-02“ dort maßgeblich; die Zitate sind dort vollständig abgelegt.

## Standards in dieser Domäne

| Standard | Beleg | Kernfakten (Kurzform — ausführlich im zentralen Register) |
|----------|-------|------------------------------------------------------------|
| **OpenID Connect Core 1.0, errata set 2 (2023-12-15)** | ✅ abgerufen 2026-11-02 | Identitätsebene **auf** OAuth 2.0; ID Token; Authorization Code Flow; ID-Token-Validierung; Claims über den End-User. Anmeldung: `sub` ↔ unsere User-ID |
| **OAuth 2.0 Authorization Framework, RFC 6749** | ✅ abgerufen 2026-11-02 | Okt. 2012, obsoletes RFC 5849; Aktualisierungen **RFC 8252** (Native Apps), **RFC 8996** (TLS-deprecated), **RFC 9700** (Security BCP) |
| **Web Authentication (WebAuthn) Level 2, W3C Rec. 08.04.2021** | ✅ abgerufen 2026-11-02 | „strong, attested, scoped, public key-based credentials“ pro Relying Party; starkes Authenteisieren von Nutzern |
| **SCIM, RFC 7643/7644** | ⚠️ **weiterhin ungeprüft** (Abruf 2026-11-02 abgebrochen, auf Anweisung nicht wiederholt) | Provisioning: Konto anlegen/patchen/deaktivieren — vor Verwendung belegen |
| **WebFinger, RFC 7033** | ✅ | Akteure über `acct:`/E-Mail auffinden |
| **kanidm SPN `name@domain`** | ✅ (Glossar geprüft) | instanz-übergreifend eindeutiger Anmeldecode |

## Einordnung der Schichten (Beschlüsse 2+3)

- Login-Ebene = **Konto-Identitäten** (`sub`, SPN). Keine Personenfelder hier.
- Externe Handles: `https://<instanz>/...`-IRIs (Beschluss 3); WebFinger verbindet E-Mail/`acct:` mit diesen Handles.
- **Trennung:** Login ≠ Identität. Beglaubigung von Schlüsseln und Personen-Vertrauen ist [identity/](../identity/index.md).

## Offene Standard-Punkte

- SCIM-Feldlisten (RFC 7643) und Endpunkt-Details (RFC 7644) belegen ⚠️
- OAuth 2.1 (Draft) beobachten; noch nicht zitierfähig
- Signatur/Token-Bindung nach innen (gRPC-Metadaten) ist Implementierung, kein Standardbedarf
