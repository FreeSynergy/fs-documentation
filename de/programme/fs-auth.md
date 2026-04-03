# fs-auth

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

`fs-auth` ist der Authentifizierungs-Service für FreeSynergy.
Er definiert 4 Protokoll-Traits und implementiert sie via Kanidm (Adapter Pattern).
Consumer-Code arbeitet ausschließlich gegen die Traits — nie gegen Kanidm direkt.

---

## Architektur

```
OAuthProvider-Trait   ← Strategy Pattern
ScimProvider-Trait    ← Strategy Pattern
SsoProvider-Trait     ← Strategy Pattern
PamProvider-Trait     ← Strategy Pattern
       ↑
KanidmBackend         ← Adapter Pattern: implementiert alle 4 Traits
```

---

## Protokoll-Traits

### OAuthProvider

| Methode          | Beschreibung                           |
|------------------|----------------------------------------|
| `authorize`      | Authorization-URL generieren           |
| `exchange_code`  | Authorization Code → Token-Paar        |
| `refresh_token`  | Access Token erneuern                  |
| `revoke_token`   | Token widerrufen                       |

### ScimProvider

| Methode        | Beschreibung                    |
|----------------|---------------------------------|
| `create_user`  | Nutzer anlegen (SCIM 2.0)       |
| `update_user`  | Nutzer aktualisieren            |
| `delete_user`  | Nutzer löschen                  |
| `list_users`   | Alle Nutzer abfragen            |

### SsoProvider

| Methode            | Beschreibung                 |
|--------------------|------------------------------|
| `sso_login`        | SSO-Login-URL generieren     |
| `validate_session` | Session validieren           |
| `logout`           | Session beenden              |

### PamProvider

| Methode           | Beschreibung                    |
|-------------------|---------------------------------|
| `pam_authenticate`| PAM-Authentifizierung           |
| `pam_authorize`   | PAM-Autorisierung               |

---

## PamIdentity — Session-Token

`PamIdentity` (Rückgabe von `authenticate_pam`) enthält seit Phase 5.1 ein `session_token`-Feld:

```rust
pub struct PamIdentity {
    pub user_id: String,
    pub username: String,
    pub groups: Vec<String>,
    pub session_token: String, // Bearer-Token aus Kanidm PAM Step 3
}
```

Der Token ist direkt nach dem Login nutzbar — kein separater `create_session`-Aufruf nötig.

---

## KanidmSetupWizard (Phase 5.1)

`fs-manager-auth` enthält einen **State Machine Wizard** zur Erstkonfiguration von Kanidm nach dem Install.

**Schritte:**
```
Domain → AdminAccount → OidcClients → Confirm → Done
```

| Schritt       | Eingabe                             |
|---------------|-------------------------------------|
| Domain        | Kanidm-Domain, z. B. `idm.example.com` |
| AdminAccount  | Admin-Benutzername + Passwort (≥ 8 Zeichen) |
| OidcClients   | OIDC-Clients (ID, Anzeigename, Redirect-URI) — optional, wiederholbar |
| Confirm       | Prüfen + Anwenden                   |
| Done          | `KanidmConfig` bereit               |

**Besonderheiten:**
- `skip_oidc()` — OidcClients-Schritt überspringen (Clients später im Manager hinzufügen)
- `KanidmConfig` ist das Output-Objekt; serialisierbar via fs-config
- i18n: alle Texte in `fs-i18n/locales/{lang}/auth-setup.ftl`

---

## OidcClientManager (Phase 5.1)

`OidcClientManager` in `fs-manager-auth` ermöglicht **Post-Wizard-Verwaltung** von OIDC-Clients.

**Command Pattern:** jede Mutation ist ein expliziter Befehl; `sync_to_kanidm` wendet ausstehende Änderungen auf die laufende Kanidm-Instanz an.

```rust
manager.add_client("forgejo", "Forgejo", "https://git.example.com/callback")?;
manager.remove_client("outline")?;
let outcome = manager.sync_to_kanidm().await?;
```

| Methode              | Beschreibung                                         |
|----------------------|------------------------------------------------------|
| `add_client`         | Neuen OIDC-Client zur Queue hinzufügen               |
| `remove_client`      | OIDC-Client aus Queue entfernen                      |
| `sync_to_kanidm`     | Ausstehende Änderungen via Kanidm REST API anwenden  |
| `fetch_from_kanidm`  | Aktuelle Client-Liste aus Kanidm lesen               |

**Fehler-Handling:** `sync_to_kanidm` fährt bei Einzel-Fehlern fort; Fehler werden in `SyncOutcome.errors` gesammelt, nicht geworfen.

---

## Desktop-Login (fs-profile)

`fs-profile` integriert Kanidm-Login direkt in den Profile-Editor:

- `FS_AUTH_URL` gesetzt → Login-Screen vor Profil-Editor
- `FS_AUTH_URL` leer → Offline-Modus, Editor direkt zugänglich
- Nach Login: Username + Session-Token in `AuthState::LoggedIn`
- Logout: Session via `invalidate_session` widerrufen → `AuthState::LoggedOut`

---

## Integration-Tests

`fs-auth/tests/kanidm_integration.rs` — Tests gegen eine laufende Kanidm-Instanz.

Alle Tests sind `#[ignore]` und werden nur explizit ausgeführt:

```bash
# Env vars setzen:
export FS_AUTH_URL=https://idm.example.com
export FS_AUTH_ADMIN_TOKEN=...
export FS_AUTH_CLIENT_ID=...
export FS_AUTH_CLIENT_SECRET=...
export FS_AUTH_TEST_USER=alice
export FS_AUTH_TEST_PASSWORD=secret

cargo test --features kanidm --test kanidm_integration -- --ignored
```

Abgedeckte Szenarien: OAuth-URL, PAM-Login (gültig + falsch), SSO-Session-Validierung,  
SSO-Session-Invalidierung, SCIM-Provision/Update/Deprovision.

---

## Repo

- Lokal: `/home/kal/Server/fs-auth/`
- GitHub: `git@github.com:FreeSynergy/fs-auth.git`
- Manager: `/home/kal/Server/fs-managers/auth/` (`fs-manager-auth`)

---

Weiter: [← Index](../INDEX.md)
