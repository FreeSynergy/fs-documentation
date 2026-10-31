# EspoCRM - Beschreibung

## Was das Programm macht

EspoCRM ist ein schlankes CRM für kleine/mittlere Vertriebsteams: Leads bis Deals, Kontakte und Aktivitäten, dazu die Möglichkeit, per Entity-Manager eigene Objekttypen zu bauen. Es ist eine einzige schlanke Anwendung (PHP + SPA) und deshalb schnell gehostet und schnell gelernt.

## Vorteile

- **leichtgewichtig**: läuft auf kleinstem VPS, schnelle Oberfläche
- **modellierbar ohne Code** (Entity-Manager ist das Alleinstellungsmerkmal)
- **faire Lizenz**: GPL-Code, optionale Pro-Erweiterungen

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **SuiteCRM** | SuiteCRM ist mächtiger (Sugar-Erbe) aber schwerfällig; Espo ist moderner/schlanker |
| **CiviCRM** | Non-Profit-Domäne (Spenden/Mitgliedschaften); Espo ist Vertriebs-CRM |
| **HubSpot** | SaaS-Suite inkl. Marketing/Content; Espo ist Daten-CRM mit eigener Infrastruktur |

## Technische Details

- **Backend**: PHP 8, MySQL/MariaDB/PostgreSQL; Single-Page-Frontend (Backbone + Handlebars, neuere Teile React)
- **Authentifizierung**: Session, API-Token, HMAC; LDAP/SAML/OIDC-Optionen
- **Extensions**: `.zip`-Installation ohne Eingriff in Core
- **Lizenz**: GPL (Core), Pro-Version kommerziell

## Für wen geeignet

- Teams, die ein schnelles CRM mit eigenen Objekttypen wollen
- FreeSynergy-Szenarien, die CRM-Felder auf das Standardmodell mappen (Lead/Account/Contact)
