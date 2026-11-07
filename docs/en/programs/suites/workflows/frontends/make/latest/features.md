# Make - Features

## Main features

### Scenario building
- Modules: triggers (webhooks, schedule, apps), actions, **routers** (branched paths), **iterator/aggregator**, **filters**, error handlers (break/ignore/resume), "sleep"
- Mapping designer: data paths visually (bubbles show records), function formulas (array/text functions)
- Data stores + "Make Table" as a simple database, variables

### Apps
- 1,500+ built-in apps; **custom apps** via OpenAPI/REST editor; "Universal" HTTP module

### Operations
- Scenario API (start/pause/scheduling via REST), webhook endpoints, execution history with error diagnostics
- Teams/approvals, EU data residency (data center regions), "scenario blueprint" sharing

## What Make CANNOT do

- **No self-hosting** (SaaS)
- **No code nodes in the core** (formulas + custom app requests instead of JS; scripting only in the app editor)
- **No BPMN process logic**, no approval workflows
- Operations consumption: long schedules eat the budget (pricing planning needed)
- No offline local flows

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| App builder (OpenAPI import) | Publish your own apps |
| Scenario REST API | official (plan-dependent: API per plan) |
| Make browser extension | Form automation (add-on) |
