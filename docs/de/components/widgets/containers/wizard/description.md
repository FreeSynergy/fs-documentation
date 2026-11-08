# Wizard

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
    Die frühere Komponente `stepper` ist eine Variante von `wizard` geworden: `assistent` (mit
    Führung) und `schrittanzeige` (nur die Schritte anzeigen).

## Beschreibung
Ein Wizard ist ein schrittweises Formular für komplexe Aufgaben.

## Verwendungszweck

- Schritt-für-Schritt-Anleitungen
- Komplexe Formulare
- Einrichtungsassistenten
- Onboarding

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Horizontal** | waagerechte Schrittanzeige |
| **Vertical** | senkrechte Schrittanzeige |
| **Stepper** | mit einer visuellen Fortschrittsanzeige |
| **schrittanzeige** | nur die Schritte anzeigen, ohne Führung |

## Features

- Schrittanzeige (Fortschrittsanzeige)
- Navigation zurück/weiter
- Validierung (pro Schritt)
- Entwurf speichern (Zwischenspeicherung)

## Abgrenzung

- **Nicht verwechseln mit** [modal](../../overlays/modal/): ein Wizard *kann* in einem
  Modal laufen, definiert ist er aber durch seine geordnete Schrittfolge und die Prüfung pro Schritt,
  das Modal durch das Overlay selbst.
- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs sind frei wechselbar, der
  Wizard führt durch eine Folge und prüft, bevor es weitergeht.
- **Nicht verwechseln mit** [progress](../../../primitives/feedback/progress/): der Fortschrittsbalken
  zeigt nur einen Anteil; die Schrittanzeige zeigt die Position, was erledigt ist und was pro Schritt
  noch aussteht.
- Die Variante `schrittanzeige` (früher `stepper`) führt nicht – sie zeigt nur Schritte an.

## Best Practices

- Klarheit
- Rückmeldung
- Fortschritt
- Flexibilität

## Struktur

```
┌─────────────────────────────────────────┐
│ Schritt 1 von 5                         │  ← Schrittanzeige
├─────────────────────────────────────────┤
│                                         │
│   Inhalt des Schritts                   │
│                                         │  ← Inhalt
├─────────────────────────────────────────┤
│ [Zurück]               [Weiter →]       │  ← Fuß
└─────────────────────────────────────────┘
```

## Siehe auch

- [containers – Übersicht](../index.md)
- [Basiskomponente](../../../primitives/basics/base.md)
