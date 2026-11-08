# Workflow-Automatisierung

## Überblick

Dieser Bereich enthält Dokumentation zu verschiedenen Plattformen für Workflow-Automatisierung und Integration.

## Verfügbare Systeme

- **n8n** - Werkzeug zur Workflow-Automatisierung
- **make** - früher Integromat
- **zapier** - Automatisierungsplattform
- **automate** - Workflow-Automatisierung
- **node-red** - Flussbasierte Programmierung
- **apache-airflow** - Workflow-Verwaltung
- **apache-airflow-composer** - Verwaltetes Airflow
- **luigi** - Workflow-Verwaltung
- **dagster** - Daten-Orchestrierung
- **prefect** - Workflow-Orchestrierung
- **kestra** - Moderne Workflow-Engine
- **temporal** - Workflow-Orchestrierung
- **caddy** - Webserver mit Automatisierung
- **traefik** - Reverse Proxy
- **nifi** - Datenfluss-Automatisierung

## Was ist Workflow-Automatisierung?

Workflow-Automatisierung bedeutet, wiederkehrende Aufgaben und Prozesse mit Software zu automatisieren. Systeme zur Workflow-Automatisierung umfassen:

- Automatisierung von Aufgaben
- Datenintegration
- Verbindung von Systemen
- Auslöser und Aktionen
- Visueller Workflow-Editor
- Überwachung und Protokollierung

## Anwendungsbereiche

- **DevOps**: CI/CD-Pipelines
- **Marketing**: Marketing-Automatisierung
- **IT**: IT-Betrieb und Automatisierung
- **Vertrieb**: Vertriebsautomatisierung
- **Kundenservice**: Automatisierung im Support
- **Data Engineering**: Datenpipelines

## Vorteile der Workflow-Automatisierung

- **Zeitersparnis**: Wiederkehrende Aufgaben automatisieren
- **Fehlervermeidung**: Menschliche Fehler minimieren
- **Skalierbarkeit**: Prozesse automatisieren
- **Transparenz**: Nachvollziehbarkeit von Prozessen
- **Integration**: Verbindung verschiedener Systeme

## Auswahlkriterien

Bei der Wahl eines Systems zur Workflow-Automatisierung solltest du folgende Kriterien berücksichtigen:

- **Funktionen**: Welche Funktionen werden gebraucht?
- **Bedienbarkeit**: Wie benutzerfreundlich ist es?
- **Integration**: Integration in bestehende Systeme
- **Skalierbarkeit**: Wie viele Workflows und Schnittstellen?
- **Open Source**: Ist das System Open Source?
- **Kosten**: Kostenlos oder kostenpflichtig?

## Verwandte Kategorien

- [Projektmanagement](../projectmanagement/) - Projektmanagement
- [Helpdesk](../../apps/helpdesk/) - Support- und Ticketsysteme
- [CRM](../../apps/people/) - Kontaktverwaltung

## Schnellstart

1. **System auswählen**: Wähle ein System anhand der Anforderungen
2. **Installation/Konto**: System installieren oder Konto anlegen
3. **Konfiguration**: System anpassen und einrichten
4. **Workflows festlegen**: Erste Workflows festlegen
5. **Integration**: Anbindung an andere Systeme

## Weitere Informationen

Weitere Informationen findest du in der Dokumentation der einzelnen Systeme zur Workflow-Automatisierung.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysierte Programme (6), nach Funktion, nichts kopiert (ADR 0012/0013):

- [Apache Airflow](frontends/apache-airflow/index.md) — Apache Airflow (Apache-2.0) orchestriert datenintensive Pipelines als **DAGs in Python**: Der Planer (Scheduler) berechnet Zeitpläne, Executoren verteilen Aufgaben an Worker.
- [Make](frontends/make/index.md) — Make (früher Integromat) ist die visuelle SaaS-Automatisierungsplattform: Szenarien aus Modulen (Auslöser → Router/Iterator/Aggregator → Aktionen), über 1.500 Apps, visuelle Datenpfade mit Blasen.
- [n8n](frontends/n8n/index.md) — n8n ist das quelloffene Werkzeug zur Workflow-Automatisierung (Node.js, „fair-code“): Knoten werden grafisch zu Workflows verbunden, Hunderte Integrationen, eigene JS-/Python-Code-Knoten, Webhooks als Auslöser, Selbst-Hosting …
- [Node-RED](frontends/node-red/index.md) — Node-RED ist die flussbasierte Programmierumgebung (Node.js, Apache-2.0) aus den IoT-Labors von IBM: Du verbindest Knoten mit Kabeln, auf denen Nachrichten fließen, mit Dashboard, MQTT- und OPC-UA-Unterstützung und …
- [Prefect](frontends/prefect/index.md) — Prefect (Apache-2.0) ist moderne Workflow-Orchestrierung in Python: `@flow`/`@task`-Dekoratoren, Deployments (Work Pools/Worker), Zeitplanung, Events/Automatisierungen, Oberfläche zur Beobachtung.
- [Zapier](frontends/zapier/index.md) — Zapier ist die größte SaaS-Automatisierungsbibliothek (über 8.000 Apps): „Zaps“ verbinden Auslöser mit Aktionen, mehrstufige Zaps und Pfade für Verzweigungen, Interfaces, Tabellen und Formulare als Mini-Apps.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
