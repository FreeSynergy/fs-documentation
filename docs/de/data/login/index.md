# Login / Konten

**Zwei Fragen, getrennt behandelt:** (a) *Wie meldet man sich an?* → Authentifizierung; (b) *Wie entsteht ein Konto?* → Provisioning. Referenz-Implementierung im Projekt: **kanidm** (OAuth/OIDC + SCIM).

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **OIDC (OpenID Connect)** | ⚠️ ungeprüft | Anmeldung: `sub`-Claim ↔ unsere User-ID |
| **SCIM, RFC 7643/7644** | ⚠️ ungeprüft | Provisioning: Konto anlegen/patchen/deaktivieren über Standard-API |
| **OAuth 2.0, RFC 6749** | ⚠️ ungeprüft | Authorisierung für APIs und Integrationen |
| **WebFinger, RFC 7033** | ✅ | Akteure über `acct:`/E-Mail auffinden |
| **kanidm SPN `name@domain`** | ✅ (Glossar geprüft) | Instanz-übergreifend eindeutiger Anmeldecode; Muster wie Matrix `@user:domain` |

## Grundregel (aus Beschluss 3)

Die Login-Ebene kennt nur **Konto-Identitäten** (`sub`, SPN). Personen**daten** bleiben in [kontakt/](../kontakt/) (JSContact), soziale Identität in [identitaet/](../identitaet/) und [profil/](../profil/). Ein Login ist kein Datenmodell, sondern der Zugang zu einem.

## Offene Punkte

- SCIM-Schema ↔ JSContact: SCIM hat ein eigenes `User`/`EnterpriseUser`-Schema — Mapping nötig, bevor wir SCIM-Endpunkte anbieten
- „Login-Historie“ (wann wo angemeldet) wäre ein eigenes Modell (`LoginEvent`) — noch nicht beschlossen

## Siehe auch

- [standards.md → Aktivitäten/API-Querschnitt](../standards.md)
- [identitaet/](../identitaet/index.md)
