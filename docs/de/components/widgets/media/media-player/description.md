# Media Player

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
Ein Media Player spielt Videos und Audio ab.

## Verwendungszweck

- Videos
- Audio
- Medien

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | eine Datei, Fläche und Bedienelemente gehören zusammen |
| **playlist** | mehrere Dateien, eine Liste mit Weiter/Zurück |
| **steuerung** | nur die Leiste; die Bild- oder Tonfläche stellt der Nutzer bereit |

## Features

- Abspielen/Pause
- Lautstärke
- Fortschritt
- Vollbild
- Untertitel

## Abgrenzung

- Diese Komponente ist die **Oberklasse** von [audio](../audio/) und [video](../video/):
  Bedienelemente, Playlist und Untertitel sind hier definiert, die beiden Unterklassen benennen nur
  ihre Unterschiede (Planabschnitt 4, Zeile 13).
- **Nicht verwechseln mit** [embed](../../../workbenches/special/embed/): ein eingebetteter Player einer
  fremden Plattform ist kein eigener Player.
- **Nicht verwechseln mit** [progress](../../../primitives/feedback/progress/): dort ist der Balken eine
  Anzeige, hier ist er eine Sprungmarke innerhalb der Datei.

## Best Practices

- Immer Untertitel anbieten, auch wenn der Ton standardmäßig aus ist.
- Die Bedienelemente nach drei Sekunden ausblenden, aber jederzeit per Tastatur und Fokus erreichbar lassen.
- Autoplay nur ohne Ton; sonst wartet die Anwendung auf eine bewusste Entscheidung.
- Den Puffer- und Ladezustand sichtbar machen, Zeiten immer als `mm:ss` anzeigen.
- Vollbild und Bild-in-Bild anbieten, damit die Wiedergabe den Arbeitsbereich nicht blockiert.

## Siehe auch

- [media – Übersicht](../index.md)
- [Audio](../audio/) und [Video](../video/) — die beiden Unterklassen
- [Embed](../../../workbenches/special/embed/) — Player anderer Anbieter
- [Basiskomponente](../../../primitives/basics/base.md)
