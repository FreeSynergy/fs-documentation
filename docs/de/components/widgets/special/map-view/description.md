# Map View (Kartenansicht)

| Feld | Wert |
|------|------|
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `standort`, `sammlung`, `route` |
| **Zustände** | `wartend`, `ortung` |
| **Gesten** | `tap`, `drag`, `pinch`, `double-tap`, `long-press` |
| **Animationen** | `fade-in`, `zoom-in` |
| **Verwandt** | `embed`, `list-view`, `icon`, `hover-card` |
| **Status** | dokumentiert |

## Beschreibung
Ein Map View zeigt interaktive Karten an (Google Maps, Leaflet, OpenStreetMap).

## Verwendungszweck

- Standort-Anzeige
- Kartenansicht
- Geo-Daten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standort** | ein Ort mit Adresse, gewöhnlich in einem Formular |
| **sammlung** | viele Marker mit Auswahl, oft zusätzlich als Liste |
| **route** | Linien und Flächen (Wege, Gebiete) statt Einzelpunkten |

## Features

- Marker
- Polyline
- Polygon
- Zoom & Pan
- Search
- Geolocation

## Abgrenzung

- **Nicht verwechseln mit** [embed](../embed/): eine fremde Kartenanwendung wird eingebettet,
  diese Komponente zeichnet selbst (OpenStreetMap, Leaflet).
- Die zugehörige Ortsliste ist eine [list-view](../../data/list-view/), der Marker ein
  [icon](../../media/icon/) — beides eigene Komponenten.
- Eine Karte ohne Geo-Bezug (Grundriss, Lageplan) ist ein [image](../../media/image/).

## Best Practices

- Kartendienst konfigurierbar halten, nicht hart verdrahten (Datenschutz, Kosten).
- Immer eine nicht-kartografische Alternative anbieten: Adresse als Text, Ort als Liste.
- Marker beschriften; Farbe allein trägt keine Information.
- Anfangsausschnitt und Zoomstufe setzen, niemand will die ganze Welt sehen.
- Ortung nur nach Einwilligung, ohne Ortung manuelle Eingabe ermöglichen.

## Siehe auch

- [special – Übersicht](../index.md)
- [Embed](../embed/) — fremde Kartendienste
- [List View](../../data/list-view/) — Ortsliste
- [Basiskomponente](../../basics/base/)
