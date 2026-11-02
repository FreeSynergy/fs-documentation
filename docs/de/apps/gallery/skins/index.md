# Gallery Skin-Dokumentation

## Übersicht

Dieses Verzeichnis enthält die Dokumentation der Programme dieser Kategorie nach dem Wiki-Schema: Menüpunkte, Funktionen, Beschreibung, Struktur/UI-UX, Tastatur-Shortcuts und API — sieben Dateien pro Programm.

Alle hier dokumentierten Programme sind **keine** FreeSynergy-Eigenentwicklungen, sondern fremde Programme, deren Oberfläche und Schnittstellen als Skin nachgebildet bzw. angebunden werden.

## Enthaltene Dokumentationen

- [Coppermine](./coppermine/index.md)
- [Damselfly](./damselfly/index.md)
- [Immich](./immich/index.md)
- [LibrePhotos](./librephotos/index.md)
- [Lychee](./lychee/index.md)
- [Nextcloud Photos](./nextcloud-photos/index.md)
- [PhotoPrism](./photoprism/index.md)
- [Piwigo](./piwigo/index.md)

## Verzeichnisstruktur

```
docs/de/apps/gallery/skins/
├── index.md              (diese Datei)
├── coppermine/   (index, menu, features, description, structure, shortcuts, api)
├── damselfly/   (index, menu, features, description, structure, shortcuts, api)
├── immich/   (index, menu, features, description, structure, shortcuts, api)
├── librephotos/   (index, menu, features, description, structure, shortcuts, api)
├── lychee/   (index, menu, features, description, structure, shortcuts, api)
├── nextcloud-photos/   (index, menu, features, description, structure, shortcuts, api)
├── photoprism/   (index, menu, features, description, structure, shortcuts, api)
└── piwigo/   (index, menu, features, description, structure, shortcuts, api)
```

## Inhalt jeder Dokumentation

Jedes Programmverzeichnis enthält **sieben** Dateien:

1. **index.md** – Übersicht des Programms und Links auf die sechs Detail-Dateien
2. **menu.md** – alle Hauptmenüpunkte, Kontext-Menüs, rollenabhängige Menüs
3. **features.md** – Hauptfunktionen, was das Programm kann und NICHT kann, Erweiterungen
4. **description.md** – Beschreibung, Vorteile, Abgrenzung, technische Details, Zielgruppen
5. **structure.md** – Fenster-/Seitenstruktur, UI/UX, Interaktionen, Responsive Design, Accessibility
6. **shortcuts.md** – alle Tastatur-Shortcuts inklusive Mac-Varianten
7. **api.md** – API-Art, Authentifizierung, Endpunkte, Beispiele, Rate Limits, Webhooks, SDKs

## Hinweise

- Alle Dokumentationen sind auf Deutsch verfasst
- Die Inhalte sind für Anwender und Administratoren geeignet
- **Tastatur-Shortcuts sind immer in der separaten Datei `shortcuts.md`**
- **API-Dokumentation ist immer in der separaten Datei `api.md`**
- Fehlende Funktionen sind ausdrücklich als nicht vorhanden markiert (❌)

## Verwandte Bereiche

- [Kategorie-Übersicht](../) – Überblick über diese Programmkategorie
- [Wiki-Skins](../../wiki/skins/) – Referenzschema dieser Dokumentation
- [Desktop-Skins](../../desktop/skins/) – gleiche Dateistruktur
- [Standardisierte Daten](../../../data/) – Felder und Modelle für alle Skin-APIs
