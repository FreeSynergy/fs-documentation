# Slider - Erscheinungsbild

## Grundlayout
Ein Slider ist ein Wertebereich mit einem verschiebbaren Regler.

```
┌─────────────────────────────────────────┐
│ Lautstärke                              │
├─────────────────────────────────────────┤
│ 0% [●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━] 100%│
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einfach** | ein Griff, Füllfläche links |
| **bereich** | zwei Griffe, der Abschnitt dazwischen ist gefüllt |

Vertikale Slider sind keine eigene Variante, sondern `orientation = vertikal`.

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | inline |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **track** | grau | Farbe der Leiste |
| **filled** | Primärfarbe | Farbe des gefüllten Teils |
| **thumb** | Primärfarbe | Farbe des Griffs |
| **disabled** | grau | deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Die Leiste füllt die verfügbare Breite (`full` in Toolbars), die Griffe bleiben
  16 px (Desktop) bzw. 24 px (Touch) groß; der Trefferbereich um den Griff bleibt 44 px.
- Auf schmalen Bildschirmen rutschen Wert und Skalenenden über oder unter die Leiste,
  nicht daneben.
- Ein Tipp auf die Leiste springt zur getroffenen Stelle, der Griff folgt mit `elastic`.

## Mit Beschriftung

```
┌─────────────────────────────────────────┐
│ 10                     [●━━━━━━━━━━]    │
│     50                  100             │
└─────────────────────────────────────────┘
```

## Vertikaler Slider

```
┌─────────────────────────────────────────┐
│ 100                                     │
│   ●                                     │
│  75                                     │
│  50                                     │
│  25                                     │
│   0                                     │
└─────────────────────────────────────────┘
```
