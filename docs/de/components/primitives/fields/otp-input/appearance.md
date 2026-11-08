# OTP Input (Einmalcode) - Erscheinungsbild

## Grundlayout

```
┌───┬───┬───┬───┬───┬───┐
│ 4 │ 2 │ 9 │   │   │   │   ein Kästchen pro Zeichen, aktives Kästchen mit Ring
└───┴───┴───┴───┴───┴───┘
        Code abgelaufen?  [Neuen senden · 24 s]
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einzelboxen** | einzelne Kästchen mit Rahmen |
| **block** | ein Feld, Zeichen mit Buchstabenabstand |

## Größen

| Größe | Kästchen | Abstand |
|-------|----------|---------|
| `small` | 32 px | 4 px |
| `medium` | 44 px | 6 px |
| `large` | 56 px | 8 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | neutraler Rahmen, Feld leer |
| `active` | aktives Kästchen mit Primärring |
| `filled` | alle Kästchen gefüllt, der Prüfen-Button wird aktiv |
| `loading` | Prüfen-Button mit Spinner, Felder gesperrt |
| `error` | Rahmen in der Fehlerfarbe, kurzes Wackeln, dann zurückgesetzt |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `ring` | Primärring am aktiven Kästchen |
| `shake` | bei einem falschen Code, siehe [shake](../../../../interactions/animations/feedback/shake/) |

## Responsiv

- Die Kästchengröße schrumpft bis auf 32 px. Darunter wechselt die Komponente auf `block`.
- Der Hilfetext unter den Kästchen bricht um. Die Kästchen bleiben in einer Zeile.
