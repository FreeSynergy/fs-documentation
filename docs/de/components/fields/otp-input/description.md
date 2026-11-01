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

Das Einmalpasswortfeld nimmt einen kurzen numerischen Code auf — je Zeichen ein Feld.
Es unterstützt Einfügen aus der Zwischenablage und Autofill aus dem Betriebssystem.

## Verwendungszweck

- Anmeldung mit Zweitfaktor
- Bestätigung einer gefährlichen Aktion
- Verifizieren einer E-Mail-Adresse oder Telefonnummer

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzelboxen** | eine Box pro Zeichen, Standard |
| **block** | ein Feld mit Zeichenabständen, für schmale Flächen |

## Features

- Vervollständigt automatisch, wenn der Code eingefügt wird
- Autofill aus dem Betriebssystem (`autocomplete = one-time-code`)
- Nach dem letzten Zeichen wird geprüft, nicht nach jedem
- Fehler: Felder leeren und kurz schütteln, Code neu eingeben

## Abgrenzung

- **Nicht verwechseln mit** [text-input](../text-input/) mit `password`: ein Passwort
  ist langfristig und frei gewählt, der Code kurz und maschinell erzeugt.
- **Nicht verwechseln mit** [tags-input](../tags-input/): dort entstehen mehrere Werte,
  hier ergibt jedes Zeichen einen Teil eines Wertes.

## Best Practices

- Länge aus dem Anbieter übernehmen (meist 6), nicht raten.
- Neuen Code erst nach Ablauf der Frist anfordern, mit Countdown.
- Keine Zeichen maskieren — der Code ist kurz und wird kontrolliert.

## Siehe auch

- [Text Input](../text-input/)
- [Basiskomponente](../../basics/base/)
