# Salesforce - Funktionen

## Hauptfunktionen

### Datenmodell und Vertrieb
- Standard-Objects (Account, Contact, Lead, Opportunity, Case, Campaign…) + unbegrenzte Custom Objects
- Lead-Converting, Stage-Pfade, Products/Pricebooks, Quotes, Forecasts
- Duplikat-Regeln, Matching, Rollenhierarchie für Datensicht

### Automatisierung
- **Flow Builder** (bildlich), alte Process Builder/Workflows, Approval Processes
- Apex (Programmiersprache) + Triggers, Formula-Felder, Validation Rules

### Kanäle und Suites
- Service Cloud (Cases, Knowledge, Omnichannel-Router), Marketing Cloud-Journey (separat), Pardot/Account Engagement, Experience Cloud-Portale
- AppExchange-Marktplatz (tausende Integrationen)

### Analyse
- Reports, Dashboards, Einstein (KI-Forecasts/Antworte, planabhängig), CRM Analytics (Tableau-Stack, Extra)

## Was Salesforce NICHT kann

- **kein Self-Hosting** — Mandant in Salesforce-Clouds (Data-Regionen wählbar)
- **kein preiswertes Einsteiger-CRM** (Lizenz-/Add-on-Kosten strukturell hoch)
- **Customizing ohne Lernkurve nicht**: Objekte/Flows brauchen Admin-Know-how
- **API-Quotas fest** (API-Calls je 24 h je Edition) — Integrationen müssen cachen
- **keine echte ERP-Funktionalität** (Rechnungen/Lager nur via Add-ons/Commerce-Cloud)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST/SOAP/Bulk/Metadata/Streaming API | offiziell |
| Webhooks-ish | Platform Events, Change Data Capture, Outbound Messages |
| AppExchange | zertifizierte Apps |
| MuleSoft | Integrationsplattform (teuer, Enterprise) |
