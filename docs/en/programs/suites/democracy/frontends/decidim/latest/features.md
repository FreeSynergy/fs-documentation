# Decidim - Features

## Main features

### Process framework
- Processes with time-boxed **phases**; components as building blocks: proposals, meetings, budgets, surveys, accountabilities (result reports), pages, blog, sortitions/votes (module)
- Proposals: comments, supports (cross marks), topic assignment, merging of similar proposals, amending

### Participation governance
- Verification systems (login with conditions), debate rules, report moderation, transparency reports
- Meetings with hybrid support (live streaming integration, attendance reports)

### Operations
- Multi-tenancy (organisations), multilingual support, newsletter and e-mail notifications, statistics export

## What Decidim does NOT do

- **no Liquid Feedback** (delegative votes: ❌ — use Liquid for that)
- **no anonymous voting** (verification takes precedence over anonymity; election systems are separate tools)
- no e-voting certification (official elections need other procedures)
- admin setup is demanding (Rails plus modules; maintenance is not trivial)

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| GraphQL API (full) | official — strong for dashboards |
| Decidim module ecosystem | Community modules (e.g. consultations, volunteers) |
| Census and geo APIs | Meeting maps with geodata |
