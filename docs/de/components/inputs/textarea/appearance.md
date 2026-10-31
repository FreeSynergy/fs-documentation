# Textarea (Mehrzeiliges Textfeld) - Aussehen

## Grundlayout

Ein Textarea ist ein mehrzeiliges Eingabefeld für Text.

## Layout

```
┌─────────────────────────────────────────┐
│ Nachricht                               │
├─────────────────────────────────────────┤
│                                         │
│  Dies ist ein Text...                   │
│  Mehrzeiliger Text                      │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

## Größe-Varianten

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Small | 200x100px | Inline |
| Medium | 300x150px | Standard |
| Large | 500x200px | Featured |
| Full | 100% | Volle Breite |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Auto-resize

```
┌─────────────────────────────────────────┐
│ Nachricht                               │
├─────────────────────────────────────────┤
│  Dies ist ein Text...                   │
│  Mehrzeiliger Text                      │
│  Neuer Text                             │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Validation States

| State | Beschreibung |
|-------|--------------|
| **Valid** | Grün |
| **Invalid** | Rot |
| **Warning** | Orange |
