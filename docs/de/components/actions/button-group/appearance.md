# Button Group (Schaltflächengruppe) - Aussehen

## Grundlayout

Verbund (zwei Buttons teilen sich eine Kante):

```
┌────────────┬────────────┐
│  Speichern │  Abbrechen │
└────────────┴────────────┘
```

Segmented Control (genau ein Segment aktiv):

```
┌──────────┬──────────┬──────────┐
│  Liste   │  Raster  │  Zeitleiste
└──────────┴──────────┴──────────┘
   aktiv = eingefärbte Fläche
```

Split-Button:

```
┌──────────────────┬─────┐
│  Speichern       │  ▾  │
└──────────────────┴─────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **verbund** | Innenseiten ohne Rundung, nur außen abgerundet |
| **segment** | ein gemeinsamer Rahmen, Segmenttrenner als feine Linien |
| **split** | wie `verbund`, letztes Element deutlich schmaler (nur Pfeil) |

## Größen

Die Größentabelle von [Button](../button/) gilt für alle Gruppenelemente;
Elemente unterschiedlicher Größe dürfen nicht in einer Gruppe stehen.

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | wie Einzelbutton, Innenseiten geteilt |
| `hover` | Ton eine Stufe dunkler, wie Button |
| `active` (Segment ausgewählt) | eingefärbte Fläche, Text in Primärfarbe |
| `focus` | Ring um das gesamte Element, nicht um die Gruppe |
| `disabled` | 40 % Deckkraft des Elements |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tone` | Flächenton wechselt wie beim Einzelbutton |
| `ring` | Fokusring am Element; Gruppenrand bleibt unverändert |
| `indicator` | Auswahl durch Fläche, nicht nur durch Farbe |

## Reaktiv

- Zu breite Gruppen werden auf schmalen Bildschirmen vertikal gestapelt.
- Beschriftungen dürfen nicht umbrechen; bei Platzmangel auf Icons umstellen.
