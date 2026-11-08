# Textarea - Erscheinungsbild

## Grundlayout
Ein Textarea ist ein mehrzeiliges Eingabefeld für Text.

```
┌─────────────────────────────────────────┐
│ Nachricht                               │
├─────────────────────────────────────────┤
│                                         │
│  Das ist ein Text...                    │
│  Mehrzeiliger Text                      │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **fix** | Rahmen mit fester Höhe, innen ein Scrollbalken |
| **mitwachsend** | der Rahmen wächst Zeile für Zeile, die Obergrenze wird zum Scrollbereich |
| **chat** | rahmenlose Zeile über der Leiste, wächst bis zu drei Zeilen |

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| small | 200x100px | inline |
| medium | 300x150px | Standard |
| large | 500x200px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **active** | dunkel | aktiver Zustand |
| **disabled** | grau | deaktiviert |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | der Rahmen leuchtet auf |
| `shadow` | der Schatten wird stärker |

## Responsiv

- Das Feld füllt die Breite des Containers. Die Höhe bleibt als Prozentwert der
  Viewport-Höhe begrenzt (höchstens 60 %), damit Bedienelemente darunter erreichbar bleiben.
- Auf schmalen Bildschirmen entfällt der Griff zum Vergrößern (`drag`). Die Höhe folgt
  dem Inhalt bis zur Obergrenze.
- Beim Senden im Chat-Modus schrumpft das Feld animiert auf eine Zeile zurück
  (Übergang `collapse` über `expand`).

## Automatische Größenanpassung

```
┌─────────────────────────────────────────┐
│ Nachricht                               │
├─────────────────────────────────────────┤
│  Das ist ein Text...                    │
│  Mehrzeiliger Text                      │
│  Neuer Text                             │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
└─────────────────────────────────────────┘
```

## Validierungszustände

| Zustand | Beschreibung |
|---------|--------------|
| **valid** | grün |
| **invalid** | rot |
| **warning** | orange |
