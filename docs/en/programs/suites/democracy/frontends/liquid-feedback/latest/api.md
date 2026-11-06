# LiquidFeedback - API Documentation

## Overview

LiquidFeedback provides **no public API**. Automation runs through the MySQL database (read-only), protocol and table exports and, if necessary, source code changes. For FreeSynergy skins, LiQu is the reference for the **delegation model**, not for integration APIs.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| REST/Webhooks | — | ❌ |
| MySQL schema (`issues`, `votes`, `delegations`) | Analysis and evaluation (read-only) | practical route (breaking changes between versions possible) |
| Export functions (initiative protocols) | HTML/PDF | official |
| GraphQL | — | ❌ |

## Pattern: evaluation skin via a DB reader

```sql
-- Example query (check the schema of the LiQu version in use!)
SELECT i.id, i.title, i.current_state,
       SUM(v.rank = 1) AS yes, SUM(v.rank = -1) AS no
FROM issues i LEFT JOIN votes v ON v.issue_id = i.id
GROUP BY i.id, i.title, i.current_state;
```

Recommendation: use a **replica**, never write to it; document column names ([fields.md](../../../../../../data/fields.md)).

## Data flow sketch

```
LiQu DB (read-only) → export job → FreeSynergy statistics pages
Initiative texts manually or protocol-based → wiki mirror (with source reference)
```

## Rate limits

Not applicable (direct database access).

## Skin note

Use the delegation and quorum logic as a model template. For real integrations, consider modern forks or governance tools with an API.
