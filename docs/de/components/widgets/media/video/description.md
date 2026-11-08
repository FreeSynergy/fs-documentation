# Video

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base`, `media-player` |
| **Varianten** | `einzeln`, `hintergrund`, `live` |
| **Zustände** | `spielend`, `vollbild`, `gepuffert` |
| **Gesten** | `tap`, `drag`, `double-tap`, `pinch` |
| **Animationen** | `fade-out`, `progress` |
| **Verwandt** | `media-player`, `audio`, `image`, `embed` |
| **Status** | dokumentiert |

## Beschreibung
Ein Video-Element spielt Videos in verschiedenen Formaten ab. Es bietet Bedienelemente
wie Abspielen/Pause, Lautstärke und Vollbild.

## Verwendungszweck

- Anleitungsvideos zeigen
- Produktvideos präsentieren
- Videokommentare abspielen
- Live-Streams zeigen
- Hintergrundvideos

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | normale Wiedergabe mit allen Bedienelementen |
| **hintergrund** | endlos, stumm und ohne Bedienelemente hinter anderen Inhalten |
| **live** | laufender Stream ohne Vorspulen, die Zeitanzeige wird durch "live" ersetzt |

## Features

- Abspielen/Pause-Knopf
- Lautstärkeregler
- Fortschrittsleiste
- Vollbildmodus
- Untertitel
- Auswahl der Qualität
- Einstellung der Geschwindigkeit

## Abgrenzung

- Das Video erbt von [media-player](../media-player/) und benennt hier nur, was dazukommt:
  Bildfläche, Vorschaubild und Vollbild.
- **Nicht verwechseln mit** [audio](../audio/): ohne Bild ist es Audio – das Standbild allein ist
  ein [image](../../../primitives/media/image/).
- **Nicht verwechseln mit** [embed](../../../workbenches/special/embed/): Videos fremder Plattformen werden
  eingebettet, nicht abgespielt.

## Best Practices

- Immer ein Vorschaubild (`poster`) setzen, sonst ist vor dem Start nichts zu sehen.
- Autoplay nur stumm und in einer Endlosschleife; sonst startet die Wiedergabe nur auf Wunsch.
- Untertitel mitliefern – auch bei Besprechungen und Sprachnachrichten.
- Die Qualität automatisch wählen und manuell umschaltbar lassen.
- Auf dem Smartphone inline abspielen (`playsInline`), sonst springt das System in seinen eigenen Player.

## Formate

| Format | Beschreibung | Verwendung |
|--------|--------------|------------|
| **MP4** | Standardformat, weit verbreitet | alle Video-Verwendungen |
| **WEBM** | Open Source, kleine Dateigröße | Webanwendungen |
| **OGV** | Open-Source-Format | alternatives Format |
| **MKV** | Containerformat, viele Spuren | hochwertige Videos |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | Video-URL |
| `controls` | boolean | Bedienelemente anzeigen? |
| `autoplay` | boolean | automatisch abspielen? |
| `muted` | boolean | stumm? |
| `loop` | boolean | wiederholen? |
| `poster` | string | Vorschaubild |
| `playsInline` | boolean | Wiedergabe im Inline-Modus (Mobil) |
| `volume` | number | Lautstärke (0–1) |

## Siehe auch

- [media – Übersicht](../index.md)
- [Media Player](../media-player/) — gemeinsame Bedienelemente
- [Audio](../audio/) — ohne Bild
- [Basiskomponente](../../../primitives/basics/base.md)
