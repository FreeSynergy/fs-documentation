# Crm — Requirements

What `FreeSynergy.Crm` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Own object types with their own fields, same permissions as built-in ones (`object.define`) | Twenty; EspoCRM (entity manager) | typed schema; gap → own spec | proposed |
| Table, kanban and calendar views with filters, sort, grouping saved per view (`view.save`) | Twenty | view = stored query | proposed |
| Records filled in automatically from outside data (`record.enrich`) | Attio | source and time per field ⚠️; consent needed (people first) | proposed |

## Not planned (deliberately)
