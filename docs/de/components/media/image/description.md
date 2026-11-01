# Bild (Image)

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base` |
| **Varianten** | `einfach`, `vignette`, `hintergrund` |
| **Zustände** | `geladen`, `fehler` |
| **Gesten** | `tap`, `pinch`, `double-tap`, `drag` |
| **Animationen** | `skeleton`, `fade-in`, `zoom-in` |
| **Verwandt** | `gallery`, `icon`, `avatar`, `card`, `hover-card` |
| **Status** | dokumentiert |

## Beschreibung
Ein Bild-Element zeigt Grafiken, Fotos oder andere visuelle Inhalte an. Es ist eines der grundlegendsten Medien-Elemente in FreeSynergy.

## Verwendungszweck

- Profilfotos anzeigen
- Produktbilder in Katalogen
- Bilder in Artikeln und Dokumenten
- Background-Images
- Thumbnails

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | Bild im Inhaltsfluss, eigene Höhe oder Seitenverhältnis |
| **vignette** | zugeschnittenes Vorschaubild in Listen und Karten |
| **hintergrund** | Bild hinter anderem Inhalt (`backgroundSize`, `backgroundPosition`) |

Zuschnitt und Form sind keine Varianten, sondern die Attribute `fit` und `shape`.

## Features

- Responsives Bild: passende Auflösung je Breite (`srcSet`, `sizes`)
- Spätes Laden (`lazy`) mit Platzhalter (`skeleton`) oder Spinner
- Rückfallebene, wenn die Datei fehlt (`onErrorFallback`)
- Alt-Text für Screenreader, `role = presentation` bei reiner Zierde

## Abgrenzung

- **Nicht verwechseln mit** [icon](../icon/): Icons sind kleine, einfärbbare Symbole der Oberfläche.
- **Nicht verwechseln mit** [gallery](../gallery/): eine Galerie ist der Verband mehrerer Bilder
  samt Großansicht, das Bild ist ein einzelnes Element.
- **Nicht verwechseln mit** [avatar](../../data/avatar/): ein Avatar identifiziert eine Person.
- Das Aufziehen auf volle Bildschirmgröße gehört in die Galerie bzw. ein Overlay, nicht ins Bild.

## Best Practices

- Alt-Text beschreibt den Inhalt, nicht den Dateinamen; Zierbilder bekommen kein Alt-Text-Ziel.
- Immer mehrere Auflösungen anbieten und die Anzeigegröße vorgeben, damit Bilder nicht springen.
- Seitenverhältnis fest setzen, sonst verrutscht die Seite beim Laden.
- Klickbare Bilder brauchen ein deutliches Symbol und eine Tastaturalternative.
- Bei Fehler die Rückfallebene zeigen, nie ein gebrochenes Bild stehen lassen.

## Formate

| Format | Beschreibung | Verwendung |
|--------|-------------|------------|
| **JPEG/JPG** | Komprimiert, farbenfroh | Fotos, Bilder mit Farben |
| **PNG** | Transparenz, keine Komprimierung | Logos, Icons, Grafiken |
| **GIF** | Animation, Transparenz | Kleine Animationen |
| **WEBP** | Moderne Formate, kleine Dateigröße | Moderne Web-Applikationen |
| **SVG** | Vektorgraphik, skalierbar | Icons, Logos, Grafiken |
| **AVIF** | Neuestes Format, sehr klein | Hochwertige Bilder |

## Styling-Attribute

| Attribut | Wert | Beschreibung |
|----------|------|--------------|
| `src` | string | Bild-URL |
| `alt` | string | Alt-Text für Barrierefreiheit |
| `size` | enum | `thumbnail`, `small`, `medium`, `large`, `full` |
| `shape` | enum | `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover`, `contain`, `fill` |
| `loading` | enum | `lazy`, `eager` |
| `interactive` | boolean | Ist das Bild klickbar? |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Bild vergrößert sich |
| `opacity` | Deckkraft ändert sich |
| `border` | Rand leuchtet auf |
| `shadow` | Schatten wird stärker |

## Siehe auch

- [media – Übersicht](../index.md)
- [Gallery](../gallery/) — mehrere Bilder mit Großansicht
- [Icon](../icon/) — Symbol statt Foto
- [Basiskomponente](../../basics/base/)
