# Zapier - Features

## Main features

- **Zaps**: trigger→actions (multi-step, paths as branches), error replay, versioning per zap
- **Apps**: 8,000+ (instant triggers, polling, "integrations" with custom APIs)
- **Zapier Platform**: own apps (UI builder/CLI), prefill webhooks (filling forms), embed (zaps inside your own product)
- **Zapier Interfaces/Tables/Forms/Maps/Drafts**: mini apps and data storage without frontend code
- **Enterprise**: SSO, data retention, zap governance, AI actions

## What Zapier CANNOT do

- **No self-hosting / data stored only at Zapier**
- **No deep data transformations** (simple format steps; code only via "Code by Zapier" in Python/JS, limited)
- **Polling instead of push** for many triggers → latency + task consumption
- **No fine-grained scheduling intervals** (standard polling depends on the plan)
- Pricing by **tasks** — high volumes are expensive

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| Platform API/CLI | Own zap apps |
| Prefill webhooks + REST API (objects/zaps) | official |
| Zapier Agents (AI) | Agent product (new) |
