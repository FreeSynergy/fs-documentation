# Breadcrumb - Aussehen

## Grundlayout
Breadcrumbs zeigen den Pfad an (Home > Wiki > Seite > Unterpunkt).

```
┌─────────────────────────────────────────┐
│ Home > Wiki > Seite > Unterpunkt        │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Default** | Mit Pfeil-Separator (>) |
| **Arrow** | Mit Pfeil (→) |
| **Slash** | Mit Schrägstrich (/) |
| **Chevron** | Mit spitzen Klammern (›) |

## Größen

| Größe | Schriftgröße | Verwendung |
|-------|-------------|------------|
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Home** | Primärfarbe | Start |
| **Active** | Dunkel | Aktueller Pfad |
| **Inactive** | Grau | Nicht aktuelle Pfade |
| **Hover** | Heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `underline` | Unterstrich erscheint |
| `opacity` | Deckkraft ändert sich |

## Reaktiv

- Der letzte Punkt wird zuerst gekürzt, dann die Mitte: Wurzel und aktueller Ort bleiben
  immer sichtbar, dazwischen erscheint `…` als Aufklappmenü.
- Auf schmalen Bildschirmen reicht oft nur `zurueck` — ein Knopf mit dem vorherigen Namen.
- Der Pfad bricht nicht um; er bleibt einzeilig und wächst mit der verfügbaren Breite.

## With Icons

```
┌─────────────────────────────────────────┐
│ 🏠 Home > 📚 Wiki > 📄 Seite > 📝 Text │
└─────────────────────────────────────────┘
```

## Collapsed Breadcrumbs (bei wenig Platz)

```
┌─────────────────────────────────────────┐
│ Home > ... > Seite > Unterpunkt         │
└─────────────────────────────────────────┘
```
