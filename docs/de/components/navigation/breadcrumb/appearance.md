# Breadcrumb - Aussehen

## Grundlayout

Breadcrumbs zeigen den Pfad an (Home > Wiki > Seite > Unterpunkt).

## Layout

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

## Größe-Varianten

| Größe | Schriftgröße | Verwendung |
|-------|-------------|------------|
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Home** | Primärfarbe | Start |
| **Active** | Dunkel | Aktueller Pfad |
| **Inactive** | Grau | Nicht aktuelle Pfade |
| **Hover** | Heller | Hover-Zustand |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `underline` | Unterstrich erscheint |
| `opacity` | Deckkraft ändert sich |

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
