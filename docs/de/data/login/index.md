# Login / Konten

**Zwei Fragen, getrennt behandelt:** (a) *Wie meldet man sich an?* → Authentifizierung; (b) *Wie entsteht ein Konto?* → Provisioning. Referenz-Implementierung im Projekt: **kanidm** (OAuth/OIDC + SCIM).

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **OIDC Core 1.0 (errata set 2)** | ✅ abgerufen 2026-11-02 | Anmeldung: `sub`-Claim ↔ unsere User-ID; Zitat/Details in [standards.md → Nachrecherche](../standards.md) |
| **SCIM, RFC 7643/7644** | ⚠️ ungeprüft (Abruf 2026-11-02 abgebrochen) | Provisioning: Konto anlegen/patchen/deaktivieren über Standard-API |
| **OAuth 2.0, RFC 6749** | ✅ abgerufen 2026-11-02 | Authorisierung für APIs und Integrationen; Aktualisierungen RFC 8252/8996/9700 |
| **WebAuthn Level 2 (W3C, Rec. 08.04.2021)** | ✅ abgerufen 2026-11-02 | Passwortlose Public-Key-Anmeldung; Andockstelle für `identity/`-Schlüssel |
| **WebFinger, RFC 7033** | ✅ | Akteure über `acct:`/E-Mail auffinden |
| **kanidm SPN `name@domain`** | ✅ (Glossar geprüft) | Instanz-übergreifend eindeutiger Anmeldecode; Muster wie Matrix `@user:domain` |

## Grundregel (aus Beschluss 3)

Die Login-Ebene kennt nur **Konto-Identitäten** (`sub`, SPN). Personen**daten** bleiben in [contacts/](../contacts/) (JSContact), soziale Identität in [identity/](../identity/) und [profile/](../profile/). Ein Login ist kein Datenmodell, sondern der Zugang zu einem.

## Offene Punkte

- SCIM-Schema ↔ JSContact: SCIM hat ein eigenes `User`/`EnterpriseUser`-Schema — Mapping nötig, bevor wir SCIM-Endpunkte anbieten
- „Login-Historie“ (wann wo angemeldet) wäre ein eigenes Modell (`LoginEvent`) — noch nicht beschlossen

## Siehe auch

- [standards.md → Aktivitäten/API-Querschnitt](../standards.md)
- [standards.md → Nachrecherche 2026-11-02](../standards.md) (OIDC/OAuth/WebAuthn belegt)
- [identity/](../identity/index.md)
