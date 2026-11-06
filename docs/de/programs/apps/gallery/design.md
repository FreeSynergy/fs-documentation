# Galerie — Design

**Teilweise abgelöst (2026-11-06):** Die Galerie ist kein eigenes Programm mehr. Sie ist eine Workbench und ein Frontend von [`fs-files`](../files/design.md). Alben, Modi und Metadaten unten wandern dorthin; siehe den [Gesamtplan](../roadmap.md).

**Status: Vorschlag (2026-11-06).** Zurück zum [Gesamtplan](../roadmap.md) · [Anforderungen](requirements.md).

## Idee

Die Galerie besitzt die **Ansicht von Fotos und Videos**, nicht deren Bytes. Bytes liegen in [`fs-files`](../files/design.md). Die Galerie ergänzt Alben, Zeitleiste, Orte und Personen. Ein Foto bleibt eine normale Datei, die auch andere Programme nutzen können.

## Daten

| Teil | Standard | Hinweise |
|------|----------|----------|
| Foto, Video | AS2 `Image`, `Video`, verweist auf ein Objekt von `fs-files` | |
| Eingebettete Metadaten | Exif 3.1, XMP, IPTC 2025.1 | Belegt in [Standards](../../../data/standards.md). Nur lesen; Originale bleiben unberührt (ADR 0030) |
| Ort | GeoJSON, AS2 `Place` | Wird über `fs-maps` gezeigt |
| Album | AS2 `Collection` | |
| Bearbeitungen | Lücke | Als Anweisungen gespeichert, nicht als geänderte Datei |
| Gesichter | Lücke | Sensibel; siehe unten |

## Abgeleitete Daten

Vorschaubilder und Indizes lassen sich immer neu erzeugen. Deshalb werden sie getrennt von den Daten gehalten und standardmäßig nicht synchronisiert.

## Gesichter und automatische Schlagwörter

Optional und **nur lokal**: Fotos und Gesichtsdaten verlassen das Gerät nie zur Analyse. Gesichter sind biometrische Daten und fallen unter ADR 0029. Das ist standardmäßig aus und wird erklärt, bevor es eingeschaltet wird.

## Muster

| Muster | Verwendung |
|--------|------------|
| Repository | `MediaRepository`, `AlbumRepository` |
| Pipeline (Template-Methode) | Import: Metadaten lesen → Vorschaubilder → Index; jeder Schritt kann wiederholt werden |
| Strategy | Vorschaubild-Erzeugung je Format; optionale Tagging-Engine |
| Adapter | Metadaten-Crates hinter unserem eigenen Trait |
| Decorator | Vorschaubild-Cache über dem Generator |

## Kandidaten

| Zweck | Crate (2026-11-06) |
|-------|--------------------|
| Bilder dekodieren und skalieren | `image` 0.25 |
| Metadaten lesen | `kamadak-exif` 0.6 oder `nom-exif` 3.8 (liest auch Video-Metadaten, zu prüfen) |
| Moderne Formate | `ravif` 0.13, `jxl-oxide` 0.12 |

Video-Poster brauchen einen Decoder, was dieselbe Frage aufwirft wie [Streaming](../streaming/design.md#kodierung). Deshalb sind Video-Poster nicht in Stufe 1.

## Schnittstellen-Skizze

| Schnittstelle | Fähigkeiten |
|---------------|-------------|
| `Gallery` (Wurzel) | `capabilities()`, gibt die anderen heraus |
| `Library` | `media.import`, `media.list`, `media.search`, `media.delete` |
| `Albums` | `album.create`, `album.add`, `album.remove`, `album.nest` |
| `Metadata` | `metadata.read`, `metadata.edit` |
| `Timeline`, `Places` | Abfrage nach Zeit und Ort |
| `subscribe` | Live-Änderungen |

Die IDs folgen den [Anforderungen](requirements.md).

## Komponenten

Vorhanden: `gallery`, `carousel`, `image`, `video`, `map-view`, `timeline`, `description-list`. Neu: Workbench `gallery-browser`, Overlay `lightbox`. Siehe [geplante Komponenten](../../../components/planned.md).

## Stufen

1. Import aus `fs-files`, Metadaten, Vorschaubilder, Zeitleiste, Alben.
2. Workbench, Lightbox, Kartenansicht über `fs-maps`, ein erstes einfaches Frontend.
3. Teilen, Suche, nicht zerstörerische Bearbeitungen.
4. Videos mit Postern, optionale lokale Gesichts- und Objekterkennung.

## Offene Fragen

1. **Automatischer Upload vom Handy:** Das steht in den Anforderungen. Gehört es zur Galerie oder zu `fs-files`? Wir schlagen `fs-files` vor, mit der Galerie als Ansicht auf das Ergebnis.
2. **Metadaten schreiben:** nur in unsere Objekte oder auch in die Datei? Wir schlagen unsere Objekte vor, mit optionalem Export.
3. **Rohformate von Kameras:** im Umfang? Wir schlagen später vor.
