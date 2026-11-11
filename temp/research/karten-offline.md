# Recherche: kleine Offline-Karten für FreeSynergy.Maps (2026-11-11)

Anlass: Nutzer – „Lieber viele kleine Karten als eine riesige“ (Vorbild OsmAnd+). Idee: Beim Wechsel in eine
neue Region fragt die Karte, ob diese Region auch heruntergeladen werden soll.

## Was es gibt

| Anbieter | Aufteilung | Format / Lizenz | Befund |
|---|---|---|---|
| OsmAnd | Länder, große Länder in Regionen (Deutschland ~33 Teile, zusammen ~11 GB mit Standardkarten) | eigenes `.obf`; OsmAndMapCreator GPL v3 | zu groß, eigenes Format; Lizenz der Kartendateien nicht gefunden |
| Organic Maps | Länder/Regionen, `.mwm` | eigenes Format | Größe ist bekanntes Problem (Ägypten 215 MiB in einer Datei); fragt laut Drittquelle beim ersten Öffnen einer Gegend nach Download; eigener Download-Server einstellbar |
| Geofabrik | Land, Bundesland, Regierungsbezirk | OSM-Rohdaten `.pbf` | gute Quelle zum Selbstbauen, keine fertigen Karten |
| Protomaps (PMTiles) | ein Planet (~120 GB, Zoom 0–15), täglicher Build; beliebiges Gebiet herausschneidbar (`pmtiles extract --bbox`/`--region`, `--maxzoom`, `--dry-run` zeigt Größe) | Spezifikation CC0, Software BSD-3, Daten ODbL (OSM-Namensnennung) | Beispiel Berlin ~84 MB (bis Zoom 15); jede Zoomstufe weniger halbiert etwa |
| Mapterhorn (Höhen) | Planet Zoom 0–12, hochaufgelöste Regionen ab Zoom 13 | PMTiles, Terrarium/WebP; Copernicus DEM, swissALTI3D; NLnet-gefördert | Höhenrelief für das Vorbild Google Earth Pro; gesamt 2,6 TiB, daher nur ausschneiden |

## Empfehlung
1. Format **PMTiles** (offen, CC0/BSD), Daten aus dem Protomaps-Build bzw. selbst aus Geofabrik gebaut.
2. **Weltübersicht** klein (niedriger Zoom), dazu **Regionspakete** (Bundesland, in großen Ländern kleiner),
   Detail bis Zoom 15; Größe je Region mit `--dry-run` vorab messen.
3. **Ebenen als eigene Pakete:** Grundkarte, Höhen (Mapterhorn), später Orte/POI.
4. Jede Karte ist ein **Store-Paket** (signiert, Update, Spiegel nach ADR 0068).
5. **Nachfragen beim Wechsel:** Verlässt man installierte Regionen, schlägt die Karte das passende Regionspaket
   vor (mit Größe); bis dahin Zwischenspeicher für Angesehenes.
6. Nicht massenhaft von tile.openstreetmap.org laden (Nutzungsregeln).

## Offen
- Echte Größen je Bundesland mit `pmtiles extract --dry-run` messen.
- Lizenz der OsmAnd-Kartendateien (nur falls wir sie je nutzen wollten).
- Zusammenarbeit: Protomaps, Mapterhorn, Geofabrik – Verbesserungen upstream zurückgeben.

## Quellen
- https://docs.protomaps.com/basemaps/downloads
- https://docs.protomaps.com/pmtiles/cli
- https://til.simonwillison.net/gis/pmtiles
- https://protomaps.com/blog/open-core-to-open-source/
- https://wiki.openstreetmap.org/wiki/OsmAndMapCreator
- https://community.openstreetmap.org/t/why-are-the-maps-of-european-countries-in-osmand-becoming-fragmented-more-and-more/145612
- https://osmand.net/blog/merged-maps
- https://www.openstreetmap.org/user/SeverinGeo/diary/408692
- https://git.omaps.dev/organicmaps/organicmaps-tmp/issues/3977
- https://organicmaps.app/news/
- https://protomaps.com/blog/mapterhorn-terrain/
- https://nlnet.nl/project/Mapterhorn/
