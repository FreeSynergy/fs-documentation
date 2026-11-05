# Foto-Galerien

## Übersicht

Foto-Galerien verwalten Bild- und Videosammlungen: Sie indexieren Bestände, erzeugen Vorschauen, machen Inhalte durchsuchbar (Alben, Labels, Gesichter, Orte) und teilen Ergebnisse über Web-Galerien oder Apps. Die Kategorie umfasst Server zum Selbstbetrieb (Immich, PhotoPrism, Piwigo …) genauso wie in Groupware eingebettete Fotolösungen (Nextcloud Photos).

## Verfügbare Systeme

- **immich** - Self-hosted Fotoverwaltung mit Mobile-Upload, Gesichts- und Ortserkennung
- **photoprism** - Indexierung mit Labels und Gesichtern, Vue-Web-Galerie
- **librephotos** - Fotoverwaltung mit ML-Tagging und Zeitachsen-Ansicht
- **lychee** - schlanke, sichere Selbsthost-Galerie
- **piwigo** - Web-Galerie mit große Plugin- und Community-Basis
- **coppermine** - klassische PHP-Foto-Galerie (Coppermine Photo Gallery)
- **damselfly** - leichte Bildverwaltung direkt auf Lightroom-Katalogen
- **nextcloud-photos** - Foto-Ansicht und -Freigaben innerhalb von Nextcloud

## Frontends

<!-- gen:frontends (Spiegel von docs/en; ADR 0011) — edits inside are overwritten -->
Analysierte Programme (8), nach Funktionen, nichts kopiert (ADR 0012/0013):

- [Coppermine](frontends/coppermine/index.md) — Coppermine (CPG) ist ein klassischer Webbaukasten für Fotogalerien mit Alben, Kategorien, Kommentaren, Bewertungen und Rollenrechten.
- [Damselfly](frontends/damselfly/index.md) — Damselfly ist eine leichte, schnell startende Fotogalerie mit KI-Erkennung (Gesichter, Szenen, Texte/OCR, Ähnlichkeitssuche) auf Basis von PostgreSQL-Vektoren.
- [Immich](frontends/immich/index.md) — Immich ist eine selbst gehostete Foto- und Video-Verwaltung (Server + Mobile-App): Uploads vom Telefon, Gesichts- und Objekterkennung, Zeitleisten, Alben, geteilte Galerien und eine vollständige RE…
- [LibrePhotos](frontends/librephotos/index.md) — LibrePhotos ist die quelloffene Alternative zu Google Photos: Auto-Backup per App, Gesichts- und Objekterkennung, Zeitleiste, Alben und geteilte Galerien.
- [Lychee](frontends/lychee/index.md) — Lychee ist eine schlanke, selbst gehostete Fotogalerie mit Alben, Freigaben per Link und einer sauberen REST-API.
- [Nextcloud Photos](frontends/nextcloud-photos/index.md) — Die Photos-App von Nextcloud ist die Galerie-Oberfläche über der Dateien-App: Chronologie, Alben, Geteilt-Ansicht, Ordner-Auswahl und (ab NC 25+)Recognizer-/Facial-Recognition-Integration.
- [PhotoPrism](frontends/photoprism/index.md) — PhotoPrism indexiert eine vorhandene Fotosammlung, erkennt Inhalte und Gesichter und präsentiert sie als durchsuchbare Web-Galerie mit Alben und Freigaben.
- [Piwigo](frontends/piwigo/index.md) — Piwigo ist eine klassische Webbaukasten-Fotogalerie: Kategorienbaum, Rollen und Rechte pro Ordner, Themes, Erweiterungen und eine vollständige Webservice-API.

Übersicht: [frontends](frontends/index.md)
<!-- /gen:frontends -->
## Masken-Dokumentation

Programme dieser Kategorie werden nach dem Wiki-Schema dokumentiert (sieben Dateien pro Programm: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`) unter `programs/apps/gallery/masks/<programm>/`.

**dokumentiert (8 Programme):**

- [Coppermine](frontends/coppermine/index.md) - Coppermine
- [Damselfly](frontends/damselfly/index.md) - Damselfly
- [Immich](frontends/immich/index.md) - Immich
- [LibrePhotos](frontends/librephotos/index.md) - LibrePhotos
- [Lychee](frontends/lychee/index.md) - Lychee
- [Nextcloud Photos](frontends/nextcloud-photos/index.md) - Nextcloud Photos
- [PhotoPrism](frontends/photoprism/index.md) - PhotoPrism
- [Piwigo](frontends/piwigo/index.md) - Piwigo

Übersicht: [Masken-Verzeichnis](frontends/index.md)

Referenzschema: [Wiki-Masken](../wiki/frontends/index.md) · [Desktop-Masken](../../platform/desktop/frontends/index.md) · [Standardisierte Daten](../../../data/api.md)
