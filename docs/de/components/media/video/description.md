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
Ein Video-Element wiedergibt Videos in verschiedenen Formaten. Es bietet Steuerungsfunktionen wie Play/Pause, Volume und Fullscreen.

## Verwendungszweck

- Anleitungsvideos anzeigen
- Produktvideos präsentieren
- Video-Kommentare wiedergeben
- Live-Streams anzeigen
- Hintergrund-Videos

## Features

- Play/Pause-Button
- Lautstärkeregler
- Fortschrittsbalken
- Vollbild-Modus
-Untertitel

- Qualitätsauswahl
- Geschwindigkeitseinstellung

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | gewöhnliche Wiedergabe mit voller Steuerung |
| **hintergrund** | endlos, stumm und ohne Steuerung hinter anderem Inhalt |
| **live** | Laufender Stream ohne Vorspulen, Zeitangabe durch „live“ ersetzt |

## Formate

| Format | Beschreibung | Verwendung |
|--------|-------------|------------|
| **MP4** | Standard-Format, weit verbreitet | Alle Video-Anwendungen |
| **WEBM** | Open Source, kleine Dateigröße | Web-Applikationen |
| **OGV** | Open Source-Format | Alternatives Format |
| **MKV** | Container-Format, viele Streams | Hochwertige Videos |

## Abgrenzung

- Das Video erbt von [media-player](../media-player/) und nennt hier nur, was dazukommt:
  Bildfläche, Vorschaubild und Vollbild.
- **Nicht verwechseln mit** [audio](../audio/): ohne Bild ist es Audio — das Standbild allein ist
  ein [image](../image/).
- **Nicht verwechseln mit** [embed](../../special/embed/): Videos fremder Plattformen werden
  eingebettet, nicht abgespielt.

## Best Practices

- Immer ein Vorschaubild (`poster`) setzen, sonst ist vor dem Start nichts zu sehen.
- Autoplay nur stumm und in Endlosschleife; sonst startet Wiedergabe nur auf Wunsch.
- Untertitel mitführen — auch für Meetings und Sprachnachrichten.
- Qualität automatisch wählen und manuell umschaltbar lassen.
- Auf Mobil inline abspielen (`playsInline`), sonst springt das System in seinen eigenen Player.

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `src` | string | Video-URL |
| `controls` | boolean | Steuerung anzeigen? |
| `autoplay` | boolean | Auto-Wiedergabe? |
| `muted` | boolean | Stumm? |
| `loop` | boolean | Wiederholen? |
| `poster` | string | Vorschaubild |
| `playsInline` | boolean | Inline-Wiedergabe (Mobile) |
| `volume` | number | Lautstärke (0-1) |

## Siehe auch

- [media – Übersicht](../index.md)
- [Media Player](../media-player/) — gemeinsame Steuerung
- [Audio](../audio/) — ohne Bild
- [Basiskomponente](../../basics/base/)
