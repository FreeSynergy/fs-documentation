# Workflows — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Workflows` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Apache Airflow](apache-airflow/index.md) | [latest](apache-airflow/latest/description.md) | Apache Airflow (Apache-2.0) orchestriert datenintensive Pipelines als DAGs in Python: Planner (Scheduler) rechnet Zeitpläne, Executors verteilen Tasks an Worker. |
| [Make](make/index.md) | [latest](make/latest/description.md) | Make (früher Integromat) ist die visuelle SaaS-Automatisierungsplattform: Szenarien aus Modulen (Trigger → Router/Iterator/Aggregator → Aktionen), 1.500+ Apps, visuelle Datenpfade mit Bubbles. |
| [n8n](n8n/index.md) | [latest](n8n/latest/description.md) | n8n ist das quelloffene Workflow-Automatisierungswerkzeug (Node.js, „fair-code“): Nodes grafisch zu Workflows verdrahten, Hunderte Integrationen, eigene JS/Python-Code-Nodes, Webhooks als Trigger, … |
| [Node-RED](node-red/index.md) | [latest](node-red/latest/description.md) | Node-RED ist die Flow-basierte Programmier-Umgebung (Node.js, Apache-2.0) aus IBMs IoT-Schmiede: Knoten verdrahtet man per Drähten (Nachrichten fließen darüber), mit Dashboard, MQTT/OPC-UA-Support … |
| [Prefect](prefect/index.md) | [latest](prefect/latest/description.md) | Prefect (Apache-2.0) ist modernes Workflow-Orchestering in Python: `@flow`/`@task`-Dekoratoren, Deployments (Work Pools/Workers), Scheduling, Events/Automations, Observability-UI. |
| [Zapier](zapier/index.md) | [latest](zapier/latest/description.md) | Zapier ist die größte SaaS-Automatisierungsbibliothek (8.000+ Apps): „Zaps“ verknüpfen Trigger→Aktionen, mehrstufige Zaps und Paths für Verzweigungen, Interfaces/Tables/Forms als Mini-Apps. |

## Dateisatz pro Programm (ADR 0012)

```
programs/suites/workflows/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
