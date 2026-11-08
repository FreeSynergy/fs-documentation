# Combobox – Erscheinungsbild

## Grundlayout
Eine Combobox ist ein Textfeld plus eine Auswahlliste.

```
┌─────────────────────────────────────────┐
│ Land                                    │
├─────────────────────────────────────────┤
│  Deutschland ▼                          │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **einzeln** | Feld mit Pfeil, die Vorschlagsliste darunter |
| **freitext** | wie `einzeln`, aber ohne erzwungene Auswahl; der Cursor steht im Feld |
| **mehrfach** | bereits gewählte Werte als Tags im Feld, die Liste bleibt offen |

## Größen

| Größe | Höhe | Verwendung |
|------|--------|-----|
| small | 32px | im Textfluss |
| medium | 48px | Standard |
| large | 64px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|--------|-------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **active** | dunkel | aktiver Zustand |
| **disabled** | grau | deaktiviert |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `border` | der Rahmen leuchtet auf |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Die Vorschlagsliste ist höchstens `medium` hoch (8 Zeilen) und scrollt sonst;
  `swipe` bewegt sie auf Touchgeräten.
- Passt die Liste nicht unter das Feld, öffnet sie sich nach oben.
- Auf schmalen Bildschirmen wird die Liste über das Feld in voller Breite gerendert; die Ergebniszeilen
  bleiben mindestens 44 px hoch.

## Auswahlliste

```
┌─────────────────────────────────────────┐
│ Land                                    │
├─────────────────────────────────────────┤
│  Deutschland ▼                          │
├─────────────────────────────────────────┤
│  Österreich                             │
│  Schweiz                                │
│  +                                      │
└─────────────────────────────────────────┘
```

## Autovervollständigung

```
┌─────────────────────────────────────────┐
│ Land                                    │
├─────────────────────────────────────────┤
│  Deut ▼                                 │
├─────────────────────────────────────────┤
│  Deutschland                            │
│  Germaneness                            │
│  +                                      │
└─────────────────────────────────────────┘
```
