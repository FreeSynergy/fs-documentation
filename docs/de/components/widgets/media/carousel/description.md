# Carousel (Karussell)

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base`, `gallery` |
| **Varianten** | `Auto-play`, `Manual`, `Thumbnails`, `Fade Effect` |
| **Zustände** | `spielend`, `pausiert` |
| **Gesten** | `swipe`, `tap`, `drag` |
| **Animationen** | `cross-fade`, `cross-slide`, `slide-in` |
| **Verwandt** | `gallery`, `grid-view`, `image`, `tabs` |
| **Status** | dokumentiert |

## Beschreibung
Ein Karussell zeigt Inhalte nacheinander an einer Stelle: eine Folie sichtbar, die anderen
bereit, gewechselt per Knopf, Wisch oder automatisch.

## Verwendungszweck

- Bildergalerien
- Produktpräsentationen
- Werbung
- Karussells

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **automatik** | wechselt von selbst weiter |
| **manuell** | nur Knöpfe und Wischen |
| **miniaturen** | Vorschaubildstreifen unter der Folie |
| **überblenden** | Übergang als Überblendung statt Schieben |

## Features

- Navigation (Vor/Zurück)
- Autoplay
- Thumbs (Vorschaubilder)
- Touch-Swipe (Mobile)

## Abgrenzung

- **Nicht verwechseln mit** [gallery](../gallery/): die Galerie zeigt viele Bilder gleichzeitig und
  vergrößert bei Bedarf, das Karussell zeigt immer nur eines (Plan Abschnitt 4, Zeile 14).
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs setzen eine Auswahl voraus,
  ein Karussell kann sich selbst drehen.
- Der Inhalt einer Folie ist eine eigene Komponente — der Text gehört nicht in das Karussell.

## Best Practices

- Automatik bei Hover, Fokus und für Bewegungsempfindlichkeit pausieren; nicht schneller als
  fünf Sekunden pro Folie.
- Punkt- oder Zahlenanzeige zeigt immer Gesamtzahl und aktuelle Position.
- Höchstens etwa sieben Folien; alles Weitere gehört in eine Liste oder Galerie.
- Auf Mobil Wischaktion anbieten und die Pfeile ausblenden, damit die Fläche frei bleibt.

## Siehe auch

- [media – Übersicht](../index.md)
- [Gallery](../gallery/) — viele Bilder auf einmal
- [Grid View](../../data/grid-view/) — Raster statt Abfolge
- [Basiskomponente](../../basics/base/)
