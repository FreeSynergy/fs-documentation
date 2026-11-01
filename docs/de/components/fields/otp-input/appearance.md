# OTP Input (Einmalpasswort) - Aussehen

## Grundlayout

```
┌───┬───┬───┬───┬───┬───┐
│ 4 │ 2 │ 9 │   │   │   │   eine Box pro Zeichen, aktive Box mit Ring
└───┴───┴───┴───┴───┴───┘
        Code abgelaufen?  [Neuen senden · 24 s]
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einzelboxen** | getrennte Quadrate mit Rahmen |
| **block** | ein Feld, Zeichen mit Schriftabstand |

## Größen

| Größe | Box | Abstand |
|-------|-----|---------|
| `small` | 32 px | 4 px |
| `medium` | 44 px | 6 px |
| `large` | 56 px | 8 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Rahmen neutral, Feld leer |
| `active` | aktive Box mit Primärring |
| `filled` | alle Boxen gefüllt, Prüfbutton wird aktiv |
| `loading` | Prüfbutton mit Spinner, Felder gesperrt |
| `error` | Rahmen in Fehlerfarbe, kurzes Schütteln, danach leeren |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `ring` | Primärring auf der aktiven Box |
| `shake` | bei falschem Code, siehe [shake](../../../animations/feedback/shake/) |

## Reaktiv

- Boxgröße schrumpft bis 32 px; darunter wechselt die Komponente zu `block`.
- Der Hilfetext unter den Boxen bricht um, die Boxen bleiben einzeilig.
