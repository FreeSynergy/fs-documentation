# PhotoPrism - Beschreibung

## Was das Programm macht

PhotoPrism legt eine Datenbank über einen vorhandenen Foto-Ordner: Alles wird indexiert, vorschaubereit, verschlagwortet und durchsuchbar gemacht. Die Oberfläche ist eine Galerie mit starker Suche, Alben und Freigaben; die Dateien bleiben in ihrer Ordnerstruktur erhalten.

## Vorteile

- **Behält die eigene Ordnerstruktur** — kein proprietärer Katalog als einzige Wahrheit
- **Schnelle, facettenreiche Suche** (Label, Farbe, Ort, Person, Zeitraum)
- **Ressourcenschonend**: Go-Backend, läuft auf Small-Server/NAS
- **Klare Rollen** (Viewer/Contributor/Admin) für geteilte Installationen

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Immich** | App-zentriert mit Auto-Backup und eigener Ablage; PhotoPrism indexiert bestehende Ordner. |
| **LibrePhotos** | näher an Immich (Apps, Gesichts-KI), kleinere Community. |
| **Piwigo** | Webbaukasten-Galerie mit Themes und Rollen pro Ordner, aber ohne KI-Erkennung. |

## Technische Details

- **Backend**: Go, SQLite oder MariaDB/MySQL, Bildverarbeitung über Imaginary/ImageMagick
- **KI**: TensorFlow-Modelle für Labels/Gesichter (CE mit reduziertem Umfang, Plus/CE-Editionen)
- **Frontend**: Vue 2/3 SPA, serverseitig ausgeliefert, responsive
- **Deployment**: Docker Compose (Standard), Binaries, ARM64/AMD64
- **Lizenz**: Community Edition AGPLv3, Plus/CE-Erweiterungen kommerziell

## Für wen geeignet

- Sammlungen, die bereits als Ordnerbaum vorliegen und nur „galerie­tauglich“ gemacht werden sollen
- FreeSynergy-Gallery-Skins mit Modell Album / Photo / Label / Person
- Haushalte und Teams ohne Anspruch an Handy-Auto-Backup
