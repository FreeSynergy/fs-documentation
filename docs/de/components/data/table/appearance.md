# Table (Tabelle) - Aussehen

## Grundlayout
Eine Table ist eine tabellarische Darstellung mit Zeilen und Spalten.

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

| Variante | Aussehen |
|----------|----------|
| **einfach** | Kopfzeile, Zeilen, keine Steuerung |
| **daten** | Sortiersymbole in der Kopfzeile, Seitenzahlen darunter |
| **baum** | Einzug pro Ebene, Einklapp-Dreieck links |
| **inline-bearbeitung** | aktivierte Zelle zeigt Feld mit Rand, Rest bleibt ruhig |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 400px | Inline |
| Medium | 600px | Standard |
| Large | 800px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Header** | Hell | Header-Zeile |
| **Row** | Weiß/Alt | Zeilen |
| **Hover** | Heller | Hover-Zustand |
| **Active** | Primärfarbe | Aktive Zeile |
| **Disabled** | Grau | Deaktivierte Zeile |

## Hover- und Fokus-Effekte

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

## Reaktiv

- Die Tabelle füllt die Breite; reicht sie nicht, scrollt sie waagerecht (`swipe`) und die
  erste Spalte bleibt stehen.
- Unter `small` Bildschirmbreite werden die Aktionen pro Zeile hinter ein Menü gesetzt und die
  Kopfzeile bleibt beim vertikalen Scrollen sichtbar.
- Spaltenbreiten passen per `drag`; Zeilenhöhen wachsen nur, wenn Text umbricht, sonst bleiben
  sie auf einer Zeile (mindestens 44 px).
