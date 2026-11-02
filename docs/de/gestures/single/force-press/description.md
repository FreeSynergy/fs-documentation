# Force Press (Druck-Geste)

## Beschreibung

Ein Force Press nutzt einen **Drucksensor**: Nicht die Zeit oder Strecke
entscheidet, sondern die aufgewendete Kraft. Apple nannte das 3D Touch
(„Peek & Pop“), auf Trackpads heißt es Force Click, Android-Geräte mit
Druckebene nennen es Hard Press.

Ohne Drucksensor wird die Geste heute meist per **Long Press simuliert**
(Press and Hold), weil Drucksensoren in Smartphones verschwunden sind.
Web: `PointerEvent.pressure` liefert nur bei kompatibler Hardware Werte > 0.

## Verwendung

- Peek & Pop: Vorschau beim leichten Druck, Öffnen beim stärkeren Druck
- Kontextmenü ohne langes Warten
- Schnelldialoge an App-Icons (Homescreen-Shortcuts)
- Druckabhängige Pinselstärke in Zeichen-Apps (Stift)

## Druckstufen

| Stufe | Druck | Aktion |
|-------|-------|--------|
| Light Press | ab ~30% | Element gibt minimal nach |
| Peek | ab ~50% | Vorschau-Karte erscheint |
| Pop | ab ~75% | Ziel wird geöffnet |

## Dauer

- Druck aufbauen: 100–500ms
- Vorschau-Öffnen: 200–300ms

## Erkennung

| Methode | Beschreibung |
|---------|--------------|
| **Drucksensor** | Hardware misst Kraft (iOS älter, Trackpad, Stift) |
| **Long Press Fallback** | Ohne Sensor: Halten ersetzt Drücken |
| **pressure-Wert** | `pointerdown`/`pointermove` mit `pressure` 0–1 |

## Unterschied zu Long Press

- **Long Press**: Zeit entscheidet
- **Force Press**: Kraft entscheidet (Zeit gleichgültig)

## Siehe auch

- [Long Press](../long-press/description.md) - Fallback ohne Drucksensor
- [Press-Animation](../../../animations/feedback/press/description.md)
