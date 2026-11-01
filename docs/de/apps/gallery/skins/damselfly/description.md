# Damselfly - Beschreibung

## Was das Programm macht

Damselfly überwacht einen Foto-Ordner, indexiert alles und liefert eine sehr schnelle Suchgalerie mit KI-Merkmalen (Gesichter, Labels, OCR, Ähnlichkeit). Es versteht sich als ressourcenschonende, container-freundliche Alternative zu ausgewachsenen Foto-Clouds.

## Vorteile

- **schnell und leicht**: .NET-Backend, geringer Speicherbedarf, schnelle Oberfläche
- **KI ohne Cloud** inklusive OCR, was PhotoPrism in der Community-Edition fehlt
- **Einfacher Betrieb**: ein Container plus PostgreSQL

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **PhotoPrism** | ähnlicher Ansatz, größere Community, Editionen mit Funktionsunterschieden. |
| **Immich** | Foto-Cloud mit Apps/Auto-Backup; Damselfly setzt auf Ordner-Sync. |
| **Lychee** | reine Galerie ohne KI; dafür schlanke REST-API und OAuth-Logins. |

## Technische Details

- **Backend**: C#/.NET, Entity Framework, PostgreSQL mit pgvector
- **KI**: ONNX-Modelle (Face, Label, OCR, Similarity), optional GPU
- **Frontend**: React-SPA, responsive
- **Deployment**: Docker Compose (Standard), ARM64/AMD64
- **Lizenz**: AGPLv3

## Für wen geeignet

- Selbstversorger mit bestehendem Foto-Ordner und Wunsch nach KI-Suche
- FreeSynergy-Gallery-Skins mit Modell Album / Photo / Person / Label
- Umgebungen mit knapper Hardware
