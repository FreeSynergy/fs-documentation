# LiquidFeedback - Features

## Main features

### Delegation engine
- A vote can be delegated to a trusted person (chaining, revocable at any time)
- **Liquid voting**: delegation follows topic preference (issue-based)
- Counter-initiatives: rival motions compete (the one with a majority wins)

### Deliberative structures
- Argument trees for and against, with traffic-light rating
- Phases: support, discussion, vote with quorum (rejection quorum as a brake)

### Organisation
- Rooms per body or topic, membership and verification models, internal candidacies
- Export tables (PDF/HTML protocols) for organisations that must keep minutes

## What LiquidFeedback does NOT do

- **no public API** (integration only through database and export routes)
- **no open moderation suite** like Decidim (reporting is lean)
- legacy PHP codebase: modernisation has stalled (watch community forks)
- no anonymous voting (accounts plus verification)
- UI not modern (function over looks)

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| DB export (MySQL) + protocol exports | practical route for statistics |
| Forks (Liquid Democracy e.V.) | further development attempts |
