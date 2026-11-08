# Button-Gruppe – Erscheinungsbild

## Grundlayout

Verbund (zwei Buttons teilen sich eine Kante):

```
┌────────────┬────────────┐
│    Save    │   Cancel   │
└────────────┴────────────┘
```

Segmentierte Steuerung (genau ein Segment aktiv):

```
┌──────────┬──────────┬──────────┐
│  List    │  Grid    │ Timeline │
└──────────┴──────────┴──────────┘
   aktiv = farbige Fläche
```

Split-Button:

```
┌──────────────────┬─────┐
│  Save            │  ▾  │
└──────────────────┴─────┘
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **verbund** | innen liegende Seiten haben keine Rundung, nur die Außenseite ist abgerundet |
| **segment** | ein gemeinsamer Rahmen, Segmenttrenner als dünne Linien |
| **split** | wie `verbund`, das letzte Element ist deutlich schmaler (nur Pfeil) |

## Größen

Die Größentabelle von [Button](../button/) gilt für jedes Gruppenelement;
Elemente unterschiedlicher Größe dürfen nicht in derselben Gruppe stehen.

## Farben und Zustände

| Zustand | Erscheinungsbild |
|-------|------------|
| `default` | wie ein einzelner Button, innere Seiten gemeinsam genutzt |
| `hover` | Ton eine Stufe dunkler, wie bei einem Button |
| `active` (Segment gewählt) | farbige Fläche, Text in der Primärfarbe |
| `focus` | Ring um das ganze Element, nicht um die Gruppe |
| `disabled` | 40 % Deckkraft des Elements |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `tone` | der Flächenton ändert sich wie bei einem einzelnen Button |
| `ring` | Fokusring am Element; der Gruppenrand bleibt unverändert |
| `indicator` | Auswahl wird durch die Fläche gezeigt, nicht nur durch Farbe |

## Responsiv

- Zu breite Gruppen werden auf schmalen Bildschirmen untereinander gestapelt.
- Beschriftungen dürfen nicht umbrechen; wenn der Platz knapp ist, auf Icons umschalten.
