# Finder

> Kategorie: [Dateien](../../index.md) · [Frontends](../index.md)

## Was es ist

Der Dateimanager von macOS. Teil des Systems; Spotlight und iCloud Drive liegen daneben.

## Bemerkenswerte Ideen

- **Tags als Farben und Namen**, mehrere pro Element, durchsuchbar, in der Seitenleiste, nutzbar zum Gruppieren und Sortieren ✅. Control-1..7 schaltet Favoriten-Tags um, Control-0 leert sie ✅.
- **Intelligente Ordner:** ein Ordner, der Elemente nach Kriterien sammelt, die du festlegst ✅. Dieselbe Idee wie unser „Album als gespeicherte Suche“.
- **Schnellansicht (Leertaste):** volle Vorschau der meisten Dateien, Markierung, Zuschneiden von Audio und Video, Diashow, Indexblatt ✅.
- **Aliase:** eine Verknüpfungsdatei, die überall liegen kann ✅.
- **Galerieansicht** und ein **Vorschaubereich** ✅.
- **Eigene Symbole** pro Ordner: Farbe, Symbol, Emoji ✅.
- **Ordner vor Dateien** beim Sortieren als Option ✅.

## Gesehene Fähigkeiten

| Fähigkeit | Gesehen | Hinweis |
|-----------|---------|---------|
| Seitenleiste, anpassbar | ✅ | |
| Anzeigemodi inkl. Galerie | ✅ | Auf der gelesenen Seite nur Galerie genannt; Symbole, Liste, Spalten ⚠️ |
| Sortieren und Gruppieren nach Name, zuletzt geöffnetem Datum, Tag | ✅ | |
| Tags | ✅ | |
| Intelligente Ordner | ✅ | |
| Aliase | ✅ | |
| Schnellansicht | ✅ | |
| AirDrop, iCloud Drive, Geräte in der Seitenleiste | ✅ | Als verwandte Themen genannt |
| Papierkorb mit „Zurücklegen“, automatisches Leeren | ⚠️ | Die abgerufene Seite deckte das nicht ab |

## Namensregeln

⚠️ Auf den gelesenen Seiten nicht gefunden. Die Seite zu rclone mount sagt, dass macOS nicht zwischen Groß- und Kleinschreibung unterscheidet, sie aber erhält, und rät, die Unicode-Normalisierung eingeschaltet zu lassen ✅ (https://rclone.org/commands/rclone_mount/).

## Was wir übernehmen

Tags und intelligente Ordner als ein Mechanismus (`file.tag`, gespeicherte Suche). Eine schnelle Vorschau auf Leertaste, die die App nicht öffnet (`file.preview`). Aliase sind der Grund, warum eine Datei an mehreren Orten liegen soll; der Vertrag kennt nur einen Ordner pro Datei.

## Quellen (gelesen 2026-11-06)

- https://support.apple.com/guide/mac-help/organize-files-in-folders-mchlp2605/mac
- https://support.apple.com/guide/mac-help/use-quick-look-to-preview-files-mh14119/mac
- https://support.apple.com/guide/mac-help/tag-files-and-folders-mchlp15236/mac
- https://support.apple.com/guide/mac-help/change-the-way-you-view-files-and-folders-mchlp2605/mac
