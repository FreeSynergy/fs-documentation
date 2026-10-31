# Zammad - Funktionen

## Hauptfunktionen

### Kanäle und Ticketentstehung
- E-Mail (IMAP/POP/JMAP, ausgehend SMTP), Web-Formular, Telegram, WhatsApp (Cloud), Telefon/CTI, Online-Chat
- aus Artikel-Antworten entstehende Tickets/Follow-ups, Ticket-Splitting und -Merge
- import aus Zendesk, Freshdesk, OTRS, RT (Assistenten)

### Agentenarbeit
- Drei-Spalten-Maske: Kundencontext, Artikelstrom, Attribute
- Textbausteine mit Variablen, Massenaktionen (State, Owner, Tags, Priority)
- Volltextsuche (Elasticsearch/OpenSearch), gespeicherte Filter, „Overdue“-Ansichten
- Tasks (Aufgaben) mit Wiedervorlage, Kalender/Servicezeiten für SLA

### Automatisierung
- Trigger (ereignisgesteuerte Aktionen), Scheduler (zeitgesteuert), Escalations
- Webhooks (outbound, signed), inbound via API
- Barometer/Sentiment optional, Knowledge-Base mit Workflow-Freigaben

### Portal und Self-Service
- Kundenportal mit eigenen Tickets, Knowledge-Base-Artikeln, Formularen
- Single Sign-On: LDAP, OAuth2/OIDC, SAML, CAS, Microsoft

## Was Zammad NICHT kann

- **Kein ITIL-Modul** wie GLPI: keine CIs/Assets, Änderungen, Verträge (❌)
- **Kein echtes Projektmanagement** (Tickets ≠ Aufgabenverwaltung à la OpenProject)
- **Kein Telefonieserver** — CTI bindet nur an (3CX, Asterisk, Jitsi …)
- **Kein Mehrmandanten-SaaS ohne Workarounds** (Instanztrennung nötig)
- **Chat ohne eigene SIP-/Voice-Komponente**, Knowledge Base ohne Confluence-Komfort

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API /api/v1 + Webhooks | offiziell |
| Store-Apps | Jira-Sync, Microsoft 365, Slack … (admininstallierbar) |
| ES/OpenSearch | Suchindex, Voraussetzung |
| SSO | LDAP, OIDC, SAML |
| Backups | `zammad backup` (tar: DB + Storage + Config) |
