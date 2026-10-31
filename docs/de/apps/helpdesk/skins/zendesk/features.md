# Zendesk - Funktionen

## Hauptfunktionen

### Tickets und Workflows
- Tickettypen problem/incident/question/task; Status neu→open→pending→hold→solve
- **Triggers** (Ereignis sofort), **Automations** (zeit-/statusbasiert, einmal/Tag), **Macros** (Agenten-Makros mit Aktionen+Kommentar)
- Views als gespeicherte Ticketfilter; Side-Conversations („Conversations“) für Vendor-Ketten
- SLA-Badges mit Business Hours

### Kanäle
- E-Mail, Web-Formulare, Chat/Messaging (Sunshine-Threads), Voice (Cloud-Telefonie), Social
- AI: Answer-Bots, Intents, Summary/Bild-Erkennung (Plan-abhängig)

### Help Center und Knowledge
- mehrsprachiger Help Center mit Kategorien/Artikeln, Theme-Gestaltung (HBS)
- Community-Forum (ältere Pläne), „Guides“-Architektur

### Self-Service
- Client-Portal mit Custom-Objekt-Ansichten (Sunshine/Custom Objects)
- Proaktive Notifications, CSAT/Touch-Feedback

## Was Zendesk NICHT kann

- **kein Self-Hosting** — Daten liegen im Zendesk-Cloud-Zentrum (Auswahl Region eingeschränkt)
- **keine freie Datenbanksicht**; Export nur API/UI
- **Tickets ohne echte Hierarchie-Baumstruktur** (Related/Children flach)
- **Custom Objects ohne eigene Benutzeroberfläche außerhalb** (nur in Zendesk-Kontexten)
- **Preismodell pro Agent+Kanälen** — Chat/Voice kosten extra; kleine Teams zahlen überproportional

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Apps (Marketplace) | JS-Apps im Agent-Interface, App Framework |
| Webhooks + Trigger-Conditions | offiziell |
| Sunshine Platform | Custom Objects + Actions (externes System → Zendesk) |
| OAuth/JWT, SAML, OIDC | offiziell |
