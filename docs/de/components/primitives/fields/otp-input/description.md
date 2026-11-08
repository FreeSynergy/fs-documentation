# OTP Input (Einmalpasswort)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `text-input` |
| **Varianten** | `einzelboxen`, `block` |
| **Zustände** | `error`, `loading`, `filled` |
| **Gesten** | `tap`, `type` |
| **Animationen** | `shake` |
| **Verwandt** | `text-input`, `button`, `alert` |
| **Rolle** | `group` |
| **Status** | dokumentiert |

## Beschreibung

Das Feld für ein Einmalpasswort nimmt einen kurzen numerischen Code entgegen. Pro Zeichen
gibt es ein Feld. Es unterstützt Einfügen aus der Zwischenablage und das Autofill
des Betriebssystems.

## Verwendungszweck

- Anmeldung mit einem zweiten Faktor
- Bestätigung einer riskanten Aktion
- Prüfung einer E-Mail-Adresse oder Telefonnummer

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzelboxen** | ein Kästchen pro Zeichen, Standard |
| **block** | ein Feld mit Zeichenabstand, für schmale Flächen |

## Funktionen

- Vervollständigt sich von allein, wenn der Code eingefügt wird
- Autofill des Betriebssystems (`autocomplete = one-time-code`)
- Geprüft wird nach dem letzten Zeichen, nicht nach jedem einzelnen
- Bei einem Fehler werden die Felder geleert und kurz geschüttelt. Der Code wird neu eingegeben.

## Abgrenzung

- **Nicht verwechseln mit** [text-input](../text-input/) mit `password`: Ein Passwort ist
  langlebig und frei gewählt. Der Code ist kurz und maschinell erzeugt.
- **Nicht verwechseln mit** [tags-input](../tags-input/): Dort entstehen mehrere Werte.
  Hier ist jedes Zeichen Teil eines einzigen Werts.

## Best Practices

- Die Länge vom Anbieter übernehmen (meist 6). Nicht raten.
- Einen neuen Code erst nach Ablauf der Frist anfordern, mit Countdown.
- Keine Zeichen verbergen. Der Code ist kurz und wird geprüft.

## Siehe auch

- [Text Input](../text-input/)
- [Base-Komponente](../../basics/base.md)
