# Toolbar - Erscheinungsbild

## Grundaufbau

Eine Toolbar ist eine Reihe von Schaltflächen/Icons für häufige Aktionen.

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **standard** | einzeilige Leiste mit Icons |
| **kontext** | die Leiste tauscht ihre Schaltflächen, wenn sich die Auswahl ändert |
| **ribbon** | zwei oder drei Zeilen mit Gruppenüberschriften |

### Waagerecht (standard)
```
┌─────────────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]                  │
└─────────────────────────────────────────────────────┘
```
### Schwebend
```
                    ┌─────────────────────────────┐
                    │ [📄] [✏️] [✂️] [✔️]        │
                    └─────────────────────────────┘
```
### Seitlich (links/rechts)
```
┌─────┬─────────────────────────────────────────────┐
│     │ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]         │
│     │                                             │
│     │                                             │
└─────┴─────────────────────────────────────────────┘
```

## Größen

| Größe | Icongröße | Schaltflächengröße | Verwendung |
|------|-----------|-------------|-----|
| Klein | 16px | 32px | in Textzeilen |
| Mittel | 24px | 48px | Standard |
| Groß | 32px | 64px | hervorgehoben |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|-------|--------|-------------|
| **Primär** | Primärfarbe | Hauptaktion |
| **Sekundär** | Sekundärfarbe | Nebenaktion |
| **Gefahr** | Rot | gefährliche Aktion |
| **Deaktiviert** | Grau | deaktivierte Aktion |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| `color` | die Farbe ändert sich |
| `background` | der Hintergrund ändert sich |
| `scale` | leichte Vergrößerung |
| `shadow` | ein Schatten erscheint |

## Responsives Verhalten

- Die Leiste hat volle Breite und bleibt beim Scrollen oben stehen (`geklebt`). Die Gruppe
  rechts rutscht zuerst weg.
- Passt die Zeile nicht mehr, wandern die übrigen Schaltflächen hinter ein Aufklappfeld `+`,
  das die Gruppen behält.
- Auf Touchgeräten sind die Schaltflächen mindestens 44 px groß. Auf großen Bildschirmen kann
  `Icon und Text` angezeigt werden, auf kleinen nur das Icon.

## Beschriftung der Schaltflächen

| Form | Beschreibung |
|------|-------------|
| **nur Icon** | Standard, mit Tooltip |
| **nur Text** | wenn kein eindeutiges Icon existiert |
| **Icon und Text** | neue oder mehrdeutige Aktionen |

## Trenner

```
┌─────────────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] ───── [✔️] [❌] [🔍] [⚙️]            │
└─────────────────────────────────────────────────────┘
```
