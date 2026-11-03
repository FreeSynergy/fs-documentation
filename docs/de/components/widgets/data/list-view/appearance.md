# List View (Listenansicht) - Aussehen

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

| Variante | Aussehen |
|----------|----------|
| **einfach** | nur Text, optional graue Zweitzeile |
| **icon** | Symbol links vor dem Text |
| **avatar** | Bild links, Text rechts daneben |
| **badge** | Status oder Zähler am Zeilenende |
| **aktion** | Knöpfe am Zeilenende, bei Hover sichtbar |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Hover** | Heller | Hover-Zustand |
| **Active** | Primärfarbe | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `border` | Rand leuchtet auf |

## Reaktiv

- Die Liste ist immer vollbreit; die Spaltenanzahl ist nicht Größe-abhängig, sondern die
  innerzeilige Aufteilung: auf schmalen Bildschirmen rutscht der rechte Teil unter den Text.
- Sekundäraktionen werden auf Touch-Geräten durch Wischen (`swipe`) erreichbar, nicht durch
  kleine Knöpfe.
- Nachladende Listen zeigen am Ende einen `skeleton`-Platzhalter, neue Einträge gleiten mit
  `stagger` ein.

## With Icons

```
┌─────────────────────────────────────────┐
│ 📁 Datei 1                              │
│ 📁 Datei 2                              │
│ 📁 Datei 3                              │
└─────────────────────────────────────────┘
```
