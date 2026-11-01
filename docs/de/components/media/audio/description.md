# Audio

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base`, `media-player` |
| **Varianten** | `einzeln`, `playlist`, `kompakt` |
| **Zustände** | `spielend`, `pausiert` |
| **Gesten** | `tap`, `drag` |
| **Animationen** | `progress`, `pulse` |
| **Verwandt** | `media-player`, `video`, `progress` |
| **Status** | dokumentiert |

## Beschreibung
Ein Audio-Element wiedergibt Audiodateien in verschiedenen Formaten. Es bietet Steuerungsfunktionen wie Play/Pause und Lautstärke.

## Verwendungszweck

- Podcasts wiedergeben
- Musik abspielen
- Sprachnachrichten
- Soundeffekte
- Anleitungsvideos ohne Video

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | eine Datei mit voller Steuerung |
| **playlist** | mehrere Dateien mit vorheriger/nächster und Liste |
| **kompakt** | Sprachnachricht: Play, Dauer, Fortschritt, keine Lautstärke |

## Features

- Play/Pause-Button
- Lautstärkeregler
- Fortschrittsbalken
- Zeitanzeige (aktueller Zeitpunkt / Gesamtzeit)
- Timeline-Seek (klicken zum Springen)
- Wiedergabeliste

## Best Practices

- Immer `controls` anzeigen, außer bei Hintergrund-Audio
- `muted` bei `autoplay` verwenden (Browser-Anforderung)
- Alt-Text für Barrierefreiheit bereitstellen
- Verschiedene Formate für Kompatibilität bereitstellen

## Abgrenzung

- **Nicht verwechseln mit** [media-player](../media-player/): der Media Player ist die Elternklasse
  mit Steuerung, Playlist und Untertiteln; das Audio-Element erbt davon und zeigt nur Ton.
- **Nicht verwechseln mit** [video](../video/): ohne Bild ist es Audio, mit Bild Video — ein
  Video-Standbild allein ist ein [image](../image/).
- Eine Sprachnachricht im Chat ist diese Komponente in der Variante `kompakt`, keine eigene
  Komponente.

## Formate

| Format | Beschreibung | Verwendung |
|--------|-------------|------------|
| **MP3** | Standard-Format, weit verbreitet | Alle Audio-Anwendungen |
| **WAV** | Unkomprimiert, hohe Qualität | Hochwertige Audio |
| **OGG** | Open Source | Web-Applikationen |
| **AAC** | Komprimiert, hohe Qualität | Streaming |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | Audio-URL |
| `controls` | boolean | Steuerung anzeigen? |
| `autoplay` | boolean | Auto-Wiedergabe? |
| `muted` | boolean | Stumm? |
| `loop` | boolean | Wiederholen? |
| `volume` | number | Lautstärke (0-1) |
| `currentTime` | number | Aktuelle Wiedergabeposition |
| `duration` | number | Gesamtdauer des Audios |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | Controls vergrößern sich |
| `opacity` | Deckkraft ändert sich |
| `border` | Rand leuchtet auf |

## Siehe auch

- [media – Übersicht](../index.md)
- [Media Player](../media-player/) — gemeinsame Steuerung
- [Video](../video/) — mit Bild
- [Basiskomponente](../../basics/base/)
