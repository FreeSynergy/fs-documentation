# Workflow Automation

## Overview

This section contains documentation for various workflow automation and integration platforms.

## Available Systems

- **n8n** - Workflow automation tool
- **make** - formerly Integromat
- **zapier** - Automation platform
- **automate** - Workflow automation
- **node-red** - Flow-based programming
- **apache-airflow** - Workflow management
- **apache-airflow-composer** - Managed Airflow
- **luigi** - Workflow management
- **dagster** - Data orchestrator
- **prefect** - Workflow orchestration
- **kestra** - Modern workflow engine
- **temporal** - Workflow orchestration
- **caddy** - Web server with automation
- **traefik** - Reverse proxy
- **nifi** - Dataflow automation

## What is Workflow Automation?

Workflow automation is the use of software to automate repetitive tasks and processes. Workflow automation systems include:

- Task automation
- Data integration
- System connections
- Triggers and actions
- Visual workflow designer
- Monitoring and logging

## Application Areas

- **DevOps**: CI/CD pipelines
- **Marketing**: Marketing automation
- **IT**: IT operations and automation
- **Sales**: Sales automation
- **Customer Service**: Support automation
- **Data Engineering**: Data pipelines

## Benefits of Workflow Automation

- **Time savings**: Automate repetitive tasks
- **Error prevention**: Minimize human errors
- **Scalability**: Automate processes
- **Transparency**: Traceability of processes
- **Integration**: Connection of different systems

## Selection Criteria

When choosing a workflow automation system, consider the following criteria:

- **Features**: Which features are required?
- **Ease of use**: How user-friendly is it?
- **Integration**: Integration with existing systems
- **Scalability**: How many workflows and integration points?
- **Open Source**: Is the system open source?
- **Costs**: Free or paid?

## Related Categories

- [Project Management](../projectmanagement/) - Project management
- [Helpdesk](../../apps/helpdesk/) - Support and ticket systems
- [CRM](../../apps/people/) - Contact management

## Quick Start

1. **Select system**: Choose a system based on requirements
2. **Installation/Account**: Install system or create account
3. **Configuration**: Customize and configure the system
4. **Define workflows**: Define first workflows
5. **Integration**: Integration with other systems

## More Information

Further information can be found in the documentation of individual workflow automation systems.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (6), by function, nothing copied (ADR 0012/0013):

- [Apache Airflow](frontends/apache-airflow/index.md) — Apache Airflow (Apache-2.0) orchestrates data-intensive pipelines as **DAGs in Python**: the planner (scheduler) calculates schedules, executors distribute tasks to workers.
- [Make](frontends/make/index.md) — Make (formerly Integromat) is the visual SaaS automation platform: scenarios built from modules (trigger → router/iterator/aggregator → actions), 1,500+ apps, visual data paths with bubbles.
- [n8n](frontends/n8n/index.md) — n8n is the open-source workflow automation tool (Node.js, "fair-code"): wire nodes into workflows graphically, hundreds of integrations, custom JS/Python code nodes, webhooks as triggers, self-host…
- [Node-RED](frontends/node-red/index.md) — Node-RED is the flow-based programming environment (Node.js, Apache-2.0) from IBM's IoT labs: you wire nodes together with wires (messages flow along them), with a dashboard, MQTT/OPC-UA support an…
- [Prefect](frontends/prefect/index.md) — Prefect (Apache-2.0) is modern workflow orchestration in Python: `@flow`/`@task` decorators, deployments (work pools/workers), scheduling, events/automations, observability UI.
- [Zapier](frontends/zapier/index.md) — Zapier is the largest SaaS automation library (8,000+ apps): "Zaps" link triggers → actions, multi-step zaps and paths for branching, interfaces/tables/forms as mini apps.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
