# Carousel

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
Ein Carousel zeigt Inhalte nacheinander an einer Stelle: eine Folie ist sichtbar, die anderen
stehen bereit, gewechselt wird per Knopf, Wischen oder automatisch.

## Verwendungszweck

- Bildergalerien
- Produktpräsentationen
- Werbung
- Karussells

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **automatik** | läuft von selbst weiter |
| **manuell** | nur Knöpfe und Wischen |
| **miniaturen** | Streifen mit Vorschaubildern unter der Folie |
| **überblenden** | Übergang als Überblendung statt Schieben |

## Features

- Navigation (vor/zurück)
- Automatisches Abspielen
- Miniaturen (Vorschaubilder)
- Wischgeste (Mobil)

## Abgrenzung

- **Nicht verwechseln mit** [gallery](../gallery/): die Galerie zeigt viele Bilder gleichzeitig und
  vergrößert sie bei Bedarf, der Carousel zeigt immer nur eins (Planabschnitt 4, Zeile 14).
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs setzen eine Auswahl voraus,
  ein Carousel kann selbst weiterlaufen.
- Der Inhalt einer Folie ist eine Komponente für sich – der Text gehört nicht in den Carousel.

## Best Practices

- Den Automatikbetrieb bei Hover, bei Fokus und für Bewegungsempfindliche anhalten; nicht schneller
  als alle fünf Sekunden eine Folie.
- Eine Punkte- oder Zahlanzeige zeigt immer die Gesamtzahl und die aktuelle Position.
- Höchstens etwa sieben Folien; mehr gehört in eine Liste oder Galerie.
- Auf dem Smartphone die Wischgeste anbieten und die Pfeile ausblenden, damit die Fläche frei bleibt.

## Siehe auch

- [media – Übersicht](../index.md)
- [Gallery](../gallery/) — viele Bilder auf einmal
- [Grid View](../../data/grid-view/) — Raster statt Reihenfolge
- [Basiskomponente](../../../primitives/basics/base.md)
