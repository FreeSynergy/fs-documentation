# Message List (Nachrichtenliste) - Aussehen

## Grundlayout

```
┌─────────────────────────────────────────┐
│ ──────────── Yesterday ──────────────── │
│ ┌──────────────┐                        │
│ │ Hi!          │                        │
│ └──────────────┘                        │
│ ─────────── 2 unread ────────────────── │
│                        ┌──────────────┐ │
│                        │ Hello    ✓✓  │ │
│                        └──────────────┘ │
│ Anna is typing …                        │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|---|---|
| **chat** | Blasen links/rechts nach Absender, unten verankert |
| **thread** | schmale Spalte, Antwortkontext oben |
| **mail** | eine kompakte Zeile pro Mail ⚠️ |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `small` | 200 px | in einem anderen Programm eingebettet |
| `medium` | 400 px | Standard |
| `full` | 100% | Hauptbereich des Messengers |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| Standard | Oberfläche des Themes |
| Trenner | gedämpfte Linie mit zentriertem Text |
| Grenze „ungelesen“ | Akzentlinie |
| Leer | [empty-state](../../../primitives/feedback/empty-state/) |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `background` | Zeilenhervorhebung (nur wenn die Zeile auswählbar ist) |
| – | Aktionen zeigt die Blase, Gesten das Frontend |

## Reaktiv

- Blasen nutzen auf schmalen Bildschirmen höchstens 80 % der Breite.
- Ältere Nachrichten laden oben hinter einem `skeleton`-Platzhalter.
