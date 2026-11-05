# OsmAnd - Features

## Main features

### Offline maps
- Download regions (.obb), several map profiles (standard/cycle/hiking…), elevation data + contour lines, offline search + routing entirely without network

### Navigation
- Routing profiles (car/truck/bike/foot), lane/turn instructions, TMC (online), lane assistant, "drive along GPX" (follow a track)
- Public-transit stops/routes partly online (OpenTripPlanner integration)

### Your own places (frontend-relevant!)
- **My Places**: folders as layers, points with notes, GPX import from uMap/Komoot, layer visibility
- Track recording (times, elevation), "share recording"

### Map view
- 3D view, night maps, scale/measuring tool, POI overlay categories

## What OsmAnd does NOT do

- **no server/synchronisation service** — data held locally/in files (sync via your own cloud)
- **no map editor** (OSM changes only via the OSM app/web)
- Live congestion/traffic only with online services; no deep CarPlay/Android Auto integration (partly)
- iOS features lag behind Android (plugins later)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| OsmAnd intents/"API" (Android, planning plugin) | App calls with parameters |
| GPX/KML/KMZ/.ovf | Data exchange |
| Komoot bridge | Track import |
