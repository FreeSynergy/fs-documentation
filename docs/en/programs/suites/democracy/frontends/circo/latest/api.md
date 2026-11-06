# Circo - API Documentation

## Overview

Circo does **not publish an open developer API**. Integrations run through result exports and project-specific agreements with the provider. This page deliberately documents only the confirmed exchange paths.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| Exports (CSV/PDF reports) | Securing results | official |
| REST/Webhooks | — | ❌ not publicly documented |
| Project-specific interfaces | SSO/data connection | by agreement |
| GraphQL | — | ❌ |

## Practical exchange path

```
Circo project → export report (CSV/PDF)
             → FreeSynergy import script (data in the wiki/documents area)
             → link to the project page (original reference retained)
```

## Field notes (export practice)

- Contribution ID, author identifier (pseudonymised per project), phase, rating aggregates
- Keep column naming the same across projects ([fields.md](../../../../../../data/fields.md))

## Skin note

The **export reader** (import + linking) serves as the skin pattern, not a live API. When procuring, explicitly negotiate an interface clause.
