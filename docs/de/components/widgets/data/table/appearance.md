# Table - Erscheinungsbild

## Grundlayout
Eine Tabelle ist eine tabellarische Darstellung mit Zeilen und Spalten.

```
┌─────────────────────────────────────────┐
│ ID │ Name │ Alter │ Aktion               │
├─────────────────────────────────────────┤
│ 1  │ John │ 25    │ [Bearbeiten] [Löschen]│
│ 2  │ Jane │ 30    │ [Bearbeiten] [Löschen]│
│ 3  │ Bob  │ 28    │ [Bearbeiten] [Löschen]│
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einfach** | Kopfzeile, Zeilen, keine Bedienelemente |
| **daten** | Sortierzeichen im Kopf, Seitenzahlen darunter |
| **baum** | eine Einrückung pro Ebene, Aufklapp-Dreieck links |
| **inline-bearbeitung** | die aktive Zelle zeigt ein Feld mit Rand, der Rest bleibt ruhig |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 400px | inline |
| medium | 600px | Standard |
| large | 800px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Header** | hell | Kopfzeile |
| **Row** | weiß/abwechselnd | Zeilen |
| **Hover** | heller | Hover-Zustand |
| **Active** | Primärfarbe | aktive Zeile |
| **Disabled** | grau | deaktivierte Zeile |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | der Hintergrund ändert sich |
| `border` | der Rand leuchtet auf |

## Responsiv

- Die Tabelle füllt die Breite; reicht sie nicht, scrollt sie horizontal (`swipe`) und
  die erste Spalte bleibt stehen.
- Unterhalb einer kleinen Bildschirmbreite (`small`) wandern die Aktionen pro Zeile hinter ein Menü,
  und die Kopfzeile bleibt beim vertikalen Scrollen sichtbar.
- Spaltenbreiten lassen sich per `drag` anpassen; Zeilen werden nur höher, wenn Text umbricht,
  sonst bleiben sie einzeilig (mindestens 44 px).

## Sortierung

```
┌─────────────────────────────────────────┐
│ ID ▼ │ Name ▲ │ Alter │ Aktion          │
├─────────────────────────────────────────┤
│ 1  │ John │ 25  │ [Bearbeiten] [Löschen]│
│ 2  │ Jane │ 30  │ [Bearbeiten] [Löschen]│
│ 3  │ Bob  │ 28  │ [Bearbeiten] [Löschen]│
└─────────────────────────────────────────┘
```
