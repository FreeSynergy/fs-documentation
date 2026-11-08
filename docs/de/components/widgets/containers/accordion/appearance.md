# Accordion - Erscheinungsbild

## Grundlayout
Ein Accordion ist ein Stapel von Kopfzeilen, die Inhalte ein- und ausklappen.

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

| Variante | Erscheinungsbild |
|----------|------------------|
| **standard** | Kopfzeilen untereinander, eine davon offen |
| **mehrere** | mehrere Inhalte gleichzeitig sichtbar |
| **einzel** | eine einzelne Kopfzeile ohne Gruppierung |

## Größen

| Größe | Schriftgröße | Verwendung |
|-------|--------------|------------|
| small | 12px | inline |
| medium | 14px | Standard |
| large | 16px | hervorgehoben |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **aktive Kopfzeile** | Primärfarbe | aktive Kopfzeile |
| **inaktive Kopfzeile** | grau | inaktive Kopfzeile |
| **Inhalt** | dunkel | Inhalt |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | die Farbe ändert sich |
| `background` | der Hintergrund ändert sich |
| `border-bottom` | eine Unterstreichung erscheint |

## Responsiv

- Der Accordion-Stapel ist immer voll breit. Die Kopfzeile wächst mit dem Text,
  der Inhaltsbereich ist höchstens so hoch wie der Viewport.
- Auf schmalen Bildschirmen rutscht das Pfeilsymbol nach links, der Titel bleibt
  linksbündig. Die Kopfzeile ist mindestens 44 px hoch.
- Beim Schließen rücken die folgenden Kopfzeilen ohne Sprung nach oben. Die Scrollposition
  der angeklickten Kopfzeile bleibt erhalten.

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `expand` | der Inhalt klappt auf |
| `collapse` | der Inhalt klappt zu |
| `fade-in` | der Inhalt blendet ein |
| `rotate` | der Pfeil dreht sich um 90 Grad |
