# Gallery — Frontend-Dokumentation

Frontends bekannter Programme dieser Kategorie, analysiert nach ihren **Funktionen** — nichts wird kopiert (ADR 0013). Ein Programm ist hier dokumentiert, weil es weit verbreitet ist oder eine bemerkenswerte Idee hat. Unser eigenes Programm dieser Kategorie ist `FreeSynergy.Gallery` (ADR 0017); seine Fähigkeiten und sein Stand stehen in [requirements](../requirements.md).

## Programme

| Programm | Versionen | Was es ist |
|----------|-----------|------------|
| [Coppermine](coppermine/index.md) | [latest](coppermine/latest/description.md) | Coppermine (CPG) ist ein klassischer Webbaukasten für Fotogalerien mit Alben, Kategorien, Kommentaren, Bewertungen und Rollenrechten. |
| [Damselfly](damselfly/index.md) | [latest](damselfly/latest/description.md) | Damselfly ist eine leichte, schnell startende Fotogalerie mit KI-Erkennung (Gesichter, Szenen, Texte/OCR, Ähnlichkeitssuche) auf Basis von PostgreSQL-Vektoren. |
| [Immich](immich/index.md) | [latest](immich/latest/description.md) | Immich ist eine selbst gehostete Foto- und Video-Verwaltung (Server + Mobile-App): Uploads vom Telefon, Gesichts- und Objekterkennung, Zeitleisten, Alben, geteilte Galerien und eine vollständige RE… |
| [LibrePhotos](librephotos/index.md) | [latest](librephotos/latest/description.md) | LibrePhotos ist die quelloffene Alternative zu Google Photos: Auto-Backup per App, Gesichts- und Objekterkennung, Zeitleiste, Alben und geteilte Galerien. |
| [Lychee](lychee/index.md) | [latest](lychee/latest/description.md) | Lychee ist eine schlanke, selbst gehostete Fotogalerie mit Alben, Freigaben per Link und einer sauberen REST-API. |
| [Nextcloud Photos](nextcloud-photos/index.md) | [latest](nextcloud-photos/latest/description.md) | Die Photos-App von Nextcloud ist die Galerie-Oberfläche über der Dateien-App: Chronologie, Alben, Geteilt-Ansicht, Ordner-Auswahl und (ab NC 25+)Recognizer-/Facial-Recognition-Integration. |
| [PhotoPrism](photoprism/index.md) | [latest](photoprism/latest/description.md) | PhotoPrism indexiert eine vorhandene Fotosammlung, erkennt Inhalte und Gesichter und präsentiert sie als durchsuchbare Web-Galerie mit Alben und Freigaben. |
| [Piwigo](piwigo/index.md) | [latest](piwigo/latest/description.md) | Piwigo ist eine klassische Webbaukasten-Fotogalerie: Kategorienbaum, Rollen und Rechte pro Ordner, Themes, Erweiterungen und eine vollständige Webservice-API. |

## Dateisatz pro Programm (ADR 0012)

```
programs/apps/gallery/frontends/<program>/
├── index.md        was es ist, bemerkenswerte Ideen, dokumentierte Versionen, Quellen
├── changelog.md    Änderungen zwischen dokumentierten Versionen (≥ 2 Versionen)
└── <version>/
    ├── description.md    Pflicht · Ausführliche Beschreibung, Abgrenzung, für wen es passt
    ├── features.md       Pflicht · Was das Programm kann — und was nicht
    ├── layout.md         Pflicht · Fensterstruktur, Bereiche, Panels
    ├── menus.md          Pflicht · Menüstruktur, Kontextmenüs, Menüs nach Rolle
    ├── shortcuts.md      Pflicht · Tastatur-Shortcuts
    ├── api.md            Pflicht · APIs und Protokolle, Authentifizierung, Rate Limits
    ├── themes/index.md   Pflicht · Themes: Farben, Typografie, Abstände — was sich nachbauen lässt
    ├── interaction.md    bei Bedarf · Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift)
    ├── states.md         bei Bedarf · UI-Zustände und Übergänge
    ├── events.md         bei Bedarf · Ereignisse nach außen (Webhooks, Push, Streams)
    ├── limits.md         bei Bedarf · Bekannte Grenzen
    ├── i18n.md           bei Bedarf · Lokalisierung, Schreibrichtung
    └── dependencies.md   bei Bedarf · Welche unserer Bausteine ein Frontend dieser Art braucht
```

Protokolle (Matrix, IMAP, CalDAV, …) sind keine Frontends; sie stehen unter [data](../../../../data/standards.md).
