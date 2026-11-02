# Login / Konten – Beschreibung

**Was diese Domäne ist:** der **Zugang** zu FreeSynergy. Sie beantwortet zwei getrennte Fragen:

1. **Authentifizierung** — wer darf sich einloggen? (OIDC, OAuth 2.0, WebAuthn)
2. **Provisioning** — wie entstehen, ändern sich Konten? (SCIM ⚠️, kanidm als Referenz-Implementierung)

**Was sie abdeckt:**

- Konto-Identitäten: `sub`-Claim (OIDC), SPN `name@domain` (kanidm-Muster, ✅ Glossar geprüft)
- Authorisierung für APIs und Integrationen (OAuth 2.0)
- Passwortlose Anmeldung mit Public-Key-Credentials (WebAuthn)
- Akteur-Auffinden über `acct:`/E-Mail (WebFinger, RFC 7033, ✅)

**Was sie NICHT abdeckt (Grundregel aus Beschluss 3):**

| Thema | Wo es liegt |
|-------|-------------|
| Personen**daten** | [contacts/](../contacts/index.md) (JSContact-Card, verknüpft mit dem Konto) |
| Soziale Identität, Profil | [profile/](../profile/index.md) |
| Glaube/Schlüsselbeglaubigung | [identity/](../identity/index.md) — **ein Login beweist keine Identität** |

**Merksatz:** Ein Login ist kein Datenmodell, sondern der Zugang zu einem. Die Login-Ebene kennt nur Konto-Identifikatoren.
