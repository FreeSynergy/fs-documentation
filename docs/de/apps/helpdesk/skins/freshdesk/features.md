# Freshdesk - Funktionen

## Hauptfunktionen

### Tickets
- E-Mail-Ingest pro Mailbox, Portal-Formulare, Wandlerskript (Regeln beim Eingang)
- Status Open/Pending/Resolved/Closed, Prioritäten, Produkte, Gruppen, Tags, benutzerdefinierte Felder
- Saved filters + Favoriten; Bulk-Aktionen

### Automatisierung
- **Dispatch'r** (Regeln), **Workflows** (Triggers + If-Then + Scheduling), **Escalation**, **Assignment Rules** (round-robin)
- SLA-Engine mit Business Hours, Due-by-Farben
- Freddy-AI: Self-Service-Bot, Ticket-Summary, Antwortvorschläge, Sentiment (planabhängig)

### Selbstbedienung
- Knowledge Base mit Kategorien, mehrsprachige Portale, Community-Forum
- Umfragen (CSAT) nach Resolution

### Omnichannel
- E-Mail, Telefonie (Freshcaller-Integration), Chat (Freshchat), Social/Messenger (Plangrenzen beachten)

## Was Freshdesk NICHT kann

- **kein Self-Hosting**; Daten in Freshworks-Cloud (Data-Regionen wählbar, eingeschränkt)
- **keine tiefe Prozessmodellierung** (keine ITIL-Changes/CIs — GLPI)
- **API nicht für alles**: manche Automationen/Custom-Actions nur UI-seitig
- **Custom Fields limitiert** in Anzahl/Typen je Plan
- **Abrechnung pro Agent und Feature**: Light-Agents nur Tickets lesen; Chat/Telefon kosten separat

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Marketplace | hunderte Apps, Serverless-Funktionen (Freshworks Developer Platform) |
| Webhooks + API | REST v2, Event-Subscriptions |
| SSO | SAML, OIDC (neuere Pläne) |
