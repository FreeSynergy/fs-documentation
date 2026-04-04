# Tuwunel (Matrix-Homeserver)

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

Tuwunel ist ein hochperformanter Matrix-Homeserver, geschrieben in Rust.
FreeSynergy betreibt einen Tuwunel-Fork mit vorgebauter Kanidm-OIDC-Integration
und S3-kompatiblem Media-Storage.

- **Tuwunel** — Matrix-Homeserver-Container (Fork von `matrix-construct/tuwunel`)
- **fs-channel-matrix** — Adapter-Crate (Channel-Trait + BotChannel-Impl)
- **fs-manager-matrix** — Setup-Wizard + Kanidm-OIDC-Konfiguration

---

## IAM-Integration (Kanidm)

**Wichtig:** Tuwunel verwendet **keine** lokalen Accounts.
Alle Matrix-Benutzeridentitäten werden durch **Kanidm** abgesichert (OIDC).

```
   Matrix-Client
        │
        ▼
   Tuwunel
        │
   OIDC Login ──→ Kanidm (FreeSynergy IAM)
        │
   Matrix-Account = Kanidm-Identität
```

Der Setup-Wizard erzwingt die OIDC-Konfiguration.
Das Überspringen ist nur für Offline-Tests erlaubt (`skip_oidc = true`).

---

## Architektur

```
         Matrix-Client (Element, etc.)
               │
               ▼
          Zentinel (Ingress)
          /_matrix → Tuwunel :8448
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
  CS-API    S-S-API    TURN/STUN
 (Client)  (Feder.)   (VoIP :6167)
               │
          Kanidm OIDC
          (IAM / Login)
               │
          S3 Media Storage
          (opendal)

  fs-channel-matrix (Adapter)
  ├── Channel-Trait     → matrix-sdk (feature: live, deaktiviert wegen rustc ≥1.94 Bug)
  └── BotChannel-Trait  → MatrixBotAdapter (feature: matrix-bot, CS-API via reqwest)

  fs-manager-matrix (Manager)
  └── TuwunelSetupWizard
      ServerName → TlsCerts → OidcIntegration → Federation → Confirm → Done
```

---

## Adapter: fs-channel-matrix

Implementiert den `Channel`-Trait und `BotChannel`-Trait aus `fs-channel`.

| Feature | Status | Beschreibung |
|---|---|---|
| `matrix` | Deaktiviert | `matrix-sdk` (rustc ≥1.94 Recursion-Overflow, upstream Bug) |
| `matrix-bot` | **Aktiv** | CS-API via `reqwest` — kein matrix-sdk, kein Overflow |

Der `matrix-bot`-Feature wird von `fs-bots` genutzt, solange der upstream-Bug nicht behoben ist.

### Ports

| Dienst | Port | Protokoll |
|---|---|---|
| gRPC | 50071 | TCP |
| REST | 8071 | HTTP |
| Matrix | 8448 | HTTPS |
| TURN/STUN | 6167 | UDP |

---

## Setup-Wizard (TuwunelSetupWizard)

State Machine in `fs-manager-matrix`:

```
ServerName
  ↓ server_name + admin_email
TlsCerts
  ↓ ACME oder manuell (cert/key)
OidcIntegration         ← Kanidm OIDC (Pflicht für Produktion)
  ↓ issuer_url + client_id + client_secret
Federation
  ↓ federation_enabled: true/false
Confirm
  ↓ Konfiguration validieren
Done
  → TuwunelConfig (TOML → /etc/freesynergy/tuwunel/config.toml)
```

---

## Store-Einträge

| Paket | Typ | Pfad |
|---|---|---|
| `tuwunel` | container | `Store/packages/containers/tuwunel/` |
| `fs-channel-matrix` | adapter | `Store/packages/adapters/fs-channel-matrix/` |

---

## Bots-Integration

`fs-bots` verwendet `MatrixBotAdapter` (Feature `matrix-bot`) für:
- Polling via CS-API (`/_matrix/client/v3/sync`)
- Senden via `/_matrix/client/v3/rooms/{id}/send`
- DMs via `/_matrix/client/v3/createRoom` (is_direct)

Konfiguration in `bot.toml`:

```toml
[[messengers]]
kind = "matrix"

[messengers.adapter]
homeserver_url = "https://matrix.example.org"
user_id = "@fs-bot:example.org"
access_token = "..."  # oder password = "..."
rooms = ["!room:example.org"]
```

---

## Federation

Federation (Matrix Server-to-Server) ist optional.
Aktivierung im Setup-Wizard (Schritt `Federation`).
Standard: deaktiviert (privater Homeserver).

---

## Crates

| Crate | Repo |
|---|---|
| `fs-channel-matrix` | `FreeSynergy/fs-channel-matrix` |
| `fs-manager-matrix` | `FreeSynergy/fs-managers` (matrix/) |
| `fs-channel` (matrix-bot feature) | `FreeSynergy/fs-channel` |

---

## i18n

| Datei | Inhalt |
|---|---|
| `fs-i18n/locales/{lang}/matrix.ftl` | Wizard-Texte, Fehler, IAM-Hinweise |
| `fs-i18n/locales/{lang}/channel-matrix.ftl` | Adapter-Fehler, Capability-Name |
