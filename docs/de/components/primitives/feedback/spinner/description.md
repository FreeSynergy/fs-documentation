# Spinner (Ladeanzeige)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `einfach`, `mit-text`, `inline` |
| **Zustände** | `loading` ist der einzige Zustand |
| **Gesten** | keine – nicht bedienbar |
| **Animationen** | `spin`, `pulse` |
| **Verwandt** | `button`, `progress`, `skeleton`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Spinner zeigt, dass das System arbeitet, ohne dass ein Fortschrittswert bekannt ist.
Er ist die kleinste Form der Rückmeldung.

## Verwendungszweck

- Warten auf eine Antwort (Speichern, Laden, Prüfen)
- Ladezustand in [Button](../../actions/button/) und Feldern
- Aktivitätsanzeige in Leisten und Cards

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einfach** | nur die drehende Grafik |
| **mit-text** | Spinner plus Begleittext („Lädt…“) |
| **inline** | klein genug für eine Textzeile oder ein Feld |

## Funktionen

- Hintergrundring (`track`) für bessere Erkennbarkeit
- Drehgeschwindigkeit einstellbar
- In Buttons ersetzt er die Beschriftung, ohne die Breite stark zu ändern

## Abgrenzung

- **Nicht verwechseln mit** [progress](../progress/): Progress zeigt einen Umfang.
  Ein Spinner zeigt nur Aktivität.

- **Nicht verwechseln mit** [skeleton](../skeleton/): Ein Skeleton füllt einen
  Platzhalter. Ein Spinner markiert einen Vorgang.

- **Nicht verwechseln mit** dem Ladezustand von [button](../../actions/button/):
  Dieser nutzt intern einen Spinner.

## Best Practices

- Einen Spinner nie länger als einige Sekunden ohne zusätzliche Information stehen lassen.
  Sonst [progress](../progress/) oder eine Meldung zeigen.

- Der wartende Bereich bekommt `aria-busy`. Der Spinner selbst braucht keinen Text.
- Höchstens ein Spinner pro Bildschirmbereich.

## Siehe auch

- [Progress](../progress/)
- [Skeleton](../skeleton/)
- [Button](../../actions/button/)
- [Base-Komponente](../../basics/base.md)
