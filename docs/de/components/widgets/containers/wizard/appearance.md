# Wizard - Aussehen

## Grundlayout
Ein Wizard ist ein schritt-für-schritt-Formular für komplexe Aufgaben.

```
┌─────────────────────────────────────────┐
│ Schritt 1 von 5                         │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt des Schritts                   │
│                                         │
├─────────────────────────────────────────┤
│ [Zurück]              [Weiter →]        │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Horizontal** | Horizontaler Step Indicator |
| **Vertical** | Vertikaler Step Indicator |
| **Stepper** | Mit visueller Fortschrittsanzeige |
| **schrittanzeige** | Nur Anzeige der Schritte, ohne Führung |

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 300px | Kleine Wizards |
| Medium | 500px | Standard |
| Large | 700px | Große Wizards |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active Step** | Primärfarbe | Aktueller Schritt |
| **Completed Step** | Grün | Abgeschlossener Schritt |
| **Pending Step** | Grau | Ausstehender Schritt |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `border-bottom` | Unterstrich erscheint |

## Reaktiv

Der Schrittwechsel ist ein Schiebe-Übergang: vorwärts von rechts (`slide-in`), rückwärts
gespiegelt; der Step Indicator folgt mit `progress`. Auf schmaler Fläche wird der vertikale
Indicator zur Zeile aus Zähler und Leiste, der Inhalt bleibt in einer Spalte.

```css
.wizard-step        { transition: transform 200ms, opacity 200ms; }
.wizard-step--in-next { transform: translateX(24px); opacity: 0; }
.wizard-step--in-prev { transform: translateX(-24px); opacity: 0; }

@media (max-width: 600px) {
  .wizard--vertical .step-indicator { flex-direction: row; }  /* Zähler + Leiste */
}
```
