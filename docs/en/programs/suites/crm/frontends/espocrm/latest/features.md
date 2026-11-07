# EspoCRM - Features

## Main features

### Sales objects
- Leads (with conversion), accounts, contacts, opportunities with **pipeline/kanban view**
- Activities (calls, meetings, tasks) with calendar day view, email integration (IMAP attached to records)

### Platform capabilities
- **Entity Manager**: own entities/fields/relations without code; layout editor; formulas
- **Workflows**: triggers (create/update/scheduled), conditions, actions (set field, send template, create entity, fire webhook)
- **Portal**: customer login with own records + portal entities
- Stream feed, full-text search (MySQL), reports/portlets (also own SQL portlets in Pro)

### Advanced (Pro/extensions)
-Telephony integration (Twilio/3CX via extension), mass email/campaigns (Pro), call center, telephony
- Extension marketplace (free + Pro add-ons)

## What EspoCRM CANNOT do

- **No marketing automation suite level** (HubSpot dimension; Pro campaigns remain basic)
- **No ERP** (no invoices/warehouse natively — extension "Compliance"/third-party add-ons)
- **No offline client** (web SPA only)
- **Telephony not free of charge**: only as an add-on/Pro extension
- Report building blocks more limited than the SuiteCRM designer

## Extensions and integrations

| Integration | Way |
|-------------|-----|
| REST API + webhooks + HMAC | official |
| Extensions | espocrm.org marketplace (.zip) |
| SSO | LDAP, SAML, OIDC (newer versions) |
| Zapier/Make/m8n | REST/connector |
