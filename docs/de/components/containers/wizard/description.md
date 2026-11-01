# Wizard (Assistent)

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `Horizontal`, `Vertical`, `Stepper`, `schrittanzeige` |
| **Zustände** | `completed` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `slide-in`, `progress`, `highlight` |
| **Verwandt** | `modal`, `tabs`, `progress`, `field` |
| **Status** | dokumentiert |

!!! info "Standardisierung"
    Die frühere Komponente `stepper` ist als Variante in `wizard` aufgegangen: `assistent` (mit Führung) und `schrittanzeige` (nur Anzeige der Schritte).

## Beschreibung
Ein Wizard ist ein schritt-für-schritt-Formular für komplexe Aufgaben.

## Verwendungszweck

- Schritt-für-Schritt-Anleitungen
- Komplexe Formulare
- Einrichtungs-Assistenten
- Onboarding

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Horizontal** | Horizontaler Step Indicator |
| **Vertical** | Vertikaler Step Indicator |
| **Stepper** | Mit visueller Fortschrittsanzeige |
| **schrittanzeige** | nur Anzeige der Schritte, ohne Führung |

## Features

- Step Indicator (Fortschrittsanzeige)
- Back/Next-Navigation
- Validation (Pro Schritt)
- Save Draft (Zwischenspeichern)

## Abgrenzung

- **Nicht verwechseln mit** [modal](../../overlays/modal/): ein Wizard *kann* in einem Modal
  laufen; er ist aber durch die geordnete Schrittfolge und die Prüfung pro Schritt definiert,
  das Modal durch das Overlay selbst.
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs sind frei umschaltbar, der
  Wizard führt durch eine Folge und prüft vor dem Weitergehen.
- **Nicht verwechseln mit** [progress](../../feedback/progress/): die Fortschrittsbalken-
  Komponente zeigt nur einen Anteil; der Step Indicator zeigt Position, Erledigtes und
  Ausstehendes pro Schritt.
- Die Variante `schrittanzeige` (früher `stepper`) führt nicht — sie zeigt nur Schritte an.

## Best Practices

- Clarity (Klarheit)
- Feedback (Rückmeldung)
- Progress (Fortschritt)
- Flexibility (Flexibilität)

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

## Siehe auch

- [containers – Übersicht](../index.md)
- [Basiskomponente](../../basics/base/)
