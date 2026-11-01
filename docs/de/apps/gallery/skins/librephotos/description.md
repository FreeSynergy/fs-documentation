# LibrePhotos - Beschreibung

## Was das Programm macht

LibrePhotos baut eine private Foto-Cloud: Aufnahmen werden gescannt, verschlagwortet, Gesichtern und Orten zugeordnet und in einer React-Oberfläche als Zeitleiste, Album oder Karte gezeigt. Der Bestand liegt als Dateien auf dem Server.

## Vorteile

- **Kompletter Funktionsumfang einer Foto-Cloud** inkl. Apps und KI-Suche
- **Klare Python-Basis** (Django), gut anpassbar und lesbar
- **Semantische Suche** ohne Cloud-Dienste

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Immich** | größere Community, flüssigere Timeline, sauberere API; LibrePhotos ist modularer im Backend. |
| **PhotoPrism** | indexiert bestehende Ordner und ist Go-basiert; LibrePhotos verwaltet die Bibliothek selbst. |
| **Piwigo** | Webbaukasten-Galerie ohne KI, dafür Themes und Rollen pro Ordner. |

## Technische Details

- **Backend**: Python/Django, Celery-Workers, Redis, PostgreSQL
- **KI**: CLIP (Suche), face-recognition,Places365- und Objektklassifikation
- **Frontend**: React SPA, mobile Apps in React Native
- **Deployment**: Docker Compose, Worker und Web container getrennt
- **Lizenz**: AGPLv3

## Für wen geeignet

- Nutzer, die Google-Photos-Funktionalität self-hosted und Python-nah abbilden wollen
- FreeSynergy-Gallery-Skins mit Modell Album / Photo / Person / Share
- Projekte, die Erkennungs-Pipelines selbst anpassen möchten
