# Make - Funktionen

## Hauptfunktionen

### Szenario-Bau
- Module: Trigger (Webhooks, Schedule, Apps), Aktionen, **Router** (verzweigte Pfade), **Iterator/Aggregator**, **Filter**, Error-Handler (Break/Ignore/Resume), „Sleep“
- Mapping-Designer: Datenpfade visuell (Blasen zeigen Datensätze), Funktionen-Formeln (Array-/Text-Funktionen)
- Data stores + „Make Table“ als einfache Datenbank, Variablen

### Apps
- 1.500+ integrierte Apps; **Custom Apps** per OpenAPI/REST-Editor; „Universal“ HTTP-Module

### Betrieb
- Szenario-API (start/pause/scheduling via REST), Webhook-Endpunkte, Execution-History mit Fehlerdiagnose
- Teams/Freigaben, EU-Datenhaltung (Rechenzentrum-Regionen), „Scenario blueprint“ Sharing

## Was Make NICHT kann

- **kein Self-Hosting** (SaaS)
- **keine Code-Nodes im Kern** (Formeln + Custom-App-Request statt JS; Skripting nur App-Editor)
- **keine BPMN-Prozesslogik**, keine Freigabe-Workflows
- Operations-Verbrauch: lange Schedules fressen Budget (Preis-Planung nötig)
- keine Offline-Local-Flows

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| App-Builder (OpenAPI-Import) | eigene Apps veröffentlichen |
| Szenario-REST-API | offiziell (Planabhängigkeit: API pro Plan) |
| Make-Browser-Extension | Formular-Automation (Add-on) |
