# Bottom Navigation - Erscheinungsbild

## Grundlayout

Die Bottom Navigation ist eine Navigation am unteren Bildschirmrand, typisch für
Mobile-first-Design.

## Varianten

### Aktives Icon (der aktive Eintrag ist hervorgehoben)

```
┌─────────────────────────────────────────┐
│   🏠    📩   📅   👥   ⚙️              │
│   Start Post Kal. Kontakt Einst.        │
└─────────────────────────────────────────┘
```

### Textbeschriftung (mit Text)

```
┌─────────────────────────────────────────┐
│ Start │ Post │ Kal. │ Kont. │ Einst.    │
└─────────────────────────────────────────┘
```

### Nur Icon (nur Symbole)

```
┌─────────────────────────────────────────┐
│ 🏠  📩  📅  👥  ⚙️                     │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Höhe | Icon-Größe | Verwendung |
|-------|------|------------|------------|
| Small | 48px | 20px | wenige Einträge |
| Medium | 56px | 24px | Standard |
| Large | 64px | 28px | viele Einträge |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Active** | Primärfarbe | aktiver Eintrag |
| **Inactive** | grau | inaktive Einträge |
| **Hover** | heller | Hover-Zustand |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | die Farbe ändert sich |
| `scale` | Vergrößerung |
| `shadow` | Schatten |

## Responsiv

- Die Leiste ist immer volle Breite und bleibt am unteren Rand; ihr Inhalt verteilt sich
  gleichmäßig auf die Einträge.
- Reicht der Platz für Beschriftungen nicht, fällt sie auf `nur Icon` zurück, und der Name
  erscheint erst als kurzer Text, nachdem der Eintrag gewählt wurde.
- Auf großen Bildschirmen wechselt die Anwendung meist zu [sidebar](../sidebar/) oder
  [toolbar](../toolbar/); die Leiste bleibt, wenn die Anwendung mobil bleibt, sonst entfällt sie.

## Maximal 5 Einträge

```
┌─────────────────────────────────────────┐
│   🏠    📩   📅   👥   ⚙️              │
└─────────────────────────────────────────┘
```

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `fade-in` | die Beschriftung blendet ein |
| `scale-in` | das aktive Symbol wird größer |
| `slide-in` | die Markierung wandert zum aktiven Eintrag |
