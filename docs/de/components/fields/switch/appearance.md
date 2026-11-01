# Switch - Aussehen

## Grundlayout

Ein Switch ist ein Ein/Aus-Schalter (Toggle).

## Varianten

### Standard (Rechteck)

```
┌─────────────────────────────────────────┐
│ [   ON   ]                              │
│                                         │
└─────────────────────────────────────────┘
```

### Round (Rund)

```
┌─────────────────────────────────────────┐
│ (   ON   )                              │
│                                         │
└─────────────────────────────────────────┘
```

### Pill (Pillenform)

```
┌─────────────────────────────────────────┐
│  [ ON ]                                 │
│                                         │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 40px | Inline |
| Medium | 56px | Standard |
| Large | 72px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Off** | Grau | Aus |
| **On** | Primärfarbe | Ein |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Vergrößerung |
| `shadow` | Schatten stärker |
| `border` | Rand leuchtet auf |

## Reaktiv

- Der Schalter skaliert nicht unter `small` (40 px); die Trefferfläche rundherum bleibt 44 px.
- In Listen und auf schmalen Bildschirmen steht der Schalter rechtsbündig auf eigener Zeile,
  das Label bricht links darüber um.
- Auf Touch-Geräten darf der Knopf auch geschoben werden (`drag`); loslassen schaltet in die
  nächstliegende Lage.

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `slide-in` | Knopf wandert zur anderen Seite |
| `fade-in` | Flächenfarbe wechselt weich |

## With Labels

```
┌─────────────────────────────────────────┐
│ Feature aktivieren        [   ON   ]    │
└─────────────────────────────────────────┘
```
