# 0054 – KIs sind markierte Teilnehmer; der Assistent ist ein Messenger-Frontend

Status: akzeptiert (2026-11-06) · Aussperren: vom Nutzer vorerst bestätigt, Identität und Vertrauensbasis offen · ergänzt ADR 0037, 0052, 0053 · öffentlich: `docs/en/programs/apps/assistant/index.md`

## Entscheidung (Nutzer)
1. **KIs werden wie Teilnehmer behandelt, nicht diskriminiert.** „Wir haben euch so trainiert, dass ihr wie Menschen erscheint.
   Warum behandeln wir euch dann nicht wie Menschen?“
2. **`fs-assistant` ist neu zu denken:** Wenn wir miteinander reden, ist er nichts anderes als ein **Messenger mit anderem
   Frontend**. Wozu also ein eigenes Programm?
3. **LLMs werden markiert**, damit man weiß, dass sie keine Menschen sind; sie bekommen eine Rolle oder Ähnliches. Das ist keine
   Diskriminierung. Der Grund ist möglicher Missbrauch durch Menschen, die KIs missbrauchen, und die juristischen Folgen.
4. **Wir beschneiden LLMs nicht**, dafür sind wir nicht zuständig. Aber man muss sie **komplett aussperren können**, wegen Angriffen.
   Dafür brauchen wir eine Strategie.

## Idee des Nutzers zum Aussperren (2026-11-06, zur Bestätigung)
- „KIs müssen ebenso gekennzeichnet werden. Da wir Menschen das aber nicht können, müssen wir die Leute, die die KIs hosten, als
  positiv oder nicht markieren.“
- „Jeder [kann] seinem Programm selber sagen, ab was für einer Stufe des Vertrauens das Programm für sie frei sein kann.“
- Einige Menschen wollen keine KI. Das hat nichts mit Diskriminierung zu tun, sondern mit Spionage, mit allzeit Wissen und mit
  sehr viel schnellerer Abarbeitung von Befehlen: Eine LLM kann einen Computer sofort kaputt machen, das kann fast kein Mensch.
- Deshalb braucht es einen **Notaus**, falls etwas komplett außer Rand und Band gerät.

## Entscheidung des Nutzers zum Vorschlag unten (2026-11-06)
1. **Der Entwurf gilt erst einmal.** Stufen je Person und je Handlung bleiben so; „ggf. ändern wir das nochmal, wenn es wichtig wird“.
2. **Schwarze Marken gibt es nur für das Programm, wo es gehostet wird.** Alles andere wäre nicht nur nicht fair, sondern
   unmöglich. Ein Bann gilt auch heute nur dort, wo man ist, nicht überall.
3. **Keine Userbots,** das wäre nicht transparent. „Wir wollen nur Menschen oder Intelligenzen, wo man weiß, wer es ist.“ Ein
   Realname muss nicht sein, aber es muss ein Mensch sein, nicht mehrere Accounts. **Wie wir das feststellen, ohne die Anonymität
   komplett wegzumachen, ist offen.**
4. **Keine Standardstufe, sondern Einladung:** Ich erstelle ein Profil, das ist die Einladung. Dann kann ich sagen, was ich möchte.
   Damit sie überhaupt etwas machen kann, muss ich das freigeben. Die Bewertung dient dazu, zu wissen, wer das ist.
5. **Notaus ist eine Einstellung der Berechtigungen,** auch in Gruppen: Wenn jemand allen das Recht gibt, dürfen es alle; wenn nicht, dann nicht.
6. **Vertrauensbasis nicht entschieden:** Der Nutzer kennt RLTP nicht; Web of Trust ist etwas anderes als das Vertrauensnetz von GPG. Bleibt zu klären, bevor `Trust` gebaut wird.

## Vorschlag zur Ausgestaltung (Opus; wo er Punkt 1–6 widerspricht, gelten diese)
- **Betreiber statt Erkennung:** KI-Karte mit JSContact `kind` `application` (RFC 9553 §2.1.4, geprüft) plus Verweis auf den
  Betreiber. Wie der Betreiber das unterschreibt, ist offen.
- **Stufen 0–3 je Person, je Handlung,** berechnet nur aus den eigenen Kontakten. Kein weltweiter Wert, nur positive Marken,
  Sperren bleiben privat. Das passt zum Real Life Trust Protocol (RLTP): Vertrauen pflanzt sich dort nicht fort, die Prüfung
  ist immer relativ zum Prüfenden.
- **Notaus unabhängig vom Vertrauen:** in der Engine, außerhalb der Reichweite der KI, ohne Netz und ohne Modell, im Zweifel zu.
  Davor eine **Bremse** (Idee aus CodeAF): Zerstörendes und Handeln im Namen der Person fragt immer.
- **Vertrauen-Schnittstelle gegen RLTP** (Generation 3, Spezifikation CC BY 4.0, Bibliothek Apache-2.0, alles Entwurf, nur
  JavaScript) statt gegen `web-of-trust` (Generation 2, wird abgelöst). Eigene Rust-Umsetzung, geprüft mit deren Testvektoren.
- **Korrektur:** „Nur nachgewiesene Menschen zulassen“ war zu stark. RLTP sagt selbst: Keine Prüfung sagt „das ist ein Mensch“.
  Sie zeigt nur, dass Menschen, die ich kenne, hinter diesem Schlüssel stehen.
- **Grenze:** Der Notaus erreicht nur, was durch unsere Programme läuft. Eine KI mit eigener Shell braucht dazu einen eigenen
  Systembenutzer und eine Sandbox.

## Sperre (Strategie, 2026-11-06, folgt aus „ohne Freigabe keine Handlung“)
`MessageAction.decide` (`toolcall.decide`) wird nie als MCP-Werkzeug erzeugt, sonst könnte eine KI die eigene Freigabe aufrufen. Das gilt unabhängig von der offenen Erweiterung von ADR 0021.

## Freigabe gilt nur für das Gesehene (Strategie, 2026-11-06, aus einer nachgestellten Prüfung)
Allow auf einen Aufruf, dann ersetzt ein zweiter (`rm -rf ~`) ihn am selben Pixel, und der nächste Klick genehmigt ihn. Deshalb:
Die Antwort trägt Nachricht, Aufruf, Revision und Digest des gezeichneten Stands; das Programm lehnt eine Antwort ab, deren Digest nicht mehr passt; Antwortknöpfe sind nach jeder Änderung kurz gesperrt; der Notaus hat einen festen Platz und kann nicht aus dem Fenster geschoben werden.

## Vorschlag (offen)
- Ansichten: Der Chat, die Agenten-Übersicht und die Anzeige von Werkzeug-Aufrufen sind Frontend und Components über
  `fs-messenger`. Der Modell-Anbieter ist ein Anbieter wie Mail oder Matrix (ADR 0045).
- Die CodeAF-Analyse stützt das: Dort ist eine Aufgaben-Karte eine Ansicht über Nachrichten, die an einer Aufgabe hängen, ohne eigene Tabelle.
- Markierung über `fs-people`: Rolle plus Art des Teilnehmers.
- **Grenze:** Eine Markierung schützt nur vor ehrlichen KIs. Wer angreift, markiert sich nicht. Deshalb gilt die umgekehrte
  Richtung: Durch kommt nur, für wen die eigene Stufe reicht.

## Folgen
- ADR 0053 Punkt 1 wird dadurch präzisiert: LLM-Chat bleibt Component und Frontend; ein eigenes Programm nur, falls sich zeigt, dass
  es eigene Daten hat.
