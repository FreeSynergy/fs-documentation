# OsmAnd - API documentation

## Overview

OsmAnd has **no server API** — the interfaces are the file formats and (on Android) **intents** for driving the app from other apps. For FreeSynergy skins: OsmAnd is an endpoint, not a backend.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| Geo intents (`geo:lat,lng`, `http://osm.org/c/…`) | Open OsmAnd with a destination | Android standard |
| OsmAnd intents (planning plugin) | Passing route/points/KML | documented (OsmAnd wiki/plugin API) |
| "My Places" `.ovf/.gpx` | Import/export place collections | official (file formats) |
| Web API/webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Core patterns

### Open the app with a destination (web/other apps)

```html
<a href="geo:48.530,9.058?q=48.530,9.058">Open in OsmAnd</a>
```

### Have it plan a route (intents, planning plugin active)

```kotlin
val i = Intent(null, Uri.parse("https://osmand.net/go?lat=48.53&lon=9.05&z=15"))
i.setPackage("net.osmand.plus"); startActivity(i)
```

(Detail parameters per plugin version — the OsmAnd wiki "OsmAnd intents" is authoritative.)

### Data exchange

- GPX: tracks + waypoints (`<wpt lat lon name desc>`) — importable directly from a uMap export
- `.ovf`: an OsmAnd place collection (categories, points, icons) — group distribution via your own cloud

## Rate limits

Not applicable (offline).

## SDKs and client libraries

- No official SDKs; intents + files are the interface
- The OsmAnd source code (C++/Java/Swift) as the reference for parsing the formats

## Skin note

The location point skin provides **GPX/OVF from FreeSynergy data** → OsmAnd import; the other direction: recorded tracks back into the document store via the share dialog ([standpunkte.md](../../standpunkte.md)).
