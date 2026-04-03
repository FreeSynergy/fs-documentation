# Stalwart Mail (E-Mail-Service)

[← Zurück zum Index](../INDEX.md)

---

## Was ist das?

Stalwart ist ein moderner, in Rust geschriebener All-in-One-Mail-Server (SMTP + IMAP + JMAP).
FreeSynergy betreibt einen Stalwart-Fork mit vorgebauter Kanidm-OIDC-Integration und
S3-kompatiblem Storage für Mail-Daten.

- **Stalwart** — Mail-Server-Container (Fork von `stalwartlabs/stalwart`)
- **Bulwark Mail** — Webmail-Frontend (JMAP-basiert, OIDC-nativ)
- **fs-mail** — Adapter-Crate (SmtpProvider + ImapProvider + JmapProvider + StalwartBackend)
- **fs-manager-mail** — Setup-Wizard + Domain-Konfiguration

---

## Architektur

```
         Browser / Client
               │
               ▼
          Zentinel (Ingress)
          /mail → Stalwart
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
  SMTP(25)  IMAP(993)  JMAP(8080)
               │
          Bulwark Mail
          (Webmail UI)
               │
          Kanidm OIDC
          (IAM / Login)

  fs-mail (Adapter)
  ├── SmtpProvider   → StalwartBackend
  ├── ImapProvider   → StalwartBackend
  └── JmapProvider   → StalwartBackend

  fs-manager-mail (Setup-Wizard)
  └── StalwartSetupWizard (State Machine)
      Domain → TlsCerts → OidcIntegration → Confirm → Done
```

---

## Design Pattern: Adapter

`fs-mail` definiert drei Protokoll-Traits:

| Trait          | Beschreibung                                          |
|----------------|-------------------------------------------------------|
| `SmtpProvider` | Ausgehende Mail-Zustellung (send, test_connection)    |
| `ImapProvider` | Postfach-Zugriff (list_mailboxes, fetch_summaries)    |
| `JmapProvider` | Moderner Mail-Zugriff via RFC 8620/8621 (ping, URL)   |

`StalwartBackend` implementiert alle drei Traits und ist der einzige
konkrete Adapter. Weitere Backends könnten künftig dieselben Traits implementieren.

---

## `MailBackend`-Trait

```rust
pub trait MailBackend: Send + Sync {
    fn id(&self) -> &'static str;        // "stalwart"
    fn name(&self) -> &'static str;      // "Stalwart Mail"
    fn capabilities(&self) -> MailCapabilities;
}
```

`MailCapabilities` listet unterstützte Protokolle auf und wird beim
Start des Adapters an `fs-registry` gemeldet:

| Capability    | Service Role |
|---------------|--------------|
| `mail.smtp`   | Outbound-Mail |
| `mail.imap`   | Postfach-Zugriff |
| `mail.jmap`   | JMAP-Session |

---

## Setup-Wizard: `StalwartSetupWizard`

Design Pattern: **State Machine**

```
Domain → TlsCerts → OidcIntegration → Confirm → Done
```

| Schritt           | Eingaben                                     |
|-------------------|----------------------------------------------|
| `Domain`          | Mail-Domain + Admin/Postmaster-E-Mail         |
| `TlsCerts`        | ACME (Let's Encrypt) **oder** Cert/Key-Pfade  |
| `OidcIntegration` | Kanidm Issuer-URL, Client-ID, Secret (skip möglich) |
| `Confirm`         | Alle Eingaben zur Prüfung                     |
| `Done`            | `StalwartConfig` wird ausgegeben              |

`skip_oidc()` setzt `StalwartConfig::skip_oidc = true` — Stalwart verwendet
dann nur lokale Konten (kein Kanidm-Login).

---

## DNS-Einträge (nach Setup erforderlich)

| Typ   | Wert                                 |
|-------|--------------------------------------|
| MX    | Hostname dieses Servers              |
| SPF   | `v=spf1 mx ~all`                     |
| DKIM  | Wird von Stalwart beim Start generiert |
| DMARC | `v=DMARC1; p=none; rua=mailto:admin@{domain}` |

DNS-Hinweise werden im Manager-UI unter „DNS Records" angezeigt.

---

## Bus-Events

| Event                         | Topic                          |
|-------------------------------|--------------------------------|
| `MailEvent::Received`         | `mail.received`                |
| `MailEvent::Sent`             | `mail.sent`                    |
| `MailEvent::AdapterRegistered`| `mail.adapter.registered`      |
| `MailEvent::AdapterDeregistered`| `mail.adapter.deregistered`  |

---

## i18n

- Englisch: `fs-i18n/locales/en/mail.ftl`
- Deutsch:  `fs-i18n/locales/de/mail.ftl`

---

## Store-Einträge

- `packages/containers/stalwart/catalog.toml` — Stalwart Mail-Container (Fork)
  - `[adapter] id = "fs-mail"`
- `packages/containers/bulwark/catalog.toml`  — Bulwark Mail Webmail-Frontend

---

## Repos

- Fork: `/home/kal/Server/fs-stalwart/` → `git@github.com:FreeSynergy/stalwart.git`
- Adapter: `/home/kal/Server/fs-mail/` (`fs-mail`) → `git@github.com:FreeSynergy/fs-mail.git`
- Manager: `/home/kal/Server/fs-managers/mail/` (`fs-manager-mail`)

---

Weiter: [← Index](../INDEX.md)
