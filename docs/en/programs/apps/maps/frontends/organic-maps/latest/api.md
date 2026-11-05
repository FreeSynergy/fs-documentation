# Organic Maps - API documentation

## Overview

As with OsmAnd: **no server API**. The docking points are geo links/intents and file import/export (KML/BM2/GPX).

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| `geo:` links / app deep links | Open a destination in the app | official (standard geo) |
| KML/KMZ/BM2/GPX files | Bookmarks/exchange | official (app dialogs) |
| REST/webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Core patterns

```html
<a href="geo:48.530,9.058?q=48.530,9.058">Open in Organic Maps</a>
```

KML for group distribution:

```xml
<kml><Document><Placemark>
  <name>Meeting point Nordring</name>
  <Point><coordinates>9.058,48.530,0</coordinates></Point>
  <description>By the fountain, Saturdays 10 a.m.</description>
</Placemark></Document></kml>
```

Import: app → saved → "import KML"; export the same way (`.kml`).

## Rate limits

Not applicable (offline).

## Frontend note

The FreeSynergy group exports location points as **KML for Organic Maps** and GPX/OVF for OsmAnd — one dataset, two formats ([standpunkte.md](../../../standpunkte.md)).
