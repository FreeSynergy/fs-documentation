# Node-RED - Features

## Main features

### Flows and nodes
- Message-based wiring (msg objects), function nodes (JS), switch/trigger/delay rerouting, subflows with inputs/outputs, flow tabs
- HTTP-In/Out (REST server), WebSockets, MQTT, MQTT-SN, CoAP, serial/GPIO (hardware)
- Parsers (JSON/CSV/XML/YAML), time/cron triggers, context storage (flow/global)

### Dashboards and visualization
- node-red-dashboard (pages/groups/widgets: charts, buttons, tables) — de facto standard for self-built UIs
- node-red-contrib-ui (newer UI building blocks)

### Operations
- `flows.json`/`flows_cred.json` versionable, deployment hot reload, unit test framework, `node-red-admin` CLI
- Palette registry: more than 10,000 community nodes

## What Node-RED CANNOT do

- **No SSO/multi-tenancy**: single-instance tool without a user model out of the box
- **No graphical data transformation without JS** (compared to n8n's Edit Fields)
- **No batch scheduling of large data volumes** (Airflow) — real messages, not job suites
- **Dashboard widgets technically outdated** (AngularJS line) — weigh this for new projects
- Web server protection (`adminAuth`) required — open without configuration!

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| npm palettes | Settings → Palette |
| Home Assistant/Ethernet/IP/Modbus | Community nodes |
| REST via HTTP nodes | Own endpoint per flow |
