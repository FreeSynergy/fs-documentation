# Button-Gruppe – Aussehen

## Grundlayout

Verbund (zwei Buttons teilen sich eine Kante):

```
┌────────────┬────────────┐
│    Save    │   Cancel   │
└────────────┴────────────┘
```

Segmentierte Auswahl (genau ein Segment aktiv):

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

| Variante | Aussehen |
|----------|----------|
| **verbund** | die inneren Seiten sind nicht abgerundet, nur die Außenseite ist abgerundet |
| **segment** | ein gemeinsamer Rahmen, Trennlinien zwischen den Segmenten als dünne Linien |
| **split** | wie `verbund`, das letzte Element ist deutlich schmaler (nur Pfeil) |

## Größen

Die Größentabelle von [Button](../button/) gilt für jedes Element der Gruppe;
Elemente unterschiedlicher Größe dürfen nicht in derselben Gruppe stehen.

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | wie ein einzelner Button, innere Seiten gemeinsam |
| `hover` | Ton eine Stufe dunkler, wie bei einem Button |
| `active` (Segment ausgewählt) | farbige Fläche, Text in der Primärfarbe |
| `focus` | Ring um das ganze Element, nicht um die Gruppe |
| `disabled` | 40 % Deckkraft des Elements |

## Effekte bei Hover und Fokus

| Effekt | Beschreibung |
|--------|--------------|
| `tone` | der Flächenton ändert sich wie bei einem einzelnen Button |
| `ring` | Fokusring am Element; der Gruppenrahmen bleibt unverändert |
| `indicator` | Auswahl wird durch die Fläche gezeigt, nicht nur durch Farbe |

## Responsiv

- Zu breite Gruppen werden auf schmalen Bildschirmen untereinander gestapelt.
- Beschriftungen dürfen nicht umbrechen; wenn der Platz knapp wird, auf Icons umschalten.
