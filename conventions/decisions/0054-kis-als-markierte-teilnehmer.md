# 0054 – KIs sind markierte Teilnehmer; der Assistent ist ein Messenger-Frontend

Status: akzeptiert (2026-11-06) · Strategie gegen Angriffe: offen · ergänzt ADR 0037, 0052, 0053

## Entscheidung (Nutzer)
1. **KIs werden wie Teilnehmer behandelt, nicht diskriminiert.** „Wir haben euch so trainiert, dass ihr wie Menschen erscheint.
   Warum behandeln wir euch dann nicht wie Menschen?“
2. **`fs-assistant` ist neu zu denken:** Wenn wir miteinander reden, ist er nichts anderes als ein **Messenger mit anderem
   Frontend**. Wozu also ein eigenes Programm?
3. **LLMs werden markiert**, damit man weiß, dass sie keine Menschen sind; sie bekommen eine Rolle oder Ähnliches. Das ist keine
   Diskriminierung. Der Grund ist möglicher Missbrauch durch Menschen, die KIs missbrauchen, und die juristischen Folgen.
4. **Wir beschneiden LLMs nicht**, dafür sind wir nicht zuständig. Aber man muss sie **komplett aussperren können**, wegen Angriffen.
   Dafür brauchen wir eine Strategie.

## Vorschlag (offen)
- Ansichten: Der Chat, die Agenten-Übersicht und die Anzeige von Werkzeug-Aufrufen sind Frontend und Components über
  `fs-messenger`. Der Modell-Anbieter ist ein Anbieter wie Mail oder Matrix (ADR 0045).
- Markierung über `fs-people`: Rolle plus Art des Teilnehmers. JSContact `kind` kennt nach unserem Wissen `application` (zu prüfen).
- **Grenze:** Eine Markierung schützt nur vor ehrlichen KIs. Wer angreift, markiert sich nicht. Also braucht das Aussperren
  zusätzlich die umgekehrte Richtung: nur nachgewiesene Menschen zulassen, über Web of Trust (ADR 0052).

## Folgen
- ADR 0053 Punkt 1 wird dadurch präzisiert: LLM-Chat bleibt Component und Frontend; ein eigenes Programm nur, falls sich zeigt, dass
  es eigene Daten hat.
