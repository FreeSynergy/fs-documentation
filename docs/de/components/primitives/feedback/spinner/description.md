# Spinner (Ladeanzeige)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `einfach`, `mit-text`, `inline` |
| **Zustände** | `loading` ist der einzige Zustand |
| **Gesten** | keine — nicht bedienbar |
| **Animationen** | `spin`, `pulse` |
| **Verwandt** | `button`, `progress`, `skeleton`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Spinner zeigt an, dass das System arbeitet, ohne dass ein Fortschrittswert
bekannt ist. Er ist die kleinste Form der Rückmeldung.

## Verwendungszweck

- Warten auf eine Antwort (Speichern, Laden, Prüfen)
- Ladezustand in [button](../../actions/button/) und Feldern
- Aktivitätsanzeige in Leisten und Karten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | nur die rotierende Grafik |
| **mit-text** | Spinner plus Begleittext („Wird geladen…“) |
| **inline** | so klein, dass er in einer Textzeile oder einem Feld steht |

## Features

- Hintergrundring (`track`) für bessere Wahrnehmbarkeit
- Drehgeschwindigkeit anpassbar
- Ersetzt in Buttons das Label, ohne die Breite stark zu ändern

## Abgrenzung

- **Nicht verwechseln mit** [progress](../progress/): Progress zeigt eine Menge,
  Spinner nur Aktivität.

- **Nicht verwechseln mit** [skeleton](../skeleton/): Skeleton füllt einen
  Platzhalter aus, Spinner markiert einen Vorgang.

- **Nicht verwechseln mit** dem Ladezustand von [button](../../actions/button/):
  dieser verwendet intern einen Spinner.

## Best Practices

- Spinner nie länger als einige Sekunden ohne Zusatzinfo lassen – sonst
  [progress](../progress/) oder Meldung zeigen.

- Der wartende Bereich erhält `aria-busy`; der Spinner selbst braucht keinen Text.
- Pro Bildschirmbereich höchstens ein Spinner.

## Siehe auch

- [Progress](../progress/)
- [Skeleton](../skeleton/)
- [Button](../../actions/button/)
- [Basiskomponente](../../basics/base/)
