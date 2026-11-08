# Rückmeldung (Feedback)

Rückmeldungs-Animationen antworten direkt auf eine Eingabe. Sie sind kurz (meist unter
500 ms) und verändern nie das Layout – die Person soll verstehen, was ihre Aktion bewirkt hat.

## Elemente

- **shake** – kurz waagerecht rütteln (Fehler, abgelehnte Eingabe)
- **wiggle** – leicht wackeln (Bearbeitungsmodus)
- **ripple** – eine Welle vom Berührungspunkt ausbreiten
- **press** – beim Drücken minimal einsinken
- **lift** – bei Hover oder Fokus anheben (der Schatten wächst)
- **tick-draw** – einen Erfolgshaken als Linie zeichnen
- **highlight** – den Hintergrund kurz aufleuchten lassen (gefundene Stelle)
- **elastic** – über die Endposition hinausschwingen
- **rubber-band** – übermäßiges Ziehen federt zurück (Überscrollen)

## Zuordnung

| Situation | Animation |
|-----------|-----------|
| Aktion erfolgreich | ripple, tick-draw |
| ein Bedienschritt ist aktiv | press, lift |
| Aktion abgelehnt | shake, wiggle |
| Inhalt geändert oder gefunden | highlight |
| Grenze erreicht | rubber-band, elastic |

## Siehe auch

- [Übersicht Animationen](../index.md)
- [Gesten](../../gestures/) – shake und wiggle sind hier Ausgabe, dort Eingabe
- [Schleife](../loop/) – dauerhafte Signale statt einmaliger Antwort
