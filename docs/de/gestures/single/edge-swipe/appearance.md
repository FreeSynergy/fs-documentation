# Edge Swipe - Aussehen

## Grundlayout

Der Finger startet in einer schmalen Zone am Rand und zieht Inhalt nach innen;
die darunterliegende Ebene wird als Vorschau sichtbar.

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
| **Ziehen** | Inhalt folgt dem Finger, darunterliegende Ebene wird sichtbar |
| **Abschluss** | Über Threshold: Ziel laden; darunter: zurückfedern |

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Shadow Preview** | Schattenskante zeigt Tiefe der darunterliegenden Ebene |
| **Parallax** | Beide Ebenen bewegen sich unterschiedlich schnell |
| **Highlight Edge** | Leuchtkante am Rand während des Wischens |
| **None** | Kein visuelles Signal, Übergand erst beim Loslassen |

## Kante

| Kante | Typischer Ablauf |
|-------|------------------|
| Links | Vorige Seite gleitet von links herein |
| Unten | Home-Fläche skaliert aus dem Inhalt heraus |
| Oben | Panel klappt aus der Statusleiste herunter |

## Dauer

- Interaktiv: folgt dem Finger, 100–400ms
- Abschluss-Animation: 200–350ms

## Unterschied zu Swipe

- Edge Swipe: Start am Rand, Navigationsebene, Vorschau der nächsten Ebene
- Swipe: Start im Inhalt, Aktion am Inhalt, keine Eben-Vorschau
