# Zendesk - Beschreibung

## Was das Programm macht

Zendesk betreibt Support als Service: Kunden schreiben über irgendeinen Kanal, alles wird Ticket; Agenten arbeiten in Views mit Triggers/Automations, Kunden lösen sich über den Help Center selbst. Admins konfigurieren Regeln ohne Code, Entwickler via API.

## Vorteile

- **sofort einsatzbereit** (keine Installation, Channels in Stunden live)
- **API sehr vollständig** — praktisch jede UI-Funktion ist API-abgebildet
- **Ökosystem**: Tausende Marketplace-Apps

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Freshdesk** | ähnlicher SaaS-Funktionsumfang, oft günstiger; API ähnlich, Events-System kleiner |
| **Zammad** | self-hosted-Alternative mit eigener Datenhoheit, weniger AI/Telefonie-Bausatz |
| **Intercom** | Messaging-/Sales-first; Zendesk ticket-first |

## Technische Details

- **Modell**: Multi-Tenant-SaaS; Subdomain pro Konto (`firma.zendesk.com`)
- **Authentifizierung**: E-Mail+Passwort, SSO (SAML/OIDC), API-Token, OAuth, JWT for Apps
- **Datenhaltung**: Zendesk-eigen; Audit-Log-Aufbewahrung planabhängig
- **Verträge**: Agenten-/Resolution-basiert (planabhängig); Support-Tiers

## Für wen geeignet

- Firmen, die Support ohne Betrieb auslagern wollen und US/EU-Cloud-Zentren akzeptieren
- FreeSynergy-Skins für ticket-first Workflows mit sauberem REST-Vorbild
- als Referenz-API (v2) bei der Modellierung eigener Ticket-Schnittstellen
