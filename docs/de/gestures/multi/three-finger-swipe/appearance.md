# Three-Finger Swipe - Aussehen

## Grundlayout

Drei Finger wischen gemeinsam; die Ebene wechselt mit Karten-Vorschau der
Nachbarseiten/-Apps.

```
┌─────────────────────────────────────────┐
│   ●   ●   ●                             │
│    ╲  │  ╱     → Bewegung gemeinsam     │
│     ▼ ▼ ▼                               │
│  ┌────┐ ┌────┐ ┌────┐                   │
│  │App1│▶│App2│ │App3│  ← Kartenwechsel  │
│  └────┘ └────┘ └────┘                   │
└─────────────────────────────────────────┘
```

## Phasen

| Phase | Beschreibung |
|-------|--------------|
| **Anfassen** | Drei Finger erkannt, Vorschau-Karten tauchen auf |
| **Wischen** | Karten bewegen sich mit dem Finger (interaktiv) |
| **Umschalten** | Über Threshold: Ziel wird aktiv, sonst zurückfedern |

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Card Preview** | Nachbar-Ebenen als Karten links/rechts |
| **Dimming** | Aktuelle Ebene dunkelt beim Wechsel ab |
| **Haptic** | Vibration am Umschaltpunkt |

## Dauer

- Interaktiv: folgt dem Finger, 150–500ms
- Umschalt-Animation: 250–400ms

## Unterschied zu Swipe

- Swipe: Inhalt innerhalb der App, ein Finger
- Three-Finger Swipe: App-/Workspace-Ebene, drei Finger, Karten-Vorschau
