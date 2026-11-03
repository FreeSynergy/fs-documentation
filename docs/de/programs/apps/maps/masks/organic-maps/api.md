# Organic Maps - API Dokumentation

## Übersicht

Wie OsmAnd: **keine Server-API**. Andockpunkte sind Geo-Links/Intents und Datei-Import/Export (KML/BM2/GPX).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| `geo:`-Links / App-Deeplinks | Ziel in App öffnen | offiziell (Standard-geo) |
| KML/KMZ/BM2/GPX-Dateien | Bookmarks/Tausch | offiziell (App-Dialoge) |
| REST/Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Kernmuster

```html
<a href="geo:48.530,9.058?q=48.530,9.058">In Organic Maps öffnen</a>
```

KML für Gruppenverteiler:

```xml
<kml><Document><Placemark>
  <name>Treffpunkt Nordring</name>
  <Point><coordinates>9.058,48.530,0</coordinates></Point>
  <description>Brunnenseite, samstags 10 Uhr</description>
</Placemark></Document></kml>
```

Import: App → Gespeichert → „KML importieren“; Export gleicher Weg (`.kml`).

## Rate Limits

entfällt (offline).

## Skin-Hinweis

FreeSynergy-Gruppe exportiert Standpunkte als **KML für Organic Maps** und GPX/OVF für OsmAnd — ein Datensatz, zwei Formate ([standpunkte.md](../../standpunkte.md)).
