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
Ein Audio-Element spielt Audiodateien in verschiedenen Formaten ab. Es bietet Bedienelemente
wie Abspielen/Pause und Lautstärke.

## Verwendungszweck

- Podcasts abspielen
- Musik abspielen
- Sprachnachrichten
- Soundeffekte
- Anleitungsvideos ohne Video

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | eine Datei mit allen Bedienelementen |
| **playlist** | mehrere Dateien mit Zurück/Weiter und einer Liste |
| **kompakt** | Sprachnachricht: Abspielen, Dauer, Fortschritt, keine Lautstärke |

## Features

- Abspielen/Pause-Knopf
- Lautstärkeregler
- Fortschrittsleiste
- Zeitanzeige (aktuelle Position / Gesamtzeit)
- Zeitleiste zum Springen (Klick springt)
- Playlist

## Abgrenzung

- **Nicht verwechseln mit** [media-player](../media-player/): der Media Player ist die übergeordnete Klasse
  mit Bedienelementen, Playlist und Untertiteln; das Audio-Element erbt davon und zeigt nur Ton.
- **Nicht verwechseln mit** [video](../video/): ohne Bild ist es Audio, mit Bild Video – ein einzelnes
  Standbild ist ein [image](../../../primitives/media/image/).
- Eine Sprachnachricht im Chat ist diese Komponente in der Variante `kompakt`, keine eigene
  Komponente.

## Best Practices

- `controls` immer anzeigen, außer bei Hintergrundaudio
- `muted` zusammen mit `autoplay` verwenden (Anforderung der Browser)
- Alternativtext für die Barrierefreiheit angeben
- Mehrere Formate bereitstellen, damit alles abspielbar ist

## Formate

| Format | Beschreibung | Verwendung |
|--------|--------------|------------|
| **MP3** | Standardformat, weit verbreitet | alle Audio-Verwendungen |
| **WAV** | unkomprimiert, hohe Qualität | hochwertiges Audio |
| **OGG** | Open Source | Webanwendungen |
| **AAC** | komprimiert, hohe Qualität | Streaming |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | URL des Audios |
| `controls` | boolean | Bedienelemente anzeigen? |
| `autoplay` | boolean | automatisch abspielen? |
| `muted` | boolean | stumm? |
| `loop` | boolean | wiederholen? |
| `volume` | number | Lautstärke (0–1) |
| `currentTime` | number | aktuelle Abspielposition |
| `duration` | number | Gesamtdauer des Audios |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `zoom` | die Bedienelemente werden größer |
| `opacity` | die Deckkraft ändert sich |
| `border` | der Rand leuchtet auf |

## Siehe auch

- [media – Übersicht](../index.md)
- [Media Player](../media-player/) — gemeinsame Bedienelemente
- [Video](../video/) — mit Bild
- [Basiskomponente](../../../primitives/basics/base.md)
