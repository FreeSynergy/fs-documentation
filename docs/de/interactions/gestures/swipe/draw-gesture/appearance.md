# Draw Gesture - Aussehen

## Grundlayout

Über der Fläche liegt eine transparente Zeichenebene; der Strich wird live
gezeichnet, die erkannter Form folgt eine Bestätigung.

```
┌─────────────────────────────────────────┐
│      ╲                                   │
│       ╲   (gezeichnetes "V")             │
│        ╲ ╱                               │
│         ▼                                │
│   ┌──────────────┐                       │
│   │ ✓ Zurück      │  ← Bestätigung       │
│   └──────────────┘                       │
└─────────────────────────────────────────┘
```

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Trail** | Strich in Akzentfarbe folgt dem Finger/Stift |
| **Shape Snap** | Erkannte Form wird als saubere Vorlage eingeblendet |
| **Badge** | Kurzer Bestätigungs-Chip mit Aktionsnamen |
| **None** | Unsichtbar zeichnen, Aktion erfolgt direkt |

## Strich-Stärken

| Stärke | Verwendung |
|--------|------------|
| 2–3px | Gesten über Inhalt, dezent |
| 4–6px | Zeichen-Apps, Marker |
| Druckabhängig | Stift mit Pressure-Support |

## Dauer

- Erkennungs-Badge: 600–1000ms sichtbar
- Form-Einrasten: 150–250ms

## Unterschied zu Scribble

- Draw Gesture: Form/Buchstabe = Befehl, kein Text-Output
- Scribble: Handschrift = Text-Input, Feld füllt sich
