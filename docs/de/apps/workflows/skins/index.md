# Workflows Skin-Dokumentation

## Übersicht

Dieses Verzeichnis enthält die Dokumentation der Programme dieser Kategorie nach dem Wiki-Schema: Menüpunkte, Funktionen, Beschreibung, Struktur/UI-UX, Tastatur-Shortcuts und API — sieben Dateien pro Programm.

Alle hier dokumentierten Programme sind **keine** FreeSynergy-Eigenentwicklungen, sondern fremde Programme, deren Oberfläche und Schnittstellen als Skin nachgebildet bzw. angebunden werden.

## Enthaltene Dokumentationen

- [Apache Airflow](./apache-airflow/index.md)
- [Make](./make/index.md)
- [n8n](./n8n/index.md)
- [Node-RED](./node-red/index.md)
- [Prefect](./prefect/index.md)
- [Zapier](./zapier/index.md)

## Verzeichnisstruktur

```
docs/de/apps/workflows/skins/
├── index.md              (diese Datei)
├── apache-airflow/   (index, menu, features, description, structure, shortcuts, api)
├── make/   (index, menu, features, description, structure, shortcuts, api)
├── n8n/   (index, menu, features, description, structure, shortcuts, api)
├── node-red/   (index, menu, features, description, structure, shortcuts, api)
├── prefect/   (index, menu, features, description, structure, shortcuts, api)
└── zapier/   (index, menu, features, description, structure, shortcuts, api)
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
