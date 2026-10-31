# Table (Tabelle) - Aussehen

## Grundlayout

Eine Table ist eine tabellarische Darstellung mit Zeilen und Spalten.

## Layout

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ Aktion               │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ [Bearbeiten] [Lösch] │
│ 2  │ Jane │ 30    │ [Bearbeiten] [Lösch] │
│ 3  │ Bob  │ 28    │ [Bearbeiten] [Lösch] │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Simple** | Nur Darstellung |
| **Data** | Mit Sortierung, Filterung |
| **Tree** | Hierarchische Zeilen |
| **Inline Edit** | Bearbeitung in der Tabelle |

## Größe-Varianten

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 400px | Inline |
| Medium | 600px | Standard |
| Large | 800px | Featured |
| Full | 100% | Volle Breite |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Header** | Hell | Header-Zeile |
| **Row** | Weiß/Alt | Zeilen |
| **Hover** | Heller | Hover-Zustand |
| **Active** | Primärfarbe | Aktive Zeile |
| **Disabled** | Grau | Deaktivierte Zeile |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `border` | Rand leuchtet auf |

## Sortierung

```
┌─────────────────────────────────────────┐
│ ID ▼ │ Name ▲ │ Alter │ Aktion            │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ [Bearbeiten] [Lösch] │
│ 2  │ Jane │ 30    │ [Bearbeiten] [Lösch] │
│ 3  │ Bob  │ 28    │ [Bearbeiten] [Lösch] │
└─────────────────────────────────────────┘
```
