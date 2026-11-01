# Media Player (Medienwiedergabe)

| Feld | Wert |
|------|------|
| **Kategorie** | `media` |
| **Erbt von** | `base` |
| **Varianten** | `einzeln`, `playlist`, `steuerung` |
| **Zustände** | `spielend`, `pausiert`, `vollbild` |
| **Gesten** | `tap`, `drag`, `double-tap` |
| **Animationen** | `fade-out`, `progress`, `spin` |
| **Verwandt** | `audio`, `video`, `progress`, `embed` |
| **Status** | dokumentiert |

## Beschreibung
Ein Media Player wiedergibt Videos und Audios.

## Verwendungszweck

- Videos
- Audios
- Medien

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | eine Datei, Fläche und Steuerung gehören zusammen |
| **playlist** | mehrere Dateien, Liste mit nächster/vorheriger |
| **steuerung** | nur die Leiste; Bild- oder Tonfläche wird vom Nutzer gestellt |

## Features

- Play/Pause
- Volume
- Progress
- Fullscreen
- Captions

## Abgrenzung

- Diese Komponente ist die **Elternklasse** von [audio](../audio/) und [video](../video/):
  Steuerung, Playlist und Untertitel sind hier definiert, die beiden Kinder nennen nur ihre
  Unterschiede (Plan Abschnitt 4, Zeile 13).
- **Nicht verwechseln mit** [embed](../../special/embed/): ein eingebetteter Player einer fremden
  Plattform ist kein eigener Wiedergeber.
- **Nicht verwechseln mit** [progress](../../feedback/progress/): dort ist der Balken eine Anzeige,
  hier ist er eine Sprungmarke in der Datei.

## Best Practices

- Untertitel immer anbieten, auch wenn der Ton standardmäßig aus ist.
- Steuerung nach drei Sekunden ausblenden, aber per Tastatur und Fokus jederzeit erreichbar lassen.
- Autoplay nur ohne Ton; sonst wartet die Anwendung auf eine bewusste Entscheidung.
- Puffer- und Ladestatus sichtbar machen, Zeit immer als `mm:ss`.
- Vollbild und Bild-in-Bild anbieten, damit die Wiedergabe den Arbeitsbereich nicht blockiert.

## Siehe auch

- [media – Übersicht](../index.md)
- [Audio](../audio/) und [Video](../video/) — die beiden Kinder
- [Embed](../../special/embed/) — Player anderer Anbieter
- [Basiskomponente](../../basics/base/)
