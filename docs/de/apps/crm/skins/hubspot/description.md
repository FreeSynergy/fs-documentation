# HubSpot - Beschreibung

## Was das Programm macht

HubSpot beginnt mit einem kostenlosen CRM und verdient an den Hubs: Website + Formulare + E-Mails erzeugen Kontakte, die im CRM zu Deals werden. Alles ist auf einer Plattform — Tracking-Code, Consent, Formulare, Posteingang, Berichte.

## Vorteile

- **kostenloser Einstieg** mit echtem CRM (nicht Demoversion)
- **Inbound-Paket komplett**: Content→Lead→Deal aus einer Hand
- **einfache API v3** (JSON, Private-App-Token) für Synchronisation

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Salesforce** | Prozess-/Enterprise-Plattform; HubSpot ist marketing-getrieben und bedienbarer |
| **Mailchimp** | nur Kampagnen/Publikum; HubSpot ergänzt CRM/Website |
| **EspoCRM** | eigene Infrastruktur/GPL; HubSpot SaaS mit Bausatz |

## Technische Details

- **Modell**: SaaS; Portal („Account“) pro Firma, Sitze je Hub
- **Tracking**: JS-Tag auf eigener Website (Cookie/Consent-Verwaltung inklusive)
- **Authentifizierung**: E-Mail/Passwort, SSO; API: Private-App-Token (OAuth2 intern), Webhooks signiert
- **Preise**: frei → Starter → Professional → Enterprise je Hub; Kontaktstufen

## Für wen geeignet

- KMU/B2B-Teams, die Marketing + CRM verzahnen ohne Admin-Heer
- FreeSynergy-Skins für Kontakt-Deal-Pipeline-Modelle und Consent-/Tracking-Felder
