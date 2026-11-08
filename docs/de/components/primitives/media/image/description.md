# Image (Bild)

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
Ein Bildelement zeigt Grafiken, Fotos oder anderen visuellen Inhalt. Es gehört zu den
grundlegendsten Medienelementen in FreeSynergy.

## Verwendungszweck

- Profilfotos anzeigen
- Produktbilder in Katalogen
- Bilder in Artikeln und Dokumenten
- Hintergrundbilder
- Vorschaubilder

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | Bild im Inhaltsfluss, eigene Höhe oder eigenes Seitenverhältnis |
| **vignette** | zugeschnittenes Vorschaubild in Listen und Cards |
| **hintergrund** | Bild hinter anderem Inhalt (`backgroundSize`, `backgroundPosition`) |

Zuschnitt und Form sind keine Varianten, sondern die Attribute `fit` und `shape`.

## Funktionen

- Responsives Bild: pro Breite eine passende Auflösung (`srcSet`, `sizes`)
- Verzögertes Laden (`lazy`) mit einem Platzhalter (`skeleton`) oder einem Spinner
- Ersatzbild, wenn die Datei fehlt (`onErrorFallback`)
- Alternativtext für Screenreader, `role = presentation` für reine Dekoration

## Abgrenzung

- **Nicht verwechseln mit** [icon](../icon/): Icons sind kleine, einfärbbare Symbole der Fläche.
- **Nicht verwechseln mit** [gallery](../../../widgets/media/gallery/): Eine Galerie fasst
  mehrere Bilder mit einer großen Ansicht zusammen. Das Bild ist ein einzelnes Element.
- **Nicht verwechseln mit** [avatar](../../../widgets/data/avatar/): Ein Avatar identifiziert eine Person.
- Das Vergrößern auf Vollbild gehört in die Galerie oder ein Overlay, nicht in das Bild.

## Best Practices

- Der Alternativtext beschreibt den Inhalt, nicht den Dateinamen. Dekorative Bilder bekommen keinen Alternativtext.
- Immer mehrere Auflösungen anbieten und die Anzeigegröße festlegen, damit Bilder nicht springen.
- Das Seitenverhältnis fest vorgeben. Sonst verschiebt sich die Seite beim Laden.
- Klickbare Bilder brauchen ein klares Symbol und eine Tastaturalternative.
- Bei einem Fehler das Ersatzbild zeigen. Nie ein kaputtes Bild stehen lassen.

## Formate

| Format | Beschreibung | Verwendung |
|--------|--------------|------------|
| **JPEG/JPG** | komprimiert, farbig | Fotos, farbige Bilder |
| **PNG** | Transparenz, keine Kompression | Logos, Icons, Grafiken |
| **GIF** | Animation, Transparenz | kleine Animationen |
| **WEBP** | modernes Format, kleine Dateigröße | moderne Webanwendungen |
| **SVG** | Vektorgrafik, skalierbar | Icons, Logos, Grafiken |
| **AVIF** | neuestes Format, sehr klein | hochwertige Bilder |

## Gestaltungsattribute

| Attribut | Wert | Beschreibung |
|----------|------|--------------|
| `src` | string | URL des Bildes |
| `alt` | string | Alternativtext für Barrierefreiheit |
| `size` | enum | `thumbnail`, `small`, `medium`, `large`, `full` |
| `shape` | enum | `rectangular`, `circular`, `pill` |
| `fit` | enum | `cover`, `contain`, `fill` |
| `loading` | enum | `lazy`, `eager` |
| `interactive` | boolean | ist das Bild klickbar? |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | das Bild wächst |
| `opacity` | die Deckkraft ändert sich |
| `border` | der Rahmen leuchtet auf |
| `shadow` | der Schatten wird stärker |

## Siehe auch

- [media – Übersicht](../index.md)
- [Gallery](../../../widgets/media/gallery/) — mehrere Bilder mit großer Ansicht
- [Icon](../icon/) — ein Symbol statt eines Fotos
- [Base-Komponente](../../basics/base.md)
