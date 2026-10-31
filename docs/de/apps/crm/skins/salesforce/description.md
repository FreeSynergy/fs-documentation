# Salesforce - Beschreibung

## Was das Programm macht

Salesforce betreibt CRM als mehrschichtige Plattform: ein mandantenfähiger Objektdatenkern, darauf Vertriebs-/Service-Prozesse (Flows), Analysen und Portale, dazu eine API-Landschaft, mit der fast alles externalisierbar ist. Kunden mieten Mandanten (Editionen) und erweitern per Konfiguration oder Apex.

## Vorteile

- **Plattform statt Tool**: eigene Objects/Apps ohne Provider-Wechsel
- **Ökosystem**: AppExchange, Zertifizierungen, Admin-/Dev-Community
- **API-Reife** — Referenzklasse für Integrationen

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **HubSpot** | Marketing-/Content-zentriert, einfacher Einstieg; Salesforce prozess-/enterprise-lastig |
| **EspoCRM/SuiteCRM** | eigene Infrastruktur, GPL; Salesforce SaaS mit Quotas |
| **Odoo CRM** | CRM als Teil eines ERP-Bausatzes; Salesforce ohne eigene Warenwirtschaft |

## Technische Details

- **Modell**: Multi-Tenant-SaaS, Instanzen („Orgs“) nach Regionen; Sandbox-Umgebungen
- **Modellierung**: Object Manager, Page Layouts, Record Types; Metadaten-API für Deployment (SFDX/sf-CLI)
- **Programmierung**: Apex (Java-artig, getrennte Transaktionsgrenzen), Lightning Web Components
- **Authentifizierung**: Benutzer+Passwort/SSO (SAML/OIDC); API: OAuth2 (JWT Bearer, Web-Server-Flows)
- **Preise**: Lizenzmodelle je Cloud/Edition; API- und Storage-Quotas

## Für wen geeignet

- Unternehmen mit Admin-Ressourcen und Integrationsbedarf
- FreeSynergy-Skins: Salesforce-Datenmodell (Account/Contact/Opportunity) ist De-facto-Vokabular fürs [CRM-Mapping](../../../../data/modelle.md)
