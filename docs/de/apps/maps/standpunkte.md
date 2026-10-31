# Standpunkte für Gruppen

Seitenübergreifende Funktion der Kategorie Maps: **Standpunkte** sind von mehreren Menschen gemeinsam verwaltete Orte — Treffpunkte, Lagerplätze, Demorouten-Checkpoints, Angebotsorte (Marktplatz-Bezug) — mit Notizen, Zuständigkeiten und Sichtbarkeitsregeln.

## Anforderungen (kurz)

1. **Erfassen**: jedes Mitglied legt Punkte an/ändert sie (Name, Koordinaten, Notiz, Kategorie)
2. **Sehen**: live map in browser + **offline on mobile**
3. **Teilen**: Links/Einbettung for third parties, exportable data
4. **Navigation**: points reach the mobile navi (GPX/KML/OVF)
5. **Rechte**: wer darf was ändern, Sichtbarkeit pro Gruppe

## Bausteine aus dieser Kategorie

| Baustein | Beitrag |
|----------|---------|
| **uMap** | Kollaborativer Karten-Editor (Gruppen-Ebenen, Popup-Notizen, Edit-Token-Links) — Erfassen+Sehen |
| **OpenStreetMap/Overpass** | öffentliche Standpunkte (POIs) als Ausgangsdaten; Melden eigener Orte |
| **Leaflet/MapLibre** | Skin-View: FreeSynergy-GeoJSON als Live-Ebene (Web) |
| **QGIS** | Analyse: Puffer („wer wohnt <500 m?“), Clustering, Qualitätsprüfung; QGIS Server → WMS/WFS |
| **OsmAnd / Organic Maps** | mobile Navigation zu Standpunkten via GPX/OVF/KML-Import |

## Referenz-Kette (FreeSynergy-Skin)

```
FreeSynergy-DB (Tabelle: standpunkte)
   ├─ GET /geojson  →  uMap „Remote-Data“ + Leaflet/MapLibre-Dashboard
   ├─ Export GPX/KML/OVF  →  OsmAnd/Organic Maps (offline)
   └─ GeoPackage → QGIS (Prüfen/Puffern) → QGIS Server WMS (Orga-Karten)
```

Rechte bleiben in FreeSynergy (DB-Rollen); Karten-Tools sind Ansichten mit Lese-/Schreiblinks.

## Szenarien

- **Verein**: Hütten-/Wanderziele pflegen, Tour per GPX aufs Handy
- **Initiativen**: Kundgebungs-Orte + Routenpunkte (uMap öffentlich, Bearbeitbar nur per Token)
- **Marktplatz**: Anbieter-Standorte auf Karte (Skins: Kleinanzeigen/Umkreis-Suche)
- **Katastrophenschutz**: Meldepunkte via Overpass-Vergleich mit OSM-Infrastruktur

## Offene Punkte

- Kollisions-/Dublettenprüfung bei Punkt-Import (QGIS „near“ oder PostGIS)
- Zeitzonen-/Zeitstempel-Konventionen wie in [data/](../../data/modelle.md)
