# n8n - Funktionen

## Hauptfunktionen

### Workflow-Design
- Visueller Canvas: Trigger (Webhook, Schedule, Email, Chat, Queue), logische Nodes (IF/Switch/Merge/Loop), Daten-Transformer (Set/Edit Fields, Code-JS/Python)
- 400+ Integrationen (Offiziell + Community-Nodes), Sub-Workflows, Fehler-Workflows

### Ausführung
- Test-Modus (einzelne Nodes, Pin-Daten), Produktions-Modus (Aktivierung)
- Queue-Modus (Redis + Worker) für Skalierung, Retries, Error-Trigger
- Datenhaltung in Postgres/MySQL; Ausführungs-Logs mit View-Editor

### Plattform
- Credentials-Tresor (OAuth2-Flows), Umgebungsvariablen, Daten-Tabellen (neuere Versionen)
- Instanzverwaltung via REST-API + CLI (`n8n` Befehle)

## Was n8n NICHT kann

- **kein BPMN-/Business-Prozessmodell** (Datenfluss-orientiert, nicht Choreografie)
- **keine GUI-Automation/Browser-Robotik** (out of the box; Community-Nodes begrenzt)
- **Batch-/ETL-Massenlast** (Terabyte) ist Airflow-/dbt-Territorium
- **Community-Edition ohne SSO/MFA-Feinheiten** (Enterprise-Features = Enterprise)
- faire Lizenz ≠ OSI „open source“ (SaaS-Weiterverkauf untersagt)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Community-Nodes (`npm`) | Nodes nachinstallieren |
| REST-Steuerung + Webhooks | offiziell |
| LangChain/KI-Nodes | AI-Workflow-Bausteinen integriert |
