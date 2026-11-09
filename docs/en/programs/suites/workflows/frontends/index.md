# Workflows — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Workflows` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Apache Airflow](apache-airflow/index.md) | [latest](apache-airflow/latest/description.md) | Apache Airflow (Apache-2.0) orchestrates data-intensive pipelines as **DAGs in Python**: the planner (scheduler) calculates schedules, executors distribute tasks to workers. |
| [Apple Shortcuts](apple-shortcuts/index.md) | [latest](apple-shortcuts/latest/description.md) | Apple Shortcuts is the on-device automation app of Apple devices: shortcuts built from actions, started in many ways. A personal tool, not a suite. |
| [Huginn](huginn/index.md) | [latest](huginn/latest/description.md) | Huginn is a self-hosted (MIT) system of agents that watch the web and other sources and pass events to each other. |
| [Make](make/index.md) | [latest](make/latest/description.md) | Make (formerly Integromat) is the visual SaaS automation platform: scenarios built from modules (trigger → router/iterator/aggregator → actions), 1,500+ apps, visual data paths with bubbles. |
| [n8n](n8n/index.md) | [latest](n8n/latest/description.md) | n8n is the open-source workflow automation tool (Node.js, "fair-code"): wire nodes into workflows graphically, hundreds of integrations, custom JS/Python code nodes, webhooks as triggers, self-host… |
| [Node-RED](node-red/index.md) | [latest](node-red/latest/description.md) | Node-RED is the flow-based programming environment (Node.js, Apache-2.0) from IBM's IoT labs: you wire nodes together with wires (messages flow along them), with a dashboard, MQTT/OPC-UA support an… |
| [Power Automate](power-automate/index.md) | [latest](power-automate/latest/description.md) | Power Automate is Microsoft's hosted flow service with connectors, environments and approvals. A product, not a suite. |
| [Prefect](prefect/index.md) | [latest](prefect/latest/description.md) | Prefect (Apache-2.0) is modern workflow orchestration in Python: `@flow`/`@task` decorators, deployments (work pools/workers), scheduling, events/automations, observability UI. |
| [Windmill](windmill/index.md) | [latest](windmill/latest/description.md) | Windmill is an open-source platform where scripts become forms, endpoints and jobs, chained into flows and apps. |
| [Zapier](zapier/index.md) | [latest](zapier/latest/description.md) | Zapier is the largest SaaS automation library (8,000+ apps): "Zaps" link triggers → actions, multi-step zaps and paths for branching, interfaces/tables/forms as mini apps. |

## File set per program (ADR 0012)

```
programs/suites/workflows/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
