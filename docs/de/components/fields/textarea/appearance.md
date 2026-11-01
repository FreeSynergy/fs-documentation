# Textarea (Mehrzeiliges Textfeld) - Aussehen

## Grundlayout
Ein Textarea ist ein mehrzeiliges Eingabefeld für Text.

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

## Varianten

| Variante | Aussehen |
|----------|----------|
| **fix** | Rahmen fester Höhe, innen Scrollbalken |
| **mitwachsend** | Rahmen wächst zeilenweise, Obergrenze als Scrollbereich |
| **chat** | randlose Zeile über der Leiste, wächst bis drei Zeilen |

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Small | 200x100px | Inline |
| Medium | 300x150px | Standard |
| Large | 500x200px | Featured |
| Full | 100% | Volle Breite |

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

## Reaktiv

- Das Feld füllt die Breite des Containers; die Höhe bleibt in Prozent des Viewports begrenzt
  (maximal 60 %), damit darunter liegende Bedienelemente erreichbar bleiben.
- Auf schmalen Bildschirmen entfällt der Größen-Ziehgriff (`drag`), die Höhe ergibt sich aus
  dem Inhalt bis zur Obergrenze.
- Beim Senden im Chat-Modus fällt das Feld animiert auf eine Zeile zurück (`collapse`-Übergang
  über `expand`).
