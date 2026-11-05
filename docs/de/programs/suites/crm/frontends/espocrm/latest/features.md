# EspoCRM - Funktionen

## Hauptfunktionen

### Vertriebsobjekte
- Leads (mit Umwandlung), Accounts, Contacts, Opportunities mit **Pipeline-/Kanban-Ansicht**
- Activities (Calls, Meetings, Tasks) mit Kalendertagesansicht, E-Mail-Integration (IMAP-Klemmung an Records)

### Plattform-Fähigkeiten
- **Entity Manager**: eigene Entities/Felder/Relationen ohne Code; Layout-Editor; Formeln
- **Workflows**: Trigger (Create/Update/Scheduled), Bedingungen, Aktionen (Feld setzen, Template senden, Entity anlegen, Webhook auslösen)
- **Portal**: Kundenlogin mit eigenen Records + Portal-Entities
- Streams-Feed, Volltextsuche (MySQL), Reports/Portlets (auch eigene SQL-Portlets in Pro)

### Erweitert (Pro/Erweiterungen)
-Telefonie-Kopplung (Twilio/3CX über Extension), Mass E-Mail/Kampagnen (Pro), Call-Center, Telephony
- Extensions-Marktplatz (kostenlos + Pro-Addons)

## Was EspoCRM NICHT kann

- **kein Marketing-Automation-Suite-Level** (HubSpot-Dimension; Pro-Kampagnen bleiben Basics)
- **kein ERP** (keine Rechnungen/Lager nativ — Extension „Compliance“/Dritt-Addons)
- **kein Offline-Client** (nur Web-SPA)
- **Telefonie nicht frei**: nur als Zusatz-/Pro-Erweiterung
- Report-Bausteine endlicher als SuiteCRM-Designer

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + Webhooks + HMAC | offiziell |
| Extensions | espocrm.org Marketplace (.zip) |
| SSO | LDAP, SAML, OIDC (neuere Versionen) |
| Zapier/Make/m8n | REST/Connector |
