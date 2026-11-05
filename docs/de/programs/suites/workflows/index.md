# Workflow-Automatisierung

## Übersicht

Dieser Bereich enthält Dokumentation für verschiedene Workflow-Automatisierungs- und Integrations-Plattformen.

## Verfügbare Systeme

- **n8n** - Workflow Automatisierungstool
- **make** - ehemals Integromat
- **zapier** - Automatisierungsplattform
- **automate** - Workflow Automatisierung
- **node-red** - Flow-basierte Programmierung
- **apache-airflow** - Workflow Management
- **apache-airflow-composer** - Managed Airflow
- **luigi** - Workflow Management
- **dagster** - Data Orchestrator
- **prefect** - Workflow Orchestrierung
- **kestra** - Moderner Workflow Engine
- **temporal** - Workflow Orchestrierung
- **caddy** - Web Server mit Automation
- **traefik** - Reverse Proxy
- **nifi** - Dataflow Automation

## Was ist Workflow-Automatisierung?

Workflow-Automatisierung ist der Einsatz von Software zur Automatisierung von wiederkehrenden Aufgaben und Prozessen. Workflow-Automatisierungssysteme umfassen:

- Task-Automatisierung
- Datenintegration
- System-Verbindungen
- Trigger und Aktionen
- Visual Workflow-Designer
- Monitoring und Logging

## Anwendungsbereiche

- **DevOps**: CI/CD Pipelines
- **Marketing**: Marketing-Automatisierung
- **IT**: IT-Operationen und -Automatisierung
- **Sales**: Sales-Automatisierung
- **Customer Service**: Support-Automatisierung
- **Data Engineering**: Data Pipelines

## Vorteile von Workflow-Automatisierung

- **Zeitersparnis**: Automatisierung von wiederkehrenden Aufgaben
- **Fehlervermeidung**: Minimierung von menschlichen Fehlern
- **Skalierbarkeit**: Automatisierung von Prozessen
- **Transparenz**: Nachvollziehbarkeit von Prozessen
- **Integration**: Verbindung von verschiedenen Systemen

## Auswahlkriterien

Bei der Wahl eines Workflow-Automatisierungssystems sollten folgende Kriterien berücksichtigt werden:

- **Funktionen**: Welche Features sind erforderlich?
- **Benutzerfreundlichkeit**: Wie einfach ist die Bedienung?
- **Integration**: Integration mit bestehenden Systemen
- **Skalierbarkeit**: Wie viele Workflows und Integrationspunkte?
- **Open Source**: Ist das System Open Source?
- **Kosten**: Kostenlos oder kostenpflichtig?

## Verwandte Kategorien

- [Projektmanagement](../../apps/projectmanagement/) - Project Management
- [Helpdesk](../../apps/helpdesk/) - Support und Ticketsysteme
- [CRM](../../apps/contact/) - Contact Management

## Schnellstart

1. **System auswählen**: Basierend auf den Anforderungen ein System wählen
2. **Installation/Account**: System installieren oder Account erstellen
3. **Konfiguration**: System anpassen und konfigurieren
4. **Workflows definieren**: Erste Workflows definieren
5. **Integration**: Integration mit anderen Systemen

## Mehr Informationen

Weitere Informationen finden Sie in der Dokumentation der einzelnen Workflow-Automatisierungssysteme.

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (6), nach Funktionen, nichts kopiert (ADR 0012/0013):

- [apache-airflow](frontends/apache-airflow/index.md) — Apache Airflow (Apache-2.0) orchestriert datenintensive Pipelines als DAGs in Python: Planner (Scheduler) rechnet Zeitpläne, Executors verteilen Tasks an Worker.
- [make](frontends/make/index.md) — Make (früher Integromat) ist die visuelle SaaS-Automatisierungsplattform: Szenarien aus Modulen (Trigger → Router/Iterator/Aggregator → Aktionen), 1.500+ Apps, visuelle Datenpfade mit Bubbles.
- [n8n](frontends/n8n/index.md) — n8n ist das quelloffene Workflow-Automatisierungswerkzeug (Node.js, „fair-code“): Nodes grafisch zu Workflows verdrahten, Hunderte Integrationen, eigene JS/Python-Code-Nodes, Webhooks als Trigger, …
- [node-red](frontends/node-red/index.md) — Node-RED ist die Flow-basierte Programmier-Umgebung (Node.js, Apache-2.0) aus IBMs IoT-Schmiede: Knoten verdrahtet man per Drähten (Nachrichten fließen darüber), mit Dashboard, MQTT/OPC-UA-Support …
- [prefect](frontends/prefect/index.md) — Prefect (Apache-2.0) ist modernes Workflow-Orchestering in Python: `@flow`/`@task`-Dekoratoren, Deployments (Work Pools/Workers), Scheduling, Events/Automations, Observability-UI.
- [zapier](frontends/zapier/index.md) — Zapier ist die größte SaaS-Automatisierungsbibliothek (8.000+ Apps): „Zaps“ verknüpfen Trigger→Aktionen, mehrstufige Zaps und Paths für Verzweigungen, Interfaces/Tables/Forms als Mini-Apps.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
