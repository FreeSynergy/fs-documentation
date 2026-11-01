# Accordion - Aussehen

## Grundlayout
Ein Accordion ist ein Stapel von Kopfzeilen, die Inhalte ein-/ausklappen können.

```
┌─────────────────────────────────────────┐
│ ▶ Kopfzeile 1                           │
├─────────────────────────────────────────┤
│   Inhalt 1                              │
├─────────────────────────────────────────┤
│ ▶ Kopfzeile 2                           │
├─────────────────────────────────────────┤
│   Inhalt 2                              │
├─────────────────────────────────────────┤
│ ▶ Kopfzeile 3                           │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **standard** | Köpfe untereinander, einer offen |
| **mehrere** | mehrere Inhalte gleichzeitig sichtbar |
| **einzel** | ein einzelner Kopf ohne Gruppierung |

## Größen

| Größe | Schriftgröße | Verwendung |
|-------|-------------|------------|
| Small | 12px | Inline |
| Medium | 14px | Standard |
| Large | 16px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active Header** | Primärfarbe | Aktiver Header |
| **Inactive Header** | Grau | Inaktiver Header |
| **Content** | Dunkel | Inhalt |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `background` | Hintergrund ändert sich |
| `border-bottom` | Unterstrich erscheint |

## Reaktiv

- Der Akkordeonstapel ist immer vollbreit; die Kopfzeile wächst mit dem Text,
  der Inhaltbereich ist höchstens so hoch wie der Viewport.
- Auf schmalen Bildschirmen rutscht das Pfeilsymbol nach links und der Titel bleibt
  linksbündig; die Kopfzeile wird mindestens 44 px hoch.
- Beim Schließen rücken die folgenden Köpfe ohne Sprung nach, die Scrollposition des
  angeklickten Kopfes bleibt erhalten.

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `expand` | Inhalt klappt auf |
| `collapse` | Inhalt klappt zu |
| `fade-in` | Inhalt blendet ein |
| `rotate` | Pfeil dreht um 90 Grad |
