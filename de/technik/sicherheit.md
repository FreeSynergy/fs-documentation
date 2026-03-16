# Sicherheit

[← Zurück zum Index](../INDEX.md) | [Installation](installation.md) | [Rechte](../konzepte/rechte.md)

---

## Netzwerk

- **Zentinel** (Rust/Pingora) ist der einzige Service mit Zugang zum externen Netzwerk
- Alle anderen Services sind auf internen Podman-Netzwerken isoliert
- SMTP/IMAP: Layer-4 TCP-Forwarding durch Zentinel an Stalwart

## Encryption

- Secrets in SQLite mit **age** verschlüsselt
- SSH nur **ed25519** (kein RSA)
- mTLS zwischen Nodes (über CA-Hash in der Invite-Datei verifiziert)

## Invite-Tokens

- Einmalig verwendbar
- Zeitlich begrenzt (`expires_at`)
- CA-Hash verhindert MITM
- Port wird nur für die Dauer der Einladung geöffnet

## Rechte-Audit

Jede Rechte-Änderung wird protokolliert. Wer hat was wann freigegeben? Siehe [Rechte-System](../konzepte/rechte.md).

## Standard: Alles ist privat

Kein Service, kein Projekt, kein Host ist standardmäßig öffentlich. Jede Freigabe muss explizit erfolgen. Warnung + Bestätigung bei umfangreichen Freigaben.

---

Weiter: [Rechte](../konzepte/rechte.md) | [Föderation](../konzepte/foederation.md)
