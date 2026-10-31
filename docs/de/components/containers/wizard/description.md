# Wizard (Assistent)

## Beschreibung

Ein Wizard ist ein schritt-für-schritt-Formular für komplexe Aufgaben.

## Verwendungszweck

- Schritt-für-Schritt-Anleitungen
- Komplexe Formulare
- Einrichtungs-Assistenten
- Onboarding

## Struktur

```
┌─────────────────────────────────────────┐
│ Schritt 1 von 5                         │  ← Step Indicator
├─────────────────────────────────────────┤
│                                         │
│   Inhalt des Schritts                   │
│                                         │  ← Body
├─────────────────────────────────────────┤
│ [Zurück]              [Weiter →]        │  ← Footer
└─────────────────────────────────────────┘
```

## Features

- Step Indicator (Fortschrittsanzeige)
- Back/Next-Navigation
- Validation (Pro Schritt)
- Save Draft (Zwischenspeichern)

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Horizontal** | Horizontaler Step Indicator |
| **Vertical** | Vertikaler Step Indicator |
| **Stepper** | Mit visueller Fortschrittsanzeige |

## Best Practices

- Clarity (Klarheit)
- Feedback (Rückmeldung)
- Progress (Fortschritt)
- Flexibility (Flexibilität)
