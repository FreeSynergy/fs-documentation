# Zendesk - Features

## Main features

### Tickets and workflows
- Ticket types problem/incident/question/task; status new→open→pending→hold→solve
- **Triggers** (event immediately), **automations** (time/status-based, once/day), **macros** (agent macros with actions + comment)
- Views as saved ticket filters; side conversations ("conversations") for vendor chains
- SLA badges with business hours

### Channels
- Email, web forms, chat/messaging (Sunshine threads), voice (cloud telephony), social
- AI: answer bots, intents, summary/image recognition (plan-dependent)

### Help centre and knowledge
- Multilingual help centre with categories/articles, theme design (HBS)
- Community forum (older plans), "Guides" architecture

### Self-service
- Client portal with custom object views (Sunshine/custom objects)
- Proactive notifications, CSAT/touch feedback

## What Zendesk does NOT do

- **no self-hosting** — the data sits in the Zendesk cloud centre (region choice restricted)
- **no free database view**; export only via API/UI
- **Tickets without a real hierarchical tree structure** (related/children are flat)
- **Custom objects without their own user interface outside** (only within Zendesk contexts)
- **Pricing model per agent + channels** — chat/voice cost extra; small teams pay disproportionately

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Apps (marketplace) | JS apps in the agent interface, app framework |
| Webhooks + trigger conditions | official |
| Sunshine platform | Custom objects + actions (external system → Zendesk) |
| OAuth/JWT, SAML, OIDC | official |
