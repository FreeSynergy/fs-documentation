# Combobox - Aussehen

## Grundlayout
Ein Combobox ist ein Textfeld + Dropdown.

```
┌─────────────────────────────────────────┐
│ Land                                    │
├─────────────────────────────────────────┤
│  Deutschland ▼                          │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einzeln** | Feld mit Pfeil, darunter die Vorschlagsliste |
| **freitext** | wie `einzeln`, aber ohne Auswahlzwang; Cursor steht im Feld |
| **mehrfach** | bereits gewählte Werte als Tags im Feld, Liste bleibt stehen |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 32px | Inline |
| Medium | 48px | Standard |
| Large | 64px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Dropdown

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

## Auto-Complete

```
┌─────────────────────────────────────────┐
│ Land                                    │
├─────────────────────────────────────────┤
│  Deutschl ▼                             │
├─────────────────────────────────────────┤
│  Deutschland                            │
│  Deutschlandschaft                      │
│  +                                      │
└─────────────────────────────────────────┘
```

## Reaktiv

- Die Vorschlagsliste ist maximal `medium` hoch (8 Zeilen) und scrollt sonst;
  `swipe` bewegt sie auf Touch-Geräten.
- Passt die Liste nicht unter das Feld, öffnet sie sich nach oben.
- Auf schmalen Bildschirmen wird die Liste vollbreit über dem Feld gerendert, die
  Trefferzeilen bleiben mindestens 44 px hoch.
