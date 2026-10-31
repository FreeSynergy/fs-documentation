# OsmAnd - API Dokumentation

## Übersicht

OsmAnd hat **keine Server-API** — die Schnittstellen sind Dateiformate und (Android) **Intents** zum Ansteuern der App aus anderen Apps. Für FreeSynergy-Skins: OsmAnd ist Endpunkt, nicht Backend.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Geo-Intents (`geo:lat,lng`, `http://osm.org/c/…`) | OsmAnd mit Ziel öffnen | Android-Standard |
| OsmAnd-Intents (Planungs-Plugin) | Route/Punkte/KML-Übergabe | dokumentiert (OsmAnd-Wiki/Plugin-API) |
| „My Places“ `.ovf/.gpx` | Ortssammlungen importieren/exportieren | offiziell (Dateiformate) |
| Web-API/Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Kernmuster

### App mit Ziel öffnen (Web/andere Apps)

```html
<a href="geo:48.530,9.058?q=48.530,9.058">In OsmAnd öffnen</a>
```

### Route planen lassen (Intents, Planungs-Plugin aktiv)

```kotlin
val i = Intent(null, Uri.parse("https://osmand.net/go?lat=48.53&lon=9.05&z=15"))
i.setPackage("net.osmand.plus"); startActivity(i)
```

(Detail-Parameter je Plugin-Version — OsmAnd-Wiki „OsmAnd intents“ maßgeblich.)

### Datenaustausch

- GPX: Tracks + Waypoints (`<wpt lat lon name desc>`) — aus uMap-Export direkt importierbar
- `.ovf`: OsmAnd-Ortssammlung (Kategorien, Punkte, Icons) — Gruppenverteiler über eigene Cloud

## Rate Limits

entfällt (offline).

## SDKs und Client-Bibliotheken

- keine offiziellen SDKs; Intents + Dateien sind die Schnittstelle
- OsmAnd-Quellcode (C++/Java/Swift) als Referenz fürs Format-Parsing

## Skin-Hinweis

Standpunkte-Skin liefert **GPX/OVF aus FreeSynergy-Daten** → OsmAnd-Import; Gegenrichtung: aufgezeichnete Tracks per Share-Dialog zurück in die Dokumentenablage ([standpunkte.md](../../standpunkte.md)).
