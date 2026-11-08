# Switch - Erscheinungsbild

## Grundlayout

Ein Switch ist ein Ein-/Aus-Schalter (Toggle).

## Varianten

### Standard (Rechteck)

```
┌─────────────────────────────────────────┐
│ [   EIN   ]                             │
│                                         │
└─────────────────────────────────────────┘
```

### Rund

```
┌─────────────────────────────────────────┐
│ (   EIN   )                             │
│                                         │
└─────────────────────────────────────────┘
```

### Pille

```
┌─────────────────────────────────────────┐
│  [ EIN ]                                │
│                                         │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 40px | inline |
| medium | 56px | Standard |
| large | 72px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **off** | grau | aus |
| **on** | Primärfarbe | an |
| **disabled** | grau | deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | der Schatten wird stärker |
| `border` | der Rand leuchtet auf |

## Responsiv

- Der Switch wird unterhalb von `small` (40 px) nicht kleiner; der Trefferbereich um ihn bleibt 44 px.
- In Listen und auf schmalen Bildschirmen steht der Switch rechtsbündig in einer eigenen Zeile,
  das Label bricht links darüber um.
- Auf Touch-Geräten lässt sich der Griff auch ziehen (`drag`); beim Loslassen springt er in die
  nähere Stellung.

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `slide-in` | der Griff wandert auf die andere Seite |
| `fade-in` | die Oberflächenfarbe wechselt sanft |

## Mit Beschriftung

```
┌─────────────────────────────────────────┐
│ Funktion aktivieren        [   EIN   ]  │
└─────────────────────────────────────────┘
```
