# Maps — Requirements

What `FreeSynergy.Maps` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Several people edit one map live | Felt, uMap | GeoJSON | proposed |
| Maps with a guided tour or story (ordered stops) | Google Earth (Voyager, projects) | GeoJSON plus an ordered list of stops | proposed |
| Elevation profile along a drawn line | Google Earth | place (GeoJSON), elevation data | proposed |
| Layers connected to a data source that stay current | Felt | WFS, WMTS, GeoJSON | proposed |
| Comment on a map without an editing seat | Felt | ActivityStreams note | proposed |
| Map events and webhooks for embedding | Felt | HTTP webhook | proposed |

## Not planned (deliberately)
