# Map View

| Feld | Wert |
|-------|-------|
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `standort`, `sammlung`, `route` |
| **Zustände** | `wartend`, `ortung` |
| **Gesten** | `tap`, `drag`, `pinch`, `double-tap`, `long-press` |
| **Animationen** | `fade-in`, `zoom-in` |
| **Verwandt** | `embed`, `list-view`, `icon`, `hover-card` |
| **Status** | dokumentiert |

## Beschreibung
Eine Kartenansicht zeigt interaktive Karten (Google Maps, Leaflet, OpenStreetMap).

## Zweck

- Anzeige eines Ortes
- Kartenansicht
- Geodaten

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **standort** | ein Ort mit Adresse, meist innerhalb eines Formulars |
| **sammlung** | viele Marker mit Auswahl, oft zusätzlich als Liste |
| **route** | Linien und Flächen (Wege, Regionen) statt einzelner Punkte |

## Funktionen

- Marker
- Polylinie
- Polygon
- Zoomen und Verschieben
- Suche
- Standortermittlung

## Abgrenzung

- **Nicht verwechseln mit** [embed](../../../workbenches/special/embed/): Hier wird eine fremde
  Kartenanwendung eingebettet, diese Komponente zeichnet die Karte selbst (OpenStreetMap, Leaflet).
- Die passende Ortsliste ist eine [list-view](../../data/list-view/), der Marker ein
  [icon](../../../primitives/media/icon/). Beides sind eigene Komponenten.
- Eine Karte ohne Ortsbezug (Grundriss, Lageplan) ist ein [image](../../../primitives/media/image/).

## Best Practices

- Den Kartendienst konfigurierbar halten statt fest verdrahtet (Datenschutz, Kosten).
- Immer eine nicht kartografische Alternative anbieten: die Adresse als Text, den Ort als Liste.
- Marker beschriften; Farbe allein trägt keine Information.
- Start-Ansicht und Zoomstufe festlegen, niemand will die ganze Welt sehen.
- Standort nur nach Zustimmung ermitteln; ohne Ermittlung manuelle Eingabe ermöglichen.

## Siehe auch

- [special – Übersicht](../index.md)
- [Embed](../../../workbenches/special/embed/) — fremde Kartendienste
- [List View](../../data/list-view/) — Ortsliste
- [Base-Komponente](../../../primitives/basics/base.md)
