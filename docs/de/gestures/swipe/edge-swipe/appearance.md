# Edge Swipe - Aussehen

## Grundlayout

Ein oder mehrere Finger starten in einer schmalen Zone am Rand und ziehen
Inhalt nach innen; die darunterliegende Ebene wird als Vorschau sichtbar.

```
┌─────────────────────────────────────────┐
│▌ ←                                       │
│▌   Randzone (24px)                      │
│▌░░                                       │
│▌░░░  ►  Vorschau der vorigen Seite      │
│▌░░░░░                                    │
└─────────────────────────────────────────┘
```

## Phasen

| Phase | Beschreibung |
|-------|--------------|
| **Anfassen** | Rand erkannt, Vorschatten erscheint |
| **Ziehen** | Inhalt folgt den Fingern, darunterliegende Ebene wird sichtbar |
| **Abschluss** | Über Threshold: Ziel laden; darunter: zurückfedern |

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Shadow Preview** | Schattenskante zeigt Tiefe der darunterliegenden Ebene |
| **Parallax** | Beide Ebenen bewegen sich unterschiedlich schnell |
| **Highlight Edge** | Leuchtkante am Rand während des Wischens |
| **None** | Kein visuelles Signal, Übergang erst beim Loslassen |

## Kante

| Kante | Typischer Ablauf |
|-------|------------------|
| Links | Vorige Seite gleitet von links herein |
| Unten | Home-Fläche skaliert aus dem Inhalt heraus |
| Oben | Panel klappt aus der Statusleiste herunter |

## Dauer

- Interaktiv: folgt den Fingern, 100–400ms
- Abschluss-Animation: 200–350ms

## Unterschied zu Swipe

- Edge Swipe: Start am Rand, Navigationsebene, Vorschau der nächsten Ebene
- Swipe: Start im Inhalt, Aktion am Inhalt, keine Eben-Vorschau
