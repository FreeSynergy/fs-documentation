# List View - Erscheinungsbild

## Grundlayout
Vertikale Liste: ein Eintrag pro Zeile, volle Breite des Containers.

```
┌─────────────────────────────────────────┐
│ Element 1                               │
│ Element 2                               │
│ Element 3                               │
│ Element 4                               │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einfach** | nur Text, optional eine graue zweite Zeile |
| **icon** | Symbol links vor dem Text |
| **avatar** | Bild links, Text rechts daneben |
| **badge** | Status oder Zähler am Ende der Zeile |
| **aktion** | Knöpfe am Ende der Zeile, bei Hover sichtbar |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 200px | inline |
| medium | 300px | Standard |
| large | 400px | hervorgehoben |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | hell | Standard |
| **Hover** | heller | Hover-Zustand |
| **Active** | Primärfarbe | aktiver Zustand |
| **Disabled** | grau | deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | der Hintergrund ändert sich |
| `border` | der Rand leuchtet auf |

## Responsiv

- Die Liste ist immer volle Breite; die Anzahl der Spalten hängt nicht von der Größe ab, wohl aber
  die Aufteilung innerhalb einer Zeile: auf schmalen Bildschirmen rutscht der rechte Teil unter den Text.
- Zweitaktionen sind auf Touch-Geräten durch Wischen (`swipe`) erreichbar, nicht über kleine Knöpfe.
- Listen, die weitere Einträge nachladen, zeigen am Ende einen `skeleton`-Platzhalter; neue Einträge
  gleiten mit `stagger` hinein.

## Mit Icons

```
┌─────────────────────────────────────────┐
│ 📁 Datei 1                              │
│ 📁 Datei 2                              │
│ 📁 Datei 3                              │
└─────────────────────────────────────────┘
```
