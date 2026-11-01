# Feedback (feedback)

Feedback-Animationen antworten direkt auf eine Eingabe. Sie sind kurz (meist unter 500 ms)
und verändern nie das Layout – der Nutzer soll verstehen, was seine Aktion bewirkt hat.

## Elemente

- **shake** - kurz horizontal rütteln (Fehler, abgelehnte Eingabe)
- **wiggle** - leicht wackeln (Bearbeitungsmodus)
- **ripple** - Welle vom Berührungspunkt aus breiten lassen
- **press** - beim Drücken minimal absinken
- **lift** - bei Hover oder Fokus anheben (Schatten wächst)
- **tick-draw** - Erfolgshäkchen als Linie zeichnen
- **highlight** - Hintergrund kurz aufleuchten lassen (Fundstelle)
- **elastic** - über die Endposition hinausschwingen
- **rubber-band** - übermäßiges Ziehen federt zurück (Over-Scroll)

## Zuordnung

| Situation | Animation |
|-----------|-----------|
| Aktion gelungen | ripple, tick-draw |
| Bedienschritt aktiv | press, lift |
| Aktion abgelehnt | shake, wiggle |
| Inhalt geändert oder gefunden | highlight |
| Grenze erreicht | rubber-band, elastic |

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Gesten](../../gestures/) - shake und wiggle sind hier Ausgabe, dort Eingabe
- [Endlos (loop)](../loop/) - dauerhafte Signale statt einmaliger Antwort
