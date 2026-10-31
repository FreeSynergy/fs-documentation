# Mautic - Beschreibung

## Was das Programm macht

Mautic automatisiert Kommunikations-Abläufe mit eigenen Daten: Formulare sammeln Kontakte, Segmente sortieren, Kampagnen versorgen — alles auf dem eigenen Server, API-first für Synchronisation mit CRM/ERP-Skins.

## Vorteile

- **GPL + self-hosted** = DSGVO heimatnah, keine Kontakt-Preiskurve
- **REST-API breit** (contacts/campaigns/reports) — bestes Synchronisations-Substrat
- Kampagnen-Canvas erlernbar

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Mailchimp** | Komfort/Versand inkl.; Mautic Infrastruktur selbst |
| **Brevo** | SaaS-Komfort + EU; Mautic Datenhoheit |
| **Odoo Marketing** | Suite-integriert; Mautic Spezialist |

## Technische Details

- **Stack**: PHP 8/Symfony, MySQL/MariaDB; Kampagnen-/Segment-Batch über Cron (`mautic:campaigns`)
- **Auth**: Login; API: OAuth2 (empfohlen) oder Basic (API-Konten)
- **Deploy**: Docker/Composer; queue-Modi für Skalierung
- **Lizenz**: GPL

## Für wen geeignet

- Organisationen mit eigener IT und Kommunikations-Automatisierungsdrang
- FreeSynergy-Szenarien: Kontakt-Broker zwischen CRM-Skins (Webhook→Event, [modelle.md](../../../../data/modelle.md))
