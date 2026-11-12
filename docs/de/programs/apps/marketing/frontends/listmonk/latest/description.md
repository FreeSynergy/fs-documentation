# Listmonk – Beschreibung

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

## Was das Programm macht
Es verwaltet Abonnenten und Listen, erstellt Kampagnen aus Vorlagen, versendet sie und verarbeitet Bounces.

## Vorteile
- Hohe Leistung als eigenständige Binärdatei (Wortlaut der Dokumentation).
- AGPL-3.0, selbst gehostet.
- Rollen, Berechtigungen und OIDC-Anmeldung.

## Abgrenzung
| System | Unterschied |
|--------|-------------|
| Mautic | Vollständige Marketing-Automatisierung mit Kampagnenbäumen; Listmonk umfasst nur Newsletter und Listen. |
| Mailchimp | Gehosteter kommerzieller Dienst mit Zielgruppen und Automatisierungen; Listmonk wird selbst gehostet. |

## Technische Details
Go-Backend, Vue mit Buefy-Frontend, PostgreSQL (Dokumentation ✅). Hardwareanforderungen: offen.
