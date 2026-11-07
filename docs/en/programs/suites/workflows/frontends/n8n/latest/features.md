# n8n - Features

## Main features

### Workflow design
- Visual canvas: triggers (webhook, schedule, email, chat, queue), logic nodes (IF/Switch/Merge/Loop), data transformers (Set/Edit Fields, code JS/Python)
- 400+ integrations (official + community nodes), sub-workflows, error workflows

### Execution
- Test mode (individual nodes, pinned data), production mode (activation)
- Queue mode (Redis + workers) for scaling, retries, error trigger
- Data storage in Postgres/MySQL; execution logs with view editor

### Platform
- Credentials vault (OAuth2 flows), environment variables, data tables (newer versions)
- Instance management via REST API + CLI (`n8n` commands)

## What n8n CANNOT do

- **No BPMN/business process modeling** (data-flow oriented, not choreography)
- **No GUI automation/browser robotics** (out of the box; community nodes are limited)
- **Batch/ETL at massive scale** (terabytes) is Airflow/dbt territory
- **Community edition without SSO/MFA finesse** (enterprise features = Enterprise)
- Fair license ≠ OSI "open source" (resale as SaaS is prohibited)

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| Community nodes (`npm`) | Install additional nodes |
| REST control + webhooks | official |
| LangChain/AI nodes | Integrated AI workflow building blocks |
