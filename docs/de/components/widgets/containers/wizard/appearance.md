# Wizard - Erscheinungsbild

## Grundlayout
Ein Wizard ist ein schrittweises Formular für komplexe Aufgaben.

```
┌─────────────────────────────────────────┐
│ Schritt 1 von 5                         │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt des Schritts                   │
│                                         │
├─────────────────────────────────────────┤
│ [Zurück]               [Weiter →]       │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Horizontal** | waagerechte Schrittanzeige |
| **Vertical** | senkrechte Schrittanzeige |
| **Stepper** | mit einer visuellen Fortschrittsanzeige |
| **schrittanzeige** | nur die Schritte anzeigen, ohne Führung |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 300px | kleine Wizards |
| medium | 500px | Standard |
| large | 700px | große Wizards |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active step** | Primärfarbe | aktueller Schritt |
| **Completed step** | grün | abgeschlossener Schritt |
| **Pending step** | grau | ausstehender Schritt |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | die Farbe ändert sich |
| `border-bottom` | eine Unterstreichung erscheint |

## Responsiv

Der Wechsel zwischen Schritten ist eine Schiebebewegung: vorwärts von rechts (`slide-in`),
rückwärts gespiegelt; die Schrittanzeige folgt mit `progress`. Auf einer schmalen Fläche wird die
senkrechte Anzeige zu einer Zeile aus Zähler und Leiste, der Inhalt bleibt einspaltig.

```css
.wizard-step        { transition: transform 200ms, opacity 200ms; }
.wizard-step--in-next { transform: translateX(24px); opacity: 0; }
.wizard-step--in-prev { transform: translateX(-24px); opacity: 0; }

@media (max-width: 600px) {
  .wizard--vertical .step-indicator { flex-direction: row; }  /* Zähler + Leiste */
}
```
