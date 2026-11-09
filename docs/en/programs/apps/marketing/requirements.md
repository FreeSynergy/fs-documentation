# Marketing — Requirements

What `FreeSynergy.Marketing` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Cookieless measurement of page views and custom events (`event.record`) | Umami | event stream; no standard found ⚠️ | proposed |
| Funnels, retention and visitor journeys from events (`report.funnel`, `report.retention`, `report.journey`) | Umami | derived from events | proposed |
| Campaign source tracking by UTM parameters (`campaign.track`) | Umami | UTM parameters as event fields | proposed |
| Segment subscribers by a query and send campaigns from templates (`segment.query`, `campaign.send`) | Listmonk | people records, AS2 collections ⚠️ | proposed |
| Process bounces and keep transactional mail on the same API (`bounce.process`) | Listmonk | SMTP/DSN ⚠️ | proposed |

## Not planned (deliberately)
